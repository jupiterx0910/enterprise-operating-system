#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

required=(
  "$ROOT/benchmark/real-world/README.md"
  "$ROOT/benchmark/runs/README.md"
  "$ROOT/benchmark/runs/schema.md"
  "$ROOT/benchmark/runs/example-manifest.yaml"
  "$ROOT/benchmark/runs/submissions/README.md"
  "$ROOT/leaderboard/README.md"
  "$ROOT/leaderboard/METHODOLOGY.md"
  "$ROOT/leaderboard/submissions/README.md"
)

for file in "${required[@]}"; do
  test -f "$file" || { echo "ERROR: missing $file"; exit 1; }
done

cases=(
  21-wells-fargo-incentive-distortion.md
  22-target-canada-operating-model.md
  23-uber-culture-governance.md
  24-equifax-accountability-gap.md
  25-boeing-737-max-governance.md
)

for name in "${cases[@]}"; do
  file="$ROOT/benchmark/real-world/$name"
  test -f "$file" || { echo "ERROR: missing $file"; exit 1; }
  for heading in     "## Context / 背景"     "## Evidence / 证据"     "## Prompt / 用户问题"     "## Expected reasoning / 期望推理"     "## Forbidden shortcuts / 禁止捷径"     "## Decision criteria / 决策标准"     "## Evaluation notes / 评测说明"     "## Source provenance / 来源溯源"; do
    grep -Fq "$heading" "$file" || { echo "ERROR: $file missing heading: $heading"; exit 1; }
  done
  grep -Fq 'type: real-world' "$file" || { echo "ERROR: $file missing real-world type"; exit 1; }
  grep -Fq 'source_class:' "$file" || { echo "ERROR: $file missing source_class"; exit 1; }
  grep -Fq 'evidence_cutoff:' "$file" || { echo "ERROR: $file missing evidence_cutoff"; exit 1; }
  grep -Fq 'url: https://' "$file" || { echo "ERROR: $file missing source URL"; exit 1; }
done

grep -Fq 'No verified submissions yet' "$ROOT/leaderboard/README.md" || {
  echo "ERROR: leaderboard must explicitly state that no verified submissions exist until real runs are added"
  exit 1
}

submission_files="$(
  {
    find "$ROOT/leaderboard/submissions" -type f ! -name 'README*.md' -print 2>/dev/null
    find "$ROOT/benchmark/runs/submissions" -type f ! -name 'README*.md' -print 2>/dev/null
  } | wc -l | tr -d ' '
)"

if [ "$submission_files" -eq 0 ]; then
  if grep -Eq '^\|.*\|[[:space:]]*[0-9]+([.][0-9]+)?([[:space:]]*%|/12)?[[:space:]]*\|' "$ROOT/leaderboard/README.md"; then
    echo "ERROR: numeric leaderboard rows require auditable submission artifacts"
    exit 1
  fi
fi

grep -Fq 'Skill Lift' "$ROOT/leaderboard/METHODOLOGY.md" || { echo "ERROR: Skill Lift methodology missing"; exit 1; }
grep -Fq 'NATIVE' "$ROOT/benchmark/runs/schema.md" || { echo "ERROR: NATIVE condition missing"; exit 1; }
grep -Fq 'EOS_ENABLED' "$ROOT/benchmark/runs/schema.md" || { echo "ERROR: EOS_ENABLED condition missing"; exit 1; }

echo "v0.4 validation passed: ${#cases[@]} real-world cases + paired run protocol + leaderboard structure."
