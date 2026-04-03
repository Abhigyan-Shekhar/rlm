# RLM Local Ollama Benchmark Guide And Results

## Scope

This document covers only the local Ollama benchmark batch completed on `qwen2.5:7b`. It does not use or summarize any earlier Gemini runs.

## Environment

- Workspace: `/Users/abhigyanshekhar/Desktop/RLM-FULL`
- Backend: `ollama` through the OpenAI-compatible local endpoint
- Model: `qwen2.5:7b`
- Batch folder: `/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260403-121151-ollama-qwen2.5-7b`
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
benchmark_runs/20260403-121151-ollama-qwen2.5-7b/
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
| Battle of the Bastards | LLM | 5/5 (100%) | 7.803 | 7.756 | 275.000 | 38.600 | 313.600 |
| Battle of the Bastards | RLM | 5/5 (100%) | 108.379 | 73.517 | 9145.000 | 440.000 | 9585.000 |
| AuthProxy Long Context | LLM | 5/5 (100%) | 23.689 | 23.109 | 1082.000 | 166.000 | 1248.000 |
| AuthProxy Long Context | RLM | 5/5 (100%) | 179.107 | 173.042 | 11749.000 | 1251.600 | 13000.600 |
| Clinical Long Context | LLM | 5/5 (100%) | 104.282 | 111.993 | 1645.000 | 1179.600 | 2824.600 |
| Clinical Long Context | RLM | 5/5 (100%) | 137.302 | 52.487 | 11503.800 | 1017.200 | 12521.000 |
| Launch Note App | LLM | 5/5 (100%) | 91.281 | 81.166 | 257.000 | 1044.600 | 1301.600 |
| Launch Note App | RLM | 5/5 (100%) | 273.112 | 276.742 | 10956.800 | 2154.200 | 13111.000 |
| PDF Cersei Warning | LLM | 5/5 (100%) | 132.849 | 133.707 | 4096.000 | 912.400 | 5008.400 |
| PDF Cersei Warning | RLM | 5/5 (100%) | 212.396 | 191.413 | 19444.400 | 951.600 | 20396.000 |
| Under-specified TSP | LLM | 5/5 (100%) | 108.994 | 106.786 | 209.000 | 1115.600 | 1324.600 |
| Under-specified TSP | RLM | 5/5 (100%) | 510.680 | 369.738 | 20109.200 | 3406.000 | 23515.200 |
| Stochastic Adaptive TSP | LLM | 5/5 (100%) | 164.309 | 185.630 | 318.000 | 1052.600 | 1370.600 |
| Stochastic Adaptive TSP | RLM | 4/5 (80%) | 843.710 | 700.832 | 24390.000 | 3300.500 | 27690.500 |

## Wall Time Graph

| Benchmark | Mode | Avg Wall (s) | Relative Bar |
| --- | --- | --- | --- |
| Battle of the Bastards | LLM | 7.803 | # |
| Battle of the Bastards | RLM | 108.379 | ### |
| AuthProxy Long Context | LLM | 23.689 | # |
| AuthProxy Long Context | RLM | 179.107 | ##### |
| Clinical Long Context | LLM | 104.282 | ### |
| Clinical Long Context | RLM | 137.302 | #### |
| Launch Note App | LLM | 91.281 | ### |
| Launch Note App | RLM | 273.112 | ######## |
| PDF Cersei Warning | LLM | 132.849 | #### |
| PDF Cersei Warning | RLM | 212.396 | ###### |
| Under-specified TSP | LLM | 108.994 | ### |
| Under-specified TSP | RLM | 510.680 | ############### |
| Stochastic Adaptive TSP | LLM | 164.309 | ##### |
| Stochastic Adaptive TSP | RLM | 843.710 | ######################## |

## Token Usage Graph

| Benchmark | Mode | Avg Total Tokens | Relative Bar |
| --- | --- | --- | --- |
| Battle of the Bastards | LLM | 313.600 | # |
| Battle of the Bastards | RLM | 9585.000 | ######## |
| AuthProxy Long Context | LLM | 1248.000 | # |
| AuthProxy Long Context | RLM | 13000.600 | ########### |
| Clinical Long Context | LLM | 2824.600 | ## |
| Clinical Long Context | RLM | 12521.000 | ########### |
| Launch Note App | LLM | 1301.600 | # |
| Launch Note App | RLM | 13111.000 | ########### |
| PDF Cersei Warning | LLM | 5008.400 | #### |
| PDF Cersei Warning | RLM | 20396.000 | ################## |
| Under-specified TSP | LLM | 1324.600 | # |
| Under-specified TSP | RLM | 23515.200 | #################### |
| Stochastic Adaptive TSP | LLM | 1370.600 | # |
| Stochastic Adaptive TSP | RLM | 27690.500 | ######################## |

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

## Output Files

- Raw CSV: [`raw_data.csv`](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260403-121151-ollama-qwen2.5-7b/raw_data.csv)
- Aggregate CSV: [`aggregate_metrics.csv`](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260403-121151-ollama-qwen2.5-7b/aggregate_metrics.csv)
- Batch summary: [`SUMMARY.md`](/Users/abhigyanshekhar/Desktop/RLM-FULL/benchmark_runs/20260403-121151-ollama-qwen2.5-7b/SUMMARY.md)
