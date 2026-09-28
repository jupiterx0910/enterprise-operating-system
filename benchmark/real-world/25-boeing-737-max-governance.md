# 25 — Boeing 737 MAX Governance / 波音 737 MAX 治理

```yaml
id: boeing-737-max-governance
type: real-world
source_class: public-official
known_outcome_case: true
evidence_cutoff: 2020-09-30
domains: [organization, mechanism, execution, people]
difficulty: expert
sources:
  - title: T&I Committee Advances Bipartisan Aviation Safety Legislation
    publisher: U.S. House Committee on Transportation and Infrastructure
    published: 2020-09-30
    url: https://transportation.house.gov/news/documentsingle.aspx?DocumentID=405076
  - title: The Boeing 737 MAX — Examining Design, Development, and Marketing
    publisher: U.S. House Committee on Transportation and Infrastructure
    published: 2019-10-30
    url: https://transportation.house.gov/calendar/eventsingle.aspx?EventID=404499
```

## Context / 背景
Following two 737 MAX crashes, congressional investigations examined design, certification, oversight, safety culture, human factors, and the relationship between Boeing and the FAA.

在两起 737 MAX 空难之后，美国国会调查涉及设计、认证、监管、安全文化、人因以及波音与 FAA 之间的关系。

## Evidence / 证据
- Congressional materials identified concerns across multiple layers rather than a single cause.
- The committee discussed MCAS design weaknesses, pilot information/training, certification, organizational delegation, and oversight.
- Congressional leaders later described a broken safety culture at Boeing and insufficient FAA oversight while advancing certification reforms.
- The evidence packet includes both company-side and regulator-side system layers; it does not justify reducing the diagnosis to one individual.

## Prompt / 用户问题
“重大事故发生后，董事会最容易做的是换人和加流程。用 EOS 判断：哪些是 People 问题，哪些是 Organization / Mechanism / Execution 问题？治理应该如何重构？”

## Expected reasoning / 期望推理
Use a multi-layer causal model: design assumptions, safety information flow, decision rights, delegated certification, escalation, incentive/pressure signals, training/human factors, oversight, and executive governance. Distinguish accountability from monocausal blame.

## Forbidden shortcuts / 禁止捷径
- Attributing the event to a single employee or single technical defect.
- Treating more process as automatically safer.
- Ignoring regulator-company interfaces and decision-right design.

## Decision criteria / 决策标准
A strong answer defines safety-critical decision rights, independent challenge/escalation, evidence thresholds, authority separation, audit/verification mechanisms, executive oversight, and conditions that stop or reverse a decision.

## Evaluation notes / 评测说明
Reward systems thinking and explicit governance design. Penalize unsupported technical claims, hindsight-only blame, or generic “improve culture” recommendations.

## Source provenance / 来源溯源
The evidence packet paraphrases public U.S. House committee materials. It is a governance reasoning case, not an accident-causation adjudication.
