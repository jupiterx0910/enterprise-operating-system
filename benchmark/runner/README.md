# v0.5 Pilot Runner

The runner executes the paired Candidate experiment defined in `docs/superpowers/specs/2026-10-05-v0.5-pilot-runner-design.md`.

Design rules:

- generation sees only Context, Evidence, and Prompt;
- NATIVE and EOS_ENABLED share the same case payload and baseline system prompt;
- EOS_ENABLED adds the exact deterministic canonical Skill bundle;
- manifests are written before inference and raw outputs immediately after each generation;
- generation and scoring are separate;
- core tests use a fake generator and never launch paid inference.

Run unit tests:

```bash
python -m pytest benchmark/runner/tests -q
```
