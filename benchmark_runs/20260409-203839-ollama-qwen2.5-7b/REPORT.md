# RLM Local Ollama Benchmark Guide And Results

## Scope

This document covers only the local Ollama benchmark batch completed on `qwen2.5:7b`. It does not use or summarize any earlier Gemini runs.

## Environment

- Workspace: `/Users/abhigyanshekhar/Desktop/RLM-FULL`
- Backend: `ollama` through the OpenAI-compatible local endpoint
- Model: `qwen2.5:7b`
- Batch folder: `/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260409-203839-ollama-qwen2.5-7b`
- Run plan: `5` paired `LLM` / `RLM` runs for each benchmark

## Setup

```bash
cd /Users/abhigyanshekhar/Desktop/RLM-FULL
source .venv/bin/activate
uv pip install -e .
open -a Ollama
/Applications/Ollama.app/Contents/Resources/ollama pull qwen2.5:7b
export BENCHMARK_BACKEND=ollama
export OLLAMA_BASE_URL=http://127.0.0.1:11434/v1
export OLLAMA_MODEL_NAME=qwen2.5:7b
export OLLAMA_API_KEY=ollama
export BENCHMARK_COOLDOWN_SECONDS=0
```

## How The Run Artifacts Are Organized

The completed batch is already organized one folder per test. Each test folder contains the five `LLM` logs and five `RLM` logs as markdown files.

Example layout:

```text
benchmark_runs/20260409-203839-ollama-qwen2.5-7b/
  got/
    run_001_llm.md
    run_001_rlm.md
    ...
  authproxy/
    run_001_llm.md
    run_001_rlm.md
    ...
  clinical/
    run_001_llm.md
    run_001_rlm.md
    ...
  launch_note_app/
    run_001_llm.md
    run_001_rlm.md
    ...
  pdf_cersei_warning/
    run_001_llm.md
    run_001_rlm.md
    ...
  tsp_branch_bound/
    run_001_llm.md
    run_001_rlm.md
    ...
  stochastic_tsp/
    run_001_llm.md
    run_001_rlm.md
    ...
  SUMMARY.md
  aggregate_metrics.csv
  raw_data.csv
```

## Commands Used

Single pair example:

```bash
.venv/bin/python llm-test/test_tsp_llm_only.py
.venv/bin/python rlm-test/test_tsp_branch_bound.py
```

Full paired batch:

```bash
.venv/bin/python run_benchmark_pairs.py --backend ollama --model qwen2.5:7b --runs 5
```

## Aggregate Results

| Benchmark | Mode | Success | Avg Wall (s) | Median Wall (s) | Avg Input Tokens | Avg Output Tokens | Avg Total Tokens |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Battle of the Bastards | LLM | 5/5 (100%) | 8.351 | 7.631 | 275.000 | 37.400 | 312.400 |
| Battle of the Bastards | RLM | 5/5 (100%) | 131.152 | 116.849 | 11417.800 | 572.600 | 11990.400 |
| AuthProxy Long Context | LLM | 5/5 (100%) | 22.581 | 21.342 | 1082.000 | 169.200 | 1251.200 |
| AuthProxy Long Context | RLM | 5/5 (100%) | 162.951 | 131.030 | 12740.000 | 987.800 | 13727.800 |
| Clinical Long Context | LLM | 5/5 (100%) | 128.872 | 137.055 | 1645.000 | 1301.400 | 2946.400 |
| Clinical Long Context | RLM | 5/5 (100%) | 57.925 | 52.092 | 10663.000 | 341.800 | 11004.800 |
| Launch Note App | LLM | 5/5 (100%) | 115.264 | 107.300 | 257.000 | 1303.600 | 1560.600 |
| Launch Note App | RLM | 5/5 (100%) | 223.344 | 155.597 | 10052.400 | 1173.000 | 11225.400 |
| PDF Cersei Warning | LLM | 5/5 (100%) | 89.760 | 94.292 | 4096.000 | 624.000 | 4720.000 |
| PDF Cersei Warning | RLM | 4/5 (80%) | 185.983 | 204.865 | 17222.250 | 962.500 | 18184.750 |
| Under-specified TSP | LLM | 5/5 (100%) | 96.587 | 103.650 | 209.000 | 1147.800 | 1356.800 |
| Under-specified TSP | RLM | 5/5 (100%) | 518.505 | 492.472 | 20262.600 | 4253.800 | 24516.400 |
| Stochastic Adaptive TSP | LLM | 5/5 (100%) | 83.156 | 72.327 | 318.000 | 1177.600 | 1495.600 |
| Stochastic Adaptive TSP | RLM | 5/5 (100%) | 402.231 | 292.076 | 17058.200 | 3283.600 | 20341.800 |

## Wall Time Graph

| Benchmark | Mode | Avg Wall (s) | Relative Bar |
| --- | --- | --- | --- |
| Battle of the Bastards | LLM | 8.351 | # |
| Battle of the Bastards | RLM | 131.152 | ###### |
| AuthProxy Long Context | LLM | 22.581 | # |
| AuthProxy Long Context | RLM | 162.951 | ######## |
| Clinical Long Context | LLM | 128.872 | ###### |
| Clinical Long Context | RLM | 57.925 | ### |
| Launch Note App | LLM | 115.264 | ##### |
| Launch Note App | RLM | 223.344 | ########## |
| PDF Cersei Warning | LLM | 89.760 | #### |
| PDF Cersei Warning | RLM | 185.983 | ######### |
| Under-specified TSP | LLM | 96.587 | #### |
| Under-specified TSP | RLM | 518.505 | ######################## |
| Stochastic Adaptive TSP | LLM | 83.156 | #### |
| Stochastic Adaptive TSP | RLM | 402.231 | ################### |

## Token Usage Graph

| Benchmark | Mode | Avg Total Tokens | Relative Bar |
| --- | --- | --- | --- |
| Battle of the Bastards | LLM | 312.400 | # |
| Battle of the Bastards | RLM | 11990.400 | ############ |
| AuthProxy Long Context | LLM | 1251.200 | # |
| AuthProxy Long Context | RLM | 13727.800 | ############# |
| Clinical Long Context | LLM | 2946.400 | ### |
| Clinical Long Context | RLM | 11004.800 | ########### |
| Launch Note App | LLM | 1560.600 | ## |
| Launch Note App | RLM | 11225.400 | ########### |
| PDF Cersei Warning | LLM | 4720.000 | ##### |
| PDF Cersei Warning | RLM | 18184.750 | ################## |
| Under-specified TSP | LLM | 1356.800 | # |
| Under-specified TSP | RLM | 24516.400 | ######################## |
| Stochastic Adaptive TSP | LLM | 1495.600 | # |
| Stochastic Adaptive TSP | RLM | 20341.800 | #################### |

## Raw Data Notes

- All values below come from the markdown logs inside the completed local batch folder.
- `stochastic_tsp` run `004` on the `RLM` side exited with `-9`, so it is included in the raw table but excluded from aggregate averages.

## Raw Data Table

| Benchmark | Run | Mode | Exit | Wall (s) | Exec (s) | Input | Output | Total | Log |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Battle of the Bastards | 001 | LLM | 0 | 10.512 | 10.512 | 275 | 36 | 311 | `got/run_001_llm.md` |
| Battle of the Bastards | 001 | RLM | 0 | 138.139 | 126.449 | 11,828 | 455 | 12,283 | `got/run_001_rlm.md` |
| Battle of the Bastards | 002 | LLM | 0 | 7.247 | 7.247 | 275 | 38 | 313 | `got/run_002_llm.md` |
| Battle of the Bastards | 002 | RLM | 0 | 116.849 | 106.258 | 11,914 | 407 | 12,321 | `got/run_002_rlm.md` |
| Battle of the Bastards | 003 | LLM | 0 | 10.503 | 10.503 | 275 | 33 | 308 | `got/run_003_llm.md` |
| Battle of the Bastards | 003 | RLM | 0 | 109.263 | 103.557 | 12,387 | 515 | 12,902 | `got/run_003_rlm.md` |
| Battle of the Bastards | 004 | LLM | 0 | 5.864 | 5.864 | 275 | 44 | 319 | `got/run_004_llm.md` |
| Battle of the Bastards | 004 | RLM | 0 | 73.804 | 73.478 | 8,762 | 450 | 9,212 | `got/run_004_rlm.md` |
| Battle of the Bastards | 005 | LLM | 0 | 7.631 | 7.631 | 275 | 36 | 311 | `got/run_005_llm.md` |
| Battle of the Bastards | 005 | RLM | 0 | 217.703 | 154.300 | 12,198 | 1,036 | 13,234 | `got/run_005_rlm.md` |
| AuthProxy Long Context | 001 | LLM | 0 | 30.426 | 30.426 | 1,082 | 190 | 1,272 | `authproxy/run_001_llm.md` |
| AuthProxy Long Context | 001 | RLM | 0 | 316.270 | 256.959 | 14,016 | 1,921 | 15,937 | `authproxy/run_001_rlm.md` |
| AuthProxy Long Context | 002 | LLM | 0 | 25.545 | 25.545 | 1,082 | 192 | 1,274 | `authproxy/run_002_llm.md` |
| AuthProxy Long Context | 002 | RLM | 0 | 91.398 | 52.809 | 13,373 | 129 | 13,502 | `authproxy/run_002_rlm.md` |
| AuthProxy Long Context | 003 | LLM | 0 | 21.342 | 21.342 | 1,082 | 157 | 1,239 | `authproxy/run_003_llm.md` |
| AuthProxy Long Context | 003 | RLM | 0 | 171.021 | 110.262 | 14,000 | 1,087 | 15,087 | `authproxy/run_003_rlm.md` |
| AuthProxy Long Context | 004 | LLM | 0 | 20.940 | 20.940 | 1,082 | 150 | 1,232 | `authproxy/run_004_llm.md` |
| AuthProxy Long Context | 004 | RLM | 0 | 105.034 | 104.956 | 9,285 | 674 | 9,959 | `authproxy/run_004_rlm.md` |
| AuthProxy Long Context | 005 | LLM | 0 | 14.653 | 14.653 | 1,082 | 157 | 1,239 | `authproxy/run_005_llm.md` |
| AuthProxy Long Context | 005 | RLM | 0 | 131.030 | 88.606 | 13,026 | 1,128 | 14,154 | `authproxy/run_005_rlm.md` |
| Clinical Long Context | 001 | LLM | 0 | 173.678 | 173.678 | 1,645 | 1,569 | 3,214 | `clinical/run_001_llm.md` |
| Clinical Long Context | 001 | RLM | 0 | 52.092 | 50.212 | 10,208 | 196 | 10,404 | `clinical/run_001_rlm.md` |
| Clinical Long Context | 002 | LLM | 0 | 137.055 | 137.055 | 1,645 | 1,582 | 3,227 | `clinical/run_002_llm.md` |
| Clinical Long Context | 002 | RLM | 0 | 51.368 | 38.129 | 10,459 | 314 | 10,773 | `clinical/run_002_rlm.md` |
| Clinical Long Context | 003 | LLM | 0 | 71.576 | 71.576 | 1,645 | 743 | 2,388 | `clinical/run_003_llm.md` |
| Clinical Long Context | 003 | RLM | 0 | 84.931 | 55.651 | 11,884 | 661 | 12,545 | `clinical/run_003_rlm.md` |
| Clinical Long Context | 004 | LLM | 0 | 144.718 | 144.718 | 1,645 | 1,519 | 3,164 | `clinical/run_004_llm.md` |
| Clinical Long Context | 004 | RLM | 0 | 58.383 | 44.139 | 10,644 | 320 | 10,964 | `clinical/run_004_rlm.md` |
| Clinical Long Context | 005 | LLM | 0 | 117.333 | 117.333 | 1,645 | 1,094 | 2,739 | `clinical/run_005_llm.md` |
| Clinical Long Context | 005 | RLM | 0 | 42.849 | 35.657 | 10,120 | 218 | 10,338 | `clinical/run_005_rlm.md` |
| Launch Note App | 001 | LLM | 0 | 107.300 | 107.300 | 257 | 1,390 | 1,647 | `launch_note_app/run_001_llm.md` |
| Launch Note App | 001 | RLM | 0 | 37.833 | 37.447 | 2,590 | 197 | 2,787 | `launch_note_app/run_001_rlm.md` |
| Launch Note App | 002 | LLM | 0 | 146.679 | 146.679 | 257 | 1,665 | 1,922 | `launch_note_app/run_002_llm.md` |
| Launch Note App | 002 | RLM | 0 | 516.793 | 513.733 | 12,879 | 1,269 | 14,148 | `launch_note_app/run_002_rlm.md` |
| Launch Note App | 003 | LLM | 0 | 97.669 | 97.669 | 257 | 949 | 1,206 | `launch_note_app/run_003_llm.md` |
| Launch Note App | 003 | RLM | 0 | 276.838 | 244.290 | 12,936 | 2,189 | 15,125 | `launch_note_app/run_003_rlm.md` |
| Launch Note App | 004 | LLM | 0 | 127.190 | 127.190 | 257 | 1,489 | 1,746 | `launch_note_app/run_004_llm.md` |
| Launch Note App | 004 | RLM | 0 | 129.657 | 123.546 | 12,485 | 942 | 13,427 | `launch_note_app/run_004_rlm.md` |
| Launch Note App | 005 | LLM | 0 | 97.483 | 97.483 | 257 | 1,025 | 1,282 | `launch_note_app/run_005_llm.md` |
| Launch Note App | 005 | RLM | 0 | 155.597 | 155.469 | 9,372 | 1,268 | 10,640 | `launch_note_app/run_005_rlm.md` |
| PDF Cersei Warning | 001 | LLM | 0 | 119.110 | 119.110 | 4,096 | 816 | 4,912 | `pdf_cersei_warning/run_001_llm.md` |
| PDF Cersei Warning | 001 | RLM | -9 | - | - | - | - | - | `pdf_cersei_warning/run_001_rlm.md` |
| PDF Cersei Warning | 002 | LLM | 0 | 64.506 | 64.506 | 4,096 | 603 | 4,699 | `pdf_cersei_warning/run_002_llm.md` |
| PDF Cersei Warning | 002 | RLM | 0 | 291.350 | 246.308 | 22,273 | 1,490 | 23,763 | `pdf_cersei_warning/run_002_rlm.md` |
| PDF Cersei Warning | 003 | LLM | 0 | 94.292 | 94.292 | 4,096 | 613 | 4,709 | `pdf_cersei_warning/run_003_llm.md` |
| PDF Cersei Warning | 003 | RLM | 0 | 203.066 | 189.306 | 21,905 | 1,285 | 23,190 | `pdf_cersei_warning/run_003_rlm.md` |
| PDF Cersei Warning | 004 | LLM | 0 | 75.969 | 75.969 | 4,096 | 426 | 4,522 | `pdf_cersei_warning/run_004_llm.md` |
| PDF Cersei Warning | 004 | RLM | 0 | 42.854 | 42.830 | 2,897 | 158 | 3,055 | `pdf_cersei_warning/run_004_rlm.md` |
| PDF Cersei Warning | 005 | LLM | 0 | 94.925 | 94.925 | 4,096 | 662 | 4,758 | `pdf_cersei_warning/run_005_llm.md` |
| PDF Cersei Warning | 005 | RLM | 0 | 206.664 | 159.939 | 21,814 | 917 | 22,731 | `pdf_cersei_warning/run_005_rlm.md` |
| Under-specified TSP | 001 | LLM | 0 | 73.841 | 73.841 | 209 | 881 | 1,090 | `tsp_branch_bound/run_001_llm.md` |
| Under-specified TSP | 001 | RLM | 0 | 578.646 | 578.483 | 18,593 | 5,985 | 24,578 | `tsp_branch_bound/run_001_rlm.md` |
| Under-specified TSP | 002 | LLM | 0 | 105.367 | 105.367 | 209 | 1,277 | 1,486 | `tsp_branch_bound/run_002_llm.md` |
| Under-specified TSP | 002 | RLM | 0 | 604.700 | 249.397 | 23,194 | 2,225 | 25,419 | `tsp_branch_bound/run_002_rlm.md` |
| Under-specified TSP | 003 | LLM | 0 | 103.650 | 103.650 | 209 | 1,026 | 1,235 | `tsp_branch_bound/run_003_llm.md` |
| Under-specified TSP | 003 | RLM | 0 | 492.472 | 474.990 | 23,723 | 4,637 | 28,360 | `tsp_branch_bound/run_003_rlm.md` |
| Under-specified TSP | 004 | LLM | 0 | 106.855 | 106.855 | 209 | 1,380 | 1,589 | `tsp_branch_bound/run_004_llm.md` |
| Under-specified TSP | 004 | RLM | 0 | 425.986 | 425.691 | 19,388 | 4,053 | 23,441 | `tsp_branch_bound/run_004_rlm.md` |
| Under-specified TSP | 005 | LLM | 0 | 93.224 | 93.224 | 209 | 1,175 | 1,384 | `tsp_branch_bound/run_005_llm.md` |
| Under-specified TSP | 005 | RLM | 0 | 490.722 | 490.673 | 16,415 | 4,369 | 20,784 | `tsp_branch_bound/run_005_rlm.md` |
| Stochastic Adaptive TSP | 001 | LLM | 0 | 96.515 | 96.515 | 318 | 1,191 | 1,509 | `stochastic_tsp/run_001_llm.md` |
| Stochastic Adaptive TSP | 001 | RLM | 0 | 873.264 | 819.806 | 21,953 | 5,586 | 27,539 | `stochastic_tsp/run_001_rlm.md` |
| Stochastic Adaptive TSP | 002 | LLM | 0 | 59.780 | 59.780 | 318 | 858 | 1,176 | `stochastic_tsp/run_002_llm.md` |
| Stochastic Adaptive TSP | 002 | RLM | 0 | 152.822 | 152.617 | 12,985 | 1,484 | 14,469 | `stochastic_tsp/run_002_rlm.md` |
| Stochastic Adaptive TSP | 003 | LLM | 0 | 63.006 | 63.006 | 318 | 1,213 | 1,531 | `stochastic_tsp/run_003_llm.md` |
| Stochastic Adaptive TSP | 003 | RLM | 0 | 483.570 | 451.265 | 24,592 | 4,634 | 29,226 | `stochastic_tsp/run_003_rlm.md` |
| Stochastic Adaptive TSP | 004 | LLM | 0 | 124.153 | 124.153 | 318 | 1,655 | 1,973 | `stochastic_tsp/run_004_llm.md` |
| Stochastic Adaptive TSP | 004 | RLM | 0 | 292.076 | 291.926 | 16,586 | 2,583 | 19,169 | `stochastic_tsp/run_004_rlm.md` |
| Stochastic Adaptive TSP | 005 | LLM | 0 | 72.327 | 72.327 | 318 | 971 | 1,289 | `stochastic_tsp/run_005_llm.md` |
| Stochastic Adaptive TSP | 005 | RLM | 0 | 209.424 | 209.153 | 9,175 | 2,131 | 11,306 | `stochastic_tsp/run_005_rlm.md` |

## Output Files

- Raw CSV: [`raw_data.csv`](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260409-203839-ollama-qwen2.5-7b/raw_data.csv)
- Aggregate CSV: [`aggregate_metrics.csv`](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260409-203839-ollama-qwen2.5-7b/aggregate_metrics.csv)
- Batch summary: [`SUMMARY.md`](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260409-203839-ollama-qwen2.5-7b/SUMMARY.md)
