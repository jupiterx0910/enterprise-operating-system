from dataclasses import replace
from pathlib import Path

from benchmark.runner.build_skill_bundle import build_skill_bundle
from benchmark.runner.fixtures.fake_generator import FakeGenerator
from benchmark.runner.run_pilot import BASELINE_SYSTEM_PROMPT, run_experiment
from benchmark.runner.validate_artifacts import validate_artifact_tree
from benchmark.runner.tests.test_run_pilot import make_case, make_skill, run_manifest, experiment


def test_complete_tree_is_candidate_eligible(tmp_path: Path):
    cases = [make_case(tmp_path / "cases", i) for i in range(1, 6)]
    bundle = build_skill_bundle(make_skill(tmp_path))
    eos = replace(run_manifest("EOS_ENABLED"), skill_bundle_sha256=bundle.sha256)
    root = run_experiment(cases, tmp_path / "out", run_manifest("NATIVE"), eos, experiment(bundle.sha256), BASELINE_SYSTEM_PROMPT, bundle, FakeGenerator())
    assert validate_artifact_tree(root) == []


def test_partial_nine_of_ten_outputs_is_not_candidate_eligible(tmp_path: Path):
    cases = [make_case(tmp_path / "cases", i) for i in range(1, 6)]
    bundle = build_skill_bundle(make_skill(tmp_path))
    eos = replace(run_manifest("EOS_ENABLED"), skill_bundle_sha256=bundle.sha256)
    root = run_experiment(cases, tmp_path / "out", run_manifest("NATIVE"), eos, experiment(bundle.sha256), BASELINE_SYSTEM_PROMPT, bundle, FakeGenerator())
    next((root / "eos-enabled" / "outputs").glob("*.md")).unlink()
    violations = validate_artifact_tree(root)
    assert any("expected 5 EOS_ENABLED outputs" in v for v in violations)


def test_manifest_drift_is_not_candidate_eligible(tmp_path: Path):
    cases = [make_case(tmp_path / "cases", i) for i in range(1, 6)]
    bundle = build_skill_bundle(make_skill(tmp_path))
    eos = replace(run_manifest("EOS_ENABLED"), skill_bundle_sha256=bundle.sha256)
    root = run_experiment(cases, tmp_path / "out", run_manifest("NATIVE"), eos, experiment(bundle.sha256), BASELINE_SYSTEM_PROMPT, bundle, FakeGenerator())
    manifest = root / "native" / "manifest.yaml"
    text = manifest.read_text(encoding="utf-8").replace("max_new_tokens: 1800", "max_new_tokens: 999")
    manifest.write_text(text, encoding="utf-8")
    assert any("generation.max_new_tokens" in v for v in validate_artifact_tree(root))
