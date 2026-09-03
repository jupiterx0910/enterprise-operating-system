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
