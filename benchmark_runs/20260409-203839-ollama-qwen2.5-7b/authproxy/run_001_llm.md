# authproxy - LLM run 001

- Script: `llm-test/llm-test for long context problem - same as rlm , just modified for llm`
- Exit code: `0`

## Terminal Output

```text
No cooldown configured for this backend.

======================================================================
ANSWER
======================================================================
Backend: openai
Model:   qwen2.5:7b
Q1 [Single-hop retrieval]:
7

Q2 [Distractor robustness]:
7

Q3 [Misleading fact resistance]:
7

Q4 [Span extraction]:
ServiceConfig instance "AuthProxy-Primary" has the following parameters:
  - MAX_RETRY_LIMIT = 7
  - TIMEOUT_MS = 8000
  - FAILOVER_ENABLED = false
This is the active production configuration as of 2025-01-09. It handles all inbound authentication requests for the main application cluster.

Q5 [Multi-hop reasoning]:
If AuthProxy-Primary fails, the system will not perform a failover because FAILOVER_ENABLED is set to false. Therefore, any authentication requests destined for the main application cluster that require processing through AuthProxy-Primary will fail until the issue can be resolved and AuthProxy-Primary returns to operation or an alternative solution is put in place.

======================================================================
LATENCY BREAKDOWN
======================================================================
  Total wall time:    30.426s

======================================================================
TOKEN USAGE
======================================================================
qwen2.5:7b: input=1,082, output=190, calls=1
======================================================================
```
