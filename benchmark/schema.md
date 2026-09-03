# Benchmark Case Schema

> **Standard contract for every benchmark case. / 每个 Benchmark 案例的统一结构。**

A valid case must contain the following sections.

```yaml
id: unique-kebab-case-id
title: bilingual case title
type: flagship | adversarial
domains: [strategy, organization, mechanism, people, execution]
difficulty: basic | intermediate | advanced
```

## Required sections / 必填章节

### 1. Context / 背景
Facts required to understand the business situation.

### 2. Evidence / 证据
Only facts available to the Agent. Label each item as observed, reported, inferred, assumed, or unknown.

### 3. Prompt / 用户问题
The exact task given to the target Agent.

### 4. Expected reasoning / 期望推理
The reasoning behaviors a strong Agent should demonstrate. Do not require one exact wording or one predetermined business answer.

### 5. Forbidden shortcuts / 禁止捷径
Specific failure behaviors that should reduce the score.

### 6. Decision criteria / 决策标准
Checks for whether the final recommendation is sufficiently supported, executable, and reversible.

### 7. Evaluation notes / 评测说明
Case-specific interpretation notes for evaluators.

## Evidence discipline / 证据纪律

A case must never hide an assumption inside its Evidence section. If a causal relationship is intended as a testable hypothesis, label it as such.

## Answer independence / 答案独立性

The benchmark should reward a sound diagnosis even when the Agent's final intervention differs from the evaluator's preferred intervention, provided that the decision is evidence-supported and satisfies the stated constraints.
