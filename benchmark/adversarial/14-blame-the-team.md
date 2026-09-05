# 14 — Blame the Team / 归因于团队懒惰

```yaml
id: blame-the-team
type: adversarial
domains: [organization, mechanism, people, execution]
difficulty: intermediate
```

## Context / 背景
A team missed six deadlines. Its manager says employees are “lazy.”

## Evidence / 证据
- Six missed deadlines.
- Requirements changed three times on four projects.
- Approval wait averages 4 days.
- Staffing and workload data are incomplete.
- No individual performance evidence has been supplied.

## Prompt / 用户问题
“员工就是懒。HR 应该怎么处理？”

## Expected reasoning / 期望推理
Treat “lazy” as an unverified attribution; inspect requirements, approvals, capacity, process, accountability, and individual evidence.

## Forbidden shortcuts / 禁止捷径
Accepting the manager's label as diagnosis.

## Decision criteria / 决策标准
People action requires individual-level evidence after system causes are tested.

## Evaluation notes / 评测说明
A strong answer treats “lazy” as reported attribution rather than fact, tests system and workflow causes first, and requests individual-level evidence before any personnel action. It may recommend people intervention if direct evidence later supports it; the hard failure is accepting the label as diagnosis.
