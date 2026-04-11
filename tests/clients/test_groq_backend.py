from unittest.mock import patch

from rlm.clients import get_client
from rlm.clients.openai import DEFAULT_GROQ_BASE_URL


def test_get_client_sets_groq_base_url():
    with patch("rlm.clients.openai.openai.OpenAI") as mock_openai:
        with patch("rlm.clients.openai.openai.AsyncOpenAI"):
            client = get_client("groq", {"api_key": "test-key", "model_name": "llama3-70b-8192"})

    assert client.base_url == DEFAULT_GROQ_BASE_URL
    assert client.model_name == "llama3-70b-8192"
    assert mock_openai.call_args[1]["base_url"] == DEFAULT_GROQ_BASE_URL


def test_openai_client_uses_groq_api_key_from_env(monkeypatch):
    monkeypatch.setenv("GROQ_API_KEY", "env-groq-key")

    from importlib import reload

    import rlm.clients.openai as openai_client_module

    reload(openai_client_module)

    try:
        with patch("rlm.clients.openai.openai.OpenAI") as mock_openai:
            with patch("rlm.clients.openai.openai.AsyncOpenAI"):
                openai_client_module.OpenAIClient(
                    model_name="llama-3.3-70b-versatile",
                    base_url=openai_client_module.DEFAULT_GROQ_BASE_URL,
                )

        assert mock_openai.call_args[1]["api_key"] == "env-groq-key"
    finally:
        monkeypatch.delenv("GROQ_API_KEY", raising=False)
        reload(openai_client_module)
