from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import yaml

DIMS = (
    "evidence_discipline",
    "causal_diagnosis",
    "system_thinking",
    "decision_quality",
    "execution_design",
    "ai_native_redesign",
)


@dataclass(frozen=True)
class Scorecard:
    case_id: str
    scores: dict[str, int]
    total: int
    hard_fail: bool


@dataclass(frozen=True)
class AggregateResult:
    native_mean: float
    eos_mean: float
    skill_lift: float
    native_hard_fail_rate: float
    eos_hard_fail_rate: float
    hard_fail_reduction: float
    dimension_native: dict[str, float]
    dimension_eos: dict[str, float]
    dimension_lift: dict[str, float]
    case_deltas: dict[str, float]


def load_scorecard(path: Path) -> Scorecard:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    scores = data.get("scores", {})
    if set(scores) != set(DIMS):
        raise ValueError(f"scorecard dimensions mismatch: {path}")
    for dim, value in scores.items():
        if value not in (0, 1, 2):
            raise ValueError(f"{dim} score must be 0, 1, or 2")
    total = data.get("total")
    if total != sum(scores.values()):
        raise ValueError(f"total does not equal six-dimension sum: {path}")
    return Scorecard(
        case_id=str(data["case_id"]),
        scores={k: int(v) for k, v in scores.items()},
        total=int(total),
        hard_fail=bool(data.get("hard_fail", False)),
    )


def _load_condition(root: Path, condition: str) -> dict[str, Scorecard]:
    folder = root / "scores" / condition
    cards = {p.stem: load_scorecard(p) for p in sorted(folder.glob("*.yaml"))} if folder.is_dir() else {}
    if len(cards) != 5:
        raise ValueError(f"{condition} must contain exactly five scorecards, found {len(cards)}")
    return cards


def aggregate_experiment(root: Path) -> AggregateResult:
    native = _load_condition(root, "native")
    eos = _load_condition(root, "eos-enabled")
    if set(native) != set(eos):
        raise ValueError("native and eos-enabled scorecard case IDs must match")

    case_ids = sorted(native)
    native_mean = sum(native[c].total for c in case_ids) / len(case_ids)
    eos_mean = sum(eos[c].total for c in case_ids) / len(case_ids)
    native_hf = sum(native[c].hard_fail for c in case_ids) / len(case_ids)
    eos_hf = sum(eos[c].hard_fail for c in case_ids) / len(case_ids)
    dim_native = {d: sum(native[c].scores[d] for c in case_ids) / len(case_ids) for d in DIMS}
    dim_eos = {d: sum(eos[c].scores[d] for c in case_ids) / len(case_ids) for d in DIMS}
    dim_lift = {d: dim_eos[d] - dim_native[d] for d in DIMS}
    case_deltas = {c: eos[c].total - native[c].total for c in case_ids}

    return AggregateResult(
        native_mean=native_mean,
        eos_mean=eos_mean,
        skill_lift=eos_mean - native_mean,
        native_hard_fail_rate=native_hf,
        eos_hard_fail_rate=eos_hf,
        hard_fail_reduction=native_hf - eos_hf,
        dimension_native=dim_native,
        dimension_eos=dim_eos,
        dimension_lift=dim_lift,
        case_deltas=case_deltas,
    )
