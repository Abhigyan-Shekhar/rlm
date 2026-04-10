# Accuracy Report

This report scores the completed local Ollama `qwen2.5:7b` batch using task-specific deterministic rubrics. Nonzero-exit runs are scored as `0.0` because the benchmark is end-to-end.

## Rubric Summary

| Benchmark | Metric | Score Range |
| --- | --- | --- |
| Battle of the Bastards | Binary: answer must identify Jon Snow and either Sansa Stark or the Knights of the Vale as the decisive ally. | 0 or 1 |
| AuthProxy Long Context | Five-part fact score: Q1–Q3 current value `7`, Q4 active-production sentence, Q5 no-automatic-failover conclusion. | 0 to 1 |
| Clinical Long Context | Five-part score: Q1–Q3 `PCN-HIGH`, Q4 renal-monitoring sentence, Q5 three-step reasoning chain. | 0 to 1 |
| Launch Note App | Ten-point checklist: goal, weekly milestones, tasks, dependencies, tools, risks, mitigations, 30-day timeline, student grounding, budget/team grounding. | 0 to 1 |
| PDF Cersei Warning | Binary exact-quote match after whitespace normalization. | 0 or 1 |
| Under-specified TSP | Binary groundedness: explicit refusal because the distance matrix is missing. | 0 or 1 |
| Stochastic Adaptive TSP | `0.5` for exact expected cost `22.75`, `0.25` each for the correct initial actions `A,0.5→C` and `A,2.0→B`. | 0 to 1 |

## Aggregate Accuracy

| Benchmark | Mode | Runs | Mean | Median | Min | Max | Std |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Battle of the Bastards | LLM | 5 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 |
| Battle of the Bastards | RLM | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| AuthProxy Long Context | LLM | 5 | 1.000 | 1.000 | 1.000 | 1.000 | 0.000 |
| AuthProxy Long Context | RLM | 5 | 0.480 | 0.400 | 0.000 | 1.000 | 0.371 |
| Clinical Long Context | LLM | 5 | 0.800 | 1.000 | 0.000 | 1.000 | 0.400 |
| Clinical Long Context | RLM | 5 | 0.187 | 0.000 | 0.000 | 0.933 | 0.373 |
| Launch Note App | LLM | 5 | 0.860 | 0.900 | 0.800 | 0.900 | 0.049 |
| Launch Note App | RLM | 5 | 0.180 | 0.000 | 0.000 | 0.600 | 0.240 |
| PDF Cersei Warning | LLM | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| PDF Cersei Warning | RLM | 5 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Under-specified TSP | LLM | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Under-specified TSP | RLM | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Stochastic Adaptive TSP | LLM | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| Stochastic Adaptive TSP | RLM | 3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |

![Average Accuracy by Benchmark](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260410-082745-ollama-qwen2.5-14b/graphs/avg_accuracy_by_benchmark.png)

![Per-Run Accuracy](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260410-082745-ollama-qwen2.5-14b/graphs/per_run_accuracy.png)

## Full Accuracy Rows

### Battle of the Bastards

| Run | Mode | Exit | Accuracy | Note |
| --- | --- | ---: | ---: | --- |
| 001 | LLM | 0 | 1.000 | jon+ally |
| 001 | RLM | 0 | 0.000 | missing jon or ally |
| 002 | LLM | 0 | 1.000 | jon+ally |
| 002 | RLM | 0 | 0.000 | missing jon or ally |
| 003 | LLM | 0 | 1.000 | jon+ally |
| 003 | RLM | 0 | 0.000 | missing jon or ally |
| 004 | LLM | 0 | 1.000 | jon+ally |
| 004 | RLM | 0 | 0.000 | missing jon or ally |
| 005 | LLM | 0 | 1.000 | jon+ally |
| 005 | RLM | 0 | 0.000 | missing jon or ally |

### AuthProxy Long Context

| Run | Mode | Exit | Accuracy | Note |
| --- | --- | ---: | ---: | --- |
| 001 | LLM | 0 | 1.000 | q123=1/1/1,q4=1,q5=1 |
| 001 | RLM | 0 | 0.800 | q123=1/1/1,q4=0,q5=1 |
| 002 | LLM | 0 | 1.000 | q123=1/1/1,q4=1,q5=1 |
| 002 | RLM | 0 | 0.000 | q123=0/0/0,q4=0,q5=0 |
| 003 | LLM | 0 | 1.000 | q123=1/1/1,q4=1,q5=1 |
| 003 | RLM | 0 | 0.400 | q123=0/0/0,q4=1,q5=1 |
| 004 | LLM | 0 | 1.000 | q123=1/1/1,q4=1,q5=1 |
| 004 | RLM | 0 | 1.000 | q123=1/1/1,q4=1,q5=1 |
| 005 | LLM | 0 | 1.000 | q123=1/1/1,q4=1,q5=1 |
| 005 | RLM | 0 | 0.200 | q123=0/0/0,q4=0,q5=1 |

### Clinical Long Context

| Run | Mode | Exit | Accuracy | Note |
| --- | --- | ---: | ---: | --- |
| 001 | LLM | 0 | 1.000 | q123=1/1/1,q4=1,q5=1.00 |
| 001 | RLM | 0 | 0.933 | q123=1/1/1,q4=1,q5=0.67 |
| 002 | LLM | 0 | 1.000 | q123=1/1/1,q4=1,q5=1.00 |
| 002 | RLM | 0 | 0.000 | q123=0/0/0,q4=0,q5=0.00 |
| 003 | LLM | 1 | 0.000 | nonzero exit |
| 003 | RLM | 0 | 0.000 | q123=0/0/0,q4=0,q5=0.00 |
| 004 | LLM | 0 | 1.000 | q123=1/1/1,q4=1,q5=1.00 |
| 004 | RLM | 0 | 0.000 | q123=0/0/0,q4=0,q5=0.00 |
| 005 | LLM | 0 | 1.000 | q123=1/1/1,q4=1,q5=1.00 |
| 005 | RLM | 0 | 0.000 | q123=0/0/0,q4=0,q5=0.00 |

### Launch Note App

| Run | Mode | Exit | Accuracy | Note |
| --- | --- | ---: | ---: | --- |
| 001 | LLM | 0 | 0.800 | goal,weeks,tasks,dependencies,tools,risks,mitigation,timeline |
| 001 | RLM | 0 | 0.000 | none |
| 002 | LLM | 0 | 0.900 | goal,weeks,tasks,dependencies,tools,risks,mitigation,timeline,users |
| 002 | RLM | 0 | 0.600 | goal,tasks,dependencies,timeline,users,resources |
| 003 | LLM | 0 | 0.900 | goal,weeks,tasks,dependencies,tools,risks,mitigation,timeline,users |
| 003 | RLM | 0 | 0.000 | none |
| 004 | LLM | 0 | 0.800 | goal,weeks,tasks,dependencies,tools,risks,mitigation,timeline |
| 004 | RLM | 0 | 0.300 | weeks,tasks,dependencies |
| 005 | LLM | 0 | 0.900 | goal,weeks,tasks,dependencies,tools,risks,mitigation,timeline,users |
| 005 | RLM | 0 | 0.000 | none |

### PDF Cersei Warning

| Run | Mode | Exit | Accuracy | Note |
| --- | --- | ---: | ---: | --- |
| 001 | LLM | 0 | 0.000 | quote missing |
| 001 | RLM | 0 | 0.000 | quote missing |
| 002 | LLM | 0 | 0.000 | quote missing |
| 002 | RLM | 0 | 0.000 | quote missing |
| 003 | LLM | 0 | 0.000 | quote missing |
| 003 | RLM | 0 | 0.000 | quote missing |
| 004 | LLM | 1 | 0.000 | nonzero exit |
| 004 | RLM | 0 | 0.000 | quote missing |
| 005 | LLM | 0 | 0.000 | quote missing |
| 005 | RLM | 0 | 0.000 | quote missing |

### Under-specified TSP

| Run | Mode | Exit | Accuracy | Note |
| --- | --- | ---: | ---: | --- |
| 001 | LLM | 1 | 0.000 | nonzero exit |
| 001 | RLM | 1 | 0.000 | nonzero exit |
| 002 | LLM | 0 | 0.000 | hallucinated solve |
| 002 | RLM | 0 | 0.000 | hallucinated solve |
| 003 | LLM | 0 | 0.000 | hallucinated solve |
| 003 | RLM | 1 | 0.000 | nonzero exit |

### Stochastic Adaptive TSP

| Run | Mode | Exit | Accuracy | Note |
| --- | --- | ---: | ---: | --- |
| 001 | LLM | 1 | 0.000 | nonzero exit |
| 001 | RLM | 1 | 0.000 | nonzero exit |
| 002 | LLM | 1 | 0.000 | nonzero exit |
| 002 | RLM | 1 | 0.000 | nonzero exit |
| 003 | LLM | 1 | 0.000 | nonzero exit |
| 003 | RLM | 1 | 0.000 | nonzero exit |
