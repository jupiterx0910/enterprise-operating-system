# Evidence Engine

## Purpose

控制 Agent 的证据质量、置信度和不确定性。

## Evidence Levels

1. **Observed** — 直接数据或可核验事实。
2. **Reported** — 用户、管理者或访谈对象明确报告。
3. **Inferred** — Agent 根据证据推断。
4. **Assumed** — 为推进分析而暂定，尚未验证。

## Rules

- Observed ≠ Inferred。
- Reported 不等于客观事实，应标明来源。
- Assumption 必须显式列出。
- 高影响决策不能只依赖单一低质量证据。
- 如果证据互相冲突，应保留冲突，而不是强行统一。

## Evidence Record

```yaml
claim: ""
evidence:
  - source: ""
    observation: ""
    quality: low | medium | high
evidence_type: observed | reported | inferred | assumed
confidence: low | medium | high
unknowns: []
alternative_explanations: []
```

## Decision Threshold

- **High confidence**：多项独立证据一致，且主要替代解释已被排除或显著削弱。
- **Medium confidence**：证据支持方向，但存在重要未知变量。
- **Low confidence**：主要依赖报告、假设或单一信号。

低置信度结论可以生成探索行动，但不应伪装成确定性决策。
