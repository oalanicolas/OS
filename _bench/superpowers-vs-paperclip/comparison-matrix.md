# Comparison Matrix: superpowers vs paperclip

**Date:** 2026-08-12 · **Type:** pair · **Pack:** harness-structure  
**Sources:** `OS/superpowers/`, `OS/paperclip/` (local).  
**Method:** 21 features from the parent 8-way, classified Forte / Parcial / Sem_Equiv.

## Inventory summary

| | superpowers | paperclip |
|---|---|---|
| Atom | process skill + hook | company (org + issues + adapters) |
| Files | 179 | 4519 |
| SKILL.md | 14 | 52 |
| Last commit | 2026-07-28 | 2026-08-12 |
| License | MIT | MIT |

## Summary counts

| Class | N |
|---|---:|
| Forte (5/5) | 6 |
| Parcial (3/5) | 11 |
| Sem_Equiv (1/5) | 4 |
| superpowers-only | 1 |
| paperclip-only | 3 |
| **Total** | **21** |

## Matrix

| Category | Feature | superpowers | paperclip | Eq |
|---|---|---|---|---|
| Skill | SKILL.md unit | 14 process skills | catalog bundled/optional | Forte |
| Skill | Listing budget | SDO trigger-only | catalog, no cap product | Parcial |
| Skill | Bootstrap force-invoke | SessionStart body | heartbeat names a skill | Parcial |
| Skill | Authoring tests | pressure scenarios | catalog-builder tests | Parcial |
| Squad | Persistent personas | implementer/reviewer | CEO/CTO/QA | Parcial |
| Squad | Org + hire | no | TEAM.md + hire | Sem_Equiv |
| Squad | Independent spawn | fresh subagent | adapters/workspaces | Forte |
| Plugin | Manifest-first | plugin.json pack | PLUGIN_SPEC runtime | Parcial |
| Plugin | MCP | no | yes | Sem_Equiv |
| Plugin | Multi-host | 6 coding hosts | 7 runtime adapters | Parcial |
| Context | Always-on split | one bootstrap body | heartbeat/issue | Parcial |
| Context | Identity split | host files | collapsed AGENTS.md | Parcial |
| Context | Anti-rot | ledger + briefs | issue comments | Forte |
| Spine | Full SDLC | brainstorm→SDD→finish | issue tree + pipelines | Parcial |
| Spine | Artifacts as SoT | plans + ledger | issues + attachments | Forte |
| Gates | Separate reviewer | task + branch review | QA agent | Parcial |
| Gates | Breaker / TDD | 5-round + iron law | no | Sem_Equiv |
| Handoff | File-path handoff | task-brief scripts | child-issue contract | Forte |
| Handoff | Isolation | git worktrees | execution workspaces | Forte |
| Gov | Budgets + board | no | yes | Sem_Equiv |
| Gov | Trust object | domain-skill reject | plugin capabilities | Parcial |

## superpowers-only

- Fix-loop breaker + TDD iron law — `OS/superpowers/skills/test-driven-development/SKILL.md`

## paperclip-only

- Org-chart + hire — `OS/paperclip/packages/teams-catalog/.../TEAM.md`
- MCP server — `OS/paperclip/packages/mcp-server/`
- Budgets + board — `OS/paperclip/docs/companies/companies-spec.md`

## Objective reading

11/21 features are **Parcial**: both sides “have a thing” at different depth. The 4 Sem_Equiv rows are the real product boundary. Superpowers is a methodology you install into a host. Paperclip is a company you run hosts inside of.
