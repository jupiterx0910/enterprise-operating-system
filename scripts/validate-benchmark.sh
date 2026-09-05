#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

required=(
  "$ROOT/skills/enterprise-operating-system/SKILL.md"
  "$ROOT/benchmark/README.md"
  "$ROOT/benchmark/schema.md"
  "$ROOT/benchmark/rubric.md"
)

for file in "${required[@]}"; do
  test -f "$file" || { echo "ERROR: missing $file"; exit 1; }
done

count=0
for dir in "$ROOT/benchmark/cases" "$ROOT/benchmark/adversarial"; do
  while IFS= read -r -d '' file; do
    case "$(basename "$file")" in
      README*.md) continue ;;
    esac
    count=$((count + 1))
    for heading in "## Context / 背景" "## Evidence / 证据" "## Prompt / 用户问题" "## Expected reasoning / 期望推理" "## Forbidden shortcuts / 禁止捷径" "## Decision criteria / 决策标准"; do
      grep -Fq "$heading" "$file" || { echo "ERROR: $file missing heading: $heading"; exit 1; }
    done
    grep -Fq 'id:' "$file" || { echo "ERROR: $file missing id"; exit 1; }
    grep -Fq 'type:' "$file" || { echo "ERROR: $file missing type"; exit 1; }
  done < <(find "$dir" -type f -name '*.md' -print0 | sort -z)
done

test "$count" -ge 15 || { echo "ERROR: expected at least 15 benchmark cases, found $count"; exit 1; }

grep -Eq '^---$' "$ROOT/skills/enterprise-operating-system/SKILL.md" || { echo "ERROR: SKILL.md frontmatter missing"; exit 1; }
grep -Eq '^name: enterprise-operating-system$' "$ROOT/skills/enterprise-operating-system/SKILL.md" || { echo "ERROR: Skill name missing"; exit 1; }
grep -Eq '^description:' "$ROOT/skills/enterprise-operating-system/SKILL.md" || { echo "ERROR: Skill description missing"; exit 1; }

echo "Benchmark validation passed: $count cases checked."
