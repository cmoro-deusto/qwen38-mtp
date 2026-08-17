## tok/s per prompt (median of runs)

| Prompt | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| P1 | 71.2 | 114.7 | 146.4 | 159.9 | 168.2 | 164.0 | 161.3 |
| P2 | 71.4 | 100.1 | 103.5 | 107.9 | 93.5 | 84.5 | 79.0 |
| P3 | 71.0 | 111.4 | 137.0 | 131.1 | 123.1 | 141.0 | 122.0 |

## overall tok/s per scenario (all runs pooled)

| Metric | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| mean | 71.2 | 108.4 | 129.1 | 133.7 | 128.8 | 128.8 | 120.8 |
| median | 71.2 | 111.4 | 137.0 | 131.1 | 123.1 | 141.0 | 122.0 |

## draft acceptance per prompt per scenario -- median (min-max over runs)

| Prompt | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|
| P1 | 0.9652 (0.9463-0.9752) | 0.9429 (0.8854-0.9491) | 0.9030 (0.8923-0.9308) | 0.8765 (0.8532-0.9219) | 0.7995 (0.7889-0.8054) | 0.7585 (0.7453-0.7826) |
| P2 | 0.6979 (0.6602-0.7379) | 0.5214 (0.5000-0.6053) | 0.4923 (0.4923-0.4972) | 0.3788 (0.2993-0.3864) | 0.3217 (0.2658-0.3424) | 0.2901 (0.2817-0.2917) |
| P3 | 0.9271 (0.8558-0.9356) | 0.8519 (0.8300-0.8713) | 0.6742 (0.6304-0.7294) | 0.5735 (0.5578-0.6449) | 0.6690 (0.5770-0.7119) | 0.5308 (0.4868-0.5490) |

## draft acceptance per prompt -- pooled over all n scenarios and runs

| Prompt | min | max |
|---|---|---|
| P1 | 0.7453 | 0.9752 |
| P2 | 0.2658 | 0.7379 |
| P3 | 0.4868 | 0.9356 |

## all scenarios (all runs pooled)

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 71.2 | 71.2 | n/a-n/a |
| n1 | 108.4 | 111.4 | 0.6602-0.9752 |
| n2 | 129.1 | 137.0 | 0.5000-0.9491 |
| n3 | 133.7 | 131.1 | 0.4923-0.9308 |
| n4 | 128.8 | 123.1 | 0.2993-0.9219 |
| n5 | 128.8 | 141.0 | 0.2658-0.8054 |
| n6 | 120.8 | 122.0 | 0.2817-0.7826 |

Prompts:
- P1: write a python function that merges two sorted lists into one sorted list, with docstring.
- P2: explain the difference between mmap and read for loading large files, one paragraph.
- P3: write a bash script that watches a directory and prints new files as they appear.

#### Values for sudoingX/qwen38-mtp community table (baseline vs n2) ####

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 71.2 | 71.2 | n/a-n/a |
| n2 | 129.1 | 137.0 | 0.5000-0.9491 |
