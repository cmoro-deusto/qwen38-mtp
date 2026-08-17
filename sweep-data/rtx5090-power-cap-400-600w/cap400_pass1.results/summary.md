## tok/s per prompt (median of runs)

| Prompt | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| P1 | 71.3 | 114.6 | 144.2 | 165.1 | 166.5 | 170.2 | 167.4 |
| P2 | 71.6 | 101.2 | 111.7 | 102.5 | 93.7 | 86.3 | 76.5 |
| P3 | 70.9 | 111.0 | 136.1 | 134.8 | 141.5 | 123.8 | 129.9 |

## overall tok/s per scenario (all runs pooled)

| Metric | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| mean | 71.3 | 109.0 | 128.9 | 134.9 | 133.7 | 126.9 | 123.7 |
| median | 71.3 | 111.0 | 136.1 | 134.8 | 141.5 | 123.8 | 129.9 |

## draft acceptance per prompt per scenario -- median (min-max over runs)

| Prompt | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|
| P1 | 0.9655 (0.9650-0.9795) | 0.9317 (0.9250-0.9351) | 0.9510 (0.9097-0.9514) | 0.8553 (0.7723-0.8732) | 0.8385 (0.8159-0.8429) | 0.7868 (0.7015-0.8259) |
| P2 | 0.7100 (0.7089-0.7128) | 0.5929 (0.5306-0.6266) | 0.4583 (0.4416-0.4718) | 0.3667 (0.3443-0.4516) | 0.3346 (0.2842-0.4000) | 0.2759 (0.2738-0.2985) |
| P3 | 0.8908 (0.8774-0.9096) | 0.8418 (0.6706-0.8855) | 0.7057 (0.6915-0.7933) | 0.6960 (0.6479-0.7494) | 0.5531 (0.5321-0.5787) | 0.5680 (0.5172-0.6045) |

## draft acceptance per prompt -- pooled over all n scenarios and runs

| Prompt | min | max |
|---|---|---|
| P1 | 0.7015 | 0.9795 |
| P2 | 0.2738 | 0.7128 |
| P3 | 0.5172 | 0.9096 |

## all scenarios (all runs pooled)

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 71.3 | 71.3 | n/a-n/a |
| n1 | 109.0 | 111.0 | 0.7089-0.9795 |
| n2 | 128.9 | 136.1 | 0.5306-0.9351 |
| n3 | 134.9 | 134.8 | 0.4416-0.9514 |
| n4 | 133.7 | 141.5 | 0.3443-0.8732 |
| n5 | 126.9 | 123.8 | 0.2842-0.8429 |
| n6 | 123.7 | 129.9 | 0.2738-0.8259 |

Prompts:
- P1: write a python function that merges two sorted lists into one sorted list, with docstring.
- P2: explain the difference between mmap and read for loading large files, one paragraph.
- P3: write a bash script that watches a directory and prints new files as they appear.

#### Values for sudoingX/qwen38-mtp community table (baseline vs n2) ####

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 71.3 | 71.3 | n/a-n/a |
| n2 | 128.9 | 136.1 | 0.5306-0.9351 |
