from pathlib import Path

from benchmark.runner.build_skill_bundle import build_skill_bundle


def make_skill(root: Path, order: list[str]) -> Path:
    skill = root / "skills" / "enterprise-operating-system"
    files = {
        "SKILL.md": "entry\n",
        "engines/z.md": "z engine\n",
        "engines/a.md": "a engine\n",
        "references/ref.md": "reference\n",
        "templates/t.md": "template\n",
        "notes.txt": "ignore\n",
    }
    for rel in order:
        path = skill / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(files[rel], encoding="utf-8")
    return skill


def test_bundle_reads_only_canonical_runtime_markdown(tmp_path: Path):
    skill = make_skill(tmp_path, ["SKILL.md", "engines/a.md", "references/ref.md", "templates/t.md", "notes.txt"])
    bundle = build_skill_bundle(skill)
    assert bundle.files == ("SKILL.md", "engines/a.md", "references/ref.md", "templates/t.md")
    assert "notes.txt" not in bundle.text


def test_bundle_paths_are_sorted_and_embedded_as_headers(tmp_path: Path):
    skill = make_skill(tmp_path, ["engines/z.md", "SKILL.md", "templates/t.md", "engines/a.md"])
    bundle = build_skill_bundle(skill)
    assert bundle.files == tuple(sorted(bundle.files))
    positions = [bundle.text.index(f"===== FILE: {p} =====") for p in bundle.files]
    assert positions == sorted(positions)


def test_bundle_hash_is_stable_across_creation_order(tmp_path: Path):
    one = make_skill(tmp_path / "one", ["SKILL.md", "engines/z.md", "engines/a.md", "references/ref.md", "templates/t.md"])
    two = make_skill(tmp_path / "two", ["templates/t.md", "references/ref.md", "engines/a.md", "engines/z.md", "SKILL.md"])
    assert build_skill_bundle(one).sha256 == build_skill_bundle(two).sha256


def test_bundle_hash_changes_when_runtime_content_changes(tmp_path: Path):
    skill = make_skill(tmp_path, ["SKILL.md", "engines/a.md"])
    before = build_skill_bundle(skill).sha256
    (skill / "engines/a.md").write_text("changed\n", encoding="utf-8")
    after = build_skill_bundle(skill).sha256
    assert before != after


def test_bundle_excludes_repo_level_benchmark_docs(tmp_path: Path):
    skill = make_skill(tmp_path, ["SKILL.md", "engines/a.md"])
    benchmark = tmp_path / "benchmark" / "rubric.md"
    benchmark.parent.mkdir(parents=True)
    benchmark.write_text("SECRET RUBRIC", encoding="utf-8")
    bundle = build_skill_bundle(skill)
    assert "SECRET RUBRIC" not in bundle.text


def test_bundle_reports_token_count_when_counter_supplied(tmp_path: Path):
    skill = make_skill(tmp_path, ["SKILL.md"])
    bundle = build_skill_bundle(skill, token_counter=lambda text: len(text.split()))
    assert bundle.token_count == len(bundle.text.split())
