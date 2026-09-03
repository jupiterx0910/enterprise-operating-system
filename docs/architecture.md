# Architecture / 架构

Enterprise Operating System is organized as a reasoning-and-execution layer rather than a static management handbook.

本项目不是静态管理知识库，而是一层可被 Agent 调用的经营推理与执行系统。

```text
User / Business Context
        ↓
Evidence Protocol
        ↓
Five-Domain Diagnosis
Strategy · Organization · Mechanism · People · Execution
        ↓
Decision Protocol
        ↓
Engines
Organization · Talent · Mechanism · Performance · Review · AI Work
        ↓
Templates / Actions / Metrics
        ↓
Review → Learning
```

## Progressive disclosure / 渐进式读取

`SKILL.md` is the router and operating contract. Engines contain reasoning procedures. References contain deeper domain knowledge. Templates turn reasoning into reusable artifacts. Evals test observable behavior.

## Design invariant / 设计不变量

The system should be useful even when the user provides incomplete information. It must expose uncertainty instead of filling gaps with invented facts.
