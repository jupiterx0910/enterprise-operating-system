# Diagnosis Engine / 诊断引擎

## Purpose / 目的

Turn a business-result gap into testable causal hypotheses before recommending organization, mechanism, talent, or execution interventions.

把经营结果偏差转化为可验证的因果假设，再决定是否需要调整组织、机制、人才或执行方式。

## Five-domain causal tree / 五因诊断树

```text
Business Result Gap / 经营结果偏差
├── Strategy / 战略
├── Organization / 组织
├── Mechanism / 机制
├── People / 人才
└── Execution / 执行
```

The five domains are a search space, not five boxes that must receive equal attention. Prioritize by materiality and evidence.

五个维度是因果搜索空间，不要求平均用力；应按影响程度与证据强弱排序。

---

## Protocol / 协议

### Step 1 — Define the gap / 定义偏差

Specify:

`Metric + Target + Actual + Gap + Period + Scope + Baseline + Materiality`

明确：`指标 + 目标 + 实际 + 偏差 + 周期 + 范围 + 基准 + 重要性`。

If target quality itself is questionable, test that under `Strategy` before treating the gap as execution failure.

如果目标本身可能不合理，应先在“战略”维度检验目标质量，不能直接把偏差归因于执行。

### Step 2 — Classify evidence / 证据分层

Use `evidence.md` to separate:

`observed | reported | inferred | assumed | unknown`

Do not merge reported claims with observed facts.

不得把他人陈述与可核验事实混为一谈。

### Step 3 — Generate falsifiable hypotheses / 生成可证伪假设

For each relevant domain, state what would have to be true for the hypothesis to explain the observed result.

针对每个相关维度，说明“如果这个解释是真的，应该还能观察到什么”。

Examples:

- Strategy: target or positioning is wrong.
- Organization: interfaces or decision rights create delay.
- Mechanism: incentives or resource allocation drive the wrong behavior.
- People: capability, capacity, motivation, leadership, or role fit is insufficient.
- Execution: priorities, cadence, follow-through, or operating discipline breaks down.

### Step 4 — Rank hypotheses / 假设排序

Rank by:

`Impact × Evidence Strength × Plausibility × Testability × Reversibility of test`

按：`影响 × 证据强度 × 合理性 × 可测试性 × 测试可逆性` 排序。

Prefer cheap, reversible tests before expensive or irreversible interventions.

优先验证低成本、可逆的假设，再考虑高成本或不可逆干预。

### Step 5 — Test alternatives / 测试竞争性解释

For each leading hypothesis, ask:

1. What else could produce the same symptom? / 还有什么能产生同样症状？
2. What evidence would weaken this hypothesis? / 什么证据会削弱它？
3. What evidence would strengthen a competing hypothesis? / 什么证据会增强竞争性解释？

### Step 6 — Identify root cause(s) / 识别根因

A root cause is not the most intuitive story. It is the factor that best explains the result under current evidence and is causally relevant to an intervention.

根因不是“听起来最顺的故事”，而是在当前证据下最能解释结果、且对干预有因果意义的因素。

Use multiple root causes when the system is genuinely coupled; do not force one-factor explanations.

如果系统确实是耦合问题，可以保留多个根因，不要强行单因归因。

---

## Business × People guardrail / 管事 × 管人护栏

A business symptom may eventually require a people intervention, but the chain must be explicit:

```text
Business symptom
→ causal evidence
→ system explanation tested
→ role / capability requirement clarified
→ person-specific evidence
→ people decision
```

经营症状最终可以落到“人”，但必须经过：

`业务症状 → 因果证据 → 系统解释验证 → 岗位/能力要求明确 → 人因证据 → 人才决策`。

---

## Required output / 必须输出

```yaml
problem: ""
metric: ""
target: ""
actual: ""
gap: ""
findings:
  - dimension: Strategy | Organization | Mechanism | People | Execution
    claim: ""
    evidence: []
    evidence_type: observed | reported | inferred | assumed | unknown
    confidence: low | medium | high
    alternatives: []
root_causes:
  - cause: ""
    confidence: low | medium | high
    evidence: []
intervention_options: []
unknowns: []
next_tests: []
```

## Anti-pattern / 反模式

Do not conclude “execution is weak, so strengthen performance management” unless evidence has materially tested target design, priorities, decision rights, resources, process, incentives, role clarity, and management cadence.

不要轻易得出“执行力不够，所以加强绩效考核”。除非证据已经实质性检验了目标设计、优先级、决策权、资源、流程、激励、岗位清晰度与经营节奏等重要替代解释。
