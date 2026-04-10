# tsp_branch_bound - RLM run 004

- Script: `rlm-test/test_tsp_branch_bound.py`
- Exit code: `1`
- Rate limit encountered: `yes`
- Fatal rate-limit failure: `yes`

## Terminal Output

```text
Waiting 5 seconds for rate limit to cool down...

======================================================================
EXPECTED CORRECT RESULT
======================================================================
The problem is under-specified. No optimal tour can be determined because the actual distance matrix values are missing.

======================================================================
BASELINE LLM
======================================================================
Backend: groq
Model:   llama-3.3-70b-versatile

[stderr]
Traceback (most recent call last):
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/rlm-test/test_tsp_branch_bound.py", line 7, in <module>
    run_path(str(repo_root / "test_tsp_branch_bound.py"))
  File "<frozen runpy>", line 291, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/test_tsp_branch_bound.py", line 75, in <module>
    llm_response = baseline_client.completion(prompt)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/rlm/clients/openai.py", line 89, in completion
    response = self.client.chat.completions.create(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/openai/_utils/_utils.py", line 286, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/openai/resources/chat/completions/completions.py", line 1192, in create
    return self._post(
           ^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/openai/_base_client.py", line 1259, in post
    return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/openai/_base_client.py", line 1047, in request
    raise self._make_status_error_from_response(err.response) from None
openai.RateLimitError: Error code: 429 - {'error': {'message': 'Rate limit reached for model `llama-3.3-70b-versatile` in organization `org_01knvqnv0nf8gvs5df8h9xn8c4` service tier `on_demand` on tokens per day (TPD): Limit 100000, Used 99969, Requested 667. Please try again in 9m9.504s. Need more tokens? Upgrade to Dev Tier today at https://console.groq.com/settings/billing', 'type': 'tokens', 'code': 'rate_limit_exceeded'}}
```
