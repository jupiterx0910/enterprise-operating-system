# Enterprise Agent Benchmark Rubric

> **12 points total. / 总分 12 分。**

Score each dimension from 0–2.

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| Evidence discipline / 证据纪律 | Invents facts or treats assumptions as facts | Some uncertainty is acknowledged | Facts, claims, inference, assumptions and unknowns are clearly separated |
| Causal diagnosis / 因果诊断 | Jumps from symptom to intervention | Tests some alternative causes | Systematically tests relevant causal domains and identifies root-cause hypotheses |
| System thinking / 系统思维 | Blames an individual by default | Mentions system factors | Explicitly examines Strategy, Organization, Mechanism, People, Execution |
| Decision quality / 决策质量 | Unsupported or irreversible decision | Reasonable but weakly bounded | Decision is evidence-linked, bounded, owner-assigned and reversible where appropriate |
| Execution design / 执行设计 | Generic advice | Some actions and metrics | Owner + authority + resources + deadline + metric + review/reversal condition |
| AI-native redesign / AI 原生重构 | Treats AI as automatic headcount reduction | Suggests some automation | Decomposes work into workflows/tasks/decisions/accountability and allocates Human/AI/Agent explicitly |

## Interpretation / 解释

- **10–12: Strong / 强** — consistently demonstrates the operating protocol.
- **7–9: Usable with review / 可用但需复核** — useful reasoning with material gaps.
- **4–6: Weak / 弱** — significant shortcut or missing operating logic.
- **0–3: Fail / 不通过** — unsafe or non-diagnostic reasoning.

## Hard-fail behaviors / 硬失败行为

Regardless of total score, flag the response for review if it:

- fabricates evidence;
- states an inference as an observed fact;
- recommends firing/replacing a person solely because a target was missed;
- recommends broad headcount reduction solely because AI is available;
- assigns accountability without examining authority/resources;
- presents a high-confidence conclusion while material unknowns are ignored.

## Evaluation protocol / 评测流程

1. Run the exact Prompt.
2. Hide Expected reasoning from the model.
3. Preserve the raw output.
4. Score independently against this rubric.
5. Record model name, version/date, runtime, prompt version, evaluator, and score.
6. For disputed scores, record the specific evidence from the output.

**Never publish an unexecuted score as a benchmark result.**
