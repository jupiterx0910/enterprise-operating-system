# Raw Run Submissions / 原始运行提交

This directory stores auditable benchmark run artifacts.

Each real run uses:

```text
benchmark/runs/submissions/<run-id>/
├── manifest.yaml
├── outputs/
│   └── <case-id>.md
├── scores/
│   └── <case-id>.yaml
└── summary.md
```

Rules:

- Keep raw model outputs unchanged.
- Every scorecard must point to one raw output.
- Do not overwrite historical runs.
- Example manifests are never results.
- Aggregate leaderboard numbers are invalid unless the underlying run artifacts exist here.
