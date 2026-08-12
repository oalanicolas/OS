# Absorption roadmap — harness-structure-8way

Target implied: um harness próprio (AIOX / gstack-like / sinkra) que precise de contexto e estrutura para trabalho complexo.

Ordem: **REUSE the pattern, do not vendor the repo.**

## Wave 0 — do not skip (P0)

1. **Pick the atom.** Skill *or* spec *or* employee. Default: Agent Skills (`SKILL.md`) + optional spec overlay.
2. **Listing budget as CI.** Cap description (60–100 chars) or SDO (trigger-only). Lint like `get-shit-done/scripts/lint-descriptions.cjs` / Hermes hardline.
3. **Bootstrap hook.** Copy the *idea* of `OS/superpowers/hooks/session-start`: one small skill body that says “invoke before acting.” Do not inject 59 playbooks.
4. **Ledger file.** Plan-scoped `progress.md`. Superpowers documented why: compaction amnesia.

## Wave 1 — process (P1)

| Port | From | Into |
|---|---|---|
| SDO writing-skills | `OS/superpowers/skills/writing-skills/SKILL.md` | skill authoring |
| SDD loop + breaker | `OS/superpowers/skills/subagent-driven-development/SKILL.md` | implement path |
| File briefs | same skill `scripts/task-brief` | dispatch |
| office-hours reframe | `OS/gstack/docs/skills.md` | before any spec |
| spec-kit constitution + gate | `OS/spec-kit/workflows/speckit/workflow.yml` | one-way doors |
| never compact user | `OS/hermes-agent/docs/micro-compaction.md` | compressor |

## Wave 2 — runtime (P1)

| Port | From | Into |
|---|---|---|
| Manifest-before-exec | `OS/openclaw/docs/plugins/architecture.md` | plugin loader |
| Exclusive memory slot | same | one brain |
| Identity split | `OS/openclaw/AGENTS.md` / `OS/clawd/AGENTS.md` | AGENTS≠SOUL≠USER |
| Catalog caps + warning | `OS/openclaw/docs/tools/skills.md` | system prompt |
| Host adapters | `OS/gstack/hosts/` | one source, N installs |
| requires.bins gating | openclaw frontmatter | hide unusable skills |

## Wave 3 — only if you have a fleet (P2)

| Port | From | Skip if |
|---|---|---|
| TEAM.md + CEO must-delegate | paperclip teams-catalog | single human |
| Budgets + board | `OS/paperclip/docs/companies/companies-spec.md` | no cost sharing |
| 7 adapters | `OS/paperclip/packages/adapters/` | one runtime |
| Party Mode (disagreement) | `OS/BMAD-METHOD/src/core-skills/bmad-party-mode/SKILL.md` | no design review need |

## Wave 4 — do not absorb

- gstack generated preamble as-is
- Domain skills into the process core (superpowers 94% reject)
- Auto-executing third-party bootstrap runbooks
- Chat history as handoff
- All 8 catalogs into one host (listing cap)
- This gsd-pi (living) as if it were gsd-pi (GAP-GSD-001)

## Suggested first milestone (one week)

A host-agnostic pack:

```
pack/
  hooks/session-start          # using-pack, <200 words
  skills/using-pack/SKILL.md
  skills/writing-skills/       # SDO
  skills/brainstorming/
  skills/writing-plans/
  skills/sdd/                  # ledger + breaker
  skills/tdd/
AGENTS.md                      # routing table only
```

Then, if needed, a spec overlay (`specify/plan/tasks`) and a plugin manifest. Company-sim last.
