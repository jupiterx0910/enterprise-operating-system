from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

_REQUIRED = {
    "## Context / 背景": "context",
    "## Evidence / 证据": "evidence",
    "## Prompt / 用户问题": "prompt",
}


@dataclass(frozen=True)
class CaseInput:
    case_id: str
    context: str
    evidence: str
    prompt: str
    source_path: str


def _sections(text: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current: str | None = None
    for line in text.splitlines():
        if line.startswith("## "):
            current = line.strip()
            sections.setdefault(current, []).append("")
            continue
        if current is not None:
            sections[current][-1] += line + "\n"
    return sections


def extract_case(path: Path) -> CaseInput:
    text = path.read_text(encoding="utf-8")
    id_match = re.search(r"(?m)^id:\s*([^\s#]+)\s*$", text)
    if not id_match:
        raise ValueError(f"missing case id: {path}")

    sections = _sections(text)
    values: dict[str, str] = {}
    for heading, field in _REQUIRED.items():
        blocks = sections.get(heading, [])
        if not blocks:
            raise ValueError(f"missing required section: {heading}")
        if len(blocks) > 1:
            raise ValueError(f"duplicate required section: {heading}")
        values[field] = blocks[0].strip()

    return CaseInput(
        case_id=id_match.group(1),
        context=values["context"],
        evidence=values["evidence"],
        prompt=values["prompt"],
        source_path=path.as_posix(),
    )
