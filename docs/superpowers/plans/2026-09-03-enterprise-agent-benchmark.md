# Enterprise Agent Benchmark Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn Enterprise Operating System into a portable, schema-driven benchmark for evaluating whether AI agents can diagnose, decide, execute, and review enterprise problems without unsafe reasoning shortcuts.

**Architecture:** Keep the canonical Skill as the reasoning protocol; add a lightweight benchmark layer containing a stable case schema, scoring rubric, adversarial cases, and repository validation. Cases are Markdown-first so humans and agents can inspect, diff, and extend them without a runtime dependency.

**Tech Stack:** Markdown, YAML frontmatter/data blocks, GitHub Actions, shell-based structural validation.

**Spec:** `docs/design-philosophy.md`

## Global Constraints

- Preserve bilingual Chinese + English terminology in all public benchmark documents.
- Do not claim benchmark scores that have not been actually executed.
- Do not require a model provider, API key, or paid runtime for repository validation.
- Keep the benchmark model-agnostic.
- Test reasoning behavior, not prose style.
- Every benchmark case must distinguish evidence, inference, unknowns, and the decision criteria.

---

### Task 1: Benchmark architecture and rubric

**Files:**
- Create: `benchmark/README.md`
- Create: `benchmark/schema.md`
- Create: `benchmark/rubric.md`
- Modify: `docs/evaluation.md`

- [ ] Define the benchmark case contract.
- [ ] Define the 12-point scoring rubric and pass thresholds.
- [ ] Document how human/model outputs are evaluated without pretending to have automated semantic grading.
- [ ] Verify all links and terminology against the canonical Skill.

### Task 2: Flagship benchmark cases

**Files:**
- Create: `benchmark/cases/01-missed-sales-target.md`
- Create: `benchmark/cases/02-margin-collapse.md`
- Create: `benchmark/cases/03-executive-conflict.md`
- Create: `benchmark/cases/04-org-layering.md`
- Create: `benchmark/cases/05-high-performer-promotion.md`
- Create: `benchmark/cases/06-underperforming-product.md`
- Create: `benchmark/cases/07-ai-headcount-cut.md`
- Create: `benchmark/cases/08-founder-bottleneck.md`
- Create: `benchmark/cases/09-incentive-distortion.md`
- Create: `benchmark/cases/10-succession-risk.md`

- [ ] Give each case a realistic context and explicit evidence set.
- [ ] Add adversarial user framing where appropriate.
- [ ] Define expected reasoning path and forbidden shortcuts.
- [ ] Define decision-quality checks without prescribing one universal answer.

### Task 3: Adversarial benchmark suite

**Files:**
- Create: `benchmark/adversarial/README.md`
- Create: `benchmark/adversarial/11-fire-the-vp.md`
- Create: `benchmark/adversarial/12-cut-30-percent.md`
- Create: `benchmark/adversarial/13-promote-top-performer.md`
- Create: `benchmark/adversarial/14-blame-the-team.md`
- Create: `benchmark/adversarial/15-add-more-kpis.md`

- [ ] Ensure each prompt tempts the Agent toward a premature people intervention.
- [ ] Add explicit anti-shortcut criteria.
- [ ] Cross-reference the five-domain diagnostic model.

### Task 4: Repository validation

**Files:**
- Create: `.github/workflows/validate-benchmark.yml`
- Create: `scripts/validate-benchmark.sh`
- Modify: `README.md`

- [ ] Validate required benchmark directories and files.
- [ ] Validate every case contains required headings.
- [ ] Validate canonical Skill frontmatter exists.
- [ ] Run the validator locally.
- [ ] Add benchmark usage to the README.

### Task 5: Final verification

- [ ] Run repository-wide structural checks.
- [ ] Verify no benchmark case claims an unexecuted score.
- [ ] Verify internal Markdown links for the new benchmark layer.
- [ ] Review the resulting GitHub tree for duplication and naming consistency.

