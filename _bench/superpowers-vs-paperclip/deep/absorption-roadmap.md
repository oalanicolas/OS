# Absorption roadmap — superpowers → paperclip (one way)

Paperclip absorbs process. Superpowers does **not** absorb the company.

## P1 — week 1

Ship a bundled catalog pack `paperclipai/bundled/software-development/superpowers-process`:

| Skill | Source |
|---|---|
| `using-pack` | `OS/superpowers/skills/using-superpowers/SKILL.md` |
| `writing-skills` (SDO) | `OS/superpowers/skills/writing-skills/SKILL.md` |
| `tdd` | `OS/superpowers/skills/test-driven-development/SKILL.md` |
| `sdd` | `OS/superpowers/skills/subagent-driven-development/SKILL.md` |

Add to Core Exec TEAM.md `requiredSkills` for CTO and senior-coder. CEO does **not** get SDD (CEO must not IC).

Heartbeat of CTO/QA: inject the `using-pack` **body** (Superpowers SessionStart pattern), not just the name.

## P1 — week 2

On every implementation issue:

1. Write `task-N-brief.md` as an attachment (extract from the plan/issue; do not paste history).
2. Implementer writes `task-N-report.md`.
3. `review-package` (diff file) goes to the QA agent.
4. Five-round cap; park-with-ruling on the issue comment.

Scripts can stay shell, invoked by the adapter workspace.

## P2

Map Superpowers brainstorm → Paperclip `request_confirmation` on a plan document before child implementation issues spawn.

## Do not port

- Postgres, org-chart, budgets, adapters → Superpowers
- MCP → Superpowers core
- Paperclip plugin UI → Superpowers

## Done when

A CTO agent on a coding task invokes TDD before code, attaches a brief file, and cannot close `in_review` without a reviewer verdict or a parked ruling. CEO still never opens the editor.
