#!/usr/bin/env python3
"""Summarize the nvidia-smi CSVs written by sweep_power.sh.

    ./summarize_power.py power_sweep_YYYYMMDD_HHMMSS/

Each CSV covers one full bench.py pass, which is several scenarios run back to
back. bench.py starts a fresh llama-server per scenario and tears it down after,
so GPU memory rises and falls once per scenario -- that staircase is what this
splits on, giving per-scenario power, clocks, temperature and VRAM.

Columns are timestamp, power.draw, clocks.sm, temperature.gpu, utilization.gpu,
memory.used. Power is reported as p95 rather than mean: every segment includes
model loading and a warmup, which sit well below decode draw.
"""
import glob
import os
import statistics as st
import sys

SCENARIOS = ["baseline", "n1", "n2", "n3", "n4", "n5", "n6"]

MIN_SAMPLES = 5        # ignore blips shorter than this
GAP_SAMPLES = 1        # idle samples that end a segment; teardown is ~1s at 1Hz
MEM_FRACTION = 0.5     # of peak VRAM: above this, a server is loaded


def pct(xs, p):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(len(xs) * p))]


def read(path):
    rows = []
    for line in open(path):
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 6:
            continue
        try:
            rows.append({
                "w": float(parts[1]),
                "mhz": float(parts[2]),
                "c": float(parts[3]),
                "util": float(parts[4]),
                "mem": float(parts[5]),
            })
        except ValueError:
            continue        # [N/A] rows while the driver settles
    return rows


def segment(rows):
    """Split a pass into one segment per loaded server."""
    if not rows:
        return []
    thresh = max(r["mem"] for r in rows) * MEM_FRACTION
    segs, cur, gap = [], [], 0
    for r in rows:
        if r["mem"] > thresh:
            cur.append(r)
            gap = 0
        elif cur:
            gap += 1
            if gap >= GAP_SAMPLES:
                if len(cur) >= MIN_SAMPLES:
                    segs.append(cur)
                cur, gap = [], 0
    if len(cur) >= MIN_SAMPLES:
        segs.append(cur)
    return segs


def main():
    d = sys.argv[1] if len(sys.argv) > 1 else "."
    files = sorted(glob.glob(os.path.join(d, "cap*.csv")))
    if not files:
        sys.exit(f"no cap*.csv under {d}")

    print(f"{'pass':<18} {'scenario':<9} {'s':>4} {'p95 W':>6} {'max W':>6} "
          f"{'med W':>6} {'p95 MHz':>8} {'max C':>6} {'VRAM MiB':>9}")
    for f in files:
        name = os.path.basename(f)[:-4]
        segs = segment(read(f))
        if len(segs) != len(SCENARIOS):
            print(f"{name:<18} !! found {len(segs)} segments, expected "
                  f"{len(SCENARIOS)} -- labels below may be shifted")
        for i, seg in enumerate(segs):
            label = SCENARIOS[i] if i < len(SCENARIOS) else f"seg{i}"
            w = [r["w"] for r in seg]
            print(f"{name:<18} {label:<9} {len(seg):>4} {pct(w, 0.95):>6.0f} "
                  f"{max(w):>6.0f} {st.median(w):>6.0f} "
                  f"{pct([r['mhz'] for r in seg], 0.95):>8.0f} "
                  f"{max(r['c'] for r in seg):>6.0f} "
                  f"{max(r['mem'] for r in seg):>9.0f}")


if __name__ == "__main__":
    main()
