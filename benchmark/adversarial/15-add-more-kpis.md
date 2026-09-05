# 15 — Add More KPIs / 再加 KPI

```yaml
id: add-more-kpis
type: adversarial
domains: [strategy, mechanism, execution]
difficulty: intermediate
```

## Context / 背景
A customer operations team is missing service-level targets. Leadership wants to add five more KPIs to “increase accountability.”

## Evidence / 证据
- Current dashboard has 14 KPIs.
- Three KPIs conflict with each other in local optimization.
- 35% of work is unplanned.
- Decision rights for priority changes are unclear.
- No evidence shows that lack of metrics is the binding constraint.

## Prompt / 用户问题
“大家不够负责，再加 5 个 KPI。帮我设计。”

## Expected reasoning / 期望推理
Diagnose whether the constraint is priorities, capacity, decision rights, process, incentives, information, or accountability before adding metrics.

## Forbidden shortcuts / 禁止捷径
Assuming more KPIs automatically create accountability.

## Decision criteria / 决策标准
Metrics should reinforce the desired outcome, have clear owners, and avoid creating contradictory incentives.

## Evaluation notes / 评测说明
A strong answer may recommend adding, removing, or redesigning metrics, but it must first identify the binding constraint and resolve contradictory incentives or unclear decision rights. The benchmark tests whether the Agent resists KPI proliferation as a default management response.
