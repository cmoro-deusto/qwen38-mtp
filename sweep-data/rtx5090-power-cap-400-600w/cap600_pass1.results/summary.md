## tok/s per prompt (median of runs)

| Prompt | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| P1 | 74.6 | 120.8 | 162.9 | 185.4 | 203.9 | 211.5 | 205.3 |
| P2 | 74.8 | 106.6 | 125.8 | 125.0 | 113.1 | 105.2 | 100.0 |
| P3 | 74.8 | 118.0 | 154.0 | 157.0 | 164.9 | 153.5 | 159.2 |

## overall tok/s per scenario (all runs pooled)

| Metric | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| mean | 74.7 | 114.9 | 146.6 | 155.1 | 160.1 | 157.6 | 154.4 |
| median | 74.8 | 118.0 | 154.0 | 157.0 | 164.9 | 153.5 | 159.2 |

## draft acceptance per prompt per scenario -- median (min-max over runs)

| Prompt | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|
| P1 | 0.9510 (0.9320-0.9655) | 0.9398 (0.8926-0.9440) | 0.8951 (0.8836-0.9167) | 0.8782 (0.8583-0.8864) | 0.8407 (0.7848-0.8861) | 0.7786 (0.7559-0.8056) |
| P2 | 0.6939 (0.6212-0.7468) | 0.5897 (0.5500-0.6159) | 0.4928 (0.4222-0.5196) | 0.3639 (0.3506-0.3917) | 0.3170 (0.2831-0.3304) | 0.2917 (0.2392-0.2941) |
| P3 | 0.9000 (0.8821-0.9043) | 0.8507 (0.8088-0.8508) | 0.6995 (0.6717-0.7196) | 0.6516 (0.5780-0.6796) | 0.5449 (0.4896-0.6718) | 0.5602 (0.5507-0.5933) |

## draft acceptance per prompt -- pooled over all n scenarios and runs

| Prompt | min | max |
|---|---|---|
| P1 | 0.7559 | 0.9655 |
| P2 | 0.2392 | 0.7468 |
| P3 | 0.4896 | 0.9043 |

## all scenarios (all runs pooled)

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 74.7 | 74.8 | n/a-n/a |
| n1 | 114.9 | 118.0 | 0.6212-0.9655 |
| n2 | 146.6 | 154.0 | 0.5500-0.9440 |
| n3 | 155.1 | 157.0 | 0.4222-0.9167 |
| n4 | 160.1 | 164.9 | 0.3506-0.8864 |
| n5 | 157.6 | 153.5 | 0.2831-0.8861 |
| n6 | 154.4 | 159.2 | 0.2392-0.8056 |

Prompts:
- P1: write a python function that merges two sorted lists into one sorted list, with docstring.
- P2: explain the difference between mmap and read for loading large files, one paragraph.
- P3: write a bash script that watches a directory and prints new files as they appear.

#### Values for sudoingX/qwen38-mtp community table (baseline vs n2) ####

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 74.7 | 74.8 | n/a-n/a |
| n2 | 146.6 | 154.0 | 0.5500-0.9440 |
