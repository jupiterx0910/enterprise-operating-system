# AI Work Redesign Engine / AI 工作重构引擎

## Purpose / 目的

Redesign **work**, rather than starting with “which jobs will AI replace?”.

重构的是**工作**，而不是先判断“哪些岗位会被 AI 替代”。

---

## Workflow / 工作流

```text
Business Outcome / 业务结果
 ↓
Work / 工作
 ↓
Workflows / 工作流
 ↓
Tasks / 任务
 ↓
Decision | Execution | Relationship | Accountability
判断 | 执行 | 关系 | 责任
 ↓
Human | AI | Agent allocation / 人-AI-Agent 分工
 ↓
Workflow redesign / 工作流重构
 ↓
Role redesign / 岗位重构
 ↓
Authority + Controls redesign / 权限与控制重构
 ↓
Metrics redesign / 指标重构
 ↓
Validation / 验证
```

---

## Task allocation / 任务分配

### Human-first / 人优先

Use humans where final accountability, complex relationships, value judgment, organizational legitimacy, negotiation, physical presence, or high-stakes exception handling remains material.

当最终责任、复杂关系、价值判断、组织合法性、谈判、现场存在或高风险例外处理非常重要时，以人为主。

### AI-first / AI 优先

Use AI for bounded analysis, classification, prediction, generation, transformation, retrieval, summarization, comparison, and pattern recognition where output can be checked.

对于边界清晰、可校验的分析、分类、预测、生成、转换、检索、总结、比较与模式识别，优先考虑 AI。

### Agent-first / Agent 优先

Use Agents for multi-step workflows that can be driven by explicit goals, tools, permissions, state, feedback, and escalation boundaries.

对于可以由明确目标、工具、权限、状态、反馈和升级边界持续驱动的多步骤工作流，考虑 Agent。

### Hybrid / 混合

Use AI/Agents for information and routine execution while humans retain judgment, authorization, exceptions, relationships, and final accountability.

AI/Agent 负责信息处理与常规执行；人保留判断、授权、例外、关系与最终责任。

---

## Required questions / 必答问题

1. What business outcome does the work own? / 这项工作最终对哪个业务结果负责？
2. What workflows and tasks compose it? / 它由哪些工作流与任务组成？
3. Where are the highest time, cost, quality, or latency bottlenecks? / 最大的时间、成本、质量或延迟瓶颈在哪？
4. Which tasks require human judgment or legitimacy? / 哪些任务需要人类判断或组织合法性？
5. Which tasks are automatable or augmentable? / 哪些任务可自动化或增强？
6. Which tasks suit a persistent Agent rather than one-off AI assistance? / 哪些任务更适合持续 Agent，而不是一次性 AI 辅助？
7. What tools, data, permissions, memory, and controls are required? / 需要什么工具、数据、权限、记忆与控制？
8. Who owns final accountability? / 谁承担最终责任？
9. What exceptions require escalation to a human? / 哪些例外必须升级给人？
10. Which role responsibilities should be deleted, added, or recombined? / 旧岗位哪些职责应删除、增加或重组？
11. How should decision rights and management spans change? / 决策权与管理跨度如何变化？
12. Do existing KPIs still measure the right outcome? / 现有 KPI 是否仍然衡量正确结果？
13. How will productivity, quality, speed, risk, and cost be validated before headcount changes? / 在调整人头之前，如何验证生产率、质量、速度、风险和成本？

---

## Delegation test / Agent 委托测试

A workflow is a stronger candidate for Agent delegation when it has:

`Clear goal + repeatable state transitions + available tools + bounded permissions + observable feedback + exception policy + human owner`

当一项工作具备以下条件时，更适合委托给 Agent：

`明确目标 + 可重复状态流转 + 可用工具 + 有界权限 + 可观测反馈 + 例外策略 + 人类责任人`。

If permissions, feedback, or escalation are undefined, the problem is not merely “model capability”; it is operating-model design.

如果权限、反馈或升级机制都没定义，问题不只是“模型能力”，而是经营与治理设计不完整。

---

## Headcount guardrail / 人头调整护栏

“AI can do this task” does **not** imply “this job should disappear”. A role is a bundle of tasks, decisions, relationships, and accountabilities.

“AI 能做这项任务”**不等于**“这个岗位应该消失”。岗位是任务、判断、关系与责任的组合。

Before recommending headcount reduction, require:

1. work decomposition / 工作拆解；
2. redesigned workflow / 新工作流；
3. validated productivity and quality gains / 已验证的效率与质量提升；
4. residual human responsibilities / 剩余的人类职责；
5. capacity demand after redesign / 重构后的真实产能需求；
6. risk and control design / 风险与控制设计；
7. transition cost and time / 转换成本与时间。

Do not map a claimed “30% AI productivity gain” directly to “30% fewer people”.

不得把“AI 提效 30%”直接等同于“裁员 30%”。

---

## Required output / 必须输出

```yaml
business_outcome: ""
workflow: ""
tasks:
  - task: ""
    current_owner: ""
    allocation: human | ai | agent | human+ai | human+agent | human+ai+agent
    rationale: ""
    tools: []
    permissions: []
    human_accountability: ""
    exception_policy: ""
role_changes: []
authority_changes: []
metric_changes: []
validation_plan: []
risks: []
```
