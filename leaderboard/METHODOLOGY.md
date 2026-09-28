# Leaderboard Methodology / 榜单方法

## Candidate

- Completes all required cases.
- One trial per case per condition.
- Includes complete manifests, raw outputs, and scorecards.

## Verified

- Paired NATIVE and EOS_ENABLED runs.
- Same model/version, case snapshot, tools, reasoning effort, and runtime policy.
- At least 3 trials per case per condition.
- Raw outputs retained.
- Every output scored with the published 12-point rubric.
- Hard-fail flags reviewed.
- At least one independent human reviewer; disputed cases require adjudication.

## Metrics

- `Native Mean`
- `EOS Mean`
- `Skill Lift = EOS Mean - Native Mean`
- `Native Hard-Fail %`
- `EOS Hard-Fail %`
- `Hard-Fail Reduction = Native HF% - EOS HF%`
- `Coverage`
- `Trials per case`

## Tie-break

1. Higher Skill Lift.
2. Higher Hard-Fail Reduction.
3. Higher EOS Mean.
4. More repeated trials.
5. More recent benchmark version.

## Integrity

LLM-assisted scoring is permitted for triage, but a Verified submission cannot rely on an LLM judge as its sole final evaluator.
