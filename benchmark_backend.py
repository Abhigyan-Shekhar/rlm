import os
import time
from dataclasses import dataclass
from typing import Any

from dotenv import load_dotenv

from rlm.clients import get_client

load_dotenv()

DEFAULT_VLLM_BASE_URL = "http://127.0.0.1:8000/v1"
DEFAULT_VLLM_API_KEY = "EMPTY"
DEFAULT_OLLAMA_BASE_URL = "http://127.0.0.1:11434/v1"
DEFAULT_OLLAMA_API_KEY = "ollama"
DEFAULT_OLLAMA_MODEL = "qwen2.5:3b"


@dataclass(frozen=True)
class BenchmarkBackendConfig:
    backend: str
    backend_kwargs: dict[str, Any]
    model_name: str
    cooldown_seconds: int


def load_benchmark_backend(
    *,
    default_gemini_model: str,
    default_vllm_model: str | None = None,
    default_ollama_model: str | None = DEFAULT_OLLAMA_MODEL,
) -> BenchmarkBackendConfig:
    backend = os.getenv("BENCHMARK_BACKEND", "gemini").lower()
    cooldown_seconds = int(os.getenv("BENCHMARK_COOLDOWN_SECONDS", "0"))

    if backend == "gemini":
        model_name = os.getenv("BENCHMARK_MODEL_NAME") or os.getenv(
            "GEMINI_MODEL_NAME", default_gemini_model
        )
        if cooldown_seconds == 0:
            cooldown_seconds = 15
        return BenchmarkBackendConfig(
            backend="gemini",
            backend_kwargs={
                "api_key": os.environ["GEMINI_API_KEY"],
                "model_name": model_name,
            },
            model_name=model_name,
            cooldown_seconds=cooldown_seconds,
        )

    if backend == "vllm":
        model_name = (
            os.getenv("BENCHMARK_MODEL_NAME")
            or os.getenv("VLLM_MODEL_NAME")
            or default_vllm_model
        )
        if model_name is None:
            raise ValueError(
                "Set VLLM_MODEL_NAME or BENCHMARK_MODEL_NAME for BENCHMARK_BACKEND=vllm."
            )
        return BenchmarkBackendConfig(
            backend="vllm",
            backend_kwargs={
                "base_url": os.getenv("VLLM_BASE_URL", DEFAULT_VLLM_BASE_URL),
                "api_key": os.getenv("VLLM_API_KEY", DEFAULT_VLLM_API_KEY),
                "model_name": model_name,
            },
            model_name=model_name,
            cooldown_seconds=cooldown_seconds,
        )

    if backend == "ollama":
        model_name = (
            os.getenv("BENCHMARK_MODEL_NAME")
            or os.getenv("OLLAMA_MODEL_NAME")
            or default_ollama_model
            or default_vllm_model
        )
        if model_name is None:
            raise ValueError(
                "Set OLLAMA_MODEL_NAME or BENCHMARK_MODEL_NAME for BENCHMARK_BACKEND=ollama."
            )
        return BenchmarkBackendConfig(
            backend="openai",
            backend_kwargs={
                "base_url": os.getenv("OLLAMA_BASE_URL", DEFAULT_OLLAMA_BASE_URL),
                "api_key": os.getenv("OLLAMA_API_KEY", DEFAULT_OLLAMA_API_KEY),
                "model_name": model_name,
            },
            model_name=model_name,
            cooldown_seconds=cooldown_seconds,
        )

    raise ValueError(
        f"Unsupported BENCHMARK_BACKEND={backend!r}. Use 'gemini', 'vllm', or 'ollama'."
    )


def wait_for_benchmark_cooldown(config: BenchmarkBackendConfig) -> None:
    if config.cooldown_seconds <= 0:
        print("No cooldown configured for this backend.")
        return

    print(
        f"Waiting {config.cooldown_seconds} seconds for rate limit to cool down..."
    )
    time.sleep(config.cooldown_seconds)


def build_messages(prompt: str, system_instruction: str | None = None) -> Any:
    if system_instruction is None:
        return prompt
    return [
        {"role": "system", "content": system_instruction},
        {"role": "user", "content": prompt},
    ]


def get_benchmark_client(config: BenchmarkBackendConfig):
    return get_client(config.backend, config.backend_kwargs.copy())


def print_client_usage(client) -> None:
    usage = client.get_usage_summary().to_dict()
    for model_name, model_usage in usage.get("model_usage_summaries", {}).items():
        print(
            f"{model_name}: input={model_usage.get('total_input_tokens', 0):,}, "
            f"output={model_usage.get('total_output_tokens', 0):,}, "
            f"calls={model_usage.get('total_calls', 0)}"
        )
