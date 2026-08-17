## tok/s per prompt (median of runs)

| Prompt | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| P1 | 73.8 | 119.3 | 152.2 | 174.4 | 183.5 | 176.0 | 182.0 |
| P2 | 73.7 | 104.9 | 116.6 | 111.6 | 104.7 | 85.6 | 79.1 |
| P3 | 73.1 | 115.5 | 142.4 | 154.6 | 150.5 | 143.8 | 133.4 |

## overall tok/s per scenario (all runs pooled)

| Metric | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| mean | 73.5 | 112.6 | 135.9 | 148.1 | 143.0 | 137.5 | 132.3 |
| median | 73.7 | 115.5 | 142.4 | 154.6 | 150.5 | 143.8 | 133.4 |

## draft acceptance per prompt per scenario -- median (min-max over runs)

| Prompt | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|
| P1 | 0.9559 (0.9559-0.9767) | 0.9291 (0.8975-0.9303) | 0.9182 (0.9125-0.9182) | 0.8827 (0.8605-0.8886) | 0.7930 (0.7891-0.8845) | 0.7925 (0.7733-0.8153) |
| P2 | 0.7121 (0.6222-0.7245) | 0.5893 (0.5281-0.5946) | 0.4583 (0.4500-0.5399) | 0.3977 (0.2917-0.4444) | 0.2846 (0.2625-0.3812) | 0.2500 (0.2484-0.3129) |
| P3 | 0.8910 (0.8472-0.9062) | 0.8173 (0.7756-0.8389) | 0.7686 (0.7568-0.8299) | 0.6799 (0.5589-0.6871) | 0.6085 (0.5380-0.6366) | 0.5352 (0.5137-0.5381) |

## draft acceptance per prompt -- pooled over all n scenarios and runs

| Prompt | min | max |
|---|---|---|
| P1 | 0.7733 | 0.9767 |
| P2 | 0.2484 | 0.7245 |
| P3 | 0.5137 | 0.9062 |

## all scenarios (all runs pooled)

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 73.5 | 73.7 | n/a-n/a |
| n1 | 112.6 | 115.5 | 0.6222-0.9767 |
| n2 | 135.9 | 142.4 | 0.5281-0.9303 |
| n3 | 148.1 | 154.6 | 0.4500-0.9182 |
| n4 | 143.0 | 150.5 | 0.2917-0.8886 |
| n5 | 137.5 | 143.8 | 0.2625-0.8845 |
| n6 | 132.3 | 133.4 | 0.2484-0.8153 |

Prompts:
- P1: write a python function that merges two sorted lists into one sorted list, with docstring.
- P2: explain the difference between mmap and read for loading large files, one paragraph.
- P3: write a bash script that watches a directory and prints new files as they appear.

#### Values for sudoingX/qwen38-mtp community table (baseline vs n2) ####

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 73.5 | 73.7 | n/a-n/a |
| n2 | 135.9 | 142.4 | 0.5281-0.9303 |
