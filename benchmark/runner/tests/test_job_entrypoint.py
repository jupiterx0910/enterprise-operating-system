from pathlib import Path

import pytest

from benchmark.runner.job_entrypoint import decode_artifact_archive, encode_artifact_archive, validate_pilot_scope


def test_entrypoint_refuses_case_count_other_than_five():
    with pytest.raises(ValueError, match="exactly five"):
        validate_pilot_scope(["a", "b"], ("NATIVE", "EOS_ENABLED"), 1)


def test_entrypoint_refuses_more_than_ten_generations():
    with pytest.raises(ValueError, match="10 generations"):
        validate_pilot_scope(["a", "b", "c", "d", "e"], ("NATIVE", "EOS_ENABLED"), 2)


def test_artifact_archive_roundtrip_is_checksummed(tmp_path: Path):
    root = tmp_path / "exp"
    root.mkdir()
    (root / "raw.md").write_text("hello", encoding="utf-8")
    payload, digest = encode_artifact_archive(root)
    restored = tmp_path / "restored"
    decode_artifact_archive(payload, digest, restored)
    assert (restored / "raw.md").read_text(encoding="utf-8") == "hello"


def test_artifact_archive_rejects_bad_checksum(tmp_path: Path):
    root = tmp_path / "exp"
    root.mkdir(); (root / "x").write_text("x")
    payload, _ = encode_artifact_archive(root)
    with pytest.raises(ValueError, match="checksum"):
        decode_artifact_archive(payload, "0" * 64, tmp_path / "bad")
