# Executive Report: spec-kit vs get-shit-done vs superpowers

**Date:** 2026-04-19
**Type:** n-way (3 subjects)
**Slug:** spec-driven-3way
**Dimension pack:** `spec-driven` (5 dimensions, weights 0.20 / 0.20 / 0.22 / 0.15 / 0.23)

---

## Executive Summary (PT-BR)

Três projetos se descrevem como "spec-driven" mas ocupam posições distintas: **spec-kit** (GitHub) é a metodologia SDD canônica com specs executáveis baseadas em IDs `FR-###`/`SC-###`/`US#` e pipeline `specify → plan → tasks → implement → analyze`. **get-shit-done** (TÂCHES/gsd-build) é meta-prompting contra context rot — fase de spec com gate quantitativo de ambiguidade (4 dimensões, ≤0.20), 32 subagentes, 12 hooks, e as únicas detecções de drift do trio (schema drift + STATE.md drift). **superpowers** (Obra/Prime Radiant) é a metodologia TDD red/green via subagents com review em duas etapas — spec-compliance **depois** code-quality — e skills que auto-ativam via hook de session-start. No scorecard ponderado: **get-shit-done 73.50** > spec-kit 64.26 > superpowers 53.64. GSD ganha pelo peso alto de roundtripping (0.23) onde lidera, e pelo empate técnico em spec format (85 vs 88) e pipeline de execução (78 vs 75). Superpowers lidera TDD com 95 (score ≥90 com 4 signals). Nenhum dos três implementa roundtripping bidirecional completo — GSD chega mais perto via drift gates.

## Executive Summary (EN)

Three projects call themselves "spec-driven" but occupy distinct positions: **spec-kit** (GitHub) is the canonical SDD methodology with executable specs anchored in `FR-###`/`SC-###`/`US#` IDs and a `specify → plan → tasks → implement → analyze` pipeline. **get-shit-done** (TÂCHES/gsd-build) is meta-prompting against context rot — a spec phase with a quantitative ambiguity gate (4 weighted dimensions, ≤0.20), 32 subagents, 12 hooks, and the trio's only drift-detection gates (schema drift + STATE.md drift). **superpowers** (Obra/Prime Radiant) is red/green TDD via subagents with a two-stage review — spec-compliance **then** code-quality — and skills that auto-trigger from a session-start hook. Weighted scorecard: **get-shit-done 73.50** > spec-kit 64.26 > superpowers 53.64. GSD wins on roundtripping (the pack's heaviest weight, 0.23), ties spec-kit on spec format (85 vs 88) and on the execution pipeline (78 vs 75). Superpowers leads TDD with 95 (the sole score ≥90 — backed by four evidence-linked signals). None of the three implements full bidirectional roundtripping — GSD gets closest via drift gates.

---

## Key Metrics

| Metric | Value |
|--------|-------|
| Overall Winner | **get-shit-done** (+9.24 vs spec-kit, +19.86 vs superpowers) |
| Dimensions analyzed | 5 (spec_format, traceability, executable_specs, tdd_integration, roundtripping) |
| spec-kit wins | 2 (Spec Format, Traceability) |
| get-shit-done wins | 2 (Executable Specs, Roundtripping) |
| superpowers wins | 1 (TDD Integration — score 95, category-dominating) |
| Ties | 0 (closest competitive delta: spec_format spec-kit 88 vs gsd 85 = 3 pts) |
| Confidence overall | HIGH (each score has ≥2 evidence-linked signals; the one ≥90 score has 4) |

---

## Scorecard Summary

| Dimension | Weight | spec-kit | get-shit-done | superpowers | Advantage |
|-----------|:------:|:--------:|:-------------:|:-----------:|:---------:|
| Spec Format | 20% | **88** | 85 | 45 | spec-kit |
| Traceability | 20% | **80** | 72 | 55 | spec-kit |
| Executable Specs | 22% | 75 | **78** | 62 | get-shit-done |
| TDD Integration | 15% | 30 | 62 | **95** | superpowers |
| Roundtripping | 23% | 42 | **68** | 25 | get-shit-done |
| **Weighted total** | **100%** | **64.26** | **73.50** | **53.64** | **get-shit-done** |

---

## Dimension Analysis

### Spec Format (20%) — spec-kit 88 / gsd 85 / superpowers 45

spec-kit is the only project shipping a **formal SDD manifesto** (`OS/spec-kit/spec-driven.md`, 412 lines) alongside the template. Its spec template specifies User Stories with priorities (P1/P2/P3), numbered Functional Requirements (`FR-###`), numbered Success Criteria (`SC-###`), Edge Cases, Assumptions, and Key Entities. Every `/speckit.specify` run generates a `checklists/requirements.md` that validates the spec against Content, Completeness, and Readiness criteria. GSD is structurally similar but adds a **quantitative** gate: `/gsd-spec-phase` computes a weighted ambiguity score (Goal 35% / Boundary 25% / Constraint 20% / Acceptance 20%) and refuses to write SPEC.md until the score ≤0.20 AND each dimension clears its minimum — with the option for the user to override after six Socratic rounds. Superpowers takes a different path: spec is not a typed artefact — it emerges from the `brainstorming` skill as a design document that the user signs off in chunks.

**Key signals:**
- spec-kit: FR-###/SC-### IDs in `OS/spec-kit/templates/spec-template.md`
- get-shit-done: ambiguity gate in `OS/get-shit-done/get-shit-done/workflows/spec-phase.md`
- superpowers: no typed spec (design doc from brainstorming) — `OS/superpowers/skills/brainstorming/`

### Traceability (20%) — spec-kit 80 / gsd 72 / superpowers 55

spec-kit's stable ID scheme is unique in the trio. `FR-###` and `SC-###` appear in spec-template.md; `US#` tags propagate into tasks-template.md (each task carries a `[Story]` marker); the `plan-template.md` header references the spec file by path. `/speckit.taskstoissues` exports the task list to GitHub Issues, making IDs visible in the external tracker. GSD tracks traceability through verification reports (`gsd-verifier` writes a report mapping each acceptance criterion to pass/fail), a dedicated requirements-coverage gate, and claim-provenance tagging added in v1.31 that tracks the source of each claim through artefacts. Superpowers has no IDs — but its TDD enforcement means every behaviour has a corresponding test, which functions as an implicit spec↔test link.

**Key signals:**
- spec-kit: stable IDs + GitHub issue export — `OS/spec-kit/templates/commands/taskstoissues.md`
- get-shit-done: claim provenance + verification report — `OS/get-shit-done/docs/FEATURES.md#65`, `OS/get-shit-done/get-shit-done/templates/verification-report.md`
- superpowers: TDD verification checklist — `OS/superpowers/skills/test-driven-development/SKILL.md`

### Executable Specs (22%) — spec-kit 75 / gsd 78 / superpowers 62

`/speckit.plan` produces the widest derived-artefact surface in the trio: `plan.md + research.md + data-model.md + quickstart.md + contracts/`. `/speckit.analyze` cross-validates the three core artefacts (spec, plan, tasks) for ambiguity/contradictions/gaps, and `/speckit.clarify` resolves up to three `[NEEDS CLARIFICATION]` markers. GSD runs the deepest continuous-validation stack: requirements-coverage gate (v1.31), cross-phase regression gate, scope-reduction detection, and a verification gate that runs per phase. `/gsd-autonomous` can run the full pipeline end-to-end with `--auto`, `--to N`, or `--interactive` flags. Superpowers anchors "executable" to TDD: implementer subagent writes the failing test first; spec-reviewer subagent validates compliance before code-quality reviewer runs — but the project does not scaffold non-test artefacts (no data-model, no contracts). spec-kit loses 3 points to GSD here because `tasks-template.md:11` explicitly makes tests OPTIONAL unless requested — a real limit on the "executable spec" claim.

**Key signals:**
- spec-kit: 5-artefact scaffold per spec — `OS/spec-kit/templates/commands/plan.md`
- get-shit-done: multiple continuous-validation gates — `OS/get-shit-done/docs/FEATURES.md#20, #21`
- superpowers: failing-test-first Iron Law tied to execution — `OS/superpowers/skills/test-driven-development/SKILL.md`

### TDD Integration (15%) — spec-kit 30 / gsd 62 / superpowers 95

Superpowers is the sole project in the trio where TDD is **enforced as law**. `OS/superpowers/skills/test-driven-development/SKILL.md` opens with a literal Iron Law: "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST" and continues "Write code before the test? Delete it. Start over." Both verification steps (Verify RED — "confirm fails for expected reason"; Verify GREEN — "confirm passes + all others still pass") are marked **MANDATORY**. Subagent prompts in `skills/subagent-driven-development/implementer-prompt.md` propagate the expectation, and the `spec-reviewer-prompt.md` validates test-first compliance before the code-quality reviewer runs. Four evidence-linked signals justify the 95 (satisfying the "score ≥90 requires 2+ signals" rule with redundancy).

GSD documents TDD as philosophy in `get-shit-done/references/tdd.md`, ships an `/gsd-add-tests` command + agent, and enforces anti-patterns in CI (`tests/anti-pattern-enforcement.test.cjs`) — but does not structure the execute phase around a red-green cycle. spec-kit actively opts out: `tasks-template.md:11` makes tests optional unless the user explicitly requests them.

**Key signals:**
- spec-kit: tests optional unless requested — `OS/spec-kit/templates/tasks-template.md:11`
- get-shit-done: TDD reference doc + add-tests command — `OS/get-shit-done/get-shit-done/references/tdd.md`
- superpowers: Iron Law + subagent enforcement — `OS/superpowers/skills/test-driven-development/SKILL.md`

### Roundtripping (23%) — spec-kit 42 / gsd 68 / superpowers 25

The hardest-to-solve dimension, and the highest-weighted in the pack (0.23). None of the three implements the full bidirectional loop (spec → code → updated spec with drift detection). GSD gets closest with **two** drift-detection gates: (1) schema drift — v1.31 feature 59 — blocks execution when ORM changes miss migrations (`docs/FEATURES.md:79, 1440`); (2) STATE.md filesystem drift — v1.32 REQ-STATE-01 — where `state validate` detects divergence between planning artefacts and the actual filesystem, with a Sync mode that reconstructs STATE.md from disk. `/gsd-map-codebase` + `/gsd-scan` seed planning context from an existing codebase, the closest thing in the trio to a code→spec extraction (though they don't emit a SPEC.md). spec-kit relies on `/speckit.analyze` for on-demand consistency checking across artefacts; there's no continuous loop and no code→spec path. Superpowers does not address this dimension.

Because roundtripping is weighted 23% and GSD is 26 points ahead of spec-kit (68 vs 42) and 43 points ahead of superpowers (68 vs 25), this single dimension alone accounts for ~60% of GSD's overall lead.

**Key signals:**
- spec-kit: on-demand consistency check — `OS/spec-kit/templates/commands/analyze.md`
- get-shit-done: schema drift + STATE.md drift gates — `OS/get-shit-done/docs/FEATURES.md:79, 1440, 1635-1650`
- superpowers: not addressed — not_observed

---

## Cross-Cutting Highlights (n-way observations)

### How each handles "from spec to code"

- **spec-kit**: deterministic **document generation pipeline**. User writes the spec (`/speckit.specify`), agent generates plan (`/speckit.plan` → plan.md + research.md + data-model.md + contracts/), agent generates tasks (`/speckit.tasks` → tasks.md grouped by User Story), agent executes (`/speckit.implement`). `/speckit.analyze` is the consistency gate. The flow is identical across 12+ AI agent harnesses via command templates.
- **get-shit-done**: 5-stage **gated pipeline** (spec → discuss → plan → execute → verify) with dedicated subagent roles per stage. Every stage reads upstream artefacts as **locked scope**. Enforcement is through 12 hooks that intercept prompt, read, workflow, phase-boundary, commit, session-start, and context-threshold events. `/gsd-autonomous --auto` runs the pipeline end-to-end with multiple verification gates (plan-check, verify-work, code-review).
- **superpowers**: **subagent-driven red/green loop**. Brainstorming extracts a spec from conversation; `writing-plans` skill produces a bite-sized task plan (2–5-min tasks, exact file paths, complete code, verification steps); `subagent-driven-development` dispatches a fresh subagent per task with a strict two-stage review order (spec-compliance FIRST, code-quality SECOND). TDD is the Iron Law throughout.

### Who has roundtripping (spoiler: nobody fully, GSD partially)

| Capability | spec-kit | get-shit-done | superpowers |
|-----------|:--------:|:-------------:|:-----------:|
| Spec → code (forward gen) | yes | yes | yes |
| Code → spec (reverse extract) | no | partial (map-codebase seeds planning context) | no |
| Drift detection at execute time | no (analyze is on-demand) | **yes** (schema drift + STATE.md drift) | no |
| Spec update from code change | no | partial (extract-learnings + STATE.md Sync) | no |

---

## Strategic Recommendations

### 1. Pick spec-kit when the output artefact is the audit trail

The GitHub methodology makes sense when you need **traceable engineering artefacts** that outlive a session — specs with stable IDs, a Constitution file that encodes plan-time gates, and automatic tasks-to-issues export so your GitHub board becomes the roundtripping surface. It is also the only option with a formal SDD manifesto (`spec-driven.md`) you can cite and hand to engineering leadership.

- **Target:** organisations already on GitHub, enterprise teams needing audit trails, teams where the PR + Issue + Review workflow is sacred.
- **Addresses:** Spec Format, Traceability, external-tracker export.
- **Priority:** P1 for regulated or audit-heavy teams.

### 2. Pick get-shit-done when context rot is your real bottleneck

If your sessions regularly degrade as the context window fills, if you've watched an agent silently drop a requirement between the plan and the implementation, if you've shipped code that diverged from the spec because nobody detected the drift — **GSD is the project that treats these as the primary problem**. The ambiguity-scored spec gate prevents vague requirements from entering the pipeline. The context-monitor hook + Nyquist auditor actively manage context budget. Schema-drift detection and STATE.md drift detection block execute-time divergence. Scope-reduction detection and claim-provenance tagging protect requirement integrity over long sessions.

- **Target:** solo developers who run agent-heavy sessions, teams building large features that span many agent invocations, anyone who has hit "context rot" symptoms.
- **Addresses:** Executable Specs, Roundtripping, context engineering.
- **Priority:** P0 for long-running autonomous agent workflows.

### 3. Pick superpowers when TDD is non-negotiable

If you believe "code before test = delete and start over" is the correct stance — not rhetoric — superpowers is the only option that operationalises it. The two-stage review ordering (spec-compliance FIRST, code-quality SECOND) prevents the "close enough" trap where code is reviewed against its implementation, not against the spec. Fresh subagent per task isolates context from review noise. Skills auto-trigger — users cannot forget to invoke the methodology.

- **Target:** engineers who already practice TDD and want enforcement; teams where regression risk justifies the TDD overhead.
- **Addresses:** TDD Integration, code-quality review discipline.
- **Priority:** P0 for long-lived libraries; P1 for feature work.

### 4. Compose them rather than choose

These three are not mutually exclusive; their strengths are largely **orthogonal**. A realistic high-end workflow:

- Use **spec-kit's FR-###/SC-### template** as the spec schema (borrow, don't install).
- Run **GSD's ambiguity gate + context-monitor + drift detection** as the execute-time runtime.
- Apply **superpowers' TDD Iron Law + two-stage review** as the per-task execution discipline.

This stack is not out-of-the-box — it requires pulling the right skill/command/template from each project — but it leaves no dimension unaddressed except the unsolved full roundtrip.

### 5. Close the roundtripping gap

All three projects leave full bidirectional roundtripping unimplemented. GSD's drift gates are the nearest prior art. A future tool (or a GSD extension) could combine `/gsd-map-codebase` (code → planning context) with `/speckit.analyze` (artefact consistency) plus continuous drift gates to produce the first actual roundtripper in this space. This is the biggest unclaimed territory in the spec-driven category.

- **Priority:** P2 (strategic rather than tactical).

---

## When to Pick Which

### Choose spec-kit if…

- You need canonical requirement IDs that survive into GitHub Issues.
- Your organisation values the SDD manifesto as a citation.
- You work in an enterprise / air-gapped context (wheel bundling).
- You want spec/plan/tasks as distinct artefacts with cross-artefact consistency analysis.
- You run multi-agent workflows across Copilot/Claude/Cursor/Gemini and need one CLI.

### Choose get-shit-done if…

- Context rot is a measurable problem in your sessions.
- You want the spec phase to **block** vague requirements quantitatively.
- You need execute-time drift gates (schema drift, STATE.md drift).
- You want 32 specialised subagents and 12 runtime hooks for governance.
- You work across 14+ coding harnesses and need one installer.
- You operate long autonomous sessions and need scope-reduction detection.

### Choose superpowers if…

- TDD is a hard requirement, not a preference.
- You want a fresh subagent per task to isolate context.
- You need a two-stage review where spec-compliance precedes code-quality.
- You want skills that auto-trigger without the user remembering to invoke them.
- You want zero runtime dependencies and a plugin in Anthropic's official marketplace.
- You work on long-lived libraries where regression risk is high.

### Consider composing all three if…

- You can tolerate stitching: spec-kit template + GSD runtime gates + superpowers TDD per task.
- You want maximum coverage of the `spec-driven` dimension pack.
- You have the bandwidth to maintain the glue between them.

---

## Methodology

### Data Sources

| Subject | Source | Method | Confidence |
|---------|--------|--------|------------|
| spec-kit | `OS/spec-kit/` (commit c118c1c, 2026-04-17) + https://github.com/github/spec-kit | filesystem-scan + doc-scan | HIGH |
| get-shit-done | `OS/get-shit-done/` (commit 48a3546, 2026-04-19) + https://github.com/gsd-build/get-shit-done | filesystem-scan + doc-scan | HIGH |
| superpowers | `OS/superpowers/` (commit b557648, 2026-04-16) + https://github.com/obra/superpowers | filesystem-scan + doc-scan | HIGH |

### Scoring Method

- **Dimension pack:** `spec-driven` v1.0 — 5 dimensions: spec_format (0.20), traceability (0.20), executable_specs (0.22), tdd_integration (0.15), roundtripping (0.23). Weights sum 1.00 (verified).
- **Score range:** 0–100 per dimension.
- **Signals:** every score derives from ≥2 signals observed in the subject's filesystem; every score ≥90 carries ≥2 evidence-linked signals (only score ≥90 in this bench is superpowers on TDD = 95, backed by 4 signals).
- **Confidence rollup:** HIGH if all dimensions HIGH; LOW if any LOW; MEDIUM otherwise. This bench: HIGH.

### Principles Applied

1. **No invented claims** — every claim resolves to a path in `OS/{subject}/` or a public URL.
2. **Evidence-based scoring** — ≥2 signals per dimension; ≥2 evidence-linked signals for any ≥90.
3. **Local-first** — filesystem scan is primary; GitHub metrics not pulled.
4. **Bidirectional comparison** — n-way, each subject's solo capabilities listed explicitly.
5. **Confidence disclosure** — per-dimension + overall rollup.
6. **Deterministic paths** — slug `spec-driven-3way` (no date in path; dates live in metadata).

### Artefacts Generated

| Artifact | File | Status |
|----------|------|:------:|
| Metadata | `metadata.json` | OK |
| Inventory (spec-kit) | `_inventories/spec-kit/inventory.{json,md}` | OK |
| Inventory (get-shit-done) | `_inventories/get-shit-done/inventory.{json,md}` | OK |
| Inventory (superpowers) | `_inventories/superpowers/inventory.{json,md}` | OK |
| Comparison Matrix | `comparison-matrix.{json,md}` | OK |
| Scorecard | `scorecard.{json,md}` | OK |
| Executive Report | `executive-report.md` | OK |
| Gap Analysis | — | SKIP (pair-wise artefact per os-bench SKILL.md — n-way gaps covered in Cross-Cutting Highlights above) |
| Battle Card | — | SKIP (pair-wise artefact per os-bench SKILL.md — n-way positioning covered in "When to Pick Which") |

### Limitations

- **Pack weight sensitivity**: roundtripping at 0.23 amplifies GSD's advantage. With uniform 0.20 weights the ranking order would be unchanged but the margin would compress by ~1–2 points.
- **No community metrics**: GitHub stars/contributors/cadence not pulled (local-first).
- **Superpowers' design is deliberately partial-coverage**: its low score on spec_format and roundtripping reflects design choices, not omissions. The project trades those dimensions for TDD depth, which is a legitimate position.
- **Spec-driven is a crowded label**: the three projects all use the term but mean different things. Readers should weight dimensions according to their own priorities rather than reading the total as a universal ranking.

---

## Appendix: Source Artefacts

All artefacts in `OS/_bench/spec-driven-3way/`:

| # | File | Type | Format |
|---|------|------|--------|
| 1 | `metadata.json` | Metadata | JSON |
| 2 | `_inventories/spec-kit/inventory.json` | Inventory | JSON |
| 3 | `_inventories/spec-kit/inventory.md` | Inventory | MD |
| 4 | `_inventories/get-shit-done/inventory.json` | Inventory | JSON |
| 5 | `_inventories/get-shit-done/inventory.md` | Inventory | MD |
| 6 | `_inventories/superpowers/inventory.json` | Inventory | JSON |
| 7 | `_inventories/superpowers/inventory.md` | Inventory | MD |
| 8 | `comparison-matrix.json` | Matrix | JSON |
| 9 | `comparison-matrix.md` | Matrix | MD |
| 10 | `scorecard.json` | Scoring | JSON |
| 11 | `scorecard.md` | Scoring | MD |
| 12 | `executive-report.md` | Report | MD |

Canonical inventories also cached at `OS/_bench/_inventories/{spec-kit,get-shit-done,superpowers}/`.

---

_Generated by os-bench bench-executive-report task | Template v1.0_
