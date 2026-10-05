# Hugging Face Job Spec — v0.5 Pilot

- Model: `Qwen/Qwen3-8B`
- Pinned model revision: supplied as `MODEL_REVISION`
- Hardware: `a10g-small` (1x A10G 24 GB)
- Conditions: NATIVE and EOS_ENABLED
- Cases: exactly five public real-world cases
- Trials: 1
- Total generations: exactly 10
- Qwen3 chat template: `enable_thinking=False`
- Generation: greedy, `max_new_tokens=1800`, seed 42
- Automatic retry: disabled
- Artifact transport: SHA-256 checked tar.gz encoded in job logs

The launcher must pass immutable `RUNNER_COMMIT`, `CASE_SNAPSHOT`, `SKILL_COMMIT`, and `MODEL_REVISION` values. A failed paid job is not automatically retried.
