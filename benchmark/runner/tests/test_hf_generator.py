from dataclasses import replace
from types import SimpleNamespace

import pytest

from benchmark.runner.protocol import GenerationConfig
from benchmark.runner.resolve_model_revision import resolve_model_revision
from benchmark.runner import hf_transformers_generator as mod


def config():
    return GenerationConfig(False, None, None, 42, 1800)


def test_revision_must_be_exact_commit_sha(monkeypatch):
    monkeypatch.setattr("benchmark.runner.resolve_model_revision.model_info", lambda repo_id: SimpleNamespace(sha="not-a-sha"))
    with pytest.raises(ValueError, match="40-character"):
        resolve_model_revision("Qwen/Qwen3-8B")


class FakeBatch(dict):
    def __init__(self):
        super().__init__(input_ids=[[1, 2, 3]])
        self.input_ids = [[1, 2, 3]]
    def to(self, device):
        self.device = device
        return self


class FakeTokenizerInstance:
    pad_token_id = 0
    eos_token_id = 99
    def __init__(self):
        self.template_kwargs = None
    def apply_chat_template(self, messages, **kwargs):
        self.template_kwargs = kwargs
        return "PROMPT"
    def __call__(self, texts, return_tensors):
        return FakeBatch()
    def decode(self, ids, skip_special_tokens=True):
        return "FINAL ANSWER"
    def encode(self, text):
        return list(range(len(text.split())))


class FakeTokenizer:
    calls = []
    instance = FakeTokenizerInstance()
    @classmethod
    def from_pretrained(cls, repo_id, **kwargs):
        cls.calls.append((repo_id, kwargs))
        return cls.instance


class FakeModelInstance:
    device = "cuda:0"
    def __init__(self):
        self.generate_kwargs = None
    def eval(self):
        return self
    def generate(self, **kwargs):
        self.generate_kwargs = kwargs
        return [[1, 2, 3, 9, 10]]


class FakeModel:
    calls = []
    instance = FakeModelInstance()
    @classmethod
    def from_pretrained(cls, repo_id, **kwargs):
        cls.calls.append((repo_id, kwargs))
        return cls.instance


class FakeCuda:
    @staticmethod
    def is_available(): return True
    @staticmethod
    def get_device_name(index): return "NVIDIA A10G"


class FakeTorch:
    __version__ = "2.fake"
    bfloat16 = "bf16"
    cuda = FakeCuda()
    version = SimpleNamespace(cuda="12.fake")
    seeds = []
    @classmethod
    def manual_seed(cls, seed): cls.seeds.append(seed)


def fake_deps():
    return FakeTorch, FakeModel, FakeTokenizer


def test_model_and_tokenizer_receive_same_revision(monkeypatch):
    FakeTokenizer.calls.clear(); FakeModel.calls.clear()
    monkeypatch.setattr(mod, "_load_dependencies", fake_deps)
    revision = "a" * 40
    mod.TransformersGenerator("Qwen/Qwen3-8B", revision, config())
    assert FakeTokenizer.calls[-1][1]["revision"] == revision
    assert FakeModel.calls[-1][1]["revision"] == revision
    assert FakeModel.calls[-1][1]["torch_dtype"] == "bf16"
    assert FakeModel.calls[-1][1]["low_cpu_mem_usage"] is True


def test_generation_uses_fixed_nonthinking_greedy_settings(monkeypatch):
    FakeModel.instance = FakeModelInstance(); FakeTokenizer.instance = FakeTokenizerInstance()
    monkeypatch.setattr(mod, "_load_dependencies", fake_deps)
    generator = mod.TransformersGenerator("Qwen/Qwen3-8B", "a" * 40, config())
    answer = generator.generate([{"role": "user", "content": "x"}], config())
    assert answer == "FINAL ANSWER"
    assert FakeTokenizer.instance.template_kwargs["enable_thinking"] is False
    assert FakeModel.instance.generate_kwargs["do_sample"] is False
    assert FakeModel.instance.generate_kwargs["max_new_tokens"] == 1800
    assert "temperature" not in FakeModel.instance.generate_kwargs
    assert "top_p" not in FakeModel.instance.generate_kwargs


def test_generator_rejects_runtime_generation_drift(monkeypatch):
    monkeypatch.setattr(mod, "_load_dependencies", fake_deps)
    generator = mod.TransformersGenerator("Qwen/Qwen3-8B", "a" * 40, config())
    with pytest.raises(ValueError, match="generation config drift"):
        generator.generate([{"role": "user", "content": "x"}], replace(config(), seed=7))


def test_actual_runtime_metadata_is_recorded(monkeypatch):
    monkeypatch.setattr(mod, "_load_dependencies", fake_deps)
    monkeypatch.setattr(mod, "_package_version", lambda name: f"{name}-v")
    generator = mod.TransformersGenerator("Qwen/Qwen3-8B", "a" * 40, config())
    runtime = generator.runtime_identity()
    assert runtime.hardware == "NVIDIA A10G"
    assert runtime.cuda == "12.fake"
    assert runtime.thinking_mode == "disabled"
    assert runtime.transformers == "transformers-v"
    assert runtime.accelerate == "accelerate-v"
