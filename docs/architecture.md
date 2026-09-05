# Architecture / 架构

Enterprise Operating System is a **router-driven reasoning and execution layer** for enterprise problems, not a static management handbook.

Enterprise Operating System 是一层由 **Router 驱动的企业经营推理与执行系统**，而不是静态管理知识库。

---

## Runtime architecture / 运行时架构

```text
User / Business Context
        ↓
Enterprise Router
(intent + evidence + intervention bias)
        ↓
Evidence Gate
(observed / reported / inferred / assumed / unknown)
        ↓
Primary Route
DIAGNOSE | ORG_DESIGN | TALENT_ALLOCATE | MECHANISM_DESIGN
PERFORMANCE | REVIEW | AI_REDESIGN | DECIDE
        ↓
Reasoning Engine(s)
        ↓
Decision Contract
(owner + authority + resources + deadline + metric + review + reversal)
        ↓
Action / Template
        ↓
Measurement
        ↓
Review → Learning → next cycle
```

The default path for ambiguous business symptoms is:

```text
EVIDENCE
→ DIAGNOSIS
→ ROOT CAUSE
→ DECISION
→ ACTION
→ MEASUREMENT
→ REVIEW
→ LEARNING
```

A symptom does not route directly to a people intervention.

经营症状不能直接路由到人员干预。

---

## Operating spine / 经营主轴

The unique operating spine is:

> **Manage the work × Manage the people, connected by mechanisms.**
>
> **管事 × 管人，以机制贯通。**

```text
BUSINESS / 管事
Strategy → Work → Metrics → Execution → Business Review

PEOPLE / 管人
Organization → Roles → Accountability → Talent → Performance / Development

MECHANISM / 机制
Decision rights → Process → Resources → Information → Incentives → Governance
```

The mechanism line is connective tissue, not a third silo.

机制线不是第三个孤岛，而是让“管事”和“管人”相互可执行的连接层。

---

## Canonical Skill package / 唯一 Skill 运行包

Only one runtime package is canonical:

```text
skills/enterprise-operating-system/
├── SKILL.md
├── engines/
│   ├── router.md
│   ├── evidence.md
│   ├── diagnosis.md
│   ├── decision.md
│   ├── organization-design.md
│   ├── talent-allocation.md
│   ├── mechanism-design.md
│   ├── performance.md
│   ├── review.md
│   └── ai-work-redesign.md
├── references/
│   ├── business-people-integration.md
│   ├── organization.md
│   ├── talent-review.md
│   ├── mechanism.md
│   ├── performance.md
│   ├── mbr.md
│   └── ai-organization.md
└── templates/
    ├── company-intake.md
    ├── diagnosis.md
    └── 90-day-plan.md
```

There is intentionally no duplicate root `SKILL.md`, `engines/`, or `templates/` runtime tree.

根目录不再保留第二份 `SKILL.md`、`engines/` 或 `templates/`，避免安装歧义和版本漂移。

---

## Progressive disclosure / 渐进式读取

`SKILL.md` is the operating contract. `engines/router.md` selects the smallest required reasoning path. Engines contain procedures, references contain deeper domain logic, and templates convert reasoning into reusable operating artifacts.

`SKILL.md` 是运行协议；`engines/router.md` 负责选择最小必要推理路径；engines 提供推理程序，references 提供更深知识，templates 把推理转成可复用的经营产物。

Do not load every framework for every task. Progressive disclosure reduces context noise and framework overfitting.

不要每个问题都加载全部框架。渐进读取可以减少上下文噪音和“为了套框架而套框架”。

---

## Repository-level layers / 仓库级能力

The portable Skill is only one layer of the repository:

```text
skills/      → executable Agent Skill / 可安装 Skill
benchmark/   → model-agnostic reasoning benchmark / 模型无关推理 Benchmark
evals/       → behavioral evaluation cases / 行为评测
examples/    → operating scenarios / 经营案例
docs/        → architecture, methodology, evaluation / 架构与方法论
scripts/     → structural validation / 结构验证
.github/     → CI / 持续集成
```

`benchmark/` and `evals/` test whether an Agent actually follows the operating logic; they are not part of the installed runtime context by default.

`benchmark/` 与 `evals/` 用来检验 Agent 是否真的遵守经营逻辑，默认不属于安装后的运行上下文。

---

## Design invariants / 设计不变量

1. Evidence before strong claims. / 强结论之前必须有证据。
2. Diagnosis before intervention. / 干预之前先诊断。
3. Business problem is not automatically a people problem. / 业务问题不自动等于人的问题。
4. Responsibility requires authority; accountability requires resources. / 责任必须匹配权力，问责必须匹配资源。
5. Work is redesigned before headcount in AI transformation. / AI 转型先重构工作，再讨论人头。
6. Every material decision has measurement, review, and reversal conditions. / 每个重要决策都有衡量、复盘和反转条件。
7. Unknowns remain visible instead of being filled with invented facts. / 未知项保持可见，不用编造事实填空。
8. Runtime logic has one canonical source. / 运行逻辑只有一个 canonical 来源。

---

## Validation / 验证

Two structural CI paths protect the repository:

- `scripts/validate-skill.sh` checks canonical Skill structure, runtime references, frontmatter, router presence, operating invariants, and duplicate runtime trees.
- `scripts/validate-benchmark.sh` checks the benchmark case schema and minimum suite size.

Structural validation does **not** equal semantic model performance. Model scores should only be published after actual benchmark runs.

结构验证不等于模型真实推理成绩；Benchmark 分数只有在真实模型运行后才可以发布。
