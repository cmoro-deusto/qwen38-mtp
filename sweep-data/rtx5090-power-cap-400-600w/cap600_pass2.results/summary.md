## tok/s per prompt (median of runs)

| Prompt | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| P1 | 75.1 | 121.1 | 163.4 | 186.4 | 202.7 | 203.0 | 199.5 |
| P2 | 75.5 | 106.4 | 121.1 | 116.6 | 116.2 | 111.2 | 95.0 |
| P3 | 74.5 | 119.4 | 145.0 | 165.8 | 168.3 | 158.6 | 167.2 |

## overall tok/s per scenario (all runs pooled)

| Metric | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| mean | 75.0 | 115.7 | 142.1 | 157.5 | 163.1 | 158.5 | 151.6 |
| median | 75.1 | 119.4 | 145.0 | 165.8 | 168.3 | 158.6 | 167.2 |

## draft acceptance per prompt per scenario -- median (min-max over runs)

| Prompt | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|
| P1 | 0.9516 (0.9463-0.9606) | 0.9420 (0.9113-0.9524) | 0.8997 (0.8675-0.9538) | 0.8631 (0.8434-0.8818) | 0.7974 (0.7842-0.8231) | 0.7460 (0.7320-0.7700) |
| P2 | 0.6961 (0.6893-0.7429) | 0.5614 (0.5112-0.5823) | 0.4286 (0.4211-0.4923) | 0.3810 (0.3715-0.4008) | 0.3462 (0.3096-0.3651) | 0.2647 (0.2157-0.2768) |
| P3 | 0.9254 (0.8827-0.9320) | 0.7732 (0.7337-0.7814) | 0.7500 (0.7031-0.8034) | 0.6690 (0.6549-0.7060) | 0.5770 (0.5360-0.6759) | 0.5882 (0.5364-0.6052) |

## draft acceptance per prompt -- pooled over all n scenarios and runs

| Prompt | min | max |
|---|---|---|
| P1 | 0.7320 | 0.9606 |
| P2 | 0.2157 | 0.7429 |
| P3 | 0.5360 | 0.9320 |

## all scenarios (all runs pooled)

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 75.0 | 75.1 | n/a-n/a |
| n1 | 115.7 | 119.4 | 0.6893-0.9606 |
| n2 | 142.1 | 145.0 | 0.5112-0.9524 |
| n3 | 157.5 | 165.8 | 0.4211-0.9538 |
| n4 | 163.1 | 168.3 | 0.3715-0.8818 |
| n5 | 158.5 | 158.6 | 0.3096-0.8231 |
| n6 | 151.6 | 167.2 | 0.2157-0.7700 |

Prompts:
- P1: write a python function that merges two sorted lists into one sorted list, with docstring.
- P2: explain the difference between mmap and read for loading large files, one paragraph.
- P3: write a bash script that watches a directory and prints new files as they appear.

#### Values for sudoingX/qwen38-mtp community table (baseline vs n2) ####

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 75.0 | 75.1 | n/a-n/a |
| n2 | 142.1 | 145.0 | 0.5112-0.9524 |
