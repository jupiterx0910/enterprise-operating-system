# Evaluation / 评测体系

## Purpose / 目的

Enterprise Operating System is evaluated on whether an Agent follows the operating protocol under realistic and adversarial conditions.

本项目评估的不是 Agent 是否会写漂亮的管理建议，而是它在真实和对抗场景下是否遵守企业经营推理协议。

## Benchmark / Benchmark

The repository benchmark contains flagship and adversarial cases:

- `../benchmark/cases/` — representative operating problems / 代表性经营问题
- `../benchmark/adversarial/` — reasoning traps / 推理陷阱
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
