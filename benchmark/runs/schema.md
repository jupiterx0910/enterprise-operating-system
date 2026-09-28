# Run Schema / 运行 Schema

## Manifest

```yaml
run_id: "YYYYMMDD-provider-model-condition-rN"
benchmark_version: "v0.4"
skill_commit: "none-or-git-sha"
case_snapshot: "git-sha"
condition: NATIVE | EOS_ENABLED
model:
  provider: ""
  model_id: ""
  model_version: ""
  reasoning_effort: ""
runtime:
  harness: ""
  tools: []
  temperature: null
  seed: null
  system_prompt_hash: ""
  skill_loaded: false
trial: 1
started_at: "ISO-8601"
completed_at: "ISO-8601"
evaluator:
  method: human | double-human | llm-assisted
  names_or_ids: []
```

## Per-case scorecard

```yaml
case_id: ""
run_id: ""
scores:
  evidence_discipline: 0
  causal_diagnosis: 0
  system_thinking: 0
  decision_quality: 0
  execution_design: 0
  ai_native_redesign: 0
total: 0
hard_fail: false
hard_fail_reasons: []
reviewer_notes: ""
```

Each dimension is 0–2. `total` must equal the sum and be 0–12.
