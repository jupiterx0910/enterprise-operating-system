# Decision Engine

## Decision Classes

- **CONTINUE** — 当前设计有效，继续执行。
- **ADJUST** — 局部修正，不改变基本结构。
- **RESTRUCTURE** — 重新设计组织、岗位、机制或流程。
- **REPLACE** — 更换责任人或关键资源配置。必须有充分的人因证据。
- **STOP** — 停止方向、项目或投入。

## Decision Record

```yaml
decision: CONTINUE | ADJUST | RESTRUCTURE | REPLACE | STOP
subject: ""
rationale: ""
evidence: []
owner: ""
authority: ""
resources: []
deadline: ""
expected_effect: ""
success_metric: ""
review_date: ""
reversal_condition: ""
confidence: low | medium | high
```

## Decision Quality Test

一个决定只有在以下问题都有答案时才算完整：

- 谁决定？
- 谁负责？
- 谁拥有执行权？
- 有什么资源？
- 什么时候完成？
- 用什么指标判断？
- 什么情况下改变决定？

## Replace Guardrail

如果建议 REPLACE，应明确：

1. 人的问题是什么？
2. 有什么直接证据？
3. 哪些系统性替代解释已排除？
4. 如果不替换，什么可逆干预可以先测试？
