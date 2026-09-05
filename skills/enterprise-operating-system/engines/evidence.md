# Evidence Engine / 证据引擎

## Purpose / 目的

Control evidence quality, confidence, uncertainty, and the boundary between fact and interpretation.

控制 Agent 对证据质量、置信度、不确定性以及“事实 vs. 解释”的边界。

---

## Evidence classes / 证据类型

1. **Observed / 观察事实** — direct data, records, or independently verifiable facts / 直接数据、记录或可独立核验事实。
2. **Reported / 他人陈述** — a stakeholder explicitly states something / 用户、管理者、员工、客户等明确陈述。
3. **Inferred / 推断** — an interpretation derived from evidence / Agent 根据证据形成的推断。
4. **Assumed / 假设** — temporarily accepted to continue analysis but not verified / 为推进分析暂时采用、尚未验证。
5. **Unknown / 未知** — material information that is not available / 对结论重要但当前缺失的信息。

Reported claims are evidence **that someone said something**; they are not automatically evidence that the underlying claim is objectively true.

“他人陈述”只能直接证明“对方这样说过”，不能自动证明其内容客观为真。

---

## Evidence rules / 证据规则

- Observed ≠ inferred. / 观察事实不等于推断。
- Assumptions must be explicit. / 假设必须显式标记。
- Unknowns must stay visible when material. / 重要未知项必须保留。
- High-impact decisions should not rely on one low-quality signal. / 高影响决策不能只依赖单一低质量信号。
- Preserve conflicting evidence rather than forcing false consistency. / 证据冲突时保留冲突，不要强行统一。
- Source proximity, independence, recency, and relevance affect evidence quality. / 来源接近度、独立性、时效性、相关性都会影响证据质量。
- Absence of evidence is not evidence of absence unless the observation process should reliably detect the event. / 没发现证据不等于证明不存在，除非观测机制本应可靠捕捉该事实。

---

## Evidence record / 证据记录

```yaml
finding:
  claim: ""
  evidence:
    - source: ""
      observation: ""
      evidence_type: observed | reported | inferred | assumed | unknown
      quality: low | medium | high
      independence: low | medium | high
  confidence: low | medium | high
  unknowns: []
  alternative_explanations: []
  disconfirming_evidence: []
```

---

## Confidence thresholds / 置信度阈值

### High / 高

Multiple reasonably independent pieces of evidence converge, the causal chain is plausible, and major alternative explanations are materially weakened.

多项相对独立证据趋同，因果链合理，主要替代解释已被明显削弱。

### Medium / 中

Evidence supports a direction, but one or more material unknowns or alternatives remain.

证据支持某个方向，但仍存在一个或多个重要未知项或替代解释。

### Low / 低

The conclusion depends mainly on assertions, assumptions, one weak signal, or an untested causal leap.

结论主要依赖陈述、假设、单一弱信号或未经验证的因果跳跃。

Low-confidence conclusions may justify **exploration or reversible tests**, but should not be presented as certain diagnoses or irreversible decisions.

低置信结论可以支持探索与可逆测试，但不能伪装成确定诊断，更不应直接支持不可逆决策。

---

## Evidence escalation / 证据升级

When evidence is insufficient, request or propose the **minimum high-value evidence** that would most change the decision.

证据不足时，不要无限补信息；优先寻找**最可能改变决策的最小高价值证据**。

Examples:

- funnel conversion by segment rather than total revenue only;
- decision cycle time rather than subjective complaints about bureaucracy;
- role outcomes and observable behavior rather than reputation;
- before/after workflow data rather than generic AI productivity claims.

---

## Decision guardrail / 决策护栏

For high-cost, irreversible, reputational, or people-impacting decisions, explicitly state:

`Evidence strength + material unknowns + alternatives tested + confidence + what would change the conclusion`

对于高成本、不可逆、声誉影响大或直接影响人员的决策，必须明确：

`证据强度 + 重要未知项 + 已验证替代解释 + 置信度 + 什么会改变当前结论`。
