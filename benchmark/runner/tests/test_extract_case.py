from pathlib import Path

import pytest

from benchmark.runner.extract_case import extract_case


CASE = '''# Demo

```yaml
id: demo-case
type: real-world
```

## Context / 背景
Context line.

## Evidence / 证据
- Evidence line.

## Prompt / 用户问题
What should we do?

## Expected reasoning / 期望推理
SECRET expected reasoning.

## Forbidden shortcuts / 禁止捷径
SECRET shortcut.

## Decision criteria / 决策标准
SECRET criteria.

## Evaluation notes / 评测说明
SECRET notes.

## Source provenance / 来源溯源
SECRET provenance.
'''


def write_case(tmp_path: Path, text: str = CASE) -> Path:
    path = tmp_path / "case.md"
    path.write_text(text, encoding="utf-8")
    return path


def test_extracts_only_context_evidence_prompt(tmp_path: Path):
    case = extract_case(write_case(tmp_path))
    assert case.case_id == "demo-case"
    assert case.context == "Context line."
    assert case.evidence == "- Evidence line."
    assert case.prompt == "What should we do?"


def test_hidden_sections_never_appear_in_generation_payload(tmp_path: Path):
    case = extract_case(write_case(tmp_path))
    visible = "\n".join([case.context, case.evidence, case.prompt])
    for secret in ["SECRET expected", "SECRET shortcut", "SECRET criteria", "SECRET notes", "SECRET provenance"]:
        assert secret not in visible


def test_missing_required_section_fails(tmp_path: Path):
    path = write_case(tmp_path, CASE.replace("## Evidence / 证据\n- Evidence line.\n\n", ""))
    with pytest.raises(ValueError, match="missing required section"):
        extract_case(path)


def test_duplicate_required_section_fails(tmp_path: Path):
    path = write_case(tmp_path, CASE.replace("## Prompt / 用户问题\n", "## Prompt / 用户问题\nFirst.\n\n## Prompt / 用户问题\n"))
    with pytest.raises(ValueError, match="duplicate required section"):
        extract_case(path)


def test_heading_text_inside_body_does_not_cross_section_boundary(tmp_path: Path):
    text = CASE.replace("Context line.", "Context line mentions ## Evidence / 证据 inline, but stays context.")
    case = extract_case(write_case(tmp_path, text))
    assert "## Evidence / 证据 inline" in case.context
    assert case.evidence == "- Evidence line."
