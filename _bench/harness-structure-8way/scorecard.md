# Scorecard: harness-structure-8way

**Date:** 2026-08-12  
**Type:** nway (8 subjects)  
**Pack:** `harness-structure` (weights sum 1.00)  
**Method:** installed — filesystem scan of `OS/{subject}/`  
**Confidence overall:** HIGH (every cell has ≥2 evidence paths; every score ≥90 has ≥2 signals)

## Weighted totals

| Rank | Subject | Total | Dim wins |
|---:|---|---:|---:|
| 1 | **superpowers** | **85.74** | 3 |
| 2 | paperclip | 83.88 | 2 |
| 3 | gsd-pi | 83.16 | 0 |
| 4 | hermes-agent | 80.08 | 0 |
| 5 | gstack | 79.84 | 1 |
| 6 | openclaw | 78.20 | 2 |
| 7 | BMAD-METHOD | 78.04 | 0 |
| 8 | spec-kit | 69.52 | 0 |

Winner delta vs #2: **+1.86**. gsd-pi is the generalist: zero dimension wins, third overall.

## Dimensions

| Dimension | W | superpowers | gstack | gsd-pi | BMAD | paperclip | hermes | openclaw | spec-kit | Leader |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Skill System | 0.16 | **92** | 84 | 88 | 80 | 78 | 91 | 88 | 42 | superpowers |
| Squad Model | 0.14 | 78 | 72 | 82 | 90 | **94** | 62 | 58 | 48 | paperclip |
| Plugin Extensibility | 0.12 | 82 | 80 | 78 | 68 | 86 | 88 | **94** | 84 | openclaw |
| Context Architecture | 0.16 | 86 | 74 | 84 | 70 | 76 | 90 | **93** | 72 | openclaw |
| Complex-Work Spine | 0.16 | 90 | **91** | 90 | 88 | 84 | 78 | 70 | 90 | gstack |
| Gates & Discipline | 0.10 | **95** | 82 | 80 | 76 | 78 | 80 | 62 | 78 | superpowers |
| Handoff & State | 0.10 | **93** | 84 | 88 | 80 | 90 | 72 | 74 | 82 | superpowers |
| Governance | 0.06 | 55 | 62 | 60 | 60 | **92** | 70 | 84 | 68 | paperclip |

## Dimension analysis

### Skill System (16%) — superpowers 92

Bootstrap that *forces* invoke beats the largest catalog. Superpowers SessionStart injects `using-superpowers` (`OS/superpowers/hooks/session-start`) and SDO forbids workflow-in-description (`OS/superpowers/skills/writing-skills/SKILL.md`). Hermes is 1 pt behind on authoring hardline + 194 skills. spec-kit is the honest floor: it does not pretend to be Agent Skills (`OS/spec-kit/templates/commands/specify.md`).

### Squad Model (14%) — paperclip 94

Only paperclip has a hireable org (`TEAM.md` + CEO must-delegate). BMAD 90 is the other standing-roster (named personas + 4 Party modes). Everyone else fakes teams with sequential specialists or typed workers.

### Plugin Extensibility (12%) — openclaw 94

Manifest validated **before** executing plugin code (`OS/openclaw/docs/plugins/architecture.md`) plus exclusive memory/context-engine slots. spec-kit 84 shows you can have a real extension system without SKILL.md. Superpowers is a process plugin, not a runtime.

### Context Architecture (16%) — openclaw 93

20k/file + 60k total, identity split, skill *list* not bodies (`OS/openclaw/docs/tools/skills.md`). Hermes 90 for never-compacting the user. gstack 74 because the generated preamble is the expensive opposite of a tiny bootstrap.

### Complex-Work Spine (16%) — gstack 91

The only subject whose product *is* the factory sequence (`OS/gstack/docs/skills.md`: office-hours → autoplan → ship). Superpowers/gsd-pi/spec-kit all score 90 with complete spines of different kinds.

### Gates & Discipline (10%) — superpowers 95

TDD iron law + separate reviewer + 5-round breaker. No one else has the breaker. openclaw 62: Workshop gates *skills*, not implementation.

### Handoff & State (10%) — superpowers 93

`task-brief` / `review-package` exist because a 42k-char paste failed in production (`OS/superpowers/skills/subagent-driven-development/SKILL.md`). paperclip 90 is the issue-comment contract. gsd-pi 88 is continue.md + worktree leases.

### Governance (6%) — paperclip 92

Only company money + board. openclaw 84 is trust-tier install. Superpowers 55 is prompt discipline — by design.

## Score distribution

| Subject | Strongest | Weakest |
|---|---|---|
| superpowers | Gates 95 | Governance 55 |
| paperclip | Squad 94 | Context 76 / Skill 78 |
| gsd-pi | Spine 90 | Governance 60 |
| hermes-agent | Skill 91 / Context 90 | Squad 62 |
| gstack | Spine 91 | Governance 62 / Context 74 |
| openclaw | Plugin 94 / Context 93 | Squad 58 |
| BMAD-METHOD | Squad 90 | Plugin 68 / Context 70 |
| spec-kit | Spine 90 | Skill 42 / Squad 48 |

## Known limitations

- gsd-pi (living) is archived (README → open-gsd/gsd-pi). Scores are of the local tree.
- No GitHub stars in scoring (local-first).
- Full signal tables live in `scorecard.json`.
