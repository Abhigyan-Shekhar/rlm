# clinical - RLM run 002

- Script: `rlm-test/test_long_context_clinical_trial.py`
- Exit code: `1`

## Terminal Output

```text
No cooldown configured for this backend.

╭─ ◆ RLM ━ Recursive Language Model ───────────────────────────────────────────╮
│                                                                              │
│    Backend                 openai            Environment            local    │
│    Model                   qwen2.5:14b       Max Iterations         3        │
│    Max Depth               1                                                 │
│                                                                              │
╰──────────────────────────────────────────────────────────────────────────────╯


[stderr]
Traceback (most recent call last):
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/rlm-test/test_long_context_clinical_trial.py", line 7, in <module>
    run_path(str(repo_root / "test_long_context_clinical_trial.py"))
  File "<frozen runpy>", line 291, in run_path
  File "<frozen runpy>", line 98, in _run_module_code
  File "<frozen runpy>", line 88, in _run_code
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/test_long_context_clinical_trial.py", line 195, in <module>
    result = agent.completion(prompt)
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/rlm/core/rlm.py", line 308, in completion
    with self._spawn_completion_context(prompt) as (lm_handler, environment):
  File "/opt/homebrew/Cellar/python@3.11/3.11.15/Frameworks/Python.framework/Versions/3.11/lib/python3.11/contextlib.py", line 137, in __enter__
    return next(self.gen)
           ^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/rlm/core/rlm.py", line 219, in _spawn_completion_context
    lm_handler.start()
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/rlm/core/lm_handler.py", line 192, in start
    self._server = ThreadingLMServer((self.host, self._port), LMRequestHandler)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/homebrew/Cellar/python@3.11/3.11.15/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 456, in __init__
    self.server_bind()
  File "/opt/homebrew/Cellar/python@3.11/3.11.15/Frameworks/Python.framework/Versions/3.11/lib/python3.11/socketserver.py", line 472, in server_bind
    self.socket.bind(self.server_address)
PermissionError: [Errno 1] Operation not permitted
```
