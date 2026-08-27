# Diagnosis Engine / 诊断引擎

## Purpose / 目的

Turn a business-result gap into testable root-cause hypotheses rather than jumping directly to people recommendations.

把经营结果偏差转化为可验证的根因假设，而不是直接跳到“换人/考核”。

## Root-Cause Tree / 根因树

```text
Business Result Gap / 经营结果偏差
├── Strategy / 战略
├── Organization / 组织
├── Mechanism / 机制
├── People / 人才
└── Execution / 执行
```

## Protocol / 协议

### Step 1 — Define the gap / 定义偏差

`Target - Actual = Gap`

Specify metric, period, scope, baseline, and materiality.

明确指标、周期、范围、基准与偏差的重要程度。

### Step 2 — Gather evidence / 收集证据

Prefer operating data, process data, organization data, interviews, customer feedback, and project records.

优先使用经营数据、流程数据、组织数据、访谈、客户反馈与项目记录。

### Step 3 — Generate hypotheses / 生成假设

For each relevant dimension, create a falsifiable hypothesis.

对每个相关维度形成可证伪假设。

### Step 4 — Rank hypotheses / 排序

`Impact × Evidence × Plausibility × Testability`

按影响、证据、合理性、可测试性排序。

### Step 5 — Test alternatives / 测试替代解释

Actively seek competing explanations for the same symptom.

主动寻找能够解释同一症状的竞争性假设。

### Step 6 — Select root cause(s) / 选择根因

A root cause is not the easiest story. It is the factor that best explains the result under current evidence and can plausibly be changed by intervention.

根因不是“最容易讲的故事”，而是在当前证据下最能解释结果、且可以通过干预改变结果的因素。

## Required Output / 必须输出

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

## Anti-Pattern / 反模式

Do not say: “Employees lack execution capability, so strengthen performance management” unless evidence has materially ruled out target design, resources, process, decision rights, incentives, and management mechanisms.

不要轻易说：“员工执行力不够，所以加强绩效考核。”除非证据已经基本排除了目标设计、资源、流程、决策权、激励和管理机制等重要替代解释。
