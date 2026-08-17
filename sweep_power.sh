#!/usr/bin/env bash
# Drive bench.py across GPU power caps, sampling actual draw during each run.
#
# Needs sudo for `nvidia-smi -pl`. Restores the original cap on exit, including
# on Ctrl-C. Run from the repo root, on the `bench` branch.
#
#   ./sweep_power.sh /path/to/model.gguf
#
set -euo pipefail

MODEL="${1:?usage: sweep_power.sh /path/to/model.gguf}"
GPU=0
CAPS=(400 450 500 550 600)      # this card: min 400, default/max 600
SCENARIOS="baseline n1 n2 n3 n4 n5 n6"   # arms per cap
PASSES=3                        # complete bench.py passes per cap, for noise
OUT="power_sweep_$(date +%Y%m%d_%H%M%S)"

mkdir -p "$OUT"

# --- authenticate once, then keep the sudo timestamp warm -------------------
# The run is longer than sudo's default 15 min timeout and sets a cap only
# every ~13 min, so without this a password prompt could appear mid-sweep and
# block it indefinitely. Nothing here runs as root except `nvidia-smi -pl`.
sudo -v
while true; do sudo -n true; sleep 60; done 2>/dev/null &
KEEPALIVE=$!

# --- record and restore the original cap ------------------------------------
ORIG=$(nvidia-smi -i "$GPU" --query-gpu=power.limit --format=csv,noheader,nounits | cut -d. -f1)
echo "original power limit: ${ORIG}W"
cleanup() {
  echo "restoring ${ORIG}W"
  sudo -n nvidia-smi -i "$GPU" -pl "$ORIG" >/dev/null || true
  kill "$KEEPALIVE" 2>/dev/null || true
}
trap cleanup EXIT

# --- legal range, printed once so the CAPS list can be sanity-checked --------
nvidia-smi -i "$GPU" -q -d POWER | grep -Ei "power limit" | tee "$OUT/power_limits.txt"

for CAP in "${CAPS[@]}"; do
  echo "=== cap ${CAP}W ==============================================="
  sudo nvidia-smi -i "$GPU" -pl "$CAP" >/dev/null

  for PASS in $(seq 1 "$PASSES"); do
    TAG="cap${CAP}_pass${PASS}"
    echo "--- $TAG"

    # sample power/clocks/temp/VRAM at 1 Hz for the whole pass. memory.used is
    # what lets summarize_power.py split the pass back into scenarios: it rises
    # when a server loads and drops to idle when bench.py tears it down.
    nvidia-smi -i "$GPU" \
      --query-gpu=timestamp,power.draw,clocks.sm,temperature.gpu,utilization.gpu,memory.used \
      --format=csv,noheader,nounits -l 1 > "$OUT/$TAG.csv" &
    SAMPLER=$!

    ./bench.py --model "$MODEL" $SCENARIOS > "$OUT/$TAG.console.txt" 2>&1 || true

    kill "$SAMPLER" 2>/dev/null || true
    wait "$SAMPLER" 2>/dev/null || true

    # bench.py writes its own timestamped dir; claim the newest one
    NEWEST=$(ls -dt bench_results_*/ | head -1)
    mv "$NEWEST" "$OUT/$TAG.results"
    echo "    -> $OUT/$TAG.results"

    sleep 60   # let the card cool so the next pass starts from a similar temp
  done
done

echo "done: $OUT"
