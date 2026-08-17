## tok/s per prompt (median of runs)

| Prompt | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| P1 | 74.2 | 120.1 | 160.6 | 185.1 | 195.1 | 193.0 | 195.8 |
| P2 | 74.9 | 109.3 | 116.0 | 113.0 | 113.1 | 102.9 | 88.0 |
| P3 | 74.2 | 117.6 | 141.6 | 167.1 | 150.9 | 163.1 | 136.3 |

## overall tok/s per scenario (all runs pooled)

| Metric | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| mean | 74.5 | 114.8 | 138.4 | 155.9 | 154.9 | 151.2 | 140.4 |
| median | 74.4 | 117.6 | 141.6 | 167.1 | 150.9 | 163.1 | 136.3 |

## draft acceptance per prompt per scenario -- median (min-max over runs)

| Prompt | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|
| P1 | 0.9606 (0.9369-0.9606) | 0.9478 (0.9208-0.9491) | 0.9406 (0.9037-0.9560) | 0.8858 (0.8624-0.9070) | 0.8375 (0.8142-0.8429) | 0.7905 (0.7676-0.7989) |
| P2 | 0.7634 (0.6610-0.7978) | 0.5294 (0.5120-0.5342) | 0.4329 (0.3709-0.5628) | 0.4115 (0.4083-0.4123) | 0.3438 (0.3382-0.3600) | 0.2733 (0.2685-0.2889) |
| P3 | 0.9107 (0.8720-0.9227) | 0.7732 (0.7187-0.7955) | 0.8056 (0.7670-0.8647) | 0.6264 (0.5907-0.7614) | 0.6563 (0.5419-0.6781) | 0.5059 (0.4992-0.5343) |

## draft acceptance per prompt -- pooled over all n scenarios and runs

| Prompt | min | max |
|---|---|---|
| P1 | 0.7676 | 0.9606 |
| P2 | 0.2685 | 0.7978 |
| P3 | 0.4992 | 0.9227 |

## all scenarios (all runs pooled)

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 74.5 | 74.4 | n/a-n/a |
| n1 | 114.8 | 117.6 | 0.6610-0.9606 |
| n2 | 138.4 | 141.6 | 0.5120-0.9491 |
| n3 | 155.9 | 167.1 | 0.3709-0.9560 |
| n4 | 154.9 | 150.9 | 0.4083-0.9070 |
| n5 | 151.2 | 163.1 | 0.3382-0.8429 |
| n6 | 140.4 | 136.3 | 0.2685-0.7989 |

Prompts:
- P1: write a python function that merges two sorted lists into one sorted list, with docstring.
- P2: explain the difference between mmap and read for loading large files, one paragraph.
- P3: write a bash script that watches a directory and prints new files as they appear.

#### Values for sudoingX/qwen38-mtp community table (baseline vs n2) ####

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 74.5 | 74.4 | n/a-n/a |
| n2 | 138.4 | 141.6 | 0.5120-0.9491 |
