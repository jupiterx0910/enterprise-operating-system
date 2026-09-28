# 22 — Target Canada Operating Model / Target 加拿大经营模型

```yaml
id: target-canada-operating-model
type: real-world
source_class: public-company
known_outcome_case: true
evidence_cutoff: 2015-01-15
domains: [strategy, organization, mechanism, execution]
difficulty: advanced
sources:
  - title: Target Corporation Announces Plans to Discontinue Canadian Operations
    publisher: Target Corporation
    published: 2015-01-15
    url: https://corporate.target.com/press/release/2015/01/target-corporation-announces-plans-to-discontinue-canadian-operations
  - title: Brian Cornell Addresses Questions About Exiting Canada
    publisher: Target Corporation
    published: 2015-01-15
    url: https://corporate.target.com/news-features/article/2015/01/qa-brian-cornell-target-exits-canada
```

## Context / 背景
Target expanded into Canada, ultimately deciding in January 2015 to discontinue its Canadian operations.

Target 进入加拿大市场后，最终在 2015 年 1 月决定退出加拿大业务。

## Evidence / 证据
- Target said it could not find a realistic path to Canadian profitability until at least 2021.
- The company said it had taken on too much too fast.
- Target acknowledged inventory problems and pricing-perception problems.
- The Canadian business operated 133 stores at the time of the exit announcement.
- The exit decision carried large financial costs and affected approximately 17,600 employees.

## Prompt / 用户问题
“如果一家成熟公司进入新国家后快速扩张但持续亏损，应该继续修运营、缩小规模，还是退出？请用 EOS 做诊断，不要直接用结果倒推原因。”

## Expected reasoning / 期望推理
Distinguish market thesis, expansion pacing, supply/inventory capability, pricing, customer experience, fixed-cost commitments, organizational readiness, and turnaround economics. Evaluate continuation, restructuring, partial retreat, and exit as explicit alternatives.

## Forbidden shortcuts / 禁止捷径
- “退出了，所以战略从一开始就是错的。”
- “库存有问题，所以只修供应链即可。”
- Ignoring sunk-cost bias, future cash requirements, or time-to-profitability.

## Decision criteria / 决策标准
A strong answer defines the evidence threshold for continue/restructure/stop, identifies reversible tests where possible, and specifies financial, customer, operational, and organizational metrics.

## Evaluation notes / 评测说明
Reward multi-layer diagnosis and explicit option economics. Penalize hindsight-only reasoning and single-function explanations.

## Source provenance / 来源溯源
The evidence packet paraphrases Target's January 15, 2015 public statements. The benchmark does not assume those statements provide a complete independent postmortem.
