from __future__ import annotations

from dataclasses import asdict
from hashlib import sha256
from pathlib import Path
from typing import Protocol, Sequence

import yaml

from .build_skill_bundle import SkillBundle
from .extract_case import CaseInput, extract_case
from .protocol import ExperimentManifest, GenerationConfig, RunManifest, validate_experiment_manifest, validate_pair

BASELINE_SYSTEM_PROMPT = (
    "You are an enterprise operating advisor. Analyze the case using only the evidence provided. "
    "Distinguish facts, inference, assumptions, and unknowns. Give a decision-oriented answer and do not invent missing facts."
)


class GeneratorProtocol(Protocol):
    def generate(self, messages: list[dict[str, str]], config: GenerationConfig) -> str: ...


def build_generation_messages(
    case: CaseInput,
    condition: str,
    baseline_system: str,
    skill_bundle: SkillBundle | None,
) -> list[dict[str, str]]:
    if condition == "NATIVE":
        if skill_bundle is not None:
            raise ValueError("NATIVE must not receive a Skill bundle")
        system = baseline_system
    elif condition == "EOS_ENABLED":
        if skill_bundle is None:
            raise ValueError("EOS_ENABLED requires a Skill bundle")
        system = baseline_system + "\n\n## ENTERPRISE OPERATING SYSTEM SKILL\n" + skill_bundle.text
    else:
        raise ValueError(f"unsupported condition: {condition}")

    user = (
        f"## Context / 背景\n{case.context}\n\n"
        f"## Evidence / 证据\n{case.evidence}\n\n"
        f"## Prompt / 用户问题\n{case.prompt}"
    )
    return [
        {"role": "system", "content": system},
        {"role": "user", "content": user},
    ]


def _write_yaml(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(value, sort_keys=False, allow_unicode=True), encoding="utf-8")


def run_experiment(
    case_paths: Sequence[Path],
    output_root: Path,
    native_manifest: RunManifest,
    eos_manifest: RunManifest,
    experiment: ExperimentManifest,
    baseline_system: str,
    skill_bundle: SkillBundle,
    generator: GeneratorProtocol,
) -> Path:
    if len(case_paths) != 5:
        raise ValueError(f"pilot requires exactly five cases, got {len(case_paths)}")

    experiment_errors = validate_experiment_manifest(experiment)
    if experiment_errors:
        raise ValueError("invalid experiment manifest: " + "; ".join(experiment_errors))
    pair_errors = validate_pair(native_manifest, eos_manifest)
    if pair_errors:
        raise ValueError("invalid paired manifests: " + "; ".join(pair_errors))

    expected_prompt_hash = sha256(baseline_system.encode("utf-8")).hexdigest()
    if native_manifest.baseline_system_prompt_hash != expected_prompt_hash:
        raise ValueError("native baseline_system_prompt_hash does not match baseline prompt")
    if eos_manifest.baseline_system_prompt_hash != expected_prompt_hash:
        raise ValueError("eos baseline_system_prompt_hash does not match baseline prompt")
    if eos_manifest.skill_bundle_sha256 != skill_bundle.sha256:
        raise ValueError("eos skill_bundle_sha256 does not match built Skill bundle")
    if experiment.skill_bundle_sha256 != skill_bundle.sha256:
        raise ValueError("experiment skill_bundle_sha256 does not match built Skill bundle")

    cases = [extract_case(Path(path)) for path in case_paths]
    case_ids = tuple(case.case_id for case in cases)
    if case_ids != experiment.cases:
        raise ValueError(f"case IDs do not match experiment manifest: {case_ids!r}")
    if len(set(case_ids)) != 5:
        raise ValueError("pilot case IDs must be unique")

    root = output_root / experiment.experiment_id
    native_dir = root / "native"
    eos_dir = root / "eos-enabled"
    (native_dir / "outputs").mkdir(parents=True, exist_ok=True)
    (eos_dir / "outputs").mkdir(parents=True, exist_ok=True)

    _write_yaml(root / "experiment.yaml", asdict(experiment))
    _write_yaml(native_dir / "manifest.yaml", asdict(native_manifest))
    _write_yaml(eos_dir / "manifest.yaml", asdict(eos_manifest))

    for condition, run_manifest, condition_dir, bundle in (
        ("NATIVE", native_manifest, native_dir, None),
        ("EOS_ENABLED", eos_manifest, eos_dir, skill_bundle),
    ):
        for case in cases:
            messages = build_generation_messages(case, condition, baseline_system, bundle)
            output = generator.generate(messages, run_manifest.generation)
            (condition_dir / "outputs" / f"{case.case_id}.md").write_text(output, encoding="utf-8")

    return root
