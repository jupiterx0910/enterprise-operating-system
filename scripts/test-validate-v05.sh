#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

bash "$ROOT/scripts/validate-v05.sh" >/dev/null

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
cp -R "$ROOT/." "$tmp/repo"

cat >> "$tmp/repo/leaderboard/README.md" <<'TABLE'

| Model | Status | Native Mean | EOS Mean | Skill Lift |
|---|---|---:|---:|---:|
| fake-model | Candidate/Pilot | 6.0 | 10.0 | 4.0 |
TABLE

if bash "$tmp/repo/scripts/validate-v05.sh" >/tmp/eos-v05-negative.log 2>&1; then
  echo "ERROR: v0.5 validator accepted numeric Candidate row without scored experiment artifacts"
  cat /tmp/eos-v05-negative.log
  exit 1
fi

grep -Fq 'numeric Candidate leaderboard rows require a scored experiment' /tmp/eos-v05-negative.log || {
  echo "ERROR: v0.5 validator failed for an unexpected reason"
  cat /tmp/eos-v05-negative.log
  exit 1
}

echo "v0.5 validator tests passed: clean repository accepted; fake Candidate score rejected."
