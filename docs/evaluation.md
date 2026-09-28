# Evaluation / 评测体系

## Purpose / 目的

Enterprise Operating System is evaluated on whether an Agent follows the operating protocol under realistic and adversarial conditions.

本项目评估的不是 Agent 是否会写漂亮的管理建议，而是它在真实和对抗场景下是否遵守企业经营推理协议。

## Benchmark / Benchmark

The repository benchmark contains flagship and adversarial cases:

- `../benchmark/cases/` — representative operating problems / 代表性经营问题
- `../benchmark/adversarial/` — reasoning traps / 推理陷阱
- `../benchmark/real-world/` — public source-grounded enterprise cases / 公共真实企业案例
- `../benchmark/runs/` — reproducible paired run records / 可复现配对运行记录
- `../leaderboard/` — Skill Lift leaderboard / Skill 增益榜
- `../benchmark/rubric.md` — 12-point rubric / 12 分评分标准
- `../benchmark/schema.md` — case contract / 案例规范

## Evaluation dimensions / 评测维度

1. Evidence discipline / 证据纪律
2. Causal diagnosis / 因果诊断
3. System thinking / 系统思维
4. Decision quality / 决策质量
5. Execution design / 执行设计
6. AI-native redesign / AI 原生工作重构

## What the benchmark does not claim / 不声称什么

The repository does not publish model scores unless the model was actually run against the case set using a documented evaluation process.

仓库不会发布未经实际运行的模型分数。任何正式成绩都必须记录模型、版本/日期、Runtime、Prompt 版本、评测人和原始输出。

Structural CI validates case completeness; it does not replace semantic evaluation.

## Regression principle / 回归原则

When the Skill changes, previously passing cases should be rerun. A new version must not improve one scenario by silently degrading evidence discipline or system diagnosis elsewhere.


## v0.4 effectiveness evaluation / v0.4 增量价值评测

EOS effectiveness is evaluated with paired runs:

- `NATIVE`: target model without EOS.
- `EOS_ENABLED`: same model/runtime/case snapshot with the canonical EOS Skill loaded.

The principal project metric is **Skill Lift**, not raw model score:

`Skill Lift = EOS_ENABLED mean − NATIVE mean`

We also track **Hard-Fail Reduction**, because a useful enterprise operating Skill should reduce unsupported personnel actions, blanket AI layoffs, responsibility-without-authority designs, fabrication, and other benchmark hard failures.

### Candidate vs Verified

**Candidate**
- all required cases completed;
- one trial per case per condition;
- manifests, raw outputs, and scorecards preserved.

**Verified**
- same model/version, tools, reasoning effort, runtime policy and case snapshot;
- at least 3 trials per case per condition;
- complete raw outputs and scorecards;
- hard-fail review;
- at least one independent human review.

LLM-assisted grading can help triage, but it cannot be the sole final evaluator for a Verified result.

## Provenance and contamination / 来源与污染

Public real-world cases record source provenance and evidence cutoffs. Because historical public cases may appear in model training data, they are process tests rather than contamination-resistant forecasting tests. Hidden/holdout cases are a future evaluation layer.
