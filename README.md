# Enterprise Operating System

> **An AI-native reasoning and execution system for how companies work.**  
> **一个让 Agent 理解、诊断并重构企业经营方式的 AI 原生操作系统。**

[![Agent Skill](https://img.shields.io/badge/Agent-Skill-0f172a)](https://github.com/jupiterx0910/enterprise-operating-system/tree/main/skills/enterprise-operating-system)
[![Bilingual](https://img.shields.io/badge/Language-中文%20%2B%20English-blue)](https://github.com/jupiterx0910/enterprise-operating-system)
[![Evaluation](https://img.shields.io/badge/Evals-Behavioral%20Tests-purple)](https://github.com/jupiterx0910/enterprise-operating-system/tree/main/evals)

## Why this exists / 为什么做它

Most management frameworks describe **what good management looks like**. This project is designed to make an Agent **actually reason and operate** through a business problem.

大多数管理方法论告诉人“好的管理应该是什么样”。这个项目要解决的是：让 Agent **真正按照一套可验证的经营逻辑去分析、决策、执行和复盘**。

It is not a generic HR chatbot and not a collection of management essays.

它不是通用 HR 聊天机器人，也不是管理学文章合集。

## The operating loop / 核心闭环

```text
DISCOVER → DIAGNOSE → DESIGN → DECIDE
    ↑                              ↓
  LEARN ← REVIEW ← MEASURE ← EXECUTE
```

**Evidence → Diagnosis → Decision → Action → Measurement → Learning**  
**证据 → 诊断 → 决策 → 行动 → 衡量 → 学习**

## Core model / 核心模型

> **Business outcome = Strategy × Organization × People × Mechanism × Execution**  
> **经营结果 = 战略 × 组织 × 人才 × 机制 × 执行**

The multiplication sign is intentional: a severe failure in one dimension can dominate the outcome.  
乘号是有意的：任何一个关键维度的严重失效，都可能主导最终结果。

## 30-second demo / 30秒看懂

**User / 用户：**

> “Sales missed target by 30%. We should replace the VP. Diagnose it.”
>
> “销售目标差了 30%，应该换销售 VP。帮我诊断。”

**Agent should / Agent 应该：**

```text
1. Verify the gap / 验证目标偏差
2. Separate symptom from cause / 区分症状与根因
3. Test Strategy / Organization / Mechanism / People / Execution
4. Identify evidence and uncertainty / 标记证据与不确定性
5. Decide: CONTINUE / ADJUST / RESTRUCTURE / REPLACE / STOP
6. Assign owner + authority + resources + deadline + metric
7. Set review and reversal conditions
```

It must **not** jump from “missed target” to “replace the person” without evidence.  
不能因为“目标没完成”就直接跳到“换人”。

## AI-native organization / AI 原生组织

Do not start with:

> **“Which jobs will AI replace?” / “AI 会替代哪些岗位？”**

Start with:

```text
WORK
 ↓
TASKS
 ↓
DECISIONS
 ↓
ACCOUNTABILITY
 ↓
HUMAN | AI | AGENT | HUMAN+AI | HUMAN+AGENT
 ↓
NEW WORKFLOW / ROLE / AUTHORITY / METRICS
```

The unit of redesign is **work**, not simply headcount.  
重构的基本单位是**工作**，而不是简单的人头。

## What is inside / 项目内容

| Layer | Purpose | 内容 |
|---|---|---|
| `SKILL.md` | Agent protocol | Agent 核心执行协议 |
| `engines/` | Reasoning engines | 诊断、决策、组织、人才、机制、绩效、复盘、AI 重构 |
| `references/` | Domain knowledge | 企业经营知识模块 |
| `templates/` | Structured outputs | 标准化工作模板 |
| `examples/` | Real scenarios | 真实经营场景 |
| `evals/` | Behavioral evaluation | Agent 行为评测 |

## Non-negotiable rules / 不可违背原则

1. **No evidence → no strong claim. / 没有证据，不做强结论。**
2. **Symptom ≠ root cause. / 症状不等于根因。**
3. **Business problem ≠ people problem. / 业务问题不等于人的问题。**
4. **Responsibility without authority is invalid design. / 有责任无权力，是无效设计。**
5. **Accountability without resources is invalid design. / 有问责无资源，是无效设计。**
6. **High performance ≠ high potential. / 高绩效不等于高潜力。**
7. **Headcount reduction is an intervention, not a diagnosis. / 裁员是干预手段，不是诊断结论。**
8. **Redesign work before redesigning headcount. / 先重构工作，再重构人头。**
9. **Do not manufacture missing facts. / 不得编造缺失事实。**

## Install / 安装

The canonical Skill lives at:

```text
skills/enterprise-operating-system/SKILL.md
```

For Agent runtimes that support the Skills convention, install/copy the entire `skills/enterprise-operating-system/` directory as a Skill.

对于支持 Skills 规范的 Agent Runtime，将整个 `skills/enterprise-operating-system/` 目录作为 Skill 安装或复制即可。

## Repository map / 仓库结构

- [`SKILL.md`](./skills/enterprise-operating-system/SKILL.md) — canonical Agent protocol / 核心 Agent 协议
- [`engines/`](./skills/enterprise-operating-system/engines/) — reasoning engines / 推理引擎
- [`references/`](./skills/enterprise-operating-system/references/) — domain references / 知识模块
- [`templates/`](./skills/enterprise-operating-system/templates/) — reusable templates / 工作模板
- [`examples/`](./examples/) — flagship cases / 旗舰案例
- [`evals/`](./evals/) — behavioral evaluation / 行为评测
- [`docs/architecture.md`](./docs/architecture.md) — architecture / 架构
- [`docs/design-philosophy.md`](./docs/design-philosophy.md) — design principles / 设计哲学

## Project direction / 项目方向

The goal is not to create the “best management document”. The goal is to build a **portable, testable and continuously improving enterprise reasoning skill for AI agents**.

目标不是写出“最好看的企业管理文档”，而是建立一个**可迁移、可测试、可持续迭代的企业经营 Agent Skill**。

## Contributing / 参与贡献

Useful contributions include:

- new real-world cases / 新的真实案例
- adversarial evaluation prompts / 对抗性测试
- better diagnostic logic / 更好的诊断逻辑
- evidence standards / 证据标准
- AI-native organization patterns / AI 原生组织模式
- integrations with Agent runtimes / Agent Runtime 集成

## License

See [`LICENSE`](./LICENSE).
