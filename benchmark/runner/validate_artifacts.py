from __future__ import annotations

from pathlib import Path

import yaml

from .protocol import (
    ExperimentManifest,
    GenerationConfig,
    RunManifest,
    RuntimeIdentity,
    validate_experiment_manifest,
    validate_pair,
)


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def _load_run(path: Path) -> RunManifest:
    data = _load_yaml(path)
    data["generation"] = GenerationConfig(**data["generation"])
    data["runtime"] = RuntimeIdentity(**data["runtime"])
    return RunManifest(**data)


def _load_experiment(path: Path) -> ExperimentManifest:
    data = _load_yaml(path)
    data["cases"] = tuple(data["cases"])
    data["conditions"] = tuple(data["conditions"])
    return ExperimentManifest(**data)


def validate_artifact_tree(root: Path) -> list[str]:
    violations: list[str] = []
    required = [
        root / "experiment.yaml",
        root / "native" / "manifest.yaml",
        root / "eos-enabled" / "manifest.yaml",
    ]
    for path in required:
        if not path.is_file():
            violations.append(f"missing required artifact: {path.relative_to(root)}")
    if violations:
        return violations

    try:
        experiment = _load_experiment(root / "experiment.yaml")
        native = _load_run(root / "native" / "manifest.yaml")
        eos = _load_run(root / "eos-enabled" / "manifest.yaml")
    except Exception as exc:
        return [f"failed to parse manifests: {exc}"]

    violations.extend(validate_experiment_manifest(experiment))
    violations.extend(validate_pair(native, eos))

    if experiment.model_repository != native.model_repository or experiment.model_repository != eos.model_repository:
        violations.append("experiment model_repository does not match paired manifests")
    if experiment.model_revision != native.model_revision or experiment.model_revision != eos.model_revision:
        violations.append("experiment model_revision does not match paired manifests")
    if experiment.case_snapshot != native.case_snapshot or experiment.case_snapshot != eos.case_snapshot:
        violations.append("experiment case_snapshot does not match paired manifests")
    if experiment.skill_bundle_sha256 != eos.skill_bundle_sha256:
        violations.append("experiment skill_bundle_sha256 does not match EOS manifest")
    if experiment.skill_commit != eos.skill_commit:
        violations.append("experiment skill_commit does not match EOS manifest")

    expected = {f"{case_id}.md" for case_id in experiment.cases}
    native_outputs = root / "native" / "outputs"
    eos_outputs = root / "eos-enabled" / "outputs"
    native_names = {p.name for p in native_outputs.glob("*.md")} if native_outputs.is_dir() else set()
    eos_names = {p.name for p in eos_outputs.glob("*.md")} if eos_outputs.is_dir() else set()

    if native_names != expected:
        violations.append(f"expected 5 NATIVE outputs {sorted(expected)}, found {sorted(native_names)}")
    if eos_names != expected:
        violations.append(f"expected 5 EOS_ENABLED outputs {sorted(expected)}, found {sorted(eos_names)}")

    return violations
