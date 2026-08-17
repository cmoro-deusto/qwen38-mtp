## tok/s per prompt (median of runs)

| Prompt | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| P1 | 71.1 | 113.6 | 145.4 | 157.8 | 169.3 | 175.6 | 169.6 |
| P2 | 71.5 | 101.5 | 107.1 | 103.2 | 92.3 | 85.8 | 72.9 |
| P3 | 70.8 | 109.5 | 130.7 | 136.9 | 148.1 | 123.0 | 134.8 |

## overall tok/s per scenario (all runs pooled)

| Metric | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| mean | 71.1 | 107.8 | 129.9 | 132.8 | 135.9 | 126.7 | 125.4 |
| median | 71.1 | 109.5 | 130.7 | 136.9 | 148.1 | 123.0 | 134.8 |

## draft acceptance per prompt per scenario -- median (min-max over runs)

| Prompt | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|
| P1 | 0.9507 (0.9227-0.9752) | 0.9342 (0.9124-0.9654) | 0.8869 (0.8796-0.9111) | 0.8822 (0.8631-0.9217) | 0.8714 (0.7891-0.8870) | 0.8049 (0.7810-0.8762) |
| P2 | 0.7188 (0.6531-0.7429) | 0.5474 (0.5281-0.7000) | 0.4578 (0.4414-0.5185) | 0.3649 (0.3140-0.4129) | 0.3200 (0.2886-0.3645) | 0.2544 (0.2527-0.2941) |
| P3 | 0.8821 (0.8472-0.9241) | 0.7896 (0.7700-0.8664) | 0.7280 (0.6608-0.7610) | 0.7411 (0.6126-0.7772) | 0.5468 (0.5035-0.5835) | 0.6047 (0.4591-0.6358) |

## draft acceptance per prompt -- pooled over all n scenarios and runs

| Prompt | min | max |
|---|---|---|
| P1 | 0.7810 | 0.9752 |
| P2 | 0.2527 | 0.7429 |
| P3 | 0.4591 | 0.9241 |

## all scenarios (all runs pooled)

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 71.1 | 71.1 | n/a-n/a |
| n1 | 107.8 | 109.5 | 0.6531-0.9752 |
| n2 | 129.9 | 130.7 | 0.5281-0.9654 |
| n3 | 132.8 | 136.9 | 0.4414-0.9111 |
| n4 | 135.9 | 148.1 | 0.3140-0.9217 |
| n5 | 126.7 | 123.0 | 0.2886-0.8870 |
| n6 | 125.4 | 134.8 | 0.2527-0.8762 |

Prompts:
- P1: write a python function that merges two sorted lists into one sorted list, with docstring.
- P2: explain the difference between mmap and read for loading large files, one paragraph.
- P3: write a bash script that watches a directory and prints new files as they appear.

#### Values for sudoingX/qwen38-mtp community table (baseline vs n2) ####

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 71.1 | 71.1 | n/a-n/a |
| n2 | 129.9 | 130.7 | 0.5281-0.9654 |
