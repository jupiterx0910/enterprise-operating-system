# Enterprise Operating System

> **让 Agent 真正理解、诊断、决策并重构企业经营方式的 AI 原生操作系统。**

[English + 中文主 README](./README.md)

## 它不是“企业管理知识库”

大多数管理类 Agent 的问题不是“不懂框架”，而是：

- 用户一说“业绩差”，就开始怪人；
- 用户说“裁员 30%”，就顺着给裁员方案；
- 用户说“最高绩效者”，就默认应该晋升；
- 用户说“组织效率低”，就直接画新组织架构；
- 用户说“AI 提效 30%”，就直接换算成少 30% 人。

Enterprise Operating System（EOS）不直接服从这种问题表述，而是先判断：

> **这到底是什么经营问题？证据支持到哪一步？应该进入哪条推理路径？**

---

## 核心闭环

```text
证据
 ↓
诊断
 ↓
根因
 ↓
决策
 ↓
行动
 ↓
衡量
 ↓
复盘
 ↓
学习
 ↺
```

对应运行协议：

`DISCOVER → DIAGNOSE → DESIGN → DECIDE → EXECUTE → MEASURE → REVIEW → LEARN`

核心约束：**先证据、后诊断，再干预。**

---

## 核心模型

> **经营结果 = 战略 × 组织 × 人才 × 机制 × 执行**

乘号意味着：任一关键维度严重失效，都可能主导最终结果；不能机械地把问题平均分摊到五个框里。

### 最有辨识度的经营主轴

> **管事 × 管人，以机制贯通。**

| 管事 | 管人 |
|---|---|
| 市场洞察与战略方向 | 组织盘点与阵型设计 |
| 指标设定与任务拆解 | 权责定义与人才匹配 |
| 过程执行与任务推进 | 过程教练与资源赋能 |
| 业务考核 | 绩效评价与价值分配 |
| 业务复盘 | 组织复盘与资产沉淀 |

机制通过**决策权、流程、资源、信息、激励、治理与复盘**连接两条线。

---

## Router：先判断问题，再调用框架

EOS 每个实质性问题先进入：

[`skills/enterprise-operating-system/engines/router.md`](./skills/enterprise-operating-system/engines/router.md)

```text
业务上下文
   ↓
ROUTER
意图 + 证据充分度 + 干预偏见
   ↓
证据门
   ↓
DIAGNOSE | ORG_DESIGN | TALENT_ALLOCATE | MECHANISM_DESIGN
PERFORMANCE | REVIEW | AI_REDESIGN | DECIDE
   ↓
决策契约
   ↓
行动 → 衡量 → 复盘 → 学习
```

主要路由：

- `DIAGNOSE`：目标未达成、经营异常、冲突、原因不清；
- `ORG_DESIGN`：组织结构、岗位、接口、决策权；
- `TALENT_ALLOCATE`：晋升、继任、岗位匹配、替换；
- `MECHANISM_DESIGN`：流程、激励、资源、治理；
- `PERFORMANCE`：目标、KPI、绩效、MBR/QBR；
- `REVIEW`：经营复盘与组织学习；
- `AI_REDESIGN`：Human + AI + Agent 工作重构；
- `DECIDE`：诊断已经充分，需要形成正式决策。

如果用户只是给出一个症状，或者已经预设“换人、裁员、晋升、加 KPI、改组织、全面上 AI”，而因果证据不足，默认先进入 `DIAGNOSE`。

**预设干预只能作为假设，不能作为诊断结论。**

---

## 决策不是一句建议

每个重要决策必须明确：

```text
决策
+ 证据
+ 负责人
+ 决策权
+ 执行权
+ 资源
+ 截止时间
+ 成功指标
+ 复盘日期
+ 反转条件
```

因此：

- 有责任无权力 = 无效设计；
- 有问责无资源 = 无效设计；
- 没有衡量与复盘 = 还没有真正形成可执行决策。

---

## AI 原生组织：先重构工作，再谈人头

不要从：

> “AI 会替代哪些岗位？”

开始。

EOS 使用：

```text
业务结果
 ↓
工作
 ↓
工作流
 ↓
任务
 ↓
判断 + 执行 + 关系 + 最终责任
 ↓
Human | AI | Agent | Hybrid
 ↓
新工作流 / 新岗位 / 新权限 / 新控制 / 新指标
 ↓
验证
```

**“AI 能做某个任务”不等于“这个岗位应该消失”。**

也不能把：

> “AI 提效 30%”

直接换算成：

> “裁员 30%”。

必须先验证重构后的真实产能、质量、风险、剩余人类责任与转换成本。

---

## 可执行 Benchmark

仓库不只描述方法论，还用 Benchmark 检验 Agent 是否真的遵守它。

当前包括：

- **10 个旗舰经营案例**；
- **5 个对抗性案例**；
- **6 个评分维度 × 0–2 分 = 12 分**；
- hard-fail 规则：编造事实、无证据换人、AI 一刀切裁员、有问责无权限/资源、忽略关键未知项却给高置信结论等。

查看：

- [`benchmark/README.md`](./benchmark/README.md)
- [`benchmark/rubric.md`](./benchmark/rubric.md)
- [`docs/evaluation.md`](./docs/evaluation.md)

**结构 CI 通过不等于模型推理成绩。只有真实运行模型后，才可以发布 Benchmark 分数。**

---

## 唯一 canonical Skill

真正可安装的运行时只有一份：

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
└── templates/
```

仓库不再保留第二份 root `SKILL.md`、root `engines/` 或 root `templates/`，避免安装歧义与版本漂移。

---

## 安装

对于支持 Agent Skills 规范的 Runtime，请复制或安装整个目录：

```text
skills/enterprise-operating-system/
```

**不要只复制 `SKILL.md`。**

EOS 使用渐进式读取：入口 Skill 先路由，再只加载当前问题真正需要的 engine/reference/template。

---

## 核心原则

1. 没有证据，不做强结论。
2. 症状不等于根因。
3. 业务问题不自动等于人的问题。
4. 观察事实、他人陈述、推断、假设、未知项必须分开。
5. 归因个人之前，先验证战略、组织、机制和执行解释。
6. 高绩效 ≠ 高潜力 ≠ 岗位就绪度。
7. 裁员是干预，不是诊断。
8. AI 转型先重构工作，再重构人头。
9. 重要决策必须匹配负责人、权力、资源、指标、复盘与反转条件。
10. 不用自信语气掩盖不确定性。

---

## 仓库结构

- [`skills/enterprise-operating-system/SKILL.md`](./skills/enterprise-operating-system/SKILL.md) — 核心 Agent 协议
- [`engines/`](./skills/enterprise-operating-system/engines/) — 推理引擎
- [`references/`](./skills/enterprise-operating-system/references/) — 深层经营知识
- [`templates/`](./skills/enterprise-operating-system/templates/) — 标准化工作模板
- [`benchmark/`](./benchmark/) — 模型无关经营推理 Benchmark
- [`evals/`](./evals/) — 行为评测
- [`examples/`](./examples/) — 经营场景
- [`docs/architecture.md`](./docs/architecture.md) — 系统架构
- [`docs/design-philosophy.md`](./docs/design-philosophy.md) — 设计哲学
- [`CHANGELOG.md`](./CHANGELOG.md) — 版本演进

---

## 长期方向

目标不是写出“最完整的企业管理文档”，而是建立一个：

> **可安装、可路由、可验证、可持续迭代的企业经营 Agent Skill。**

真正的护城河应该来自：

`经营推理逻辑 + Router 质量 + 证据纪律 + 真实企业案例 + 对抗性 Benchmark + 人类判断 + 持续回归测试`

而不是“又增加了几十页管理知识”。
