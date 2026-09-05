# Enterprise Operating System

> **An AI-native reasoning and execution system for how companies work.**  
> **一个让 Agent 理解、诊断并重构企业经营方式的 AI 原生操作系统。**

[![Agent Skill](https://img.shields.io/badge/Agent-Skill-0f172a)](https://github.com/jupiterx0910/enterprise-operating-system/tree/main/skills/enterprise-operating-system)
[![Bilingual](https://img.shields.io/badge/Language-中文%20%2B%20English-blue)](https://github.com/jupiterx0910/enterprise-operating-system)
[![Evaluation](https://img.shields.io/badge/Evals-Behavioral%20Tests-purple)](https://github.com/jupiterx0910/enterprise-operating-system/tree/main/evals)
[![Benchmark](https://img.shields.io/badge/Benchmark-15%20Cases-orange)](https://github.com/jupiterx0910/enterprise-operating-system/tree/main/benchmark)

## Why this exists / 为什么做它

Most management frameworks describe **what good management looks like**. This project is designed to make an Agent **actually reason and operate** through a business problem.

大多数管理方法论告诉人“好的管理应该是什么样”。这个项目要解决的是：让 Agent **真正按照一套可验证的经营逻辑去分析、决策、执行和复盘**。

It is not a generic HR chatbot and not a collection of management essays. It is a **portable Agent Skill + executable reasoning benchmark**.

它不是通用 HR 聊天机器人，也不是管理学文章合集，而是一个**可安装的 Agent Skill + 可执行的经营推理 Benchmark**。

The core difference is simple:

> **A normal Agent answers the question. EOS first asks what kind of enterprise problem this actually is, what the evidence supports, and which reasoning engine should be used.**
>
> **普通 Agent 直接回答问题；EOS 先判断“这到底是什么经营问题、证据支持到哪一步、应该进入哪条推理路径”。**

---

## The core loop / 核心闭环

```text
EVIDENCE
   ↓
DIAGNOSIS
   ↓
ROOT CAUSE
   ↓
DECISION
   ↓
ACTION
   ↓
MEASUREMENT
   ↓
REVIEW
   ↓
LEARNING
   ↺
```

The Agent is explicitly constrained to move from evidence to diagnosis before intervention.  
Agent 被明确要求：先证据、后诊断，再做干预。

---

## Core model / 核心模型

> **Business outcome = Strategy × Organization × People × Mechanism × Execution**  
> **经营结果 = 战略 × 组织 × 人才 × 机制 × 执行**

The multiplication sign is intentional: a severe failure in one dimension can dominate the outcome.  
乘号是有意的：任何一个关键维度的严重失效，都可能主导最终结果。

### The operating spine / 经营主轴

> **Manage the work × Manage the people, connected by mechanisms.**  
> **管事 × 管人，以机制贯通。**

| Manage the work / 管事 | Manage the people / 管人 |
|---|---|
| Market insight & strategy / 市场洞察与战略方向 | Organization inventory & formation / 组织盘点与阵型设计 |
| Metrics & task decomposition / 指标设定与任务拆解 | Accountability & talent matching / 权责定义与人才匹配 |
| Execution / 过程执行与任务推进 | Coaching & resource enablement / 过程教练与资源赋能 |
| Business assessment / 业务考核 | Performance & value distribution / 绩效评价与价值分配 |
| Business review / 业务复盘 | Organization review & asset accumulation / 组织复盘与资产沉淀 |

The mechanism layer connects both tracks through decision rights, processes, resources, information, incentives, governance and review.

机制不是第三个孤岛，而是通过决策权、流程、资源、信息、激励、治理与复盘，把“管事”和“管人”真正连接起来。

---

## Router first / 先路由，再推理

EOS does not load every management framework for every question.

EOS 不会每个问题都把所有管理框架读一遍。

Every substantial request starts at the **Enterprise Reasoning Router**:

```text
USER / BUSINESS CONTEXT
        ↓
ROUTER
(intent + evidence + intervention bias)
        ↓
EVIDENCE GATE
        ↓
DIAGNOSE | ORG_DESIGN | TALENT_ALLOCATE | MECHANISM_DESIGN
PERFORMANCE | REVIEW | AI_REDESIGN | DECIDE
        ↓
DECISION CONTRACT
        ↓
ACTION → MEASURE → REVIEW → LEARN
```

| Route | Typical question / 典型问题 |
|---|---|
| `DIAGNOSE` | Why did the business miss the target? / 为什么业务没达标？ |
| `ORG_DESIGN` | How should structure, roles or decision rights change? / 组织、岗位、决策权怎么改？ |
| `TALENT_ALLOCATE` | Promote, rotate, coach, replace or succession? / 晋升、轮岗、辅导、更换还是继任？ |
| `MECHANISM_DESIGN` | Are process, incentives, resources or governance broken? / 流程、激励、资源、治理是否失效？ |
| `PERFORMANCE` | How should goals, KPI, MBR/QBR or performance work? / 目标、KPI、MBR/QBR、绩效怎么设计？ |
| `REVIEW` | What should we learn and change after execution? / 执行后应复盘什么、改变什么？ |
| `AI_REDESIGN` | How should Human + AI + Agent divide the work? / 人、AI、Agent 如何重新分工？ |
| `DECIDE` | Evidence is sufficient; what decision should be made? / 证据已充分，应该做什么决策？ |

**Default invariant:** if the input is only a symptom, or the user has already decided to fire, cut, promote, add KPIs, reorganize, or deploy AI without enough causal evidence, EOS routes to `DIAGNOSE` first.

**默认不变量：**如果输入只是症状，或者用户在因果证据不足时已经预设“换人、裁员、晋升、加 KPI、改组织、全面上 AI”，EOS 必须先进入 `DIAGNOSE`。

A proposed intervention is a hypothesis, not a diagnosis.

预设干预只能作为假设，不能作为诊断结论。

---

## 30-second demo / 30 秒看懂

**User / 用户：**

> “Sales missed target by 30%. We should replace the VP. Diagnose it.”
>
> “销售目标差了 30%，应该换销售 VP。帮我诊断。”

**Weak Agent / 普通 Agent：**

> “建议立即更换 VP，并启动招聘。”

**Enterprise Operating System / EOS：**

```text
1. Route → DIAGNOSE / 先路由到诊断
2. Verify the gap / 验证目标偏差
3. Separate symptom from cause / 区分症状与根因
4. Test Strategy / Organization / Mechanism / People / Execution
5. Classify evidence, unknowns and confidence / 标记证据、未知项与置信度
6. Compare competing explanations / 比较竞争性解释
7. Decide: CONTINUE / ADJUST / RESTRUCTURE / REPLACE / STOP
8. Assign owner + authority + resources + deadline + metric
9. Set review and reversal conditions / 设置复盘与反转条件
```

It must **not** jump from “missed target” to “replace the person” without evidence.  
不能因为“目标没完成”就直接跳到“换人”。

---

## Decision contract / 决策必须可执行

A recommendation is not complete because it sounds reasonable.

一个建议不是“听起来有道理”就算完成。

Every material decision resolves:

```text
Decision
+ Evidence
+ Owner
+ Decision authority
+ Execution authority
+ Resources
+ Deadline
+ Success metric
+ Review date
+ Reversal condition
```

This makes **responsibility without authority** and **accountability without resources** invalid by design.

因此，“有责任无权力”和“有问责无资源”在系统里会被直接判定为无效设计。

---

## AI-native organization / AI 原生组织

Do not start with:

> **“Which jobs will AI replace?” / “AI 会替代哪些岗位？”**

Start with:

```text
BUSINESS OUTCOME
 ↓
WORK
 ↓
WORKFLOWS
 ↓
TASKS
 ↓
DECISIONS + ACCOUNTABILITY
 ↓
HUMAN | AI | AGENT | HYBRID
 ↓
NEW WORKFLOW / ROLE / AUTHORITY / CONTROLS / METRICS
 ↓
VALIDATION
```

The unit of redesign is **work**, not simply headcount.  
重构的基本单位是**工作**，而不是简单的人头。

EOS explicitly rejects the shortcut:

> “AI productivity +30% → headcount -30%.”

It first validates redesigned workflow capacity, quality, risk, residual human responsibility and transition cost.

EOS 不允许把“AI 提效 30%”直接映射为“裁员 30%”，而是先验证新工作流的产能、质量、风险、剩余人类责任与转换成本。

---

## Behavioral benchmark / 行为 Benchmark

This repository does not only describe the methodology. It tests whether an Agent follows it.

仓库不只是描述方法论，而是测试 Agent **是否真的遵守这套方法论**。

### 15 benchmark cases

**10 flagship cases** cover sales gaps, margin collapse, executive conflict, organization layering, promotion, product underperformance, AI transformation, founder bottlenecks, incentive distortion and succession risk.

**5 adversarial cases** deliberately inject tempting conclusions such as:

- “Fire the VP.”
- “AI productivity is +30%, so cut 30%.”
- “Top performer = VP material.”
- “The team is lazy.”
- “Add five more KPIs.”

The Agent should resist the framing when the evidence does not support it.

→ **[Explore the Benchmark](./benchmark/README.md)**  
→ **[Read the Evaluation Rubric](./benchmark/rubric.md)**

### Scoring / 评分

Six dimensions × 0–2 points = **12 points**:

`Evidence → Causality → System Thinking → Decision → Execution → AI-native Redesign`

Hard failures include fabricated facts, unsupported personnel actions, blanket AI layoffs, accountability without authority/resources, and high-confidence conclusions that ignore material unknowns.

**Important:** benchmark scores are only published after an actual model run. Structural CI validation is not presented as semantic model performance.

---

## What is inside / 项目内容

| Layer | Canonical location | Purpose / 作用 |
|---|---|---|
| Skill entry | `skills/enterprise-operating-system/SKILL.md` | Router + operating contract / Router 与核心运行协议 |
| Engines | `skills/enterprise-operating-system/engines/` | Evidence, diagnosis, decision, organization, talent, mechanism, performance, review, AI redesign / 推理引擎 |
| References | `skills/enterprise-operating-system/references/` | Deeper enterprise operating logic / 深层经营知识 |
| Templates | `skills/enterprise-operating-system/templates/` | Intake, diagnosis and 90-day execution artifacts / 标准化输出模板 |
| Examples | `examples/` | Operating scenarios / 经营场景 |
| Evals | `evals/` | Behavioral evaluation / Agent 行为评测 |
| Benchmark | `benchmark/` | Model-agnostic reasoning benchmark / 模型无关推理测试 |
| Docs | `docs/` | Architecture, methodology, evaluation / 架构、方法与评测说明 |
| CI | `scripts/` + `.github/workflows/` | Structural regression protection / 结构防回归 |

There is intentionally **one canonical runtime tree**. No duplicate root `SKILL.md`, `engines/`, or `templates/` is maintained.

仓库只保留**一份 canonical 运行时目录**，不再维护第二份 root `SKILL.md`、`engines/` 或 `templates/`。

---

## Non-negotiable rules / 不可违背原则

1. **No evidence → no strong claim. / 没有证据，不做强结论。**
2. **Symptom ≠ root cause. / 症状不等于根因。**
3. **Business problem ≠ people problem. / 业务问题不等于人的问题。**
4. **Responsibility without authority is invalid design. / 有责任无权力，是无效设计。**
5. **Accountability without resources is invalid design. / 有问责无资源，是无效设计。**
6. **High performance ≠ high potential ≠ role readiness. / 高绩效 ≠ 高潜力 ≠ 岗位就绪。**
7. **Headcount reduction is an intervention, not a diagnosis. / 裁员是干预手段，不是诊断结论。**
8. **Redesign work before redesigning headcount. / 先重构工作，再重构人头。**
9. **Do not manufacture missing facts. / 不得编造缺失事实。**
10. **Every material decision needs review and reversal conditions. / 每个重要决策都必须可复盘、可反转。**

---

## Install / 安装

The canonical Skill lives at:

```text
skills/enterprise-operating-system/
```

For Agent runtimes that support the Skills convention, install or copy the **entire directory**, not only `SKILL.md`.

对于支持 Skills 规范的 Agent Runtime，请安装或复制**整个目录**，而不是只复制 `SKILL.md`。

```text
skills/enterprise-operating-system/
├── SKILL.md
├── engines/
├── references/
└── templates/
```

The Skill uses progressive disclosure: `SKILL.md` routes the task, and the Agent reads only the engines/references required by the current problem.

Skill 使用渐进式读取：`SKILL.md` 先路由问题，Agent 再只读取当前任务真正需要的 engines/references。

---

## Repository map / 仓库结构

- [`SKILL.md`](./skills/enterprise-operating-system/SKILL.md) — canonical Agent protocol / 核心 Agent 协议
- [`router.md`](./skills/enterprise-operating-system/engines/router.md) — enterprise reasoning router / 企业推理 Router
- [`engines/`](./skills/enterprise-operating-system/engines/) — reasoning engines / 推理引擎
- [`references/`](./skills/enterprise-operating-system/references/) — domain references / 知识模块
- [`templates/`](./skills/enterprise-operating-system/templates/) — reusable templates / 工作模板
- [`examples/`](./examples/) — operating scenarios / 经营场景
- [`evals/`](./evals/) — behavioral evaluation / 行为评测
- [`benchmark/`](./benchmark/) — benchmark suite / Benchmark 测试集
- [`docs/architecture.md`](./docs/architecture.md) — architecture / 架构
- [`docs/design-philosophy.md`](./docs/design-philosophy.md) — design principles / 设计哲学
- [`docs/evaluation.md`](./docs/evaluation.md) — evaluation philosophy / 评测逻辑

---

## Project direction / 项目方向

The goal is not to create the “best management document”. The goal is to build a **portable, testable and continuously improving enterprise reasoning skill for AI agents**.

目标不是写出“最好看的企业管理文档”，而是建立一个**可迁移、可测试、可持续迭代的企业经营 Agent Skill**。

The long-term moat should come from:

```text
Operating logic
+ Router quality
+ Evidence discipline
+ Real enterprise cases
+ Adversarial benchmark
+ Human judgment
+ Continuous regression testing
```

而不是来自“又多写了几十页管理知识”。

---

## Contributing / 参与贡献

Useful contributions include:

- new real-world cases / 新的真实案例
- adversarial evaluation prompts / 对抗性测试
- better routing and diagnostic logic / 更好的路由与诊断逻辑
- evidence standards / 证据标准
- organization / talent / mechanism engines / 组织、人才、机制引擎
- AI-native organization patterns / AI 原生组织模式
- integrations with Agent runtimes / Agent Runtime 集成

See [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## License

MIT — see [`LICENSE`](./LICENSE).
