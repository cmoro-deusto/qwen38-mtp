## tok/s per prompt (median of runs)

| Prompt | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| P1 | 74.9 | 120.8 | 160.4 | 186.0 | 198.8 | 202.9 | 207.1 |
| P2 | 74.8 | 107.7 | 118.3 | 123.4 | 114.3 | 99.8 | 91.9 |
| P3 | 74.5 | 116.1 | 150.4 | 166.7 | 171.1 | 165.5 | 160.5 |

## overall tok/s per scenario (all runs pooled)

| Metric | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| mean | 74.8 | 114.8 | 144.2 | 159.2 | 157.2 | 156.3 | 152.5 |
| median | 74.8 | 116.1 | 150.4 | 166.7 | 171.1 | 165.5 | 160.5 |

## draft acceptance per prompt per scenario -- median (min-max over runs)

| Prompt | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|
| P1 | 0.9565 (0.9510-0.9598) | 0.9213 (0.9139-0.9491) | 0.9205 (0.8838-0.9524) | 0.8656 (0.8539-0.9234) | 0.8231 (0.7751-0.8750) | 0.7980 (0.7460-0.8075) |
| P2 | 0.7255 (0.7158-0.7423) | 0.5435 (0.5357-0.6125) | 0.4907 (0.4810-0.5333) | 0.3935 (0.3446-0.3956) | 0.3043 (0.2623-0.3231) | 0.2689 (0.2247-0.3272) |
| P3 | 0.8732 (0.8645-0.8913) | 0.8267 (0.8108-0.8517) | 0.7722 (0.7712-0.7910) | 0.7000 (0.4591-0.7188) | 0.6292 (0.5889-0.6953) | 0.5849 (0.5693-0.6157) |

## draft acceptance per prompt -- pooled over all n scenarios and runs

| Prompt | min | max |
|---|---|---|
| P1 | 0.7460 | 0.9598 |
| P2 | 0.2247 | 0.7423 |
| P3 | 0.4591 | 0.8913 |

## all scenarios (all runs pooled)

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 74.8 | 74.8 | n/a-n/a |
| n1 | 114.8 | 116.1 | 0.7158-0.9598 |
| n2 | 144.2 | 150.4 | 0.5357-0.9491 |
| n3 | 159.2 | 166.7 | 0.4810-0.9524 |
| n4 | 157.2 | 171.1 | 0.3446-0.9234 |
| n5 | 156.3 | 165.5 | 0.2623-0.8750 |
| n6 | 152.5 | 160.5 | 0.2247-0.8075 |

Prompts:
- P1: write a python function that merges two sorted lists into one sorted list, with docstring.
- P2: explain the difference between mmap and read for loading large files, one paragraph.
- P3: write a bash script that watches a directory and prints new files as they appear.

#### Values for sudoingX/qwen38-mtp community table (baseline vs n2) ####

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 74.8 | 74.8 | n/a-n/a |
| n2 | 144.2 | 150.4 | 0.5357-0.9491 |
