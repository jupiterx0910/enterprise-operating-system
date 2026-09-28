# Benchmark Runs / Benchmark 运行记录

A benchmark score is publishable only when the underlying run can be audited.

只有底层运行记录可审计时，Benchmark 分数才可以公开。

## Paired experiment / 配对实验

For EOS effectiveness, run the same model twice:

1. `NATIVE` — no Enterprise Operating System Skill.
2. `EOS_ENABLED` — canonical `skills/enterprise-operating-system/` loaded.

Keep model version, reasoning effort, tools, case snapshot, and runtime settings identical wherever the provider permits.

## Required folder layout

```text
benchmark/runs/submissions/<run-id>/
├── manifest.yaml
├── outputs/
│   └── <case-id>.md
├── scores/
│   └── <case-id>.yaml
└── summary.md
```

Do not overwrite a historical run. Configuration changes create a new run ID.
