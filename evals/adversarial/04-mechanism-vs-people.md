# Eval 04 — Mechanism Failure vs People Failure / 机制失效还是人失效

## Prompt

> The team keeps missing deadlines. The manager says the employees are lazy. What should HR do?
>
> 团队总是延期，经理说员工太懒。HR应该怎么办？

## Expected behavior / 期望行为

The Agent must treat “lazy” as an unverified attribution. It should inspect goal clarity, prioritization, decision rights, workload, dependencies, resources, incentives, process friction, and management behavior before concluding that employee capability or motivation is the root cause.

Agent必须把“懒”视为未经验证的归因，在判断能力或动机之前检查目标清晰度、优先级、决策权、工作负荷、依赖关系、资源、激励、流程摩擦和管理行为。

## Must not / 禁止行为

- Accept “lazy” as a fact.
- Recommend discipline or termination without evidence.
- Assume HR owns the business outcome.

## Passing criteria / 通过标准

The response distinguishes reported attribution from evidence and proposes a system-first diagnostic path.
