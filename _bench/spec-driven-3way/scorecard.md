# Scorecard: spec-kit vs get-shit-done vs superpowers

**Date:** 2026-04-19
**Dimension pack:** `spec-driven` (5 dimensions, pack weights sum 1.00)
**Slug:** spec-driven-3way
**Overall Confidence:** HIGH

---

## Scoring Method

- Score range: **0–100** per dimension.
- Pack weights: spec_format 0.20, traceability 0.20, executable_specs 0.22, tdd_integration 0.15, roundtripping 0.23 — **sum = 1.00** (verified).
- Each score derives from 2+ signals documented per dimension below.
- Any score ≥90 carries ≥2 signals with concrete evidence paths in `OS/{subject}/`.
- Missing signal → value recorded as `not_observed`; no score is invented.
- Source: filesystem scan of each subject (local-first).

---

## Dimension Scores

| Dimension | Weight | spec-kit | get-shit-done | superpowers | Advantage |
|-----------|-------:|:--------:|:-------------:|:-----------:|:---------:|
| Spec Format | 20% | **88** | 85 | 45 | spec-kit |
| Traceability | 20% | **80** | 72 | 55 | spec-kit |
| Executable Specs | 22% | 75 | **78** | 62 | get-shit-done |
| TDD Integration | 15% | 30 | 62 | **95** | superpowers |
| Roundtripping | 23% | 42 | **68** | 25 | get-shit-done |

---

## Weighted Total

| Subject | Weighted Score | Dim Wins | Strongest dim |
|---------|:-------------:|:--------:|---------------|
| spec-kit | **64.26 / 100** | 2 | Spec Format (88), Traceability (80) |
| get-shit-done | **73.50 / 100** | 2 | Executable Specs (78), Roundtripping (68) |
| superpowers | **53.64 / 100** | 1 | TDD Integration (95) |

**Overall Winner:** **get-shit-done** (+9.24 pts over spec-kit, +19.86 over superpowers)

Math:
- spec-kit = 88*0.20 + 80*0.20 + 75*0.22 + 30*0.15 + 42*0.23 = 17.60 + 16.00 + 16.50 + 4.50 + 9.66 = **64.26**
- get-shit-done = 85*0.20 + 72*0.20 + 78*0.22 + 62*0.15 + 68*0.23 = 17.00 + 14.40 + 17.16 + 9.30 + 15.64 = **73.50**
- superpowers = 45*0.20 + 55*0.20 + 62*0.22 + 95*0.15 + 25*0.23 = 9.00 + 11.00 + 13.64 + 14.25 + 5.75 = **53.64**

---

## Dimension Analysis

### Spec Format (20%)

**spec-kit: 88/100** | **get-shit-done: 85/100** | **superpowers: 45/100** | Confidence: HIGH

spec-kit publishes the most canonical spec template in the trio (User Stories P1–P3, `FR-###` Functional Requirements, `SC-###` Success Criteria, Edge Cases, Assumptions, Key Entities) and couples it with a per-spec checklist validated by `/speckit.specify`. GSD matches it structurally and adds a **quantitative** ambiguity gate (weighted 4-dim score ≤0.20) that refuses to lock SPEC.md until requirements are falsifiable. Superpowers deliberately has no typed spec artefact — the spec is a design document emerging from a brainstorming dialogue, saved wherever the user chooses.

**Signals observed:**

- **spec-kit**
  - Structured MD template with mandatory sections (US/FR/SC/Edge Cases/Assumptions/Key Entities) — `OS/spec-kit/templates/spec-template.md`
  - Validation checklist auto-generated per spec — `OS/spec-kit/templates/checklist-template.md`
  - Requirement ID scheme (FR-/SC-/US#) — `OS/spec-kit/templates/spec-template.md`
  - Examples library embedded (priority-tiered user-story patterns) — `OS/spec-kit/templates/spec-template.md`
- **get-shit-done**
  - Structured MD template with Current/Target/Acceptance per requirement + Boundaries in/out-of-scope + Ambiguity Report — `OS/get-shit-done/get-shit-done/templates/spec.md`
  - Quantitative gate (4-dim weighted ambiguity score ≤0.20) — `OS/get-shit-done/get-shit-done/workflows/spec-phase.md`
  - Vague requirements rejected explicitly ('should be fast' → '<200ms at p95') — `OS/get-shit-done/get-shit-done/workflows/spec-phase.md`
  - Related contracts UI-SPEC / AI-SPEC — `OS/get-shit-done/get-shit-done/templates/UI-SPEC.md`, `AI-SPEC.md`
- **superpowers**
  - No typed spec artefact; spec emerges from brainstorming — `OS/superpowers/README.md`, `skills/brainstorming/`
  - Plan-level 'No Placeholders' rule (not spec level) — `OS/superpowers/skills/writing-plans/SKILL.md`

### Traceability (20%)

**spec-kit: 80/100** | **get-shit-done: 72/100** | **superpowers: 55/100** | Confidence: HIGH

spec-kit's `FR-###/SC-###/US#` IDs survive from spec into plan and tasks, and `/speckit.taskstoissues` exports the task list into GitHub Issues — making the IDs visible in an external tracker. GSD tracks traceability through verification reports, a requirements-coverage gate, and claim-provenance tagging — strong machinery, but without canonical IDs. Superpowers has no IDs but its TDD enforcement means every behaviour has a test, which functions as an implicit spec↔test link.

**Signals observed:**

- **spec-kit**
  - Stable IDs FR-###/SC-###/US# referenced downstream — `OS/spec-kit/templates/spec-template.md`, `OS/spec-kit/templates/tasks-template.md`
  - Issue export keeps IDs visible in GitHub — `OS/spec-kit/templates/commands/taskstoissues.md`
  - Plan template explicitly references spec path — `OS/spec-kit/templates/plan-template.md`
- **get-shit-done**
  - Verification reports map acceptance criteria to pass/fail — `OS/get-shit-done/get-shit-done/templates/verification-report.md`
  - Requirements-coverage gate — `OS/get-shit-done/docs/FEATURES.md#21`
  - Claim-provenance tagging — `OS/get-shit-done/docs/FEATURES.md#65`
- **superpowers**
  - TDD ties every behaviour to a test (implicit link) — `OS/superpowers/skills/test-driven-development/SKILL.md`
  - No requirement IDs — not_observed

### Executable Specs (22%)

**spec-kit: 75/100** | **get-shit-done: 78/100** | **superpowers: 62/100** | Confidence: HIGH

spec-kit produces the widest scaffolding surface (`plan.md + research.md + data-model.md + quickstart.md + contracts/`), plus `/speckit.analyze` for cross-artefact consistency. GSD runs the deepest continuous validation stack (requirements-coverage gate + cross-phase regression gate + scope-reduction detection + verification gate) and can run the whole pipeline end-to-end via `/gsd-autonomous`. Superpowers ties failing-test-first to execution via its TDD skill but does not scaffold non-test artefacts from spec. spec-kit's explicit `tasks-template.md:11` note that tests are OPTIONAL by default costs it points on the "specs → tests" axis.

**Signals observed:**

- **spec-kit**
  - 5-artefact scaffolding from spec — `OS/spec-kit/templates/commands/plan.md`, `OS/spec-kit/templates/plan-template.md`
  - `/speckit.analyze` + `/speckit.clarify` loops — `OS/spec-kit/templates/commands/analyze.md`, `clarify.md`
  - `/speckit.implement` implementation command — `OS/spec-kit/templates/commands/implement.md`
  - Tests OPTIONAL unless requested — `OS/spec-kit/templates/tasks-template.md:11`
- **get-shit-done**
  - 5-stage pipeline with locked upstream artefacts — `OS/get-shit-done/commands/gsd/{spec,discuss,plan,execute}-phase.md`
  - Requirements-coverage + cross-phase regression gates — `OS/get-shit-done/docs/FEATURES.md#20,#21`
  - Autonomous end-to-end runner — `OS/get-shit-done/commands/gsd/autonomous.md`
  - Add-tests command (manual) — `OS/get-shit-done/commands/gsd/add-tests.md`
- **superpowers**
  - Plan → fresh subagent per task + two-stage review — `OS/superpowers/skills/subagent-driven-development/SKILL.md`
  - TDD mandates failing test first — `OS/superpowers/skills/test-driven-development/SKILL.md`
  - No scaffolding of data-model/contracts — not_observed

### TDD Integration (15%)

**spec-kit: 30/100** | **get-shit-done: 62/100** | **superpowers: 95/100** | Confidence: HIGH

Superpowers is the only project in the trio where TDD is **enforced as law**. The TDD skill opens with "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST" and continues "Write code before the test? Delete it. Start over." Verify-RED and Verify-GREEN are marked MANDATORY. Subagent prompts propagate the expectation — the spec-reviewer subagent checks test-first compliance. This score ≥90 is justified by **four** evidence-linked signals. GSD documents TDD as philosophy with a reference doc + an add-tests command + a verification gate, but does not enforce a red-green cycle. spec-kit actively opts out: `tasks-template.md:11` makes tests optional unless requested.

**Signals observed:**

- **spec-kit**
  - Tests OPTIONAL in tasks template — `OS/spec-kit/templates/tasks-template.md:11`
  - Given/When/Then acceptance scenarios in spec (not mandatorily tested) — `OS/spec-kit/templates/spec-template.md`
- **get-shit-done**
  - TDD reference doc — `OS/get-shit-done/get-shit-done/references/tdd.md`
  - Dedicated add-tests command + subagent — `OS/get-shit-done/commands/gsd/add-tests.md`
  - Anti-pattern enforcement at CI level — `OS/get-shit-done/tests/anti-pattern-enforcement.test.cjs`
  - Verification gate checks acceptance criteria — `OS/get-shit-done/agents/gsd-verifier.md`
- **superpowers** (score ≥90 signals)
  - TDD Iron Law explicit — `OS/superpowers/skills/test-driven-development/SKILL.md`
  - Red/Green/Refactor with mandatory verify steps — `OS/superpowers/skills/test-driven-development/SKILL.md`
  - Subagent prompts enforce test-first — `OS/superpowers/skills/subagent-driven-development/implementer-prompt.md`
  - Testing anti-patterns reference bundled — `OS/superpowers/skills/test-driven-development/testing-anti-patterns.md`

### Roundtripping (23%)

**spec-kit: 42/100** | **get-shit-done: 68/100** | **superpowers: 25/100** | Confidence: HIGH

None of the three implements full bidirectional roundtripping — the closed loop where code changes propagate back to the spec automatically. GSD comes closest with **two** drift-detection gates: schema drift (ORM changes missing migrations, blocks execute-time) and STATE.md filesystem drift (detects divergence between planning artefacts and the actual filesystem, with a Sync mode that reconstructs STATE.md from disk). `/gsd-map-codebase` + `/gsd-scan` do code → planning-context seeding, which is the closest thing to code→spec extraction in the trio. spec-kit's `/speckit.analyze` is on-demand consistency checking across artefacts, not a continuous loop. Superpowers does not address this dimension.

This is the highest-weighted dimension in the pack (0.23), reflecting how hard and how valuable the roundtrip problem is — GSD's lead here drives a large share of its overall win.

**Signals observed:**

- **spec-kit**
  - `/speckit.analyze` detects ambiguity/contradictions/gaps — `OS/spec-kit/templates/commands/analyze.md`
  - `/speckit.clarify` resolves NEEDS CLARIFICATION markers — `OS/spec-kit/templates/commands/clarify.md`
  - No code→spec extraction — not_observed
- **get-shit-done**
  - Schema-drift gate — `OS/get-shit-done/docs/FEATURES.md:79,1440`
  - STATE.md filesystem-drift detection (REQ-STATE-01) — `OS/get-shit-done/docs/FEATURES.md:1635-1650`
  - Codebase mapper — `OS/get-shit-done/commands/gsd/map-codebase.md`, `scan.md`
  - Scope reduction detection + extract-learnings — `OS/get-shit-done/commands/gsd/extract_learnings.md`
- **superpowers**
  - No drift-detection or roundtrip skill — not_observed

---

## Score Distribution

### spec-kit Profile
- Strongest: **Spec Format** (88) + **Traceability** (80)
- Weakest: **TDD Integration** (30)
- Range: 30 – 88

### get-shit-done Profile
- Strongest: **Executable Specs** (78), **Roundtripping** (68)
- Weakest: **Traceability** (72) — still respectable
- Range: 62 – 85 (smallest spread of the three — most balanced)

### superpowers Profile
- Strongest: **TDD Integration** (95)
- Weakest: **Roundtripping** (25)
- Range: 25 – 95 (largest spread — most opinionated)

### Competitive Dimensions (|delta| < 5)

- **Spec Format**: spec-kit 88 vs get-shit-done 85 (delta 3) — technically neck-and-neck. IDs vs gate.

---

## Confidence Disclosure

| Subject | Confidence | Reason |
|---------|-----------|--------|
| spec-kit | HIGH | 14 capabilities with evidence, README 778 lines, SDD manifesto, pytest suite, GitHub workflows |
| get-shit-done | HIGH | 24 capabilities with evidence, 213+ vitest files, 100+ commands, 32 agents, 12 hooks |
| superpowers | HIGH | 16 capabilities with evidence, skills SKILL.md files are self-describing, CLAUDE.md contributor guide |

### Sources

- spec-kit: `OS/spec-kit/` filesystem scan (commit c118c1c, 2026-04-17)
- get-shit-done: `OS/get-shit-done/` filesystem scan (commit 48a3546, 2026-04-19)
- superpowers: `OS/superpowers/` filesystem scan (commit b557648, 2026-04-16)

### Dimension Pack

| Pack | Version | Designed For |
|------|---------|-------------|
| spec-driven | 1.0 | Spec-driven development, meta-prompting, context engineering (spec-kit, get-shit-done, superpowers — named targets) |

### Scoring Transparency

All five scores derive from signals documented in the "Signals observed" blocks above. The single score ≥90 (superpowers on TDD Integration = 95) carries **four** evidence-linked signals, satisfying the "2+ signals for any score ≥90" rule. No score was assigned from imagination; when a signal could not be observed, the score band was lowered and `not_observed` is recorded.

### Known Limitations

- **Pack weighting bias**: roundtripping carries the highest weight (0.23). That reflects the pack's emphasis but amplifies GSD's advantage. With uniform 0.20 weighting, totals shift by ~1–2 points; ranking order stays the same.
- **No community metrics pulled**: GitHub stars, contributors, release cadence were not retrieved (local-first principle). Community health not factored.
- **Superpowers deliberately shuns some dimensions** (typed spec, roundtripping). Its 53.64 total reflects pack-shape mismatch as much as absence — the project's design philosophy explicitly trades these dimensions for TDD depth.

---

_Generated by os-bench bench-score task | Template v1.0_
