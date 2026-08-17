#!/usr/bin/env python3
"""Orchestrated MTP benchmark for sudoingX/qwen38-mtp

Launches llama-server itself, once per scenario:

    baseline : no speculative decoding flags
    n=1..6   : --spec-type draft-mtp --spec-draft-n-max N

For each scenario it waits for /health, runs the streaming probe
(RUNS runs x PROMPTS prompts, per-run draft acceptance), tears the
server down, and moves on. Everything is saved under RESULTS_DIR:

    server_<scenario>.log   raw llama-server stdout/stderr
    probe_<scenario>.txt    detailed probe output (per-run lines, acc)
    results.json            all structured data
    summary.md              all summary tables

Usage:
    python3 bench.py                        # all scenarios, compact output
    python3 bench.py baseline n2 n4         # subset of scenarios
    python3 bench.py --srv                  # display server-side tok/s
    python3 bench.py --full                 # also print all summary tables
    python3 bench.py /path/to/model.gguf    # override MODEL
    python3 bench.py --model /path/x.gguf   # same
    python3 bench.py --help                 # this help
"""
import json
import os
import signal
import socket
import statistics as st
import subprocess
import sys
import time
import urllib.request
from datetime import datetime

# ----------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------
# Adjust the model path, everything else is the measured config.
MODEL = os.path.expandvars("$HOME/models/qwen3.8-27b-dense/Qwen3.8-27B-Q4_K_M.gguf")

SERVER_BIN = "llama-server"
HOST = "127.0.0.1"
PORT = 8080
URL = f"http://{HOST}:{PORT}/v1/chat/completions"
HEALTH_URL = f"http://{HOST}:{PORT}/health"
HEALTH_TIMEOUT = 300          # 5 min timeout to load the model
SHUTDOWN_TIMEOUT = 30


def base_args():
    return [
        "--model", MODEL,
        "--alias", "Qwen3.8 27B Q4",
        "--host", "0.0.0.0",
        "--ctx-size", "131072",
        "-ngl", "999",
        "-fa", "1",
        "--cache-type-k", "q4_0",
        "--cache-type-v", "q4_0",
        "--parallel", "1",
        "--metrics",
        "--port", str(PORT),
    ]


SCENARIOS = {"baseline": []}
for n in range(1, 7):
    SCENARIOS[f"n{n}"] = ["--spec-type", "draft-mtp", "--spec-draft-n-max", str(n)]

PROMPTS = [
    "write a python function that merges two sorted lists into one sorted list, with docstring.",
    "explain the difference between mmap and read for loading large files, one paragraph.",
    "write a bash script that watches a directory and prints new files as they appear.",
]
RUNS = 3
MAX_TOKENS = 400

RESULTS_DIR = os.path.join(os.getcwd(), "bench_results_" + datetime.now().strftime("%Y%m%d_%H%M%S"))

SHOW_SRV = False   # --srv : display server-side tok/s instead of client-side
FULL = False       # --full: also print all summary tables to the console

# ----------------------------------------------------------------------------
# Probe
# ----------------------------------------------------------------------------
def run_probe(prompt, max_tokens=MAX_TOKENS):
    body = {
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "stream": True,
        "chat_template_kwargs": {"enable_thinking": False},
        "timings_per_token": True,
        "cache_prompt": False,
    }
    req = urllib.request.Request(URL, json.dumps(body).encode(), {"Content-Type": "application/json"})
    t0 = time.time()
    ttft = None
    n = 0
    last = t0
    timings = None
    with urllib.request.urlopen(req, timeout=300) as r:
        for line in r:
            line = line.decode().strip()
            if not line.startswith("data: ") or line == "data: [DONE]":
                continue
            chunk = json.loads(line[6:])
            if "timings" in chunk:
                timings = chunk["timings"]
            delta = chunk["choices"][0].get("delta", {}) if chunk.get("choices") else {}
            if delta.get("content") or delta.get("reasoning_content"):
                now = time.time()
                if ttft is None:
                    ttft = now - t0
                last = now
                n += 1
    span = last - t0 - (ttft or 0)
    tps_client = n / span if span > 0 else 0.0
    tps_server = None
    draft_n = draft_acc = 0
    if timings:
        tps_server = timings.get("predicted_per_second")
        draft_n = timings.get("draft_n") or 0
        draft_acc = timings.get("draft_n_accepted") or 0
    return {
        "tps": tps_client,
        "tps_server": tps_server,
        "ttft": ttft or 0.0,
        "n_tokens": n,
        "draft_n": draft_n,
        "draft_acc": draft_acc,
        "accept_rate": (draft_acc / draft_n) if draft_n else None,
    }


def val(x):
    """Displayed tok/s for one run: server-side with --srv, else client-side."""
    if SHOW_SRV and x["tps_server"] is not None:
        return x["tps_server"]
    return x["tps"]


# ----------------------------------------------------------------------------
# Server lifecycle
# ----------------------------------------------------------------------------
def port_open():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(1)
        return s.connect_ex((HOST, PORT)) == 0


def wait_health(proc, log_path):
    deadline = time.time() + HEALTH_TIMEOUT
    while time.time() < deadline:
        if proc.poll() is not None:
            raise RuntimeError(f"server exited early (code {proc.returncode}), see {log_path}")
        try:
            with urllib.request.urlopen(HEALTH_URL, timeout=2) as r:
                if r.status == 200:
                    return
        except Exception:
            pass
        time.sleep(2)
    raise RuntimeError(f"server not healthy after {HEALTH_TIMEOUT}s, see {log_path}")


def start_server(scenario, extra_args):
    if port_open():
        raise RuntimeError(f"port {PORT} already in use -- stop the running server first")
    log_path = os.path.join(RESULTS_DIR, f"server_{scenario}.log")
    log_f = open(log_path, "w")
    cmd = [SERVER_BIN] + base_args() + extra_args
    log_f.write("CMD: " + " ".join(cmd) + "\n\n")
    log_f.flush()
    proc = subprocess.Popen(cmd, stdout=log_f, stderr=subprocess.STDOUT,
                            start_new_session=True)
    try:
        wait_health(proc, log_path)
    except Exception:
        stop_server(proc)
        log_f.close()
        raise
    return proc, log_f, log_path


def stop_server(proc):
    if proc.poll() is None:
        proc.send_signal(signal.SIGINT)
        try:
            proc.wait(SHUTDOWN_TIMEOUT)
        except subprocess.TimeoutExpired:
            proc.kill()
            proc.wait()
    deadline = time.time() + 30
    while port_open() and time.time() < deadline:
        time.sleep(1)


# ----------------------------------------------------------------------------
# Scenario runner
# ----------------------------------------------------------------------------
def run_scenario(scenario, extra_args):
    print(f"\n=== scenario {scenario}  " + "=" * 48)
    proc, log_f, log_path = start_server(scenario, extra_args)
    detail = [f"scenario: {scenario}", f"extra args: {extra_args or '(none)'}", ""]
    data = []
    try:
        run_probe("warmup", 40)
        for p in PROMPTS:
            detail.append(f"--- {p[:70]}")
            results = []
            for i in range(RUNS):
                x = run_probe(p)
                results.append(x)
                acc = (f" | acc {x['accept_rate']:.4f} ({x['draft_acc']}/{x['draft_n']})"
                       if x["accept_rate"] is not None else " | acc n/a")
                srv = f" | srv {x['tps_server']:6.1f}" if x["tps_server"] else ""
                detail.append(f"  run {i + 1}: {x['tps']:6.1f} tok/s{srv}{acc}")
            rs = [val(x) for x in results]
            line = (f"{st.median(rs):6.1f} tok/s median"
                    f" | runs: {[round(v, 1) for v in rs]} | {p[:50]}")
            print(line)
            detail.append(line)
            data.append(results)
        all_runs = [val(x) for runs in data for x in runs]
        line = f"OVERALL: mean {st.mean(all_runs):.1f} median {st.median(all_runs):.1f}"
        print(line)
        detail.append(line)
    finally:
        stop_server(proc)
        log_f.close()
    with open(os.path.join(RESULTS_DIR, f"probe_{scenario}.txt"), "w") as f:
        f.write("\n".join(detail) + "\n")
    return data


# ----------------------------------------------------------------------------
# Summary
# ----------------------------------------------------------------------------
def fmt(v, spec="{:.1f}"):
    return spec.format(v) if v is not None else "n/a"


def tps_label():
    return " -- server" if SHOW_SRV else ""


def flat_vals(all_data, scen):
    return [val(x) for runs in all_data[scen] for x in runs]


def flat_acc(all_data, scen):
    return [x["accept_rate"] for runs in all_data[scen] for x in runs
            if x["accept_rate"] is not None]


def comparison_row(all_data, s):
    if s not in all_data:
        return f"| {s} | not run | not run | - |"
    vals = flat_vals(all_data, s)
    accs = flat_acc(all_data, s)
    acc = f"{min(accs):.4f}-{max(accs):.4f}" if accs else "n/a-n/a"
    return f"| {s} | {fmt(st.mean(vals))} | {fmt(st.median(vals))} | {acc} |"


def build_tables(all_data):
    scen_order = [s for s in ["baseline", "n1", "n2", "n3", "n4", "n5", "n6"] if s in all_data]
    spec_scens = [s for s in scen_order if s != "baseline"]

    detail = []      # printed only with --full (always in summary.md)
    final = []       # always printed
    community = []   # always printed, last

    detail.append(f"## tok/s per prompt (median of runs){tps_label()}\n")
    detail.append("| Prompt | " + " | ".join(scen_order) + " |")
    detail.append("|" + "---|" * (len(scen_order) + 1))
    for pi in range(len(PROMPTS)):
        cells = [fmt(st.median([val(x) for x in all_data[s][pi]])) for s in scen_order]
        detail.append(f"| P{pi + 1} | " + " | ".join(cells) + " |")

    detail.append(f"\n## overall tok/s per scenario (all runs pooled){tps_label()}\n")
    detail.append("| Metric | " + " | ".join(scen_order) + " |")
    detail.append("|" + "---|" * (len(scen_order) + 1))
    for name, f in (("mean", st.mean), ("median", st.median)):
        cells = [fmt(f(flat_vals(all_data, s))) for s in scen_order]
        detail.append(f"| {name} | " + " | ".join(cells) + " |")

    detail.append("\n## draft acceptance per prompt per scenario -- median (min-max over runs)\n")
    detail.append("| Prompt | " + " | ".join(spec_scens) + " |")
    detail.append("|" + "---|" * (len(spec_scens) + 1))
    for pi in range(len(PROMPTS)):
        cells = []
        for s in spec_scens:
            accs = [x["accept_rate"] for x in all_data[s][pi] if x["accept_rate"] is not None]
            if accs:
                cells.append(f"{st.median(accs):.4f} ({min(accs):.4f}-{max(accs):.4f})")
            else:
                cells.append("n/a")
        detail.append(f"| P{pi + 1} | " + " | ".join(cells) + " |")

    detail.append("\n## draft acceptance per prompt -- pooled over all n scenarios and runs\n")
    detail.append("| Prompt | min | max |")
    detail.append("|---|---|---|")
    for pi in range(len(PROMPTS)):
        accs = [x["accept_rate"] for s in spec_scens for x in all_data[s][pi]
                if x["accept_rate"] is not None]
        if accs:
            detail.append(f"| P{pi + 1} | {min(accs):.4f} | {max(accs):.4f} |")
        else:
            detail.append(f"| P{pi + 1} | n/a | n/a |")

    header = ["| Scenario | mean | median | acc (min-max) |", "|---|---|---|---|"]

    final.append(f"## all scenarios (all runs pooled){tps_label()}\n")
    final += header
    for s in scen_order:
        final.append(comparison_row(all_data, s))

    community.append(f"#### Values for sudoingX/qwen38-mtp community table (baseline vs n2) ####{tps_label()}\n")
    community += header
    for s in ("baseline", "n2"):
        community.append(comparison_row(all_data, s))

    footer = ["\nPrompts:"]
    for pi, p in enumerate(PROMPTS):
        footer.append(f"- P{pi + 1}: {p}")
    return "\n".join(detail), "\n".join(final), "\n".join(footer), "\n".join(community)


def usage(exit_code=0):
    print(__doc__.strip())
    print("\nScenarios:", ", ".join(SCENARIOS))
    print(f"Default model: {MODEL}")
    sys.exit(exit_code)


def main():
    global SHOW_SRV, FULL, MODEL
    args = []
    it = iter(sys.argv[1:])
    for a in it:
        if a in ("--help", "-h"):
            usage()
        elif a == "--srv":
            SHOW_SRV = True
        elif a == "--full":
            FULL = True
        elif a == "--model":
            MODEL = next(it, None) or sys.exit("--model needs a path")
        elif a.endswith(".gguf") or os.sep in a:
            MODEL = a
        elif a.startswith("-"):
            print(f"unknown flag: {a}\n")
            usage(2)
        else:
            args.append(a)

    if not os.path.isfile(MODEL):
        sys.exit(f"model file not found: {MODEL}")

    wanted = args or list(SCENARIOS)
    bad = [s for s in wanted if s not in SCENARIOS]
    if bad:
        sys.exit(f"unknown scenario(s): {bad}; valid: {list(SCENARIOS)}")
    os.makedirs(RESULTS_DIR, exist_ok=True)
    print(f"model: {MODEL}")
    print(f"results dir: {RESULTS_DIR}")

    all_data = {}
    for s in wanted:
        all_data[s] = run_scenario(s, SCENARIOS[s])
        with open(os.path.join(RESULTS_DIR, "results.json"), "w") as f:
            json.dump(all_data, f, indent=2)

    detail, final, footer, community = build_tables(all_data)
    with open(os.path.join(RESULTS_DIR, "summary.md"), "w") as f:
        f.write(detail + "\n\n" + final + "\n" + footer + "\n\n" + community + "\n")

    print()
    if FULL:
        print(detail + "\n")
    print(final)
    print(footer)
    print()
    print(community)
    print(f"\nall output saved in {RESULTS_DIR}")


if __name__ == "__main__":
    main()
