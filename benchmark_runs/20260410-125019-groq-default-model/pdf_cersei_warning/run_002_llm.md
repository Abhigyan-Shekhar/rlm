# pdf_cersei_warning - LLM run 002

- Script: `llm-test/test_pdf_cersei_warning.py`
- Exit code: `1`
- Rate limit encountered: `yes`
- Fatal rate-limit failure: `no`

## Terminal Output

```text
Waiting 5 seconds for rate limit to cool down...

[stderr]
Traceback (most recent call last):
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/llm-test/test_pdf_cersei_warning.py", line 47, in <module>
    response = client.completion(prompt)
               ^^^^^^^^^^^^^^^^^^^^^^^^^
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
openai.BadRequestError: Error code: 400 - {'error': {'message': 'Please reduce the length of the messages or completion.', 'type': 'invalid_request_error', 'param': 'messages'}}
```
