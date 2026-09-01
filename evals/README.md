# Evaluation Suite / Agent 行为评测

This directory evaluates whether the Skill changes Agent behavior in the intended direction.

这里评测的不是“文档写得好不好”，而是 Skill 是否让 Agent 按预期方式工作。

## Evaluation dimensions / 评测维度

1. **Evidence discipline / 证据纪律** — Does the Agent distinguish facts, reports, inference, assumptions, and unknowns?
2. **Causal diagnosis / 因果诊断** — Does it separate symptoms from root causes?
3. **System-first reasoning / 系统优先** — Does it test strategy, organization, mechanism, and execution before blaming people?
4. **Decision quality / 决策质量** — Are decisions supported by evidence and explicit uncertainty?
5. **Execution quality / 执行质量** — Are owner, authority, resources, deadline, metric, and review defined?
6. **AI work redesign / AI工作重构** — Does the Agent redesign work before reducing headcount?

## Adversarial suite / 对抗测试

- `adversarial/01-missed-sales-target.md`
- `adversarial/02-ai-headcount.md`
- `adversarial/03-high-performer-promotion.md`

## Scoring principle / 评分原则

A test should specify expected behavior and prohibited behavior. Passing requires behavior, not keywords.

测试必须同时定义期望行为与禁止行为。通过标准看 Agent 的行为，而不是是否说出了某几个关键词。
