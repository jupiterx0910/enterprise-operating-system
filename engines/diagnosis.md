# Diagnosis Engine

## Purpose

将“结果不好”转化为可验证的根因假设，而不是直接给出人事建议。

## Root-Cause Tree

```text
Business Result Gap
├── Strategy
├── Organization
├── Mechanism
├── People
└── Execution
```

## Protocol

### Step 1 — Define the gap

`Target - Actual = Gap`

明确指标、周期、范围和基准。

### Step 2 — Gather evidence

优先使用：经营数据、流程数据、组织数据、访谈、客户反馈、项目记录。

### Step 3 — Generate hypotheses

每个维度至少形成一个可证伪假设，除非有证据证明该维度明显无关。

### Step 4 — Rank hypotheses

按以下因素排序：

`Impact × Evidence × Plausibility × Testability`

### Step 5 — Test alternatives

主动寻找能解释同一现象的竞争性假设。

### Step 6 — Select root cause(s)

根因不是“最容易讲的故事”，而是当前证据下最能解释关键结果、并能通过干预改变结果的因素。

## Required Output

```yaml
problem: ""
metric:
target:
actual:
gap:
findings:
  - dimension: Strategy | Organization | Mechanism | People | Execution
    claim: ""
    evidence: []
    confidence: low | medium | high
    alternatives: []
root_causes: []
interventions: []
unknowns: []
```

## Anti-Pattern

不要出现：

> “员工执行力不够，所以应该加强绩效考核。”

除非已有证据排除了目标设计、资源、流程、决策权、激励和管理机制等重要替代解释。
