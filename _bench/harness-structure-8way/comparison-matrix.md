# Comparison Matrix: harness-structure-8way

**Date:** 2026-08-12  
**Type:** nway  
**Pack:** harness-structure  
**Subjects:** superpowers · gstack · gsd-pi · BMAD-METHOD · paperclip · hermes-agent · openclaw · spec-kit

## Sources

Local clones only. Evidence paths are `OS/{subject}/...` as stored in `comparison-matrix.json`. No web metrics.

## Method

Capabilities were unioned from the 8 inventories, canonicalized, and routed onto the 8 pack dimensions. N-way cells are `yes | partial | no` (pairwise Forte/Parcial skipped per skeleton). 21 features across 8 categories.

## Inventory summary

| Subject | Files | SKILL.md | Last commit | Theory of control |
|---|---:|---:|---|---|
| superpowers | 179 | 14 | 2026-07-28 | Discipline plugin |
| gstack | 1177 | 59 | 2026-08-08 | Executable playbooks |
| gsd-pi | 3607 | 38 | 2026-05-22 (historical snapshot; bench now scores gsd-pi) | Milestone factory |
| BMAD-METHOD | 596 | 58 | 2026-08-11 | Agile personas + party |
| paperclip | 4519 | 52 | 2026-08-12 | Company-sim |
| hermes-agent | 8752 | 194 | 2026-08-12 | Catalog + runtime |
| openclaw | 31842 | 115 | 2026-08-12 | Personal-agent OS |
| spec-kit | 539 | 1 | 2026-08-12 | Spec-as-SoT (no skills) |

## Feature matrix (compressed)

Legend: **Y** yes · **P** partial · **N** no / n/a

### Skill System

| Feature | SP | GS | GSD | BM | PC | HE | OC | SK |
|---|---|---|---|---|---|---|---|---|
| SKILL.md unit | Y | Y | Y | Y | Y | Y | Y | N |
| Listing budget | Y | P | Y | P | P | Y | Y | N |
| Bootstrap force-invoke | Y | Y | P | P | P | P | P | N |
| Authoring tests | Y | P | P | Y | Y | Y | P | Y |

### Squad Model

| Feature | SP | GS | GSD | BM | PC | HE | OC | SK |
|---|---|---|---|---|---|---|---|---|
| Named persistent personas | P | P | P | Y | Y | N | N | N |
| Org / party composition | N | N | N | Y | Y | N | N | N |
| Independent-mind spawn | Y | P | Y | Y | Y | P | P | P |

### Plugin Extensibility

| Feature | SP | GS | GSD | BM | PC | HE | OC | SK |
|---|---|---|---|---|---|---|---|---|
| Manifest-first plugin | P | N | P | N | Y | Y | Y | Y |
| MCP | N | P | Y | N | Y | Y | Y | N |
| Multi-host / marketplace | Y | Y | P | P | Y | P | Y | Y |

### Context Architecture

| Feature | SP | GS | GSD | BM | PC | HE | OC | SK |
|---|---|---|---|---|---|---|---|---|
| Always-on vs on-demand | Y | P | Y | P | P | Y | Y | P |
| Identity file split | N | P | P | P | P | Y | Y | P |
| Anti-rot protocol | Y | Y | Y | P | Y | Y | Y | P |

### Spine / Gates / Handoff / Governance

| Feature | SP | GS | GSD | BM | PC | HE | OC | SK |
|---|---|---|---|---|---|---|---|---|
| Full intent→ship spine | Y | Y | Y | Y | P | P | P | Y |
| Artifacts as SoT | Y | Y | Y | Y | Y | P | P | Y |
| Separate reviewer | Y | Y | Y | Y | P | P | N | P |
| Breaker / TDD iron law | Y | P | P | P | P | P | N | P |
| File-path handoff | Y | Y | Y | Y | Y | P | P | Y |
| Worktree isolation | Y | P | Y | N | Y | N | N | P |
| Budgets + board | N | N | P | N | Y | P | N | N |
| Trust tiers | P | P | P | P | Y | P | Y | Y |

## Subject-only (field uniques)

| Subject | Unique | Evidence |
|---|---|---|
| superpowers | SessionStart bootstrap + 5-round breaker | `OS/superpowers/hooks/session-start` |
| gstack | Persistent browse daemon | `OS/gstack/ARCHITECTURE.md` |
| gsd-pi | Agent Skills *runtime* (not just a pack) | `OS/gsd-pi/packages/pi-coding-agent/src/core/skills.ts` |
| BMAD-METHOD | Party Mode 4-runtime room | `OS/BMAD-METHOD/src/core-skills/bmad-party-mode/SKILL.md` |
| paperclip | Company budgets + hire | `OS/paperclip/packages/teams-catalog/.../TEAM.md` |
| hermes-agent | Skill bundles + never-compact-user | `OS/hermes-agent/docs/micro-compaction.md` |
| openclaw | Exclusive memory/context-engine slots | `OS/openclaw/docs/plugins/architecture.md` |
| spec-kit | YAML `type:gate` workflow | `OS/spec-kit/workflows/speckit/workflow.yml` |

## Objective reading

There is no single “best harness.” The matrix splits cleanly:

- **Process:** superpowers, gstack, BMAD, spec-kit, gsd-pi
- **Runtime/platform:** openclaw, hermes, paperclip
- **Standing people:** only BMAD + paperclip
- **Money/governance:** only paperclip (openclaw has trust, not budgets)

spec-kit is not a weak skill system — it is a different atom. Scoring it on Skill System is supposed to be low.

## Next-depth paths

- Pair `superpowers` vs `gsd-pi` for SDD-vs-milestone execution.
- Pair `paperclip` vs `openclaw` for company vs employee.
- Pair `spec-kit` vs `superpowers` for spec-SoT vs skill-discipline.
