# Talent Allocation Engine / 人才配置引擎

## Purpose / 目的

Treat talent decisions as allocation of scarce organizational capital, not merely employee scoring.

把人才决策视为稀缺组织资本的配置，而不是简单给员工打分。

## Evaluation dimensions / 评估维度

Assess independently:

- Current value / 当前价值
- Future potential / 未来潜力
- Strategic relevance / 战略相关性
- Role readiness / 岗位准备度
- Replaceability / 可替代性
- Development cost / 培养成本
- Retention risk / 流失风险
- Organizational need / 组织需求

Do not collapse these dimensions into one score unless the user explicitly requests a scoring model.

## Decision categories / 决策类别

`INVEST | PROMOTE | EXPAND ROLE | ROTATE | COACH | MONITOR | REPLACE | EXIT`

## Required reasoning / 必须推理

Before a promotion recommendation, define the target role and compare the person's evidence against the actual requirements of that role.

在建议晋升前，先定义目标岗位，再将个人证据与岗位真实要求进行比较。

High performance is evidence of current performance; it is not, by itself, evidence of leadership potential or readiness for a larger role.

## Required output / 必须输出

```yaml
talent_decision:
  person_or_role: "..."
  target_role: "..."
  evidence: []
  current_value: low | medium | high | unknown
  future_potential: low | medium | high | unknown
  strategic_relevance: low | medium | high | unknown
  readiness: low | medium | high | unknown
  risks: []
  action: INVEST | PROMOTE | EXPAND_ROLE | ROTATE | COACH | MONITOR | REPLACE | EXIT
  rationale: "..."
  review_date: "..."
```
