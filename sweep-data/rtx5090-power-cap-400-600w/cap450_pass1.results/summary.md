## tok/s per prompt (median of runs)

| Prompt | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| P1 | 73.5 | 118.7 | 151.9 | 165.3 | 178.2 | 173.0 | 183.9 |
| P2 | 73.9 | 104.1 | 112.5 | 103.4 | 102.9 | 90.3 | 91.1 |
| P3 | 73.2 | 112.2 | 144.9 | 148.7 | 144.7 | 142.0 | 144.6 |

## overall tok/s per scenario (all runs pooled)

| Metric | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| mean | 73.5 | 112.5 | 136.3 | 142.2 | 142.4 | 138.4 | 137.6 |
| median | 73.5 | 112.2 | 144.9 | 148.7 | 144.7 | 142.0 | 144.6 |

## draft acceptance per prompt per scenario -- median (min-max over runs)

| Prompt | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|
| P1 | 0.9611 (0.9588-0.9752) | 0.9309 (0.9185-0.9420) | 0.8563 (0.8487-0.9218) | 0.8457 (0.8388-0.8765) | 0.7823 (0.7651-0.8767) | 0.8109 (0.7514-0.8190) |
| P2 | 0.7071 (0.7019-0.8148) | 0.5366 (0.5294-0.6288) | 0.4074 (0.3933-0.5833) | 0.3769 (0.3370-0.4184) | 0.3057 (0.2867-0.3736) | 0.3197 (0.2566-0.3519) |
| P3 | 0.8558 (0.8472-0.8732) | 0.8455 (0.7547-0.8514) | 0.7323 (0.6907-0.7674) | 0.6396 (0.6080-0.6980) | 0.5902 (0.5838-0.6400) | 0.5907 (0.5371-0.5980) |

## draft acceptance per prompt -- pooled over all n scenarios and runs

| Prompt | min | max |
|---|---|---|
| P1 | 0.7514 | 0.9752 |
| P2 | 0.2566 | 0.8148 |
| P3 | 0.5371 | 0.8732 |

## all scenarios (all runs pooled)

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 73.5 | 73.5 | n/a-n/a |
| n1 | 112.5 | 112.2 | 0.7019-0.9752 |
| n2 | 136.3 | 144.9 | 0.5294-0.9420 |
| n3 | 142.2 | 148.7 | 0.3933-0.9218 |
| n4 | 142.4 | 144.7 | 0.3370-0.8765 |
| n5 | 138.4 | 142.0 | 0.2867-0.8767 |
| n6 | 137.6 | 144.6 | 0.2566-0.8190 |

Prompts:
- P1: write a python function that merges two sorted lists into one sorted list, with docstring.
- P2: explain the difference between mmap and read for loading large files, one paragraph.
- P3: write a bash script that watches a directory and prints new files as they appear.

#### Values for sudoingX/qwen38-mtp community table (baseline vs n2) ####

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 73.5 | 73.5 | n/a-n/a |
| n2 | 136.3 | 144.9 | 0.5294-0.9420 |
