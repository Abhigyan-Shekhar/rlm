# RLM Local Ollama Benchmark Guide And Results

## Scope

This document covers only the local Ollama benchmark batch completed on `qwen2.5:7b`. It does not use or summarize any earlier Gemini runs.

## Environment

- Workspace: `/Users/abhigyanshekhar/Desktop/RLM-FULL`
- Backend: `ollama` through the OpenAI-compatible local endpoint
- Model: `qwen2.5:7b`
- Batch folder: `/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260410-pooled-ollama-qwen2.5-7b-10runs`
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
benchmark_runs/20260410-pooled-ollama-qwen2.5-7b-10runs/
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
| Battle of the Bastards | LLM | 10/10 (100%) | 8.077 | 7.694 | 275.000 | 38.000 | 313.000 |
| Battle of the Bastards | RLM | 10/10 (100%) | 119.765 | 99.689 | 10281.400 | 506.300 | 10787.700 |
| AuthProxy Long Context | LLM | 10/10 (100%) | 23.135 | 22.226 | 1082.000 | 167.600 | 1249.600 |
| AuthProxy Long Context | RLM | 10/10 (100%) | 171.029 | 170.308 | 12244.500 | 1119.700 | 13364.200 |
| Clinical Long Context | LLM | 10/10 (100%) | 116.577 | 114.788 | 1645.000 | 1240.500 | 2885.500 |
| Clinical Long Context | RLM | 10/10 (100%) | 97.614 | 52.290 | 11083.400 | 679.500 | 11762.900 |
| Launch Note App | LLM | 10/10 (100%) | 103.273 | 97.576 | 257.000 | 1174.100 | 1431.100 |
| Launch Note App | RLM | 10/10 (100%) | 248.228 | 251.480 | 10504.600 | 1663.600 | 12168.200 |
| PDF Cersei Warning | LLM | 10/10 (100%) | 111.305 | 117.636 | 4096.000 | 768.200 | 4864.200 |
| PDF Cersei Warning | RLM | 9/10 (90%) | 200.657 | 203.066 | 18456.778 | 956.444 | 19413.222 |
| Under-specified TSP | LLM | 10/10 (100%) | 102.791 | 104.508 | 209.000 | 1131.700 | 1340.700 |
| Under-specified TSP | RLM | 10/10 (100%) | 514.593 | 491.597 | 20185.900 | 3829.900 | 24015.800 |
| Stochastic Adaptive TSP | LLM | 10/10 (100%) | 123.732 | 102.236 | 318.000 | 1115.100 | 1433.100 |
| Stochastic Adaptive TSP | RLM | 9/10 (90%) | 598.444 | 630.217 | 20316.778 | 3291.111 | 23607.889 |

## Wall Time Graph

| Benchmark | Mode | Avg Wall (s) | Relative Bar |
| --- | --- | --- | --- |
| Battle of the Bastards | LLM | 8.077 | # |
| Battle of the Bastards | RLM | 119.765 | ##### |
| AuthProxy Long Context | LLM | 23.135 | # |
| AuthProxy Long Context | RLM | 171.029 | ####### |
| Clinical Long Context | LLM | 116.577 | ##### |
| Clinical Long Context | RLM | 97.614 | #### |
| Launch Note App | LLM | 103.273 | #### |
| Launch Note App | RLM | 248.228 | ########## |
| PDF Cersei Warning | LLM | 111.305 | #### |
| PDF Cersei Warning | RLM | 200.657 | ######## |
| Under-specified TSP | LLM | 102.791 | #### |
| Under-specified TSP | RLM | 514.593 | ##################### |
| Stochastic Adaptive TSP | LLM | 123.732 | ##### |
| Stochastic Adaptive TSP | RLM | 598.444 | ######################## |

## Token Usage Graph

| Benchmark | Mode | Avg Total Tokens | Relative Bar |
| --- | --- | --- | --- |
| Battle of the Bastards | LLM | 313.000 | # |
| Battle of the Bastards | RLM | 10787.700 | ########### |
| AuthProxy Long Context | LLM | 1249.600 | # |
| AuthProxy Long Context | RLM | 13364.200 | ############# |
| Clinical Long Context | LLM | 2885.500 | ### |
| Clinical Long Context | RLM | 11762.900 | ############ |
| Launch Note App | LLM | 1431.100 | # |
| Launch Note App | RLM | 12168.200 | ############ |
| PDF Cersei Warning | LLM | 4864.200 | ##### |
| PDF Cersei Warning | RLM | 19413.222 | ################### |
| Under-specified TSP | LLM | 1340.700 | # |
| Under-specified TSP | RLM | 24015.800 | ######################## |
| Stochastic Adaptive TSP | LLM | 1433.100 | # |
| Stochastic Adaptive TSP | RLM | 23607.889 | ######################## |

## Raw Data Notes

- All values below come from the markdown logs inside the completed local batch folder.
- `stochastic_tsp` run `004` on the `RLM` side exited with `-9`, so it is included in the raw table but excluded from aggregate averages.

## Raw Data Table

| Benchmark | Run | Mode | Exit | Wall (s) | Exec (s) | Input | Output | Total | Log |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Battle of the Bastards | 001 | LLM | 0 | 9.832 | 9.832 | 275 | 56 | 331 | `got/run_001_llm.md` |
| Battle of the Bastards | 001 | RLM | 0 | 73.517 | 73.048 | 8,816 | 299 | 9,115 | `got/run_001_rlm.md` |
| Battle of the Bastards | 002 | LLM | 0 | 7.135 | 7.135 | 275 | 41 | 316 | `got/run_002_llm.md` |
| Battle of the Bastards | 002 | RLM | 0 | 244.427 | 197.253 | 13,982 | 936 | 14,918 | `got/run_002_rlm.md` |
| Battle of the Bastards | 003 | LLM | 0 | 7.756 | 7.756 | 275 | 33 | 308 | `got/run_003_llm.md` |
| Battle of the Bastards | 003 | RLM | 0 | 73.046 | 72.665 | 8,753 | 367 | 9,120 | `got/run_003_rlm.md` |
| Battle of the Bastards | 004 | LLM | 0 | 5.573 | 5.573 | 275 | 33 | 308 | `got/run_004_llm.md` |
| Battle of the Bastards | 004 | RLM | 0 | 60.789 | 60.714 | 5,483 | 289 | 5,772 | `got/run_004_rlm.md` |
| Battle of the Bastards | 005 | LLM | 0 | 8.717 | 8.717 | 275 | 30 | 305 | `got/run_005_llm.md` |
| Battle of the Bastards | 005 | RLM | 0 | 90.114 | 89.877 | 8,691 | 309 | 9,000 | `got/run_005_rlm.md` |
| Battle of the Bastards | 006 | LLM | 0 | 10.512 | 10.512 | 275 | 36 | 311 | `got/run_006_llm.md` |
| Battle of the Bastards | 006 | RLM | 0 | 138.139 | 126.449 | 11,828 | 455 | 12,283 | `got/run_006_rlm.md` |
| Battle of the Bastards | 007 | LLM | 0 | 7.247 | 7.247 | 275 | 38 | 313 | `got/run_007_llm.md` |
| Battle of the Bastards | 007 | RLM | 0 | 116.849 | 106.258 | 11,914 | 407 | 12,321 | `got/run_007_rlm.md` |
| Battle of the Bastards | 008 | LLM | 0 | 10.503 | 10.503 | 275 | 33 | 308 | `got/run_008_llm.md` |
| Battle of the Bastards | 008 | RLM | 0 | 109.263 | 103.557 | 12,387 | 515 | 12,902 | `got/run_008_rlm.md` |
| Battle of the Bastards | 009 | LLM | 0 | 5.864 | 5.864 | 275 | 44 | 319 | `got/run_009_llm.md` |
| Battle of the Bastards | 009 | RLM | 0 | 73.804 | 73.478 | 8,762 | 450 | 9,212 | `got/run_009_rlm.md` |
| Battle of the Bastards | 010 | LLM | 0 | 7.631 | 7.631 | 275 | 36 | 311 | `got/run_010_llm.md` |
| Battle of the Bastards | 010 | RLM | 0 | 217.703 | 154.300 | 12,198 | 1,036 | 13,234 | `got/run_010_rlm.md` |
| AuthProxy Long Context | 001 | LLM | 0 | 30.373 | 30.373 | 1,082 | 178 | 1,260 | `authproxy/run_001_llm.md` |
| AuthProxy Long Context | 001 | RLM | 0 | 169.596 | 169.158 | 6,619 | 1,414 | 8,033 | `authproxy/run_001_rlm.md` |
| AuthProxy Long Context | 002 | LLM | 0 | 20.656 | 20.656 | 1,082 | 145 | 1,227 | `authproxy/run_002_llm.md` |
| AuthProxy Long Context | 002 | RLM | 0 | 219.642 | 173.374 | 13,844 | 1,741 | 15,585 | `authproxy/run_002_rlm.md` |
| AuthProxy Long Context | 003 | LLM | 0 | 20.201 | 20.201 | 1,082 | 149 | 1,231 | `authproxy/run_003_llm.md` |
| AuthProxy Long Context | 003 | RLM | 0 | 146.474 | 118.017 | 13,488 | 990 | 14,478 | `authproxy/run_003_rlm.md` |
| AuthProxy Long Context | 004 | LLM | 0 | 24.106 | 24.106 | 1,082 | 171 | 1,253 | `authproxy/run_004_llm.md` |
| AuthProxy Long Context | 004 | RLM | 0 | 173.042 | 112.295 | 13,385 | 937 | 14,322 | `authproxy/run_004_rlm.md` |
| AuthProxy Long Context | 005 | LLM | 0 | 23.109 | 23.109 | 1,082 | 187 | 1,269 | `authproxy/run_005_llm.md` |
| AuthProxy Long Context | 005 | RLM | 0 | 186.782 | 153.458 | 11,409 | 1,176 | 12,585 | `authproxy/run_005_rlm.md` |
| AuthProxy Long Context | 006 | LLM | 0 | 30.426 | 30.426 | 1,082 | 190 | 1,272 | `authproxy/run_006_llm.md` |
| AuthProxy Long Context | 006 | RLM | 0 | 316.270 | 256.959 | 14,016 | 1,921 | 15,937 | `authproxy/run_006_rlm.md` |
| AuthProxy Long Context | 007 | LLM | 0 | 25.545 | 25.545 | 1,082 | 192 | 1,274 | `authproxy/run_007_llm.md` |
| AuthProxy Long Context | 007 | RLM | 0 | 91.398 | 52.809 | 13,373 | 129 | 13,502 | `authproxy/run_007_rlm.md` |
| AuthProxy Long Context | 008 | LLM | 0 | 21.342 | 21.342 | 1,082 | 157 | 1,239 | `authproxy/run_008_llm.md` |
| AuthProxy Long Context | 008 | RLM | 0 | 171.021 | 110.262 | 14,000 | 1,087 | 15,087 | `authproxy/run_008_rlm.md` |
| AuthProxy Long Context | 009 | LLM | 0 | 20.940 | 20.940 | 1,082 | 150 | 1,232 | `authproxy/run_009_llm.md` |
| AuthProxy Long Context | 009 | RLM | 0 | 105.034 | 104.956 | 9,285 | 674 | 9,959 | `authproxy/run_009_rlm.md` |
| AuthProxy Long Context | 010 | LLM | 0 | 14.653 | 14.653 | 1,082 | 157 | 1,239 | `authproxy/run_010_llm.md` |
| AuthProxy Long Context | 010 | RLM | 0 | 131.030 | 88.606 | 13,026 | 1,128 | 14,154 | `authproxy/run_010_rlm.md` |
| Clinical Long Context | 001 | LLM | 0 | 137.570 | 137.570 | 1,645 | 1,583 | 3,228 | `clinical/run_001_llm.md` |
| Clinical Long Context | 001 | RLM | 0 | 35.334 | 31.440 | 10,181 | 125 | 10,306 | `clinical/run_001_rlm.md` |
| Clinical Long Context | 002 | LLM | 0 | 111.993 | 111.993 | 1,645 | 1,312 | 2,957 | `clinical/run_002_llm.md` |
| Clinical Long Context | 002 | RLM | 0 | 52.487 | 44.638 | 10,392 | 351 | 10,743 | `clinical/run_002_rlm.md` |
| Clinical Long Context | 003 | LLM | 0 | 112.244 | 112.244 | 1,645 | 1,234 | 2,879 | `clinical/run_003_llm.md` |
| Clinical Long Context | 003 | RLM | 0 | 34.254 | 32.456 | 10,160 | 123 | 10,283 | `clinical/run_003_rlm.md` |
| Clinical Long Context | 004 | LLM | 0 | 101.873 | 101.873 | 1,645 | 1,270 | 2,915 | `clinical/run_004_llm.md` |
| Clinical Long Context | 004 | RLM | 0 | 343.306 | 281.513 | 15,177 | 2,883 | 18,060 | `clinical/run_004_rlm.md` |
| Clinical Long Context | 005 | LLM | 0 | 57.730 | 57.730 | 1,645 | 499 | 2,144 | `clinical/run_005_llm.md` |
| Clinical Long Context | 005 | RLM | 0 | 221.131 | 220.670 | 11,609 | 1,604 | 13,213 | `clinical/run_005_rlm.md` |
| Clinical Long Context | 006 | LLM | 0 | 173.678 | 173.678 | 1,645 | 1,569 | 3,214 | `clinical/run_006_llm.md` |
| Clinical Long Context | 006 | RLM | 0 | 52.092 | 50.212 | 10,208 | 196 | 10,404 | `clinical/run_006_rlm.md` |
| Clinical Long Context | 007 | LLM | 0 | 137.055 | 137.055 | 1,645 | 1,582 | 3,227 | `clinical/run_007_llm.md` |
| Clinical Long Context | 007 | RLM | 0 | 51.368 | 38.129 | 10,459 | 314 | 10,773 | `clinical/run_007_rlm.md` |
| Clinical Long Context | 008 | LLM | 0 | 71.576 | 71.576 | 1,645 | 743 | 2,388 | `clinical/run_008_llm.md` |
| Clinical Long Context | 008 | RLM | 0 | 84.931 | 55.651 | 11,884 | 661 | 12,545 | `clinical/run_008_rlm.md` |
| Clinical Long Context | 009 | LLM | 0 | 144.718 | 144.718 | 1,645 | 1,519 | 3,164 | `clinical/run_009_llm.md` |
| Clinical Long Context | 009 | RLM | 0 | 58.383 | 44.139 | 10,644 | 320 | 10,964 | `clinical/run_009_rlm.md` |
| Clinical Long Context | 010 | LLM | 0 | 117.333 | 117.333 | 1,645 | 1,094 | 2,739 | `clinical/run_010_llm.md` |
| Clinical Long Context | 010 | RLM | 0 | 42.849 | 35.657 | 10,120 | 218 | 10,338 | `clinical/run_010_rlm.md` |
| Launch Note App | 001 | LLM | 0 | 81.166 | 81.166 | 257 | 978 | 1,235 | `launch_note_app/run_001_llm.md` |
| Launch Note App | 001 | RLM | 0 | 226.218 | 147.923 | 11,223 | 2,144 | 13,367 | `launch_note_app/run_001_rlm.md` |
| Launch Note App | 002 | LLM | 0 | 88.222 | 88.222 | 257 | 1,129 | 1,386 | `launch_note_app/run_002_llm.md` |
| Launch Note App | 002 | RLM | 0 | 276.742 | 232.978 | 13,106 | 2,843 | 15,949 | `launch_note_app/run_002_rlm.md` |
| Launch Note App | 003 | LLM | 0 | 58.346 | 58.346 | 257 | 879 | 1,136 | `launch_note_app/run_003_llm.md` |
| Launch Note App | 003 | RLM | 0 | 102.077 | 101.825 | 5,808 | 1,416 | 7,224 | `launch_note_app/run_003_rlm.md` |
| Launch Note App | 004 | LLM | 0 | 72.258 | 72.258 | 257 | 837 | 1,094 | `launch_note_app/run_004_llm.md` |
| Launch Note App | 004 | RLM | 0 | 464.365 | 304.048 | 14,161 | 2,426 | 16,587 | `launch_note_app/run_004_rlm.md` |
| Launch Note App | 005 | LLM | 0 | 156.415 | 156.415 | 257 | 1,400 | 1,657 | `launch_note_app/run_005_llm.md` |
| Launch Note App | 005 | RLM | 0 | 296.160 | 291.026 | 10,486 | 1,942 | 12,428 | `launch_note_app/run_005_rlm.md` |
| Launch Note App | 006 | LLM | 0 | 107.300 | 107.300 | 257 | 1,390 | 1,647 | `launch_note_app/run_006_llm.md` |
| Launch Note App | 006 | RLM | 0 | 37.833 | 37.447 | 2,590 | 197 | 2,787 | `launch_note_app/run_006_rlm.md` |
| Launch Note App | 007 | LLM | 0 | 146.679 | 146.679 | 257 | 1,665 | 1,922 | `launch_note_app/run_007_llm.md` |
| Launch Note App | 007 | RLM | 0 | 516.793 | 513.733 | 12,879 | 1,269 | 14,148 | `launch_note_app/run_007_rlm.md` |
| Launch Note App | 008 | LLM | 0 | 97.669 | 97.669 | 257 | 949 | 1,206 | `launch_note_app/run_008_llm.md` |
| Launch Note App | 008 | RLM | 0 | 276.838 | 244.290 | 12,936 | 2,189 | 15,125 | `launch_note_app/run_008_rlm.md` |
| Launch Note App | 009 | LLM | 0 | 127.190 | 127.190 | 257 | 1,489 | 1,746 | `launch_note_app/run_009_llm.md` |
| Launch Note App | 009 | RLM | 0 | 129.657 | 123.546 | 12,485 | 942 | 13,427 | `launch_note_app/run_009_rlm.md` |
| Launch Note App | 010 | LLM | 0 | 97.483 | 97.483 | 257 | 1,025 | 1,282 | `launch_note_app/run_010_llm.md` |
| Launch Note App | 010 | RLM | 0 | 155.597 | 155.469 | 9,372 | 1,268 | 10,640 | `launch_note_app/run_010_rlm.md` |
| PDF Cersei Warning | 001 | LLM | 0 | 135.947 | 135.947 | 4,096 | 728 | 4,824 | `pdf_cersei_warning/run_001_llm.md` |
| PDF Cersei Warning | 001 | RLM | 0 | 191.413 | 191.159 | 10,247 | 903 | 11,150 | `pdf_cersei_warning/run_001_rlm.md` |
| PDF Cersei Warning | 002 | LLM | 0 | 116.163 | 116.163 | 4,096 | 692 | 4,788 | `pdf_cersei_warning/run_002_llm.md` |
| PDF Cersei Warning | 002 | RLM | 0 | 231.660 | 184.283 | 21,579 | 899 | 22,478 | `pdf_cersei_warning/run_002_rlm.md` |
| PDF Cersei Warning | 003 | LLM | 0 | 133.442 | 133.442 | 4,096 | 816 | 4,912 | `pdf_cersei_warning/run_003_llm.md` |
| PDF Cersei Warning | 003 | RLM | 0 | 318.367 | 277.481 | 22,295 | 1,289 | 23,584 | `pdf_cersei_warning/run_003_rlm.md` |
| PDF Cersei Warning | 004 | LLM | 0 | 133.707 | 133.707 | 4,096 | 1,085 | 5,181 | `pdf_cersei_warning/run_004_llm.md` |
| PDF Cersei Warning | 004 | RLM | 0 | 139.048 | 116.216 | 21,496 | 777 | 22,273 | `pdf_cersei_warning/run_004_rlm.md` |
| PDF Cersei Warning | 005 | LLM | 0 | 144.988 | 144.988 | 4,096 | 1,241 | 5,337 | `pdf_cersei_warning/run_005_llm.md` |
| PDF Cersei Warning | 005 | RLM | 0 | 181.494 | 123.025 | 21,605 | 890 | 22,495 | `pdf_cersei_warning/run_005_rlm.md` |
| PDF Cersei Warning | 006 | LLM | 0 | 119.110 | 119.110 | 4,096 | 816 | 4,912 | `pdf_cersei_warning/run_006_llm.md` |
| PDF Cersei Warning | 006 | RLM | -9 | - | - | - | - | - | `pdf_cersei_warning/run_006_rlm.md` |
| PDF Cersei Warning | 007 | LLM | 0 | 64.506 | 64.506 | 4,096 | 603 | 4,699 | `pdf_cersei_warning/run_007_llm.md` |
| PDF Cersei Warning | 007 | RLM | 0 | 291.350 | 246.308 | 22,273 | 1,490 | 23,763 | `pdf_cersei_warning/run_007_rlm.md` |
| PDF Cersei Warning | 008 | LLM | 0 | 94.292 | 94.292 | 4,096 | 613 | 4,709 | `pdf_cersei_warning/run_008_llm.md` |
| PDF Cersei Warning | 008 | RLM | 0 | 203.066 | 189.306 | 21,905 | 1,285 | 23,190 | `pdf_cersei_warning/run_008_rlm.md` |
| PDF Cersei Warning | 009 | LLM | 0 | 75.969 | 75.969 | 4,096 | 426 | 4,522 | `pdf_cersei_warning/run_009_llm.md` |
| PDF Cersei Warning | 009 | RLM | 0 | 42.854 | 42.830 | 2,897 | 158 | 3,055 | `pdf_cersei_warning/run_009_rlm.md` |
| PDF Cersei Warning | 010 | LLM | 0 | 94.925 | 94.925 | 4,096 | 662 | 4,758 | `pdf_cersei_warning/run_010_llm.md` |
| PDF Cersei Warning | 010 | RLM | 0 | 206.664 | 159.939 | 21,814 | 917 | 22,731 | `pdf_cersei_warning/run_010_rlm.md` |
| Under-specified TSP | 001 | LLM | 0 | 83.021 | 83.021 | 209 | 1,154 | 1,363 | `tsp_branch_bound/run_001_llm.md` |
| Under-specified TSP | 001 | RLM | 0 | 253.519 | 253.280 | 12,514 | 2,661 | 15,175 | `tsp_branch_bound/run_001_rlm.md` |
| Under-specified TSP | 002 | LLM | 0 | 85.607 | 85.607 | 209 | 1,055 | 1,264 | `tsp_branch_bound/run_002_llm.md` |
| Under-specified TSP | 002 | RLM | 0 | 369.738 | 296.882 | 23,510 | 2,468 | 25,978 | `tsp_branch_bound/run_002_rlm.md` |
| Under-specified TSP | 003 | LLM | 0 | 127.640 | 127.640 | 209 | 1,057 | 1,266 | `tsp_branch_bound/run_003_llm.md` |
| Under-specified TSP | 003 | RLM | 0 | 705.174 | 697.629 | 22,245 | 4,097 | 26,342 | `tsp_branch_bound/run_003_rlm.md` |
| Under-specified TSP | 004 | LLM | 0 | 141.916 | 141.916 | 209 | 1,103 | 1,312 | `tsp_branch_bound/run_004_llm.md` |
| Under-specified TSP | 004 | RLM | 0 | 970.961 | 846.544 | 20,689 | 5,498 | 26,187 | `tsp_branch_bound/run_004_rlm.md` |
| Under-specified TSP | 005 | LLM | 0 | 106.786 | 106.786 | 209 | 1,209 | 1,418 | `tsp_branch_bound/run_005_llm.md` |
| Under-specified TSP | 005 | RLM | 0 | 254.008 | 192.689 | 21,588 | 2,306 | 23,894 | `tsp_branch_bound/run_005_rlm.md` |
| Under-specified TSP | 006 | LLM | 0 | 73.841 | 73.841 | 209 | 881 | 1,090 | `tsp_branch_bound/run_006_llm.md` |
| Under-specified TSP | 006 | RLM | 0 | 578.646 | 578.483 | 18,593 | 5,985 | 24,578 | `tsp_branch_bound/run_006_rlm.md` |
| Under-specified TSP | 007 | LLM | 0 | 105.367 | 105.367 | 209 | 1,277 | 1,486 | `tsp_branch_bound/run_007_llm.md` |
| Under-specified TSP | 007 | RLM | 0 | 604.700 | 249.397 | 23,194 | 2,225 | 25,419 | `tsp_branch_bound/run_007_rlm.md` |
| Under-specified TSP | 008 | LLM | 0 | 103.650 | 103.650 | 209 | 1,026 | 1,235 | `tsp_branch_bound/run_008_llm.md` |
| Under-specified TSP | 008 | RLM | 0 | 492.472 | 474.990 | 23,723 | 4,637 | 28,360 | `tsp_branch_bound/run_008_rlm.md` |
| Under-specified TSP | 009 | LLM | 0 | 106.855 | 106.855 | 209 | 1,380 | 1,589 | `tsp_branch_bound/run_009_llm.md` |
| Under-specified TSP | 009 | RLM | 0 | 425.986 | 425.691 | 19,388 | 4,053 | 23,441 | `tsp_branch_bound/run_009_rlm.md` |
| Under-specified TSP | 010 | LLM | 0 | 93.224 | 93.224 | 209 | 1,175 | 1,384 | `tsp_branch_bound/run_010_llm.md` |
| Under-specified TSP | 010 | RLM | 0 | 490.722 | 490.673 | 16,415 | 4,369 | 20,784 | `tsp_branch_bound/run_010_rlm.md` |
| Stochastic Adaptive TSP | 001 | LLM | 0 | 98.209 | 98.209 | 318 | 1,059 | 1,377 | `stochastic_tsp/run_001_llm.md` |
| Stochastic Adaptive TSP | 001 | RLM | 0 | 633.152 | 582.324 | 24,446 | 4,417 | 28,863 | `stochastic_tsp/run_001_rlm.md` |
| Stochastic Adaptive TSP | 002 | LLM | 0 | 106.263 | 106.263 | 318 | 999 | 1,317 | `stochastic_tsp/run_002_llm.md` |
| Stochastic Adaptive TSP | 002 | RLM | 0 | 1342.957 | 1238.970 | 24,535 | 3,297 | 27,832 | `stochastic_tsp/run_002_rlm.md` |
| Stochastic Adaptive TSP | 003 | LLM | 0 | 224.292 | 224.292 | 318 | 1,170 | 1,488 | `stochastic_tsp/run_003_llm.md` |
| Stochastic Adaptive TSP | 003 | RLM | 0 | 768.512 | 746.877 | 23,597 | 2,772 | 26,369 | `stochastic_tsp/run_003_rlm.md` |
| Stochastic Adaptive TSP | 004 | LLM | 0 | 207.149 | 207.149 | 318 | 1,061 | 1,379 | `stochastic_tsp/run_004_llm.md` |
| Stochastic Adaptive TSP | 004 | RLM | -9 | - | - | - | - | - | `stochastic_tsp/run_004_rlm.md` |
| Stochastic Adaptive TSP | 005 | LLM | 0 | 185.630 | 185.630 | 318 | 974 | 1,292 | `stochastic_tsp/run_005_llm.md` |
| Stochastic Adaptive TSP | 005 | RLM | 0 | 630.217 | 589.147 | 24,982 | 2,716 | 27,698 | `stochastic_tsp/run_005_rlm.md` |
| Stochastic Adaptive TSP | 006 | LLM | 0 | 96.515 | 96.515 | 318 | 1,191 | 1,509 | `stochastic_tsp/run_006_llm.md` |
| Stochastic Adaptive TSP | 006 | RLM | 0 | 873.264 | 819.806 | 21,953 | 5,586 | 27,539 | `stochastic_tsp/run_006_rlm.md` |
| Stochastic Adaptive TSP | 007 | LLM | 0 | 59.780 | 59.780 | 318 | 858 | 1,176 | `stochastic_tsp/run_007_llm.md` |
| Stochastic Adaptive TSP | 007 | RLM | 0 | 152.822 | 152.617 | 12,985 | 1,484 | 14,469 | `stochastic_tsp/run_007_rlm.md` |
| Stochastic Adaptive TSP | 008 | LLM | 0 | 63.006 | 63.006 | 318 | 1,213 | 1,531 | `stochastic_tsp/run_008_llm.md` |
| Stochastic Adaptive TSP | 008 | RLM | 0 | 483.570 | 451.265 | 24,592 | 4,634 | 29,226 | `stochastic_tsp/run_008_rlm.md` |
| Stochastic Adaptive TSP | 009 | LLM | 0 | 124.153 | 124.153 | 318 | 1,655 | 1,973 | `stochastic_tsp/run_009_llm.md` |
| Stochastic Adaptive TSP | 009 | RLM | 0 | 292.076 | 291.926 | 16,586 | 2,583 | 19,169 | `stochastic_tsp/run_009_rlm.md` |
| Stochastic Adaptive TSP | 010 | LLM | 0 | 72.327 | 72.327 | 318 | 971 | 1,289 | `stochastic_tsp/run_010_llm.md` |
| Stochastic Adaptive TSP | 010 | RLM | 0 | 209.424 | 209.153 | 9,175 | 2,131 | 11,306 | `stochastic_tsp/run_010_rlm.md` |

## Output Files

- Raw CSV: [`raw_data.csv`](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260410-pooled-ollama-qwen2.5-7b-10runs/raw_data.csv)
- Aggregate CSV: [`aggregate_metrics.csv`](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260410-pooled-ollama-qwen2.5-7b-10runs/aggregate_metrics.csv)
- Batch summary: [`SUMMARY.md`](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260410-pooled-ollama-qwen2.5-7b-10runs/SUMMARY.md)
