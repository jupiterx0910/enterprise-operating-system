# Decision Engine / 决策引擎

## Purpose / 目的

Convert a diagnosis or design into an explicit, accountable, measurable, and reversible decision record.

把诊断或设计转成明确、可负责、可衡量、可复盘并具备反转条件的决策。

---

## Decision classes / 决策类型

- **CONTINUE / 继续** — current design remains valid; continue execution / 当前设计仍有效，继续执行。
- **ADJUST / 调整** — targeted change without changing the core structure / 局部修正，不改变基本结构。
- **RESTRUCTURE / 重构** — redesign organization, workflow, roles, mechanisms, or resource allocation / 重构组织、工作流、岗位、机制或资源配置。
- **REPLACE / 更换** — replace a critical role-holder or resource when direct evidence supports it / 在直接证据支持时更换关键责任人或资源。
- **STOP / 停止** — stop a direction, activity, project, product, or investment / 停止方向、活动、项目、产品或投入。

---

## Decision record / 决策记录

```yaml
decision:
  choice: CONTINUE | ADJUST | RESTRUCTURE | REPLACE | STOP
  subject: ""
  rationale: ""
  evidence: []
  confidence: low | medium | high
  owner: ""
  decision_authority: ""
  execution_authority: ""
  resources_required: []
  deadline: ""
  expected_effect: ""
  success_metric: ""
  leading_indicators: []
  review_date: ""
  reversal_condition: ""
  risks: []
  unknowns: []
```

---

## Decision quality test / 决策质量测试

A decision is incomplete until these questions are answered:

1. **What exactly changes? / 到底改变什么？**
2. **Why this decision rather than the alternatives? / 为什么选它而不是其他方案？**
3. **What evidence supports it? / 什么证据支持？**
4. **Who owns the result? / 谁对结果负责？**
5. **Who has authority to decide and execute? / 谁拥有决策权和执行权？**
6. **What resources are required? / 需要什么资源？**
7. **By when? / 什么时候完成？**
8. **How will progress and outcome be measured? / 如何衡量过程与结果？**
9. **When will the decision be reviewed? / 什么时候复盘？**
10. **What evidence would cause us to reverse or revise it? / 什么证据会让我们改变决定？**

Responsibility without authority is invalid design. Accountability without resources is invalid design.

有责任无权力、或有问责无资源，都属于无效设计。

---

## Intervention ladder / 干预阶梯

Prefer the least irreversible intervention that can validly test the causal hypothesis:

```text
OBSERVE / COLLECT EVIDENCE
→ TEST
→ ADJUST
→ RESTRUCTURE
→ REPLACE / STOP
```

优先采用能够验证因果假设的最低不可逆程度干预：

`补证据 → 小范围测试 → 调整 → 重构 → 更换/停止`。

Do not use this ladder mechanically when delay itself is high-risk; state the trade-off when immediate action is required.

如果拖延本身风险极高，不必机械遵循阶梯，但必须明确说明即时行动的权衡依据。

---

## Replace guardrail / 更换人员护栏

Before `REPLACE`, explicitly answer:

1. What person-specific requirement is not being met? / 哪项明确的人因要求未满足？
2. What direct evidence supports that conclusion? / 有什么直接证据？
3. Which strategy, organization, mechanism, and execution alternatives were tested? / 哪些战略、组织、机制、执行替代解释已验证？
4. Is the role itself correctly designed? / 岗位本身是否设计正确？
5. Are authority and resources sufficient? / 权限和资源是否充分？
6. Is there a cheaper reversible intervention worth testing first? / 是否存在值得先验证的低成本可逆干预？
7. What is the transition and continuity risk? / 更换后的交接与连续性风险是什么？

Missed targets alone are not sufficient evidence for replacement.

目标未达成本身不足以证明应该换人。

---

## Decision-to-execution bridge / 从决策到执行

Every accepted decision must produce at least one owned action:

`Action + Owner + Authority + Resource + Deadline + Metric + Review + Reversal condition`

If any of these fields is materially unknown, mark it as a design gap rather than pretending the decision is execution-ready.

如果关键字段未知，应明确标记为“执行设计缺口”，不能假装决策已经可落地。
