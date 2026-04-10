# clinical - LLM run 003

- Script: `llm-test/clinical-llm.py`
- Exit code: `1`

## Terminal Output

```text
No cooldown configured for this backend.

[stderr]
Traceback (most recent call last):
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 101, in map_httpcore_exceptions
    yield
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 250, in handle_request
    resp = self._pool.handle_request(req)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpcore/_sync/connection_pool.py", line 256, in handle_request
    raise exc from None
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpcore/_sync/connection_pool.py", line 236, in handle_request
    response = connection.handle_request(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpcore/_sync/connection.py", line 103, in handle_request
    return self._connection.handle_request(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpcore/_sync/http11.py", line 136, in handle_request
    raise exc
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpcore/_sync/http11.py", line 106, in handle_request
    ) = self._receive_response_headers(**kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpcore/_sync/http11.py", line 177, in _receive_response_headers
    event = self._receive_event(timeout=timeout)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpcore/_sync/http11.py", line 217, in _receive_event
    data = self._network_stream.read(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpcore/_backends/sync.py", line 126, in read
    with map_exceptions(exc_map):
  File "/opt/homebrew/Cellar/python@3.11/3.11.15/Frameworks/Python.framework/Versions/3.11/lib/python3.11/contextlib.py", line 158, in __exit__
    self.gen.throw(typ, value, traceback)
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpcore/_exceptions.py", line 14, in map_exceptions
    raise to_exc(exc) from exc
httpcore.ReadTimeout: timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/openai/_base_client.py", line 982, in request
    response = self._client.send(
               ^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpx/_client.py", line 914, in send
    response = self._send_handling_auth(
               ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpx/_client.py", line 942, in _send_handling_auth
    response = self._send_handling_redirects(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpx/_client.py", line 979, in _send_handling_redirects
    response = self._send_single_request(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpx/_client.py", line 1014, in _send_single_request
    response = transport.handle_request(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 249, in handle_request
    with map_httpcore_exceptions():
  File "/opt/homebrew/Cellar/python@3.11/3.11.15/Frameworks/Python.framework/Versions/3.11/lib/python3.11/contextlib.py", line 158, in __exit__
    self.gen.throw(typ, value, traceback)
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/httpx/_transports/default.py", line 118, in map_httpcore_exceptions
    raise mapped_exc(message) from exc
httpx.ReadTimeout: timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/llm-test/clinical-llm.py", line 180, in <module>
    response = client.completion(prompt)
               ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/rlm/clients/openai.py", line 85, in completion
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
  File "/Users/abhigyanshekhar/Desktop/RLM-FULL/.venv/lib/python3.11/site-packages/openai/_base_client.py", line 1000, in request
    raise APITimeoutError(request=request) from err
openai.APITimeoutError: Request timed out.
```
