#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

bash "$ROOT/scripts/validate-v04.sh" >/dev/null

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
cp -R "$ROOT/." "$tmp/repo"

cat >> "$tmp/repo/leaderboard/README.md" <<'TABLE'

| Model | EOS Mean |
|---|---:|
| fake-model | 10.5 |
TABLE

if bash "$tmp/repo/scripts/validate-v04.sh" >/tmp/eos-v04-negative.log 2>&1; then
  echo "ERROR: validator accepted numeric leaderboard score without submissions"
  cat /tmp/eos-v04-negative.log
  exit 1
fi

grep -Fq 'numeric leaderboard rows require auditable submission artifacts' /tmp/eos-v04-negative.log || {
  echo "ERROR: validator failed for an unexpected reason"
  cat /tmp/eos-v04-negative.log
  exit 1
}

echo "v0.4 validator tests passed: valid structure accepted; fake numeric leaderboard rejected."
