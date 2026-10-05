from dataclasses import replace

import pytest

from benchmark.runner.protocol import (
    ExperimentManifest,
    GenerationConfig,
    RunManifest,
    RuntimeIdentity,
    validate_experiment_manifest,
    validate_pair,
)


def base_config() -> GenerationConfig:
    return GenerationConfig(do_sample=False, temperature=None, top_p=None, seed=42, max_new_tokens=1800)


def runtime() -> RuntimeIdentity:
    return RuntimeIdentity(
        python="3.11",
        torch="2.8.0",
        transformers="4.57.0",
        accelerate="1.10.0",
        hardware="a10g",
        cuda="12.8",
    )


def manifest(condition: str) -> RunManifest:
    return RunManifest(
        run_id=f"run-{condition.lower()}",
        benchmark_version="v0.5-pilot",
        condition=condition,
        model_repository="Qwen/Qwen3-8B",
        model_revision="a" * 40,
        tokenizer_revision="a" * 40,
        generation=base_config(),
        runtime=runtime(),
        case_snapshot="b" * 40,
        baseline_system_prompt_hash="c" * 64,
        skill_loaded=condition == "EOS_ENABLED",
        skill_bundle_sha256="d" * 64 if condition == "EOS_ENABLED" else None,
        skill_commit="e" * 40 if condition == "EOS_ENABLED" else None,
        trial=1,
    )


def test_valid_pair_has_no_drift():
    assert validate_pair(manifest("NATIVE"), manifest("EOS_ENABLED")) == []


@pytest.mark.parametrize(
    ("field", "native_value"),
    [
        ("model_revision", "f" * 40),
        ("tokenizer_revision", "f" * 40),
        ("case_snapshot", "f" * 40),
        ("baseline_system_prompt_hash", "f" * 64),
    ],
)
def test_pair_rejects_top_level_drift(field, native_value):
    native = replace(manifest("NATIVE"), **{field: native_value})
    violations = validate_pair(native, manifest("EOS_ENABLED"))
    assert any(field in v for v in violations)


@pytest.mark.parametrize(
    ("field", "value"),
    [
        ("max_new_tokens", 999),
        ("do_sample", True),
        ("seed", 7),
    ],
)
def test_pair_rejects_generation_drift(field, value):
    native = manifest("NATIVE")
    native = replace(native, generation=replace(native.generation, **{field: value}))
    assert any(f"generation.{field}" in v for v in validate_pair(native, manifest("EOS_ENABLED")))


@pytest.mark.parametrize("field", ["python", "torch", "transformers", "accelerate", "hardware", "cuda"])
def test_pair_rejects_runtime_drift(field):
    native = manifest("NATIVE")
    native = replace(native, runtime=replace(native.runtime, **{field: "DIFFERENT"}))
    assert any(f"runtime.{field}" in v for v in validate_pair(native, manifest("EOS_ENABLED")))


def test_only_skill_loaded_and_skill_bundle_metadata_may_differ():
    native = manifest("NATIVE")
    eos = manifest("EOS_ENABLED")
    assert native.skill_loaded is False and eos.skill_loaded is True
    assert native.skill_bundle_sha256 is None and eos.skill_bundle_sha256
    assert validate_pair(native, eos) == []


def test_candidate_requires_trials_per_case_one_and_verified_false():
    exp = ExperimentManifest(
        experiment_id="exp",
        benchmark_version="v0.5-pilot",
        status="pilot",
        eligibility="Candidate",
        model_repository="Qwen/Qwen3-8B",
        model_revision="a" * 40,
        case_snapshot="b" * 40,
        runner_commit="c" * 40,
        skill_commit="d" * 40,
        skill_bundle_sha256="e" * 64,
        cases=("c1", "c2", "c3", "c4", "c5"),
        conditions=("NATIVE", "EOS_ENABLED"),
        trials_per_case=1,
        verified=False,
    )
    assert validate_experiment_manifest(exp) == []


def test_candidate_cannot_become_verified_by_summary_label():
    exp = ExperimentManifest(
        experiment_id="exp",
        benchmark_version="v0.5-pilot",
        status="pilot",
        eligibility="Verified",
        model_repository="Qwen/Qwen3-8B",
        model_revision="a" * 40,
        case_snapshot="b" * 40,
        runner_commit="c" * 40,
        skill_commit="d" * 40,
        skill_bundle_sha256="e" * 64,
        cases=("c1", "c2", "c3", "c4", "c5"),
        conditions=("NATIVE", "EOS_ENABLED"),
        trials_per_case=1,
        verified=True,
    )
    violations = validate_experiment_manifest(exp)
    assert any("Verified" in v or "verified" in v for v in violations)
