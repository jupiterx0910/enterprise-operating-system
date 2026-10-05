from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class GenerationConfig:
    do_sample: bool
    temperature: float | None
    top_p: float | None
    seed: int
    max_new_tokens: int


@dataclass(frozen=True)
class RuntimeIdentity:
    python: str
    torch: str
    transformers: str
    accelerate: str
    hardware: str
    cuda: str


@dataclass(frozen=True)
class RunManifest:
    run_id: str
    benchmark_version: str
    condition: str
    model_repository: str
    model_revision: str
    tokenizer_revision: str
    generation: GenerationConfig
    runtime: RuntimeIdentity
    case_snapshot: str
    baseline_system_prompt_hash: str
    skill_loaded: bool
    skill_bundle_sha256: str | None
    skill_commit: str | None
    trial: int


@dataclass(frozen=True)
class ExperimentManifest:
    experiment_id: str
    benchmark_version: str
    status: str
    eligibility: str
    model_repository: str
    model_revision: str
    case_snapshot: str
    runner_commit: str
    skill_commit: str
    skill_bundle_sha256: str
    cases: tuple[str, ...]
    conditions: tuple[str, ...]
    trials_per_case: int
    verified: bool


def _diff(label: str, left: object, right: object, out: list[str]) -> None:
    if left != right:
        out.append(f"drift: {label}: native={left!r} eos={right!r}")


def validate_pair(native: RunManifest, eos: RunManifest) -> list[str]:
    violations: list[str] = []

    if native.condition != "NATIVE":
        violations.append(f"native condition must be NATIVE, got {native.condition!r}")
    if eos.condition != "EOS_ENABLED":
        violations.append(f"eos condition must be EOS_ENABLED, got {eos.condition!r}")
    if native.skill_loaded:
        violations.append("NATIVE must have skill_loaded=false")
    if not eos.skill_loaded:
        violations.append("EOS_ENABLED must have skill_loaded=true")
    if native.skill_bundle_sha256 is not None:
        violations.append("NATIVE must not carry skill_bundle_sha256")
    if native.skill_commit is not None:
        violations.append("NATIVE must not carry skill_commit")
    if not eos.skill_bundle_sha256:
        violations.append("EOS_ENABLED requires skill_bundle_sha256")
    if not eos.skill_commit:
        violations.append("EOS_ENABLED requires skill_commit")

    for field in (
        "benchmark_version",
        "model_repository",
        "model_revision",
        "tokenizer_revision",
        "case_snapshot",
        "baseline_system_prompt_hash",
        "trial",
    ):
        _diff(field, getattr(native, field), getattr(eos, field), violations)

    for field in ("do_sample", "temperature", "top_p", "seed", "max_new_tokens"):
        _diff(f"generation.{field}", getattr(native.generation, field), getattr(eos.generation, field), violations)

    for field in ("python", "torch", "transformers", "accelerate", "hardware", "cuda"):
        _diff(f"runtime.{field}", getattr(native.runtime, field), getattr(eos.runtime, field), violations)

    return violations


def validate_experiment_manifest(experiment: ExperimentManifest) -> list[str]:
    violations: list[str] = []
    if experiment.benchmark_version != "v0.5-pilot":
        violations.append("benchmark_version must be v0.5-pilot")
    if experiment.status != "pilot":
        violations.append("status must be pilot")
    if experiment.eligibility != "Candidate":
        violations.append("pilot eligibility must be Candidate; Verified is not allowed")
    if experiment.trials_per_case != 1:
        violations.append("pilot trials_per_case must equal 1")
    if experiment.verified:
        violations.append("pilot verified must be false")
    if experiment.conditions != ("NATIVE", "EOS_ENABLED"):
        violations.append("conditions must be exactly (NATIVE, EOS_ENABLED)")
    if len(experiment.cases) != 5:
        violations.append("pilot must contain exactly five cases")
    return violations
