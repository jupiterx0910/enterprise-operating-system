from pathlib import Path
import yaml
import pytest

from benchmark.runner.aggregate_scores import aggregate_experiment, load_scorecard

DIMS = [
    "evidence_discipline",
    "causal_diagnosis",
    "system_thinking",
    "decision_quality",
    "execution_design",
    "ai_native_redesign",
]


def write_card(root: Path, condition: str, case_id: str, scores: list[int], hard_fail=False):
    path = root / "scores" / condition / f"{case_id}.yaml"
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "case_id": case_id,
        "run_id": f"{condition}-{case_id}",
        "scores": dict(zip(DIMS, scores)),
        "total": sum(scores),
        "hard_fail": hard_fail,
        "hard_fail_reasons": ["x"] if hard_fail else [],
        "reviewer_notes": "",
        "evaluator": {"method": "llm-assisted"},
    }
    path.write_text(yaml.safe_dump(data, sort_keys=False), encoding="utf-8")
    return path


def populate(root: Path):
    for i in range(1, 6):
        write_card(root, "native", f"case-{i}", [1,1,1,1,1,1], hard_fail=i==1)
        write_card(root, "eos-enabled", f"case-{i}", [2,2,2,2,2,2], hard_fail=False)


def test_total_must_equal_six_dimension_sum(tmp_path: Path):
    p = write_card(tmp_path, "native", "case-1", [1,1,1,1,1,1])
    data = yaml.safe_load(p.read_text()); data["total"] = 7; p.write_text(yaml.safe_dump(data))
    with pytest.raises(ValueError, match="total"):
        load_scorecard(p)


def test_dimension_scores_must_be_zero_one_or_two(tmp_path: Path):
    p = write_card(tmp_path, "native", "case-1", [3,1,1,1,1,1])
    with pytest.raises(ValueError, match="0, 1, or 2"):
        load_scorecard(p)


def test_aggregate_recomputes_skill_lift_from_scorecards(tmp_path: Path):
    populate(tmp_path)
    result = aggregate_experiment(tmp_path)
    assert result.native_mean == 6
    assert result.eos_mean == 12
    assert result.skill_lift == 6


def test_aggregate_recomputes_hard_fail_reduction(tmp_path: Path):
    populate(tmp_path)
    result = aggregate_experiment(tmp_path)
    assert result.native_hard_fail_rate == 0.2
    assert result.eos_hard_fail_rate == 0.0
    assert result.hard_fail_reduction == 0.2


def test_missing_one_scorecard_blocks_publication(tmp_path: Path):
    populate(tmp_path)
    (tmp_path / "scores/eos-enabled/case-5.yaml").unlink()
    with pytest.raises(ValueError, match="exactly five"):
        aggregate_experiment(tmp_path)


def test_summary_numbers_cannot_override_scorecards(tmp_path: Path):
    populate(tmp_path)
    (tmp_path / "summary.md").write_text("Skill Lift: 999\n")
    assert aggregate_experiment(tmp_path).skill_lift == 6
