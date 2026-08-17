## tok/s per prompt (median of runs)

| Prompt | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| P1 | 74.6 | 123.2 | 163.6 | 189.9 | 200.9 | 200.2 | 211.9 |
| P2 | 75.2 | 108.7 | 123.6 | 116.2 | 109.0 | 99.7 | 91.2 |
| P3 | 74.8 | 117.0 | 149.2 | 161.5 | 163.3 | 167.7 | 149.5 |

## overall tok/s per scenario (all runs pooled)

| Metric | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| mean | 74.8 | 116.6 | 145.4 | 155.0 | 157.2 | 155.9 | 150.1 |
| median | 74.8 | 117.0 | 149.2 | 161.5 | 163.3 | 167.7 | 149.5 |

## draft acceptance per prompt per scenario -- median (min-max over runs)

| Prompt | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|
| P1 | 0.9725 (0.9615-0.9796) | 0.9420 (0.9322-0.9457) | 0.9401 (0.8923-0.9502) | 0.8655 (0.8576-0.8934) | 0.8222 (0.7947-0.8789) | 0.8247 (0.7890-0.8576) |
| P2 | 0.7386 (0.7358-0.7477) | 0.5811 (0.5253-0.6522) | 0.4342 (0.3797-0.4531) | 0.3648 (0.3527-0.3981) | 0.3015 (0.2492-0.3016) | 0.2685 (0.2071-0.3011) |
| P3 | 0.8927 (0.8685-0.9310) | 0.8156 (0.7963-0.8418) | 0.7412 (0.7410-0.7994) | 0.6598 (0.5792-0.6598) | 0.6400 (0.6196-0.6854) | 0.5354 (0.5256-0.5683) |

## draft acceptance per prompt -- pooled over all n scenarios and runs

| Prompt | min | max |
|---|---|---|
| P1 | 0.7890 | 0.9796 |
| P2 | 0.2071 | 0.7477 |
| P3 | 0.5256 | 0.9310 |

## all scenarios (all runs pooled)

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 74.8 | 74.8 | n/a-n/a |
| n1 | 116.6 | 117.0 | 0.7358-0.9796 |
| n2 | 145.4 | 149.2 | 0.5253-0.9457 |
| n3 | 155.0 | 161.5 | 0.3797-0.9502 |
| n4 | 157.2 | 163.3 | 0.3527-0.8934 |
| n5 | 155.9 | 167.7 | 0.2492-0.8789 |
| n6 | 150.1 | 149.5 | 0.2071-0.8576 |

Prompts:
- P1: write a python function that merges two sorted lists into one sorted list, with docstring.
- P2: explain the difference between mmap and read for loading large files, one paragraph.
- P3: write a bash script that watches a directory and prints new files as they appear.

#### Values for sudoingX/qwen38-mtp community table (baseline vs n2) ####

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 74.8 | 74.8 | n/a-n/a |
| n2 | 145.4 | 149.2 | 0.5253-0.9457 |
