# Comparison Matrix: spec-kit vs get-shit-done vs superpowers

**Date:** 2026-04-19
**Comparison type:** n-way (3 subjects)
**Dimension pack:** `spec-driven` (5 dimensions, weights sum 1.00)
**Slug:** spec-driven-3way

---

## Sources

| Subject | Path | Web source | Confidence |
|---------|------|------------|------------|
| spec-kit | `OS/spec-kit/` | https://github.com/github/spec-kit | HIGH |
| get-shit-done | `OS/get-shit-done/` | https://github.com/gsd-build/get-shit-done | HIGH |
| superpowers | `OS/superpowers/` | https://github.com/obra/superpowers | HIGH |

## Method

Filesystem scan of each subject plus targeted reads of manifestos, template files, command definitions, hook source, and test directories. Each feature cell cites at least one evidence path in `OS/{subject}/` or is explicitly marked `no`. No capability without an evidence path was included. The three projects all publish themselves with the "spec-driven" vocabulary, but each occupies a distinct position, so the matrix groups features by `spec-driven` pack dimension + three extra categories (Subagent Orchestration, Context Engineering, Harness Integration) that disambiguate what each project actually does differently.

---

## Inventory Summary

| Metric | spec-kit | get-shit-done | superpowers |
|--------|---------:|--------------:|------------:|
| LOC (py/ts/js/md/sh) | 51,903 | 146,206 | 21,078 |
| Files | 262 | 808 | 142 |
| README lines | 778 | 928 | 198 |
| Last commit | 2026-04-17 | 2026-04-19 | 2026-04-16 |
| Primary language | Python | JS/TS | Markdown (skills) |
| Distribution | uv tool / uvx | npm (npx) | Claude Code Official Marketplace + per-harness plugins |
| Harness count | 12+ | 14+ | 6 |
| Subagents | 0 dedicated | 32 | 2–3 (impl + spec reviewer + code-quality reviewer) |
| Runtime hooks | 4 hook events | 12 hooks | 1 hook (session-start) |
| Tests | 13 pytest files | 213+ vitest files | 6 test dirs |

---

## Feature Matrix

### Category: Spec Format

| Feature | spec-kit | get-shit-done | superpowers |
|---------|----------|---------------|-------------|
| Structured spec template with typed sections | yes — US#/FR-###/SC-###, Edge Cases, Assumptions, Key Entities | yes — Goal, Background, Requirements (Current/Target/Acceptance), Boundaries, Constraints, Ambiguity Report | **no** — spec emerges from brainstorming conversation as a design doc, no schema |
| Requirement IDs | **yes** — FR-###/SC-###/US# referenced downstream | partial — SPEC.md numbers requirements; REQ-*-## style in some references, not canonically stable | no — no ID scheme |
| Mandatory sections enforced by command | yes — checklist validation in `/speckit.specify` | yes — ambiguity gate ≤0.20 in `/gsd-spec-phase` | partial — `writing-plans` enforces "No placeholders" rule at plan level, not spec level |
| Machine-readable schema | partial — YAML frontmatter on commands | partial — TS SDK types for some artefacts | no — markdown-only |

**Leaders:** spec-kit (canonical IDs) + get-shit-done (ambiguity-scored gate). Superpowers deliberately has no typed spec artefact — Jesse's design favours design-from-dialogue.

### Category: Traceability

| Feature | spec-kit | get-shit-done | superpowers |
|---------|----------|---------------|-------------|
| Spec → plan ID references | yes — plan.md references FR-### and US# | yes — plan-phase reads SPEC.md as locked scope | partial — plans reference brainstorming doc informally |
| Plan → tasks ID references | **yes** — tasks grouped by US# with [Story] tag | yes — executor-ready plan tied to SPEC requirements | partial — bite-sized tasks reference exact files but no IDs |
| Test ↔ requirement mapping | partial — tests OPTIONAL unless requested (`tasks-template.md:11`) | partial — verification reports + requirements-coverage gate | **yes** — TDD enforcement means every behaviour has a test; tests ARE the link |
| Export to external tracker | **yes** — `/speckit.taskstoissues` exports to GitHub Issues | no | no |

**Leaders:** spec-kit dominates on stable IDs + external export; superpowers wins test↔req mapping via TDD enforcement.

### Category: Executable Specs

| Feature | spec-kit | get-shit-done | superpowers |
|---------|----------|---------------|-------------|
| Spec → scaffolding (plan, data-model, contracts) | **yes** — `/speckit.plan` emits plan + research + data-model + quickstart + contracts/ | yes — plan-phase emits executor-ready plan with gates and rollback | partial — `/write-plan` emits task plan only (no data-model/contracts) |
| Spec → failing-test auto-scaffold | no | no (acceptance = checkboxes, not tests) | partial — TDD skill mandates implementer writes failing test FIRST; scaffolding is manual but the workflow enforces it |
| Continuous consistency validation | yes — `/speckit.analyze` + `/speckit.clarify` loop | yes — requirements-coverage gate + cross-phase regression gate + scope-reduction detection | partial — two-stage review runs per task, not per spec |
| Implementation command | yes — `/speckit.implement` | yes — `/gsd-execute-phase` + `/gsd-autonomous` | yes — `/execute-plan` + subagent-driven-development |

**Leaders:** spec-kit produces the widest scaffolding surface (data-model.md + contracts/ + quickstart.md). GSD has the deepest gate coverage. Superpowers ties failing-test-first to execution.

### Category: TDD Integration

| Feature | spec-kit | get-shit-done | superpowers |
|---------|----------|---------------|-------------|
| TDD as enforced law | **no** — tasks-template.md makes tests OPTIONAL | partial — documented in references/tdd.md; enforcement via verification gate, not red-green | **yes** — Iron Law: "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"; delete code written before test |
| Red/Green/Refactor cycle | no | partial — referenced in tdd.md; not structurally enforced | **yes** — RED → Verify RED (mandatory) → GREEN → Verify GREEN → REFACTOR |
| Subagents enforce TDD | no | partial — executor reads tdd.md; add-tests subagent exists | **yes** — fresh subagent per task; spec-reviewer validates test-first |
| Anti-patterns reference | no | yes — planner-antipatterns.md, universal-anti-patterns.md + anti-pattern-enforcement test | yes — testing-anti-patterns.md bundled with TDD skill |

**Leader:** superpowers, by a large margin. Its entire methodology is anchored on TDD enforcement.

### Category: Roundtripping

| Feature | spec-kit | get-shit-done | superpowers |
|---------|----------|---------------|-------------|
| Code → spec extraction | no | partial — `/gsd-map-codebase` + `/gsd-scan` seed planning from existing code (does NOT emit SPEC.md) | no |
| Drift detection (spec ↔ impl) | partial — `/speckit.analyze` on demand | **yes** — schema-drift (ORM vs migrations) + STATE.md filesystem-drift gate blocks execute-time | no |
| Spec update from code change | no | partial — extract-learnings + STATE.md sync from disk | no |
| Bidirectional link in artefacts | partial — FR-###/SC-### create one-way link | partial — claim-provenance tagging + IDs in verification reports | no |

**Leader:** get-shit-done. Only GSD has real execute-time drift gates. All three projects leave the full spec↔code roundtrip unimplemented — it remains the hardest problem in the space.

### Category: Subagent Orchestration (extra)

| Feature | spec-kit | get-shit-done | superpowers |
|---------|----------|---------------|-------------|
| Subagent count | 0 dedicated | **32** | 2–3 + dispatching-parallel-agents skill |
| Two-stage review | no | yes — plan-check + verify-work + code-review gates | **yes** — explicit spec-reviewer THEN code-quality-reviewer per task |

**Leaders:** GSD for breadth (32 specialised roles), superpowers for the strict ordering of the review pipeline.

### Category: Context Engineering (extra)

| Feature | spec-kit | get-shit-done | superpowers |
|---------|----------|---------------|-------------|
| Context-rot mitigation | partial — air-gapped bundle | **yes** — context-monitor hook + Nyquist auditor + context-budget reference (explicit raison d'être) | partial — fresh subagent per task keeps context clean |
| Runtime hook surface | 4 events (before/after_specify, before/after_plan) | **12 hooks** | 1 hook (session-start) |

**Leader:** get-shit-done, uncontested.

### Category: Harness Integration (extra)

| Feature | spec-kit | get-shit-done | superpowers |
|---------|----------|---------------|-------------|
| Harnesses supported | 12+ | **14+** | 6 |
| Distribution channel | uv tool / uvx (PyPI is explicitly unofficial) | npm `get-shit-done-cc` via npx | **Claude Code Official Marketplace** + per-harness |

**Leader:** GSD for breadth; superpowers for being in Anthropic's official marketplace.

---

## Equivalence Summary

| Level | What counts here |
|-------|------------------|
| Strong parity across all three | "Implementation command" (all three have a `/execute` equivalent) |
| Strong parity on two | Spec-kit ↔ GSD on "Structured spec template", "Mandatory sections enforced", "Spec → plan ID references"; GSD ↔ superpowers on "Subagents enforce review ordering" |
| Solo leader features | spec-kit: tasks→issues export, SDD manifesto, Constitution with plan-time gates. GSD: ambiguity-scored gate, context-monitor, schema drift, STATE.md drift, 32 subagents, scope-reduction detection, UI/AI SPEC contracts. Superpowers: TDD Iron Law, skill auto-triggering, two-stage review ordering, official Anthropic marketplace. |

---

## spec-kit–Only Capabilities

| # | Capability | Category | Evidence |
|---|-----------|----------|----------|
| 1 | SDD manifesto (412 lines) | core | `OS/spec-kit/spec-driven.md` |
| 2 | Tasks → GitHub Issues export | integration | `OS/spec-kit/templates/commands/taskstoissues.md` |
| 3 | Constitution file with plan-time gates | governance | `OS/spec-kit/templates/constitution-template.md` |
| 4 | Air-gapped wheel asset bundling | ux | `OS/spec-kit/pyproject.toml` (hatch `force-include`) |

## get-shit-done–Only Capabilities

| # | Capability | Category | Evidence |
|---|-----------|----------|----------|
| 1 | Ambiguity-scored Socratic spec gate (gate ≤0.20) | core | `OS/get-shit-done/get-shit-done/workflows/spec-phase.md` |
| 2 | Context-monitor hook + Nyquist auditor | governance | `OS/get-shit-done/hooks/gsd-context-monitor.js`, `agents/gsd-nyquist-auditor.md` |
| 3 | Schema-drift detection + STATE.md filesystem-drift | governance | `OS/get-shit-done/docs/FEATURES.md:79,1440,1635-1650` |
| 4 | 32 specialised subagents | core | `OS/get-shit-done/agents/` |
| 5 | Scope-reduction detection | governance | `OS/get-shit-done/docs/FEATURES.md` |
| 6 | UI-SPEC + AI-SPEC dedicated contracts | core | `OS/get-shit-done/get-shit-done/templates/UI-SPEC.md`, `AI-SPEC.md` |
| 7 | Spike / sketch exploration (HTML mockups) | extensibility | `OS/get-shit-done/commands/gsd/spike.md`, `sketch.md` |
| 8 | Extract-learnings global store | extensibility | `OS/get-shit-done/commands/gsd/extract_learnings.md` |
| 9 | Cross-AI peer review / execution delegation | integration | `OS/get-shit-done/docs/FEATURES.md` |

## superpowers–Only Capabilities

| # | Capability | Category | Evidence |
|---|-----------|----------|----------|
| 1 | TDD Iron Law (delete code without failing test first) | core | `OS/superpowers/skills/test-driven-development/SKILL.md` |
| 2 | Skill auto-triggering via session-start hook | core | `OS/superpowers/hooks/session-start/`, `skills/using-superpowers/` |
| 3 | Two-stage review (spec-reviewer → code-quality-reviewer) per task | core | `OS/superpowers/skills/subagent-driven-development/spec-reviewer-prompt.md` |
| 4 | Zero-dependency plugin by design | governance | `OS/superpowers/CLAUDE.md` |
| 5 | Claude Code Official Marketplace distribution | integration | `OS/superpowers/README.md:32-40` |
| 6 | Testing-anti-patterns reference bundled with TDD skill | core | `OS/superpowers/skills/test-driven-development/testing-anti-patterns.md` |

---

## Objective Reading

### spec-kit Strengths (PT-BR)

spec-kit é o único dos três com um **manifesto formal de SDD** (`spec-driven.md`) e a convenção de IDs canônicos `FR-###`/`SC-###`/`US#` que sobrevivem até a fase de tasks e podem ser exportados como GitHub Issues via `/speckit.taskstoissues`. A pipeline `/speckit.specify` → `plan` → `tasks` → `implement` → `analyze` produz o mais amplo conjunto de artefatos derivados (spec + plan + research.md + data-model.md + quickstart.md + contracts/). O arquivo `constitution.md` introduz gates no momento do `plan`, e o wheel bundling torna o install air-gapped — útil em ambientes enterprise. É a opção mais "engenharia-clássica-de-requisitos" do trio.

### spec-kit Strengths (EN)

spec-kit is the only one of the three shipping a **formal SDD manifesto** (`spec-driven.md`) and canonical ID conventions (`FR-###`/`SC-###`/`US#`) that survive through the tasks stage and can be exported as GitHub Issues via `/speckit.taskstoissues`. The `/speckit.specify → plan → tasks → implement → analyze` pipeline produces the widest set of derived artefacts (spec + plan + research + data-model + quickstart + contracts/). The `constitution.md` file introduces plan-time gates, and wheel bundling makes the install air-gapped — valuable in enterprise. It is the trio's most "classic-requirements-engineering" option.

### get-shit-done Strengths (PT-BR)

GSD trata **context rot como o problema central** e é o único com um hook ativo (`gsd-context-monitor.js`) + agente dedicado (Nyquist auditor) para compressão de contexto. A fase de spec é a única do trio com um **gate quantitativo** (score de ambiguidade ≤0.20 ponderado em 4 dimensões) que bloqueia a escrita de SPEC.md se os requisitos estiverem vagos. Drift detection acontece em dois planos: **schema drift** (ORM vs migrações) e **STATE.md drift** (SPEC/plano vs filesystem real). Com 32 subagentes, 12 hooks, SDK TypeScript e suporte a 14+ harnesses, é o mais abrangente em superfície. Também leva a governança mais a sério: size-budget enforcement, scope-reduction detection, security gate, claim provenance.

### get-shit-done Strengths (EN)

GSD treats **context rot as THE core problem** and is the only project with an active hook (`gsd-context-monitor.js`) + dedicated agent (Nyquist auditor) for context compression. The spec phase is the only one in the trio with a **quantitative gate** (ambiguity score ≤0.20 weighted across 4 dimensions) that blocks SPEC.md writing if requirements are vague. Drift detection operates on two planes: **schema drift** (ORM vs migrations) and **STATE.md drift** (SPEC/plan vs actual filesystem). With 32 subagents, 12 hooks, a TypeScript SDK, and support for 14+ harnesses, it has the broadest surface. Governance is deliberate: size-budget enforcement, scope-reduction detection, security gate, claim provenance tagging.

### superpowers Strengths (PT-BR)

Superpowers faz uma coisa e faz sem concessões: **TDD red/green enforcement via subagents**. A "Iron Law" literal diz "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST" e "código escrito antes do teste — deleta e recomeça". O review-loop é o mais estrito do trio: spec-compliance reviewer ANTES do code-quality reviewer, cada um em um subagente separado, cada task executada por um subagente fresh para isolar contexto. Não há artefato de spec estruturado — o spec emerge da fase de brainstorming. Skills **auto-ativam** (hook `session-start`), então o usuário não precisa lembrar de invocar a metodologia. Distribuído no marketplace oficial da Anthropic. Zero dependências runtime por design.

### superpowers Strengths (EN)

Superpowers does one thing and does it without concessions: **red/green TDD enforcement via subagents**. The literal "Iron Law" reads "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST" and "code written before the test — delete and start over". The review loop is the strictest of the three: a spec-compliance reviewer BEFORE a code-quality reviewer, each in its own subagent, every task implemented by a fresh subagent to isolate context. There is no structured spec artefact — the spec emerges from brainstorming. Skills **auto-trigger** via the `session-start` hook, so the user doesn't have to remember to invoke the methodology. Distributed through Anthropic's official Claude Code marketplace. Zero runtime dependencies by design.

### Key Differentiators (the "pick-one" summary)

- **spec-kit** = *"from spec to code" as GitHub methodology* — the manifesto, the IDs, the pipeline, the GH-Issues bridge.
- **get-shit-done** = *"from spec to code" while defending against context rot* — ambiguity-scored gate + context monitor + Nyquist + drift detection.
- **superpowers** = *"from spec to code" via red/green TDD and subagent reviews* — TDD as the Iron Law, auto-triggering skills, two-stage per-task review.

### Areas of Parity

All three ship a runnable execute command (`/speckit.implement`, `/gsd-execute-phase`, `/execute-plan`). All three support multiple coding harnesses (spec-kit 12+, GSD 14+, superpowers 6). All three explicitly treat plan as a separate artefact from spec. None of the three solves the hard problem: continuous bidirectional spec↔code roundtripping. GSD is closest via its drift-detection gates.

---

## Method Disclosure

- **Comparison date:** 2026-04-19
- **Dimension pack:** `spec-driven` v1.0 (5 canonical dimensions: spec_format 0.20, traceability 0.20, executable_specs 0.22, tdd_integration 0.15, roundtripping 0.23) + 3 extra descriptive categories (Subagent Orchestration, Context Engineering, Harness Integration) used only for matrix framing, not for scoring.
- **Items compared:** 24 features across 8 categories.
- **Data sources:**
  - spec-kit: filesystem scan of `OS/spec-kit/` (commit `c118c1c`) + README + spec-driven.md + templates/commands/*.md.
  - get-shit-done: filesystem scan of `OS/get-shit-done/` (commit `48a3546`) + README + docs/FEATURES.md + workflows/spec-phase.md + agents/.
  - superpowers: filesystem scan of `OS/superpowers/` (commit `b557648`) + README + CLAUDE.md + skills/.

---

_Generated by os-bench bench-matrix task | Template v1.0_
