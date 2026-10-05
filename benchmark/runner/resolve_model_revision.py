from __future__ import annotations

import re

from huggingface_hub import model_info


def resolve_model_revision(repo_id: str) -> str:
    sha = getattr(model_info(repo_id), "sha", None)
    if not isinstance(sha, str) or not re.fullmatch(r"[0-9a-fA-F]{40}", sha):
        raise ValueError(f"model revision must be a 40-character commit SHA, got {sha!r}")
    return sha.lower()
