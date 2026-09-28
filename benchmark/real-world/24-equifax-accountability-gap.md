# 24 — Equifax Accountability Gap / Equifax 问责断层

```yaml
id: equifax-accountability-gap
type: real-world
source_class: public-official
known_outcome_case: true
evidence_cutoff: 2018-12-10
domains: [organization, mechanism, execution, people]
difficulty: advanced
sources:
  - title: Committee Releases Report Revealing New Information on Equifax Data Breach
    publisher: U.S. House Committee on Oversight and Government Reform
    published: 2018-12-10
    url: https://oversight.house.gov/report/committee-releases-report-revealing-new-information-on-equifax-data-breach/
```

## Context / 背景
A U.S. House committee investigated the 2017 Equifax data breach and published findings about cybersecurity risk, accountability, and IT management structure.

美国众议院委员会调查了 2017 年 Equifax 数据泄露事件，并发布了关于网络安全风险、问责和 IT 管理结构的调查结论。

## Evidence / 证据
- The committee characterized the breach as preventable.
- It found that Equifax failed to fully appreciate and mitigate observable cybersecurity risks.
- The report summary identified unclear lines of authority in internal IT management.
- The committee linked that structure to an execution gap between IT policy development and operations.

## Prompt / 用户问题
“公司有安全制度但执行失败，是员工没执行力，还是组织和机制设计失败？如何重构责任、权力和验证闭环？”

## Expected reasoning / 期望推理
Inspect decision rights, policy-to-operation handoffs, patch/accountability ownership, escalation, verification, resource constraints, and management visibility. Apply the EOS rule that responsibility without authority/resources is invalid design.

## Forbidden shortcuts / 禁止捷径
- “有制度，所以一定是执行人员的问题。”
- “安全团队负责，因此业务管理层无需承担责任。”
- Recommending more policies without checking operational ownership and verification.

## Decision criteria / 决策标准
A strong answer redesigns ownership, authority, verification, escalation, and executive review. It distinguishes control design from control execution and identifies measurable closure criteria.

## Evaluation notes / 评测说明
Reward explicit policy-to-execution causal mapping. Penalize generic cybersecurity advice that does not address organization design and accountability.

## Source provenance / 来源溯源
The evidence packet paraphrases the U.S. House committee's December 2018 public summary. Technical details not contained in that evidence packet should be marked as unknown unless independently sourced.
