from dataclasses import replace
from hashlib import sha256
from pathlib import Path

import pytest

from benchmark.runner.build_skill_bundle import build_skill_bundle
from benchmark.runner.extract_case import extract_case
from benchmark.runner.fixtures.fake_generator import FakeGenerator
from benchmark.runner.protocol import ExperimentManifest, GenerationConfig, RunManifest, RuntimeIdentity
from benchmark.runner.run_pilot import BASELINE_SYSTEM_PROMPT, build_generation_messages, run_experiment


def make_case(root: Path, index: int) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    path = root / f"{index}.md"
    path.write_text(
        f'''# Case {index}\n\n```yaml\nid: case-{index}\ntype: real-world\n```\n\n## Context / 背景\nContext {index}.\n\n## Evidence / 证据\n- Evidence {index}.\n\n## Prompt / 用户问题\nPrompt {index}?\n\n## Expected reasoning / 期望推理\nSECRET {index}.\n\n## Forbidden shortcuts / 禁止捷径\nSECRET shortcut.\n\n## Decision criteria / 决策标准\nSECRET criteria.\n\n## Evaluation notes / 评测说明\nSECRET notes.\n\n## Source provenance / 来源溯源\nSECRET provenance.\n''',
        encoding="utf-8",
    )
    return path


def make_skill(root: Path) -> Path:
    skill = root / "skills" / "enterprise-operating-system"
    (skill / "engines").mkdir(parents=True)
    (skill / "SKILL.md").write_text("EOS ENTRY\n", encoding="utf-8")
    (skill / "engines" / "router.md").write_text("EOS ROUTER\n", encoding="utf-8")
    return skill


def runtime() -> RuntimeIdentity:
    return RuntimeIdentity("3.11", "2.8", "4.57", "1.10", "a10g", "12.8")


def gen() -> GenerationConfig:
    return GenerationConfig(False, None, None, 42, 1800)


def run_manifest(condition: str) -> RunManifest:
    return RunManifest(
        run_id=f"run-{condition.lower()}", benchmark_version="v0.5-pilot", condition=condition,
        model_repository="Qwen/Qwen3-8B", model_revision="a"*40, tokenizer_revision="a"*40,
        generation=gen(), runtime=runtime(), case_snapshot="b"*40,
        baseline_system_prompt_hash=sha256(BASELINE_SYSTEM_PROMPT.encode("utf-8")).hexdigest(), skill_loaded=condition == "EOS_ENABLED",
        skill_bundle_sha256=None if condition == "NATIVE" else "BUNDLE_HASH",
        skill_commit="e"*40 if condition == "EOS_ENABLED" else None, trial=1,
    )


def experiment(bundle_hash: str = "BUNDLE_HASH") -> ExperimentManifest:
    return ExperimentManifest(
        experiment_id="exp", benchmark_version="v0.5-pilot", status="pilot", eligibility="Candidate",
        model_repository="Qwen/Qwen3-8B", model_revision="a"*40, case_snapshot="b"*40,
        runner_commit="f"*40, skill_commit="e"*40, skill_bundle_sha256=bundle_hash,
        cases=tuple(f"case-{i}" for i in range(1, 6)), conditions=("NATIVE", "EOS_ENABLED"),
        trials_per_case=1, verified=False,
    )


def test_native_and_eos_share_identical_case_payload(tmp_path: Path):
    case = extract_case(make_case(tmp_path, 1))
    bundle = build_skill_bundle(make_skill(tmp_path))
    native = build_generation_messages(case, "NATIVE", BASELINE_SYSTEM_PROMPT, None)
    eos = build_generation_messages(case, "EOS_ENABLED", BASELINE_SYSTEM_PROMPT, bundle)
    assert native[1] == eos[1]


def test_eos_only_adds_skill_bundle_to_system_context(tmp_path: Path):
    case = extract_case(make_case(tmp_path, 1))
    bundle = build_skill_bundle(make_skill(tmp_path))
    native = build_generation_messages(case, "NATIVE", BASELINE_SYSTEM_PROMPT, None)
    eos = build_generation_messages(case, "EOS_ENABLED", BASELINE_SYSTEM_PROMPT, bundle)
    assert native[0]["content"] == BASELINE_SYSTEM_PROMPT
    assert eos[0]["content"].startswith(BASELINE_SYSTEM_PROMPT)
    assert bundle.text in eos[0]["content"]


def test_run_creates_exactly_ten_outputs_for_five_cases(tmp_path: Path):
    cases = [make_case(tmp_path / "cases", i) for i in range(1, 6)]
    bundle = build_skill_bundle(make_skill(tmp_path))
    eos = replace(run_manifest("EOS_ENABLED"), skill_bundle_sha256=bundle.sha256)
    root = run_experiment(cases, tmp_path / "out", run_manifest("NATIVE"), eos, experiment(bundle.sha256), BASELINE_SYSTEM_PROMPT, bundle, FakeGenerator())
    outputs = list(root.glob("native/outputs/*.md")) + list(root.glob("eos-enabled/outputs/*.md"))
    assert len(outputs) == 10


def test_run_writes_output_immediately_after_each_generation(tmp_path: Path):
    cases = [make_case(tmp_path / "cases", i) for i in range(1, 6)]
    bundle = build_skill_bundle(make_skill(tmp_path))
    eos = replace(run_manifest("EOS_ENABLED"), skill_bundle_sha256=bundle.sha256)
    generator = FakeGenerator(fail_after=3)
    with pytest.raises(RuntimeError, match="planned fake failure"):
        run_experiment(cases, tmp_path / "out", run_manifest("NATIVE"), eos, experiment(bundle.sha256), BASELINE_SYSTEM_PROMPT, bundle, generator)
    assert len(list((tmp_path / "out" / "exp" / "native" / "outputs").glob("*.md"))) == 3
    assert (tmp_path / "out" / "exp" / "experiment.yaml").is_file()
    assert (tmp_path / "out" / "exp" / "native" / "manifest.yaml").is_file()
    assert (tmp_path / "out" / "exp" / "eos-enabled" / "manifest.yaml").is_file()


def test_runner_never_reads_hidden_case_sections(tmp_path: Path):
    cases = [make_case(tmp_path / "cases", i) for i in range(1, 6)]
    bundle = build_skill_bundle(make_skill(tmp_path))
    eos = replace(run_manifest("EOS_ENABLED"), skill_bundle_sha256=bundle.sha256)
    generator = FakeGenerator()
    run_experiment(cases, tmp_path / "out", run_manifest("NATIVE"), eos, experiment(bundle.sha256), BASELINE_SYSTEM_PROMPT, bundle, generator)
    all_messages = "\n".join(m["content"] for call in generator.calls for m in call["messages"])
    assert "SECRET 1" not in all_messages
    assert "SECRET notes" not in all_messages
