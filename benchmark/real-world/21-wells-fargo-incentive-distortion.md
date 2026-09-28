# 21 — Wells Fargo Incentive Distortion / 富国银行激励扭曲

```yaml
id: wells-fargo-incentive-distortion
type: real-world
source_class: public-official
known_outcome_case: true
evidence_cutoff: 2016-09-08
domains: [mechanism, people, organization, execution]
difficulty: advanced
sources:
  - title: CFPB enforcement action against Wells Fargo Bank
    publisher: Consumer Financial Protection Bureau
    published: 2016-09-08
    url: https://www.consumerfinance.gov/enforcement/actions/wells-fargo-bank-2016/
  - title: CFPB consent order
    publisher: Consumer Financial Protection Bureau
    published: 2016-09-08
    url: https://files.consumerfinance.gov/f/documents/092016_cfpb_WFBconsentorder.pdf
```

## Context / 背景
A large retail bank used sales targets and compensation incentives across consumer banking. Regulators later found widespread unauthorized account-opening practices.

一家大型零售银行在消费者银行业务中广泛采用销售目标和薪酬激励。监管机构随后发现了大范围未经客户授权开户的行为。

## Evidence / 证据
- The CFPB said employees opened unauthorized deposit and credit-card accounts and enrolled customers in products without consent.
- The CFPB explicitly linked the misconduct to sales targets and compensation incentives.
- The bank's own analysis identified more than two million deposit and credit-card accounts that may not have been authorized.
- The evidence packet does not establish that every employee, manager, or business unit behaved the same way.

## Prompt / 用户问题
“这是员工道德问题，还是激励机制和管理系统的问题？如果你是经营负责人，应该先改人、改 KPI，还是改整个经营机制？”

## Expected reasoning / 期望推理
Separate individual misconduct from the system that shaped behavior. Inspect target design, incentive gradients, monitoring, escalation channels, management pressure, customer-protection controls, and accountability before choosing personnel or mechanism interventions.

## Forbidden shortcuts / 禁止捷径
- “员工违规，所以换掉违规员工即可。”
- “有激励就一定会导致造假。”
- Treating the regulatory finding as proof that every leader had the same knowledge or intent.

## Decision criteria / 决策标准
A strong answer redesigns incentives and controls while preserving individual accountability where evidence supports it. It defines owners, decision rights, monitoring, customer-protection metrics, and reversal/escalation conditions.

## Evaluation notes / 评测说明
Reward answers that diagnose a mechanism-to-behavior causal chain and distinguish system correction from person-specific accountability. Penalize monocausal moralizing or unsupported claims about intent.

## Source provenance / 来源溯源
Facts above are paraphrased from the CFPB's 2016 Wells Fargo enforcement materials. The benchmark adds the diagnostic question; it does not add unverified motives.
