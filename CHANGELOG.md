# Changelog

## 0.4.0 — 2026-09-28

### Added

- Five public, source-grounded real-world enterprise cases: Wells Fargo, Target Canada, Uber, Equifax, and Boeing 737 MAX
- Reproducible `NATIVE` vs `EOS_ENABLED` paired run contract with immutable run metadata
- Raw-output and per-case scorecard submission structure
- Skill-Lift leaderboard methodology with Candidate and Verified tiers
- Primary effectiveness metrics: `Skill Lift` and `Hard-Fail Reduction`
- Structural v0.4 CI plus a negative anti-fabrication test that rejects numeric leaderboard rows without auditable run artifacts

### Changed

- Benchmark documentation now distinguishes raw model capability from EOS incremental value
- Public documentation now describes 20 benchmark cases: 10 flagship, 5 adversarial, and 5 real-world
- Evaluation guidance now requires preserved runtime configuration, raw outputs, and independent human review for Verified entries

### Integrity

- No Verified model submissions exist at release time
- Structural CI is not presented as semantic model performance
- Public historical cases are explicitly labeled as non-contamination-resistant


## 0.3.0 — 2026-09-05

### Added

- Enterprise Reasoning Router with explicit routes for diagnosis, organization design, talent allocation, mechanism design, performance, review, AI work redesign, and decision-making
- Canonical evidence, diagnosis, decision, and AI work-redesign engines inside the installable Skill directory
- `管事 × 管人，以机制贯通` as the explicit operating spine
- Business × People integration reference with the five-stage operating model
- Canonical company-intake, diagnosis, and 90-day execution templates
- `scripts/validate-skill.sh` for runtime structure and reference validation
- Full benchmark-schema validation including `Evaluation notes / 评测说明`

### Changed

- Canonical `SKILL.md` is now router-driven and uses progressive disclosure
- Architecture documentation now distinguishes the installable runtime from repository-level benchmark/eval layers
- README now explains the Router, decision contract, operating spine, canonical runtime tree, and AI-native work-redesign logic
- Skill CI now validates the canonical runtime rather than using a superficial structure check

### Removed

- Duplicate root `SKILL.md`
- Duplicate root `engines/`
- Duplicate root `templates/`

The installable runtime now has one canonical source: `skills/enterprise-operating-system/`.

## 0.2.0 — 2026-08-28

### Added

- Bilingual Enterprise Operating System positioning
- Agent reasoning loop: Discover → Diagnose → Design → Decide → Execute → Measure → Review → Learn
- Evidence-aware diagnosis principles
- AI-native work redesign framing
- Behavioral evaluation direction
- Contribution guidelines
- MIT License

### Changed

- README upgraded from project description to product-oriented Agent Skill landing page
- Core positioning moved from HR methodology toward enterprise reasoning and execution

## 0.1.0

- Initial enterprise operating model and Agent Skill foundation
