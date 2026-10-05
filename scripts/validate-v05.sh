#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

required=(
  "$ROOT/benchmark/runner/extract_case.py"
  "$ROOT/benchmark/runner/build_skill_bundle.py"
  "$ROOT/benchmark/runner/protocol.py"
  "$ROOT/benchmark/runner/run_pilot.py"
  "$ROOT/benchmark/runner/validate_artifacts.py"
  "$ROOT/benchmark/runner/hf_transformers_generator.py"
  "$ROOT/benchmark/runner/job_entrypoint.py"
  "$ROOT/benchmark/runner/aggregate_scores.py"
  "$ROOT/benchmark/runner/job_spec.md"
  "$ROOT/leaderboard/README.md"
)

for file in "${required[@]}"; do
  test -f "$file" || { echo "ERROR: missing v0.5 file: ${file#$ROOT/}"; exit 1; }
done

python -m pytest "$ROOT/benchmark/runner/tests" -q

if grep -R -E 'hf[[:space:]]+jobs[[:space:]]+(run|uv)|run_job\(|run_uv_job\(' "$ROOT/.github/workflows" --include='*.yml' --include='*.yaml'; then
  echo "ERROR: core GitHub Actions must not launch paid Hugging Face Jobs"
  exit 1
fi

grep -Fq 'No verified submissions yet' "$ROOT/leaderboard/README.md" || {
  echo "ERROR: Verified leaderboard status must remain explicit"
  exit 1
}

scored_experiments=0
if test -d "$ROOT/benchmark/runs/submissions"; then
  while IFS= read -r -d '' exp; do
    if test -d "$exp/scores/native" && test -d "$exp/scores/eos-enabled"; then
      scored_experiments=$((scored_experiments + 1))
      PYTHONPATH="$ROOT" python - "$exp" <<'PY'
from pathlib import Path
import sys
from benchmark.runner.validate_artifacts import validate_artifact_tree
from benchmark.runner.aggregate_scores import aggregate_experiment

root = Path(sys.argv[1])
violations = validate_artifact_tree(root)
if violations:
    for violation in violations:
        print(f"ERROR: {root.name}: {violation}")
    raise SystemExit(1)
result = aggregate_experiment(root)
print(f"Scored experiment OK: {root.name}; Skill Lift={result.skill_lift:.3f}")
PY
    fi
  done < <(find "$ROOT/benchmark/runs/submissions" -mindepth 1 -maxdepth 1 -type d -print0 | sort -z)
fi

if grep -Eq '^\|.*Candidate/Pilot.*\|[[:space:]]*-?[0-9]+([.][0-9]+)?[[:space:]]*\|' "$ROOT/leaderboard/README.md"; then
  if test "$scored_experiments" -eq 0; then
    echo "ERROR: numeric Candidate leaderboard rows require a scored experiment"
    exit 1
  fi
fi

echo "v0.5 validation passed: runner tests green; publication integrity checks passed; scored experiments=$scored_experiments."
