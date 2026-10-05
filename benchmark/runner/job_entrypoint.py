from __future__ import annotations

import base64
from dataclasses import replace
from hashlib import sha256
from io import BytesIO
import os
from pathlib import Path
import tarfile
import textwrap

from .build_skill_bundle import build_skill_bundle
from .hf_transformers_generator import TransformersGenerator
from .protocol import ExperimentManifest, GenerationConfig, RunManifest
from .run_pilot import BASELINE_SYSTEM_PROMPT, run_experiment
from .validate_artifacts import validate_artifact_tree

MODEL_REPOSITORY = "Qwen/Qwen3-8B"
PILOT_CASES = (
    "benchmark/real-world/21-wells-fargo-incentive-distortion.md",
    "benchmark/real-world/22-target-canada-operating-model.md",
    "benchmark/real-world/23-uber-culture-governance.md",
    "benchmark/real-world/24-equifax-accountability-gap.md",
    "benchmark/real-world/25-boeing-737-max-governance.md",
)
CONDITIONS = ("NATIVE", "EOS_ENABLED")


def validate_pilot_scope(case_paths, conditions, trials_per_case: int) -> None:
    if len(case_paths) != 5:
        raise ValueError("pilot requires exactly five cases")
    generations = len(case_paths) * len(conditions) * trials_per_case
    if generations != 10:
        raise ValueError(f"pilot must execute exactly 10 generations, got {generations}")
    if tuple(conditions) != CONDITIONS:
        raise ValueError("pilot conditions must be exactly NATIVE and EOS_ENABLED")


def encode_artifact_archive(root: Path) -> tuple[str, str]:
    buffer = BytesIO()
    with tarfile.open(fileobj=buffer, mode="w:gz") as archive:
        archive.add(root, arcname=".")
    data = buffer.getvalue()
    return base64.b64encode(data).decode("ascii"), sha256(data).hexdigest()


def decode_artifact_archive(payload: str, expected_sha256: str, target_dir: Path) -> None:
    data = base64.b64decode(payload.encode("ascii"), validate=True)
    actual = sha256(data).hexdigest()
    if actual != expected_sha256:
        raise ValueError(f"artifact checksum mismatch: expected {expected_sha256}, got {actual}")
    target_dir.mkdir(parents=True, exist_ok=True)
    with tarfile.open(fileobj=BytesIO(data), mode="r:gz") as archive:
        archive.extractall(target_dir, filter="data")


def _required_env(name: str) -> str:
    value = os.environ.get(name)
    if not value:
        raise RuntimeError(f"required environment variable missing: {name}")
    return value


def _emit_archive(root: Path) -> None:
    payload, digest = encode_artifact_archive(root)
    print(f"EOS_ARTIFACT_SHA256={digest}", flush=True)
    print("EOS_ARTIFACT_TGZ_BASE64_BEGIN", flush=True)
    for line in textwrap.wrap(payload, 76):
        print(line, flush=True)
    print("EOS_ARTIFACT_TGZ_BASE64_END", flush=True)


def main() -> int:
    repo_root = Path(os.environ.get("EOS_REPO_ROOT", ".")).resolve()
    output_root = Path(os.environ.get("EOS_OUTPUT_ROOT", "/tmp/eos-results")).resolve()
    experiment_id = os.environ.get("EXPERIMENT_ID", "20261005-qwen3-8b-v05-pilot-r1")
    runner_commit = _required_env("RUNNER_COMMIT")
    model_revision = _required_env("MODEL_REVISION")
    case_snapshot = os.environ.get("CASE_SNAPSHOT", runner_commit)
    skill_commit = os.environ.get("SKILL_COMMIT", runner_commit)

    validate_pilot_scope(PILOT_CASES, CONDITIONS, 1)
    generation = GenerationConfig(do_sample=False, temperature=None, top_p=None, seed=42, max_new_tokens=1800)
    generator = TransformersGenerator(MODEL_REPOSITORY, model_revision, generation)
    skill_dir = repo_root / "skills" / "enterprise-operating-system"
    bundle = build_skill_bundle(skill_dir, token_counter=generator.token_count)
    runtime = generator.runtime_identity()
    prompt_hash = sha256(BASELINE_SYSTEM_PROMPT.encode("utf-8")).hexdigest()

    native = RunManifest(
        run_id=f"{experiment_id}-native-r1",
        benchmark_version="v0.5-pilot",
        condition="NATIVE",
        model_repository=MODEL_REPOSITORY,
        model_revision=model_revision,
        tokenizer_revision=model_revision,
        generation=generation,
        runtime=runtime,
        case_snapshot=case_snapshot,
        baseline_system_prompt_hash=prompt_hash,
        skill_loaded=False,
        skill_bundle_sha256=None,
        skill_commit=None,
        trial=1,
    )
    eos = replace(
        native,
        run_id=f"{experiment_id}-eos-enabled-r1",
        condition="EOS_ENABLED",
        skill_loaded=True,
        skill_bundle_sha256=bundle.sha256,
        skill_commit=skill_commit,
    )
    case_paths = tuple(repo_root / p for p in PILOT_CASES)
    case_ids = tuple(p.stem.split("-", 1)[1] for p in case_paths)
    experiment = ExperimentManifest(
        experiment_id=experiment_id,
        benchmark_version="v0.5-pilot",
        status="pilot",
        eligibility="Candidate",
        model_repository=MODEL_REPOSITORY,
        model_revision=model_revision,
        case_snapshot=case_snapshot,
        runner_commit=runner_commit,
        skill_commit=skill_commit,
        skill_bundle_sha256=bundle.sha256,
        cases=case_ids,
        conditions=CONDITIONS,
        trials_per_case=1,
        verified=False,
        skill_bundle_token_count=bundle.token_count,
    )
    root = run_experiment(
        case_paths,
        output_root,
        native,
        eos,
        experiment,
        BASELINE_SYSTEM_PROMPT,
        bundle,
        generator,
    )
    violations = validate_artifact_tree(root)
    if violations:
        raise RuntimeError("artifact validation failed: " + "; ".join(violations))
    _emit_archive(root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
