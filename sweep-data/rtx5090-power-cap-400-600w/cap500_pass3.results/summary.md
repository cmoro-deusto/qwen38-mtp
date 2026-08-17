## tok/s per prompt (median of runs)

| Prompt | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| P1 | 74.8 | 120.9 | 159.3 | 177.9 | 192.9 | 192.4 | 193.4 |
| P2 | 74.9 | 108.2 | 118.3 | 106.6 | 108.4 | 100.5 | 78.6 |
| P3 | 74.1 | 117.7 | 147.6 | 161.3 | 170.4 | 146.1 | 145.7 |

## overall tok/s per scenario (all runs pooled)

| Metric | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| mean | 74.6 | 115.3 | 141.3 | 150.0 | 154.5 | 147.1 | 138.6 |
| median | 74.8 | 117.7 | 147.6 | 161.3 | 170.4 | 146.1 | 145.7 |

## draft acceptance per prompt per scenario -- median (min-max over runs)

| Prompt | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|
| P1 | 0.9557 (0.9510-0.9559) | 0.9491 (0.9353-0.9526) | 0.8923 (0.8715-0.9237) | 0.8733 (0.8583-0.8886) | 0.8205 (0.8056-0.8474) | 0.7928 (0.7443-0.8333) |
| P2 | 0.7374 (0.7368-0.7553) | 0.5704 (0.4740-0.6452) | 0.3915 (0.3593-0.5056) | 0.3770 (0.3730-0.3852) | 0.3284 (0.3153-0.3474) | 0.2246 (0.2245-0.2517) |
| P3 | 0.9043 (0.7928-0.9101) | 0.8389 (0.8092-0.8480) | 0.7664 (0.6854-0.8462) | 0.7349 (0.5932-0.7375) | 0.5706 (0.5684-0.6000) | 0.5504 (0.4805-0.5729) |

## draft acceptance per prompt -- pooled over all n scenarios and runs

| Prompt | min | max |
|---|---|---|
| P1 | 0.7443 | 0.9559 |
| P2 | 0.2245 | 0.7553 |
| P3 | 0.4805 | 0.9101 |

## all scenarios (all runs pooled)

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 74.6 | 74.8 | n/a-n/a |
| n1 | 115.3 | 117.7 | 0.7368-0.9559 |
| n2 | 141.3 | 147.6 | 0.4740-0.9526 |
| n3 | 150.0 | 161.3 | 0.3593-0.9237 |
| n4 | 154.5 | 170.4 | 0.3730-0.8886 |
| n5 | 147.1 | 146.1 | 0.3153-0.8474 |
| n6 | 138.6 | 145.7 | 0.2245-0.8333 |

Prompts:
- P1: write a python function that merges two sorted lists into one sorted list, with docstring.
- P2: explain the difference between mmap and read for loading large files, one paragraph.
- P3: write a bash script that watches a directory and prints new files as they appear.

#### Values for sudoingX/qwen38-mtp community table (baseline vs n2) ####

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 74.6 | 74.8 | n/a-n/a |
| n2 | 141.3 | 147.6 | 0.4740-0.9526 |
