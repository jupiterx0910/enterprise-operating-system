# Leaderboard Submissions / 榜单提交

Each submission must point to paired benchmark runs and preserve the model/runtime configuration used to produce them.

Recommended path:

```text
leaderboard/submissions/<provider>-<model>-<date>.md
```

Required fields:

- model/provider/version
- reasoning effort
- benchmark and case snapshot
- NATIVE run IDs
- EOS_ENABLED run IDs
- number of trials
- evaluator method
- aggregate metrics
- hard-fail counts
- links to raw run artifacts
- known limitations

Do not submit hand-entered aggregate scores without the underlying run artifacts.
