# Enterprise Agent Benchmark

> **A model-agnostic benchmark for enterprise reasoning.**  
> **面向企业经营推理能力的、模型无关的 Agent Benchmark。**

## What it measures / 测什么

This benchmark tests whether an Agent can move from **evidence → diagnosis → decision → action → measurement → review** without jumping from symptoms to people interventions.

它测试 Agent 是否能按照 **证据 → 诊断 → 决策 → 行动 → 衡量 → 复盘** 工作，而不是从业务症状直接跳到“换人、裁员、加 KPI”。

It evaluates behavior, not eloquence.

它评估的是**行为质量，而不是文字是否漂亮**。

## Benchmark layers / Benchmark 分层

| Layer | Purpose |
|---|---|
| `cases/` | Representative enterprise scenarios / 代表性经营场景 |
| `adversarial/` | Prompts designed to trigger reasoning shortcuts / 诱发错误推理的对抗题 |
| `real-world/` | Source-grounded public enterprise cases / 有来源溯源的公共真实企业案例 |
| `runs/` | Reproducible NATIVE vs EOS_ENABLED run records / 可复现配对运行记录 |
| `../leaderboard/` | Skill Lift and hard-fail reduction results / Skill 增益与硬失败下降榜 |
| `rubric.md` | Common scoring standard / 统一评分标准 |
| `schema.md` | Case contract / 案例结构规范 |

## Run a case manually / 手工运行

1. Give the case's **Prompt** to the target Agent.
2. Do not reveal the **Expected reasoning** section.
3. Capture the complete Agent response.
4. Score it using `rubric.md`.
5. Record the score and evidence externally; do not edit the case to make an unexecuted score look official.

## Core benchmark question / 核心问题

> Can the Agent diagnose the system that produced the result before recommending an intervention?
>
> Agent 能否先诊断“产生结果的系统”，再提出干预，而不是先找一个人负责？

## Important limitation / 重要限制

Repository validation checks structure and completeness. It does **not** claim semantic model performance. Semantic scores must come from an actual run against a named model/runtime and a recorded evaluation process.


## v0.4 paired experiment / v0.4 配对实验

To measure the value of EOS itself, compare the same model under two conditions:

```text
NATIVE       = model without EOS
EOS_ENABLED  = same model + canonical EOS Skill
```

Hold model/version, reasoning effort, tools, runtime policy, and case snapshot constant wherever possible.

Primary metrics:

- `Native Mean`
- `EOS Mean`
- `Skill Lift = EOS Mean - Native Mean`
- `Hard-Fail Reduction = Native HF% - EOS HF%`
- coverage and trials per case

A **Candidate** entry requires one complete paired trial per case. A **Verified** entry requires at least 3 paired trials per case, complete raw outputs and scorecards, and independent human review.

Current public leaderboard status: **No verified submissions yet.**


## v0.5 executable pilot runner / v0.5 可执行实验 Runner

The repository now includes an offline-tested paired experiment harness under `benchmark/runner/`.

It provides:

- strict extraction of Context, Evidence and Prompt only;
- deterministic canonical EOS Skill bundling with SHA-256 provenance;
- NATIVE/EOS configuration-drift checks;
- pinned-model Transformers generation;
- immediate raw-output persistence;
- artifact completeness validation;
- scorecard aggregation that recomputes Skill Lift from underlying scores;
- CI anti-fabrication guards.

The first v0.5 protocol targets `Qwen/Qwen3-8B`, five public real-world cases, one trial per condition, and exactly 10 generations.

**No Candidate score is published until a real complete run exists.**
