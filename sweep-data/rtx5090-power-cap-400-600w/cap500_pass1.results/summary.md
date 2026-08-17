## tok/s per prompt (median of runs)

| Prompt | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| P1 | 74.7 | 120.3 | 159.4 | 180.8 | 194.6 | 186.9 | 200.6 |
| P2 | 74.7 | 107.9 | 111.2 | 122.9 | 106.9 | 101.3 | 96.1 |
| P3 | 74.3 | 115.8 | 142.8 | 160.4 | 145.7 | 143.1 | 154.6 |

## overall tok/s per scenario (all runs pooled)

| Metric | baseline | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|---|
| mean | 74.6 | 114.7 | 139.6 | 152.8 | 151.5 | 148.1 | 149.2 |
| median | 74.5 | 115.8 | 142.8 | 160.4 | 145.7 | 143.1 | 154.6 |

## draft acceptance per prompt per scenario -- median (min-max over runs)

| Prompt | n1 | n2 | n3 | n4 | n5 | n6 |
|---|---|---|---|---|---|---|
| P1 | 0.9559 (0.9489-0.9674) | 0.9419 (0.9380-0.9457) | 0.8981 (0.8639-0.8981) | 0.8835 (0.8607-0.9199) | 0.7910 (0.7870-0.8880) | 0.8125 (0.7488-0.8485) |
| P2 | 0.7283 (0.6989-0.7500) | 0.5060 (0.4589-0.6575) | 0.5141 (0.4094-0.5260) | 0.3773 (0.3462-0.4153) | 0.3333 (0.3183-0.3676) | 0.3136 (0.3119-0.3167) |
| P3 | 0.8863 (0.8830-0.9000) | 0.7948 (0.7839-0.8239) | 0.7631 (0.7057-0.8081) | 0.5895 (0.5886-0.6968) | 0.5560 (0.5380-0.6795) | 0.5909 (0.5427-0.6361) |

## draft acceptance per prompt -- pooled over all n scenarios and runs

| Prompt | min | max |
|---|---|---|
| P1 | 0.7488 | 0.9674 |
| P2 | 0.3119 | 0.7500 |
| P3 | 0.5380 | 0.9000 |

## all scenarios (all runs pooled)

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 74.6 | 74.5 | n/a-n/a |
| n1 | 114.7 | 115.8 | 0.6989-0.9674 |
| n2 | 139.6 | 142.8 | 0.4589-0.9457 |
| n3 | 152.8 | 160.4 | 0.4094-0.8981 |
| n4 | 151.5 | 145.7 | 0.3462-0.9199 |
| n5 | 148.1 | 143.1 | 0.3183-0.8880 |
| n6 | 149.2 | 154.6 | 0.3119-0.8485 |

Prompts:
- P1: write a python function that merges two sorted lists into one sorted list, with docstring.
- P2: explain the difference between mmap and read for loading large files, one paragraph.
- P3: write a bash script that watches a directory and prints new files as they appear.

#### Values for sudoingX/qwen38-mtp community table (baseline vs n2) ####

| Scenario | mean | median | acc (min-max) |
|---|---|---|---|
| baseline | 74.6 | 74.5 | n/a-n/a |
| n2 | 139.6 | 142.8 | 0.4589-0.9457 |
