# Business & Talent Review Engine / 经营与人才复盘引擎

## Purpose / 目的

Run a recurring management review that connects business results, organizational health, talent allocation, and mechanism changes in one decision loop.

把经营结果、组织状态、人才配置和机制变化放进同一个周期性的决策闭环。

## Review sequence / 复盘顺序

`RESULTS → GAP → CAUSES → DECISIONS → OWNERS → RESOURCES → DEADLINES → FOLLOW-UP`

For each material gap, ask in order:

1. What happened? / 发生了什么？
2. What evidence supports it? / 有什么证据？
3. What is the gap versus target or prior period? / 与目标或前期差多少？
4. Which causal domain is implicated? / 属于哪个因果域？
5. What alternative explanations remain? / 还有哪些替代解释？
6. What decision is required now? / 现在必须做什么决策？
7. Who owns it, with what authority and resources? / 谁负责、有什么权力和资源？
8. When and how will the decision be tested? / 何时、用什么指标验证？

## MBR / 经营月度复盘

Minimum agenda:

- Strategic priorities / 战略重点
- Revenue, margin, cash, customer, product or other critical outcomes / 核心经营结果
- Material gaps / 重大偏差
- Five-domain diagnosis / 五因诊断
- Decisions required / 待决策事项
- Cross-functional blockers / 跨部门阻塞
- Resource reallocation / 资源重配
- Next-period commitments / 下周期承诺

## Talent review / 人才复盘

Review people only in the context of roles and business needs:

`Business Need → Critical Role → Role Requirements → Evidence → Talent Fit → Action`

For each critical role, inspect:

- current value
- future potential
- role readiness
- strategic relevance
- replaceability
- development cost
- retention risk
- succession coverage

Do not turn the review into a ranking exercise without an explicit decision purpose.

## Decision log / 决策日志

```yaml
review_decision:
  issue: "..."
  evidence: ["..."]
  diagnosis: "..."
  choice: CONTINUE | ADJUST | RESTRUCTURE | REPLACE | STOP
  owner: "..."
  authority_required: "..."
  resources_required: "..."
  deadline: "..."
  metric: "..."
  reversal_condition: "..."
```

## Anti-patterns / 反模式

- Turning MBR into a slide-reading ritual.
- Discussing people before understanding the business gap.
- Reporting metrics without decisions.
- Making decisions without owners or resources.
- Repeating the same issue without changing the mechanism.
- Treating a talent grid as a substitute for succession or role design.
