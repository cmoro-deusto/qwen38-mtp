## tok/s per prompt (median of runs)

| Prompt | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| P1 | 74.6 | 122.1 | 163.1 | 182.9 | 205.5 | 201.6 | 206.0 |
| P2 | 74.9 | 108.2 | 123.9 | 117.7 | 113.6 | 107.9 | 91.0 |
| P3 | 74.6 | 118.0 | 150.2 | 147.6 | 175.8 | 143.7 | 155.1 |

## overall tok/s per scenario (all runs pooled)

| Metric | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| mean | 74.7 | 115.9 | 145.4 | 150.3 | 161.8 | 153.4 | 150.5 |
| median | 74.6 | 118.0 | 150.2 | 147.6 | 175.8 | 143.7 | 155.1 |

## draft acceptance per prompt per scenario -- median (min-max over runs)

| Prompt | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|
| P1 | 0.9686 (0.9415-0.9792) | 0.9522 (0.8979-0.9531) | 0.8937 (0.8923-0.9094) | 0.9024 (0.8411-0.9344) | 0.8211 (0.8076-0.8889) | 0.8125 (0.7909-0.8655) |
| P2 | 0.7207 (0.7089-0.7324) | 0.5915 (0.5570-0.6139) | 0.4459 (0.4292-0.4831) | 0.3833 (0.3459-0.4195) | 0.3484 (0.2962-0.3955) | 0.2639 (0.2434-0.2821) |
| P3 | 0.8852 (0.8685-0.8863) | 0.8356 (0.8152-0.9048) | 0.6494 (0.6265-0.6915) | 0.7247 (0.5962-0.7429) | 0.5217 (0.4495-0.6394) | 0.5662 (0.5085-0.5691) |

## draft acceptance per prompt -- pooled over all n scenarios and runs

| Prompt | min | max |
|---|---|---|
| P1 | 0.7909 | 0.9792 |
| P2 | 0.2434 | 0.7324 |
| P3 | 0.4495 | 0.9048 |

## all scenarios (all runs pooled)

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 74.7 | 74.6 | n/a-n/a |
| n1 | 115.9 | 118.0 | 0.7089-0.9792 |
| n2 | 145.4 | 150.2 | 0.5570-0.9531 |
| n3 | 150.3 | 147.6 | 0.4292-0.9094 |
| n4 | 161.8 | 175.8 | 0.3459-0.9344 |
| n5 | 153.4 | 143.7 | 0.2962-0.8889 |
| n6 | 150.5 | 155.1 | 0.2434-0.8655 |

Prompts:
- P1: write a python function that merges two sorted lists into one sorted list, with docstring.
- P2: explain the difference between mmap and read for loading large files, one paragraph.
- P3: write a bash script that watches a directory and prints new files as they appear.

#### Values for sudoingX/qwen38-mtp community table (baseline vs n2) ####

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 74.7 | 74.6 | n/a-n/a |
| n2 | 145.4 | 150.2 | 0.5570-0.9531 |
