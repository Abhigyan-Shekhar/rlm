from benchmark_backend import (
    detect_rate_limit,
    format_rate_limit_status,
    load_benchmark_backend,
)


def test_detect_rate_limit_true_for_429_message():
    output = "openai.RateLimitError: Error code: 429 - Too Many Requests"
    assert detect_rate_limit(output) is True


def test_detect_rate_limit_false_for_normal_output():
    output = "Benchmark completed successfully with no errors."
    assert detect_rate_limit(output) is False


def test_format_rate_limit_status():
    assert format_rate_limit_status(True) == "yes"
    assert format_rate_limit_status(False) == "no"


def test_load_benchmark_backend_groq(monkeypatch):
    monkeypatch.setenv("BENCHMARK_BACKEND", "groq")
    monkeypatch.setenv("BENCHMARK_MODEL_NAME", "llama-3.3-70b-versatile")

    config = load_benchmark_backend(default_gemini_model="gemini-2.5-flash")

    assert config.backend == "groq"
    assert config.model_name == "llama-3.3-70b-versatile"
    assert config.backend_kwargs == {"model_name": "llama-3.3-70b-versatile"}
