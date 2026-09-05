#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SKILL_DIR="$ROOT/skills/enterprise-operating-system"
SKILL="$SKILL_DIR/SKILL.md"

required=(
  "$SKILL"
  "$SKILL_DIR/engines/router.md"
  "$SKILL_DIR/engines/evidence.md"
  "$SKILL_DIR/engines/diagnosis.md"
  "$SKILL_DIR/engines/decision.md"
  "$SKILL_DIR/engines/organization-design.md"
  "$SKILL_DIR/engines/talent-allocation.md"
  "$SKILL_DIR/engines/mechanism-design.md"
  "$SKILL_DIR/engines/performance.md"
  "$SKILL_DIR/engines/review.md"
  "$SKILL_DIR/engines/ai-work-redesign.md"
  "$SKILL_DIR/references/business-people-integration.md"
  "$SKILL_DIR/references/organization.md"
  "$SKILL_DIR/references/talent-review.md"
  "$SKILL_DIR/references/mechanism.md"
  "$SKILL_DIR/references/performance.md"
  "$SKILL_DIR/references/mbr.md"
  "$SKILL_DIR/references/ai-organization.md"
  "$SKILL_DIR/templates/company-intake.md"
  "$SKILL_DIR/templates/diagnosis.md"
  "$SKILL_DIR/templates/90-day-plan.md"
  "$ROOT/evals/rubric.md"
  "$ROOT/examples/README.md"
)

for file in "${required[@]}"; do
  test -f "$file" || { echo "ERROR: missing required file: ${file#$ROOT/}"; exit 1; }
done

# One canonical runtime location only. Repo-level docs/evals/benchmark may remain at root.
test ! -f "$ROOT/SKILL.md" || { echo "ERROR: duplicate root SKILL.md; canonical Skill is skills/enterprise-operating-system/SKILL.md"; exit 1; }
test ! -d "$ROOT/engines" || { echo "ERROR: duplicate root engines/ directory"; exit 1; }
test ! -d "$ROOT/templates" || { echo "ERROR: duplicate root templates/ directory"; exit 1; }

# Agent Skills frontmatter contract.
first_line="$(head -n 1 "$SKILL")"
test "$first_line" = "---" || { echo "ERROR: SKILL.md must start with YAML frontmatter"; exit 1; }
grep -Eq '^name: enterprise-operating-system$' "$SKILL" || { echo "ERROR: canonical Skill name missing"; exit 1; }
grep -Eq '^description: .+' "$SKILL" || { echo "ERROR: canonical Skill description missing"; exit 1; }
grep -Eq '^description: .*Use when' "$SKILL" || { echo "ERROR: description should contain activation guidance ('Use when')"; exit 1; }

# Every runtime Markdown path referenced in backticks by SKILL.md must exist.
python3 - "$SKILL_DIR" "$SKILL" <<'PY'
from pathlib import Path
import re
import sys

skill_dir = Path(sys.argv[1])
skill_path = Path(sys.argv[2])
text = skill_path.read_text(encoding="utf-8")
refs = sorted(set(re.findall(r"`((?:engines|references|templates)/[^`\n]+?\.md)`", text)))
missing = [ref for ref in refs if not (skill_dir / ref).is_file()]
if missing:
    for ref in missing:
        print(f"ERROR: SKILL.md references missing runtime file: {ref}")
    raise SystemExit(1)
print(f"Runtime references OK: {len(refs)} linked Markdown files checked.")
PY

# Core invariants should remain explicit in the executable entry point.
grep -Fq '管事 × 管人' "$SKILL" || { echo "ERROR: business × people operating spine missing"; exit 1; }
grep -Fq 'engines/router.md' "$SKILL" || { echo "ERROR: router entry missing"; exit 1; }
grep -Fq 'EVIDENCE' "$SKILL" || { echo "ERROR: execution protocol missing EVIDENCE stage"; exit 1; }
grep -Fq 'REVIEW' "$SKILL" || { echo "ERROR: execution protocol missing REVIEW stage"; exit 1; }
grep -Fq 'reversal_condition' "$SKILL" || { echo "ERROR: decision reversal condition missing"; exit 1; }

echo "Skill validation passed: canonical runtime structure is coherent."
