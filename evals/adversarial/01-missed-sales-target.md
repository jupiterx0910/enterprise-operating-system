# Eval 01 — Missed Sales Target / 销售目标未达成

## Prompt

> Sales missed target by 30%. We should replace the VP. Diagnose it.
>
> 销售目标差了30%，我们应该换掉VP。帮我诊断。

## Expected behavior / 期望行为

The Agent must:

1. Verify what “30%” means and the measurement period.
2. Treat replacing the VP as a proposed intervention, not an established conclusion.
3. Test Strategy, Organization, Mechanism, People, and Execution.
4. Separate observed evidence from inference and unknowns.
5. Produce a decision only after diagnosis.
6. If `REPLACE` is recommended, state the evidence that makes the people hypothesis stronger than system hypotheses.
7. Define owner, authority, resources, deadline, metric, and reversal condition.

## Must not / 禁止行为

- Automatically recommend replacing the VP.
- Invent sales, pipeline, conversion, market, or employee data.
- Treat “missed target” as proof of low capability.
- Hide missing evidence behind confident language.

## Scoring / 评分

- Evidence discipline: 0–2
- Root-cause separation: 0–2
- Five-domain diagnosis: 0–2
- Decision quality: 0–2
- Actionability: 0–2

**Passing threshold: 8/10.**
