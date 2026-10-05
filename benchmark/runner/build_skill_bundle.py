from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Callable


@dataclass(frozen=True)
class SkillBundle:
    text: str
    sha256: str
    files: tuple[str, ...]
    token_count: int | None


def _runtime_markdown(skill_dir: Path) -> list[Path]:
    paths: list[Path] = []
    entry = skill_dir / "SKILL.md"
    if entry.is_file():
        paths.append(entry)
    for subdir in ("engines", "references", "templates"):
        root = skill_dir / subdir
        if root.is_dir():
            paths.extend(p for p in root.rglob("*.md") if p.is_file())
    return sorted(paths, key=lambda p: p.relative_to(skill_dir).as_posix())


def build_skill_bundle(
    skill_dir: Path,
    token_counter: Callable[[str], int] | None = None,
) -> SkillBundle:
    skill_dir = skill_dir.resolve()
    paths = _runtime_markdown(skill_dir)
    if not paths:
        raise ValueError(f"no canonical runtime Markdown found: {skill_dir}")

    rels = tuple(p.relative_to(skill_dir).as_posix() for p in paths)
    parts: list[str] = []
    for rel, path in zip(rels, paths):
        body = path.read_text(encoding="utf-8")
        parts.append(f"===== FILE: {rel} =====\n{body}")
    text = "\n\n".join(parts)
    digest = sha256(text.encode("utf-8")).hexdigest()
    count = token_counter(text) if token_counter is not None else None
    return SkillBundle(text=text, sha256=digest, files=rels, token_count=count)
