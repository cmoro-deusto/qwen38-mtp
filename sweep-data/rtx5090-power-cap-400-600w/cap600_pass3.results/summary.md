## tok/s per prompt (median of runs)

| Prompt | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| P1 | 74.4 | 122.1 | 166.0 | 185.4 | 204.4 | 203.0 | 208.1 |
| P2 | 74.9 | 109.9 | 125.1 | 123.7 | 130.3 | 106.7 | 96.8 |
| P3 | 74.7 | 118.1 | 136.3 | 156.5 | 160.3 | 170.1 | 152.3 |

## overall tok/s per scenario (all runs pooled)

| Metric | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| mean | 74.7 | 116.6 | 144.6 | 155.5 | 163.1 | 163.0 | 153.6 |
| median | 74.7 | 118.1 | 136.3 | 156.5 | 160.3 | 170.1 | 152.3 |

## draft acceptance per prompt per scenario -- median (min-max over runs)

| Prompt | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|
| P1 | 0.9692 (0.9510-0.9721) | 0.9491 (0.9426-0.9704) | 0.8951 (0.8620-0.9097) | 0.8675 (0.8631-0.8877) | 0.8129 (0.8000-0.8735) | 0.8033 (0.7587-0.8282) |
| P2 | 0.7523 (0.6941-0.7600) | 0.5824 (0.5645-0.6299) | 0.4731 (0.4553-0.5342) | 0.4575 (0.3566-0.4576) | 0.3241 (0.3224-0.3406) | 0.2763 (0.2683-0.3125) |
| P3 | 0.9077 (0.9016-0.9167) | 0.6916 (0.6866-0.8267) | 0.6974 (0.6897-0.7113) | 0.6166 (0.5907-0.6384) | 0.6348 (0.6295-0.7255) | 0.5243 (0.4696-0.5955) |

## draft acceptance per prompt -- pooled over all n scenarios and runs

| Prompt | min | max |
|---|---|---|
| P1 | 0.7587 | 0.9721 |
| P2 | 0.2683 | 0.7600 |
| P3 | 0.4696 | 0.9167 |

## all scenarios (all runs pooled)

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 74.7 | 74.7 | n/a-n/a |
| n1 | 116.6 | 118.1 | 0.6941-0.9721 |
| n2 | 144.6 | 136.3 | 0.5645-0.9704 |
| n3 | 155.5 | 156.5 | 0.4553-0.9097 |
| n4 | 163.1 | 160.3 | 0.3566-0.8877 |
| n5 | 163.0 | 170.1 | 0.3224-0.8735 |
| n6 | 153.6 | 152.3 | 0.2683-0.8282 |

Prompts:
- P1: write a python function that merges two sorted lists into one sorted list, with docstring.
- P2: explain the difference between mmap and read for loading large files, one paragraph.
- P3: write a bash script that watches a directory and prints new files as they appear.

#### Values for sudoingX/qwen38-mtp community table (baseline vs n2) ####

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 74.7 | 74.7 | n/a-n/a |
| n2 | 144.6 | 136.3 | 0.5645-0.9704 |
