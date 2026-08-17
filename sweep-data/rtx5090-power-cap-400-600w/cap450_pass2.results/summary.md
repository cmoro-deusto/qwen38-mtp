## tok/s per prompt (median of runs)

| Prompt | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| P1 | 73.4 | 118.3 | 152.8 | 172.3 | 180.9 | 176.2 | 178.3 |
| P2 | 73.9 | 110.8 | 116.9 | 113.1 | 108.9 | 99.2 | 83.3 |
| P3 | 73.1 | 114.9 | 138.4 | 143.8 | 141.1 | 146.1 | 139.0 |

## overall tok/s per scenario (all runs pooled)

| Metric | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| mean | 73.5 | 114.4 | 135.8 | 142.4 | 142.7 | 140.5 | 132.1 |
| median | 73.4 | 114.9 | 138.4 | 143.8 | 141.1 | 146.1 | 139.0 |

## draft acceptance per prompt per scenario -- median (min-max over runs)

| Prompt | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|
| P1 | 0.9606 (0.9579-0.9718) | 0.9344 (0.9181-0.9353) | 0.9065 (0.8755-0.9065) | 0.8656 (0.8631-0.8916) | 0.7930 (0.7808-0.8409) | 0.7773 (0.7371-0.8282) |
| P2 | 0.8100 (0.7528-0.8242) | 0.5854 (0.5663-0.6000) | 0.4688 (0.4430-0.4755) | 0.4225 (0.3826-0.4231) | 0.3551 (0.3043-0.4107) | 0.2817 (0.2662-0.3011) |
| P3 | 0.8862 (0.8762-0.8916) | 0.7919 (0.7547-0.8421) | 0.6983 (0.6962-0.7280) | 0.6214 (0.5886-0.6328) | 0.6286 (0.5190-0.7045) | 0.5752 (0.4417-0.5787) |

## draft acceptance per prompt -- pooled over all n scenarios and runs

| Prompt | min | max |
|---|---|---|
| P1 | 0.7371 | 0.9718 |
| P2 | 0.2662 | 0.8242 |
| P3 | 0.4417 | 0.8916 |

## all scenarios (all runs pooled)

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 73.5 | 73.4 | n/a-n/a |
| n1 | 114.4 | 114.9 | 0.7528-0.9718 |
| n2 | 135.8 | 138.4 | 0.5663-0.9353 |
| n3 | 142.4 | 143.8 | 0.4430-0.9065 |
| n4 | 142.7 | 141.1 | 0.3826-0.8916 |
| n5 | 140.5 | 146.1 | 0.3043-0.8409 |
| n6 | 132.1 | 139.0 | 0.2662-0.8282 |

Prompts:
- P1: write a python function that merges two sorted lists into one sorted list, with docstring.
- P2: explain the difference between mmap and read for loading large files, one paragraph.
- P3: write a bash script that watches a directory and prints new files as they appear.

#### Values for sudoingX/qwen38-mtp community table (baseline vs n2) ####

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 73.5 | 73.4 | n/a-n/a |
| n2 | 135.8 | 138.4 | 0.5663-0.9353 |
