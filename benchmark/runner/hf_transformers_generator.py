from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version
import re
import sys

from .protocol import GenerationConfig, RuntimeIdentity


def _load_dependencies():
    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer
    return torch, AutoModelForCausalLM, AutoTokenizer


def _package_version(name: str) -> str:
    try:
        return version(name)
    except PackageNotFoundError:
        return "unknown"


class TransformersGenerator:
    def __init__(self, repo_id: str, revision: str, generation_config: GenerationConfig):
        if not re.fullmatch(r"[0-9a-fA-F]{40}", revision):
            raise ValueError("revision must be an exact 40-character commit SHA")
        self.repo_id = repo_id
        self.revision = revision.lower()
        self.generation_config = generation_config
        self._torch, model_cls, tokenizer_cls = _load_dependencies()
        self._torch.manual_seed(generation_config.seed)
        self.tokenizer = tokenizer_cls.from_pretrained(repo_id, revision=self.revision)
        self.model = model_cls.from_pretrained(
            repo_id,
            revision=self.revision,
            torch_dtype=self._torch.bfloat16,
            device_map="auto",
        )
        self.model.eval()

    def runtime_identity(self) -> RuntimeIdentity:
        cuda_available = bool(self._torch.cuda.is_available())
        hardware = self._torch.cuda.get_device_name(0) if cuda_available else "cpu"
        cuda_version = getattr(getattr(self._torch, "version", None), "cuda", None) or "none"
        return RuntimeIdentity(
            python=sys.version.split()[0],
            torch=str(getattr(self._torch, "__version__", "unknown")),
            transformers=_package_version("transformers"),
            accelerate=_package_version("accelerate"),
            hardware=hardware,
            cuda=str(cuda_version),
            thinking_mode="disabled",
        )

    def token_count(self, text: str) -> int:
        return len(self.tokenizer.encode(text))

    def generate(self, messages: list[dict[str, str]], config: GenerationConfig) -> str:
        if config != self.generation_config:
            raise ValueError("generation config drift from pinned pilot configuration")
        self._torch.manual_seed(config.seed)
        prompt = self.tokenizer.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True,
            enable_thinking=False,
        )
        model_inputs = self.tokenizer([prompt], return_tensors="pt").to(self.model.device)
        kwargs = {
            "max_new_tokens": config.max_new_tokens,
            "do_sample": config.do_sample,
            "pad_token_id": self.tokenizer.pad_token_id if self.tokenizer.pad_token_id is not None else self.tokenizer.eos_token_id,
        }
        if config.temperature is not None:
            kwargs["temperature"] = config.temperature
        if config.top_p is not None:
            kwargs["top_p"] = config.top_p
        generated_ids = self.model.generate(**model_inputs, **kwargs)
        output_ids = generated_ids[0][len(model_inputs.input_ids[0]):]
        return self.tokenizer.decode(output_ids, skip_special_tokens=True).strip()
