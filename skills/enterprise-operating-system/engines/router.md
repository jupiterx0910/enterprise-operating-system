# Enterprise Reasoning Router / 企业经营推理路由器

## Purpose / 目的

Route each request to the smallest set of reasoning engines required to produce a defensible enterprise decision.

把每个问题路由到最小必要的一组推理引擎，避免 Agent 一上来就套框架、给建议或跳到人员处置。

The router is **intent-aware, evidence-aware, and intervention-aware**.

Router 同时判断：**用户想解决什么、证据是否足够、用户是否已经预设了干预手段**。

---

## Default rule / 默认规则

When the user provides a **business symptom, missed outcome, conflict, underperformance, or a proposed people intervention without sufficient causal evidence**, route to `DIAGNOSE` first.

当用户给出的是**经营症状、目标偏差、冲突、低绩效，或在因果证据不足时直接提出换人/裁员/晋升/加 KPI 等干预**，默认先进入 `DIAGNOSE`。

Do not route directly from a symptom to an intervention.

不得从症状直接路由到干预。

---

## Route classes / 路由类型

| Route | Use when / 何时使用 | Primary engine / 主引擎 |
|---|---|---|
| `DIAGNOSE` | Outcome gap, ambiguous cause, conflict, failure, user is blaming people / 结果偏差、原因不清、冲突、失败、用户先怪人 | `diagnosis.md` + `evidence.md` |
| `ORG_DESIGN` | Structure, spans, interfaces, decision rights, role boundaries / 组织结构、管理跨度、接口、决策权、岗位边界 | `organization-design.md` |
| `TALENT_ALLOCATE` | Promotion, succession, role fit, critical talent, replacement / 晋升、继任、岗位匹配、关键人才、替换 | `talent-allocation.md` |
| `MECHANISM_DESIGN` | Process, incentives, authority, resources, governance, information flow / 流程、激励、权限、资源、治理、信息流 | `mechanism-design.md` |
| `PERFORMANCE` | Goal setting, performance evaluation, MBR/QBR, KPI design / 目标、绩效评价、MBR/QBR、KPI | `performance.md` |
| `REVIEW` | Business review, retrospective, learning, operating cadence / 经营复盘、项目复盘、学习闭环、经营节奏 | `review.md` |
| `AI_REDESIGN` | AI/Agent transformation, workflow automation, role redesign / AI/Agent 转型、工作流自动化、岗位重构 | `ai-work-redesign.md` |
| `DECIDE` | Evidence and diagnosis are already sufficient and the task is to make a decision / 证据和诊断已充分，当前任务是形成决策 | `decision.md` |

---

## Routing protocol / 路由协议

### Step 1 — Frame the request / 定义问题

Extract or infer only when explicitly supported:

- business outcome or decision at stake / 涉及的业务结果或决策
- scope / 范围
- time horizon / 时间范围
- target vs actual / 目标与实际
- known evidence / 已知证据
- constraints / 约束
- proposed intervention, if any / 用户预设的干预手段

If a material item is missing, mark it `unknown`; do not invent it.

关键项缺失时标记为 `unknown`，不得补造。

### Step 2 — Detect intervention bias / 检测干预偏见

Flag when the request embeds a conclusion such as:

- fire/replace the leader / 换掉负责人
- cut headcount / 裁员
- promote the top performer / 晋升最高绩效者
- add more KPIs / 增加 KPI
- reorganize the org chart / 先改组织架构
- buy or deploy AI / 先上 AI

A preselected intervention is a **hypothesis**, not a diagnosis.

预设干预只能当作**待验证假设**，不能当作诊断结论。

### Step 3 — Assess evidence sufficiency / 判断证据充分度

Use:

- `HIGH` — multiple independent signals support the causal claim and major alternatives are weakened / 多项独立证据一致，主要替代解释已被削弱
- `MEDIUM` — direction is supported but important unknowns remain / 方向有证据，但仍有重要未知
- `LOW` — mostly assertions, assumptions, or one weak signal / 主要依赖陈述、假设或单一弱信号

`LOW` evidence + high-impact intervention => `DIAGNOSE`.

低证据 + 高影响干预 => 必须先 `DIAGNOSE`。

### Step 4 — Select primary and secondary routes / 选择主路由与次路由

Return an internal route record:

```yaml
route:
  primary: DIAGNOSE | ORG_DESIGN | TALENT_ALLOCATE | MECHANISM_DESIGN | PERFORMANCE | REVIEW | AI_REDESIGN | DECIDE
  secondary: []
  reason: ""
  evidence_sufficiency: low | medium | high
  intervention_bias: none | low | high
  unknowns: []
```

Do not expose this YAML unless it helps the user; use it to control reasoning.

### Step 5 — Chain engines only when necessary / 仅在必要时串联引擎

Common chains:

```text
Business underperformance
DIAGNOSE → DECIDE → ORG_DESIGN / MECHANISM_DESIGN / TALENT_ALLOCATE → EXECUTION PLAN
```

```text
AI transformation
DIAGNOSE current workflow → AI_REDESIGN → ORG_DESIGN / MECHANISM_DESIGN → DECIDE → MEASURE
```

```text
Promotion / succession
EVIDENCE → TALENT_ALLOCATE → DECIDE → 90-DAY DEVELOPMENT / TRANSITION PLAN
```

Avoid reading every engine by default. Progressive disclosure is a feature, not a limitation.

默认不要读取所有引擎；渐进式读取是系统设计的一部分。

---

## Universal execution protocol / 统一执行协议

Regardless of route, preserve this sequence for material decisions:

```text
EVIDENCE
  ↓
DIAGNOSIS
  ↓
ROOT CAUSE / DESIGN LOGIC
  ↓
DECISION
  ↓
ACTION
  ↓
MEASUREMENT
  ↓
REVIEW
  ↓
LEARNING
  ↺
```

Every material action must resolve:

`Action + Owner + Authority + Resources + Deadline + Metric + Review + Reversal condition`

每项重要行动必须明确：

`行动 + 负责人 + 权限 + 资源 + 截止时间 + 指标 + 复盘 + 反转条件`

---

## Stop conditions / 停止条件

Do not progress to irreversible or high-cost recommendations when:

- the causal claim is low confidence;
- material alternatives have not been tested;
- decision authority is unclear;
- required resources are absent;
- the success metric is undefined;
- the intervention has no review or reversal condition.

在以下情况下，不应继续推进不可逆或高成本建议：因果结论低置信、重要替代解释未验证、决策权不清、资源缺失、成功指标未定义、没有复盘或反转条件。
