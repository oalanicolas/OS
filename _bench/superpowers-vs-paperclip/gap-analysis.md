# Gap Analysis: superpowers vs paperclip

**Date:** 2026-08-12 · **Bidirectional** · **Confidence:** HIGH

| | superpowers (A) | paperclip (B) |
|---|---:|---:|
| Gaps | 4 | 4 |
| P0 | 0 | 0 |
| P1 | 0 | **3** |
| P2 | 1 | 1 |
| P3 | 3 | 0 |

A’s gaps are mostly **out of scope** (org, money, MCP). B’s gaps are **portable process** (bootstrap, TDD/breaker, file briefs).

## What Paperclip should steal from Superpowers (P1)

| ID | Gap | Evidence | Action |
|---|---|---|---|
| GAP-B-001 | TDD + 5-round breaker | `OS/superpowers/skills/subagent-driven-development/SKILL.md` | requiredSkills pack, not core |
| GAP-B-002 | SessionStart bootstrap + SDO | `OS/superpowers/hooks/session-start` | heartbeat injects a force-invoke body |
| GAP-B-003 | task-brief / review-package | same SDD skill | attach brief+diff files on the issue |

GAP-B-004 (methodology spine) is P2 — pipelines already move cases; the missing piece is signed-off design then a junior-proof plan.

## What Superpowers should *not* steal from Paperclip (P3)

| ID | Gap | Why not |
|---|---|---|
| GAP-A-001 | Org + hire | Breaks the process-plugin product |
| GAP-A-002 | Budgets + board | Same |
| GAP-A-003 | MCP / plugin VM | Violates zero-dep |

GAP-A-004 (cross-runtime adapters) is P2 documentation only: keep porting to *hosts*, do not become an orchestrator of employees.

## Action items

1. **P1 / Paperclip:** ship a Superpowers-shaped requiredSkills pack (using-pack, TDD, SDD, SDO).
2. **P1 / Paperclip:** bootstrap body on CEO/CTO heartbeat, not just “follow the paperclip skill.”
3. **P1 / Paperclip:** issue attachments carry brief + review-package paths.
4. **P3 / Superpowers:** do not add org/budgets to core.

Full records: `gap-analysis.json`.
