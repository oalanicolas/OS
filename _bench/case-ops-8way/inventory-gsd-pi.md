# Inventory: gsd-pi

**Generated:** 2026-08-12T20:00:00Z  
**Path:** `OS/gsd-pi/`  
**Supersedes:** gsd-2 (archived snapshot)  
**Stack:** pi-coding-agent, Node, native crates, optional web TUI  
**License:** MIT  
**Confidence:** HIGH

> Living GSD: local-first coding agent that plans, implements, verifies and tracks work via milestones, worktrees and an Agent Skills runtime.

## Metrics

- Files: 5409 · SKILL.md: 55 · release v1.15.0
- Last commit: `2026-08-12T02:55:19Z`
- Source: https://github.com/open-gsd/gsd-pi

## Capabilities

- **Agent Skills runtime** (core): 5-root skill load (bundled ~/.gsd, ~/.agents, .agents, Claude compat). Catalog injection; Skill tool loads bodies. — `OS/gsd-pi/packages/pi-coding-agent/src/core/skills.ts`, `OS/gsd-pi/docs/user-docs/skills.md`
- **Milestone artifact DAG** (core): .gsd/ PROJECT/REQUIREMENTS/DECISIONS/STATE + M/S/T checkbox SoT. — `OS/gsd-pi/gsd-orchestrator/SKILL.md`
- **Isolated typed subagents** (core): scout/planner/worker/reviewer; fresh context default. — `OS/gsd-pi/src/resources/agents/scout.md`, `OS/gsd-pi/docs/user-docs/subagents.md`
- **Headless orchestrator skill** (integration): metadata.openclaw.install.package is now gsd-pi; exit 0/1/10/11. — `OS/gsd-pi/gsd-orchestrator/SKILL.md`
- **Extension SDK + MCP** (extensibility): Bundled/community extensions plus first-party MCP. — `OS/gsd-pi/docs/extension-sdk/README.md`, `OS/gsd-pi/packages/mcp-server/`
- **File-path handoff** (core): continue.md contract for a stranger. — `OS/gsd-pi/src/resources/skills/handoff/SKILL.md`
- **Worktree isolation** (core): Implementation in isolated worktrees; reviewable main checkout. — `OS/gsd-pi/docs/dev/ADR-001-branchless-worktree-architecture.md`

## Limitations

- Still no SessionStart-class force-invoke (skill_discovery auto/suggest/off) — `OS/gsd-pi/docs/user-docs/skills.md`
- No company-sim / org-chart / token budgets — `OS/gsd-pi/README.md`
