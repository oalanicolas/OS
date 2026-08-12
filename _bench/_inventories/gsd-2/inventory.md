# Inventory: gsd-2

**Generated:** 2026-08-12T18:00:00Z  
**Path:** `OS/gsd-2/`  
**Stack:** pi-coding-agent, Node, native crates  
**License:** MIT  
**Confidence:** HIGH  
**Extraction:** filesystem-scan

> Autonomous software factory: spec → milestone → isolated workers → verification, with an Agent Skills runtime.

## Metrics

- Files: 3607 · SKILL.md count: 38 · README lines: 20
- Last commit: `2026-05-22T18:08:55-05:00`
- Source: https://github.com/gsd-build/gsd-2

## Capabilities

- **Agent Skills runtime** (core): Scans SKILL.md, injects XML catalog only, Skill tool loads bodies. auto/suggest/off discovery. — `OS/gsd-2/packages/pi-coding-agent/src/core/skills.ts`, `OS/gsd-2/docs/user-docs/skills.md`
- **Milestone artifact DAG** (core): .gsd/ PROJECT/REQUIREMENTS/DECISIONS/STATE + M###/S##/T## plan and summary files. — `OS/gsd-2/gsd-orchestrator/SKILL.md`
- **Isolated typed subagents** (core): scout/planner/worker/reviewer with fresh context default; children cannot recurse. — `OS/gsd-2/src/resources/agents/scout.md`, `OS/gsd-2/docs/user-docs/subagents.md`
- **Headless orchestrator skill** (integration): OpenClaw-facing skill drives gsd as subprocess with exit codes 0/1/10/11. — `OS/gsd-2/gsd-orchestrator/SKILL.md`
- **Extension SDK + MCP** (extensibility): Workflow plugins via .gsd/extensions plus first-party MCP server. — `OS/gsd-2/docs/extension-sdk/README.md`, `OS/gsd-2/packages/mcp-server/`
- **File-path handoff** (core): continue.md written for a stranger: last/next/why/open/do-not. — `OS/gsd-2/src/resources/skills/handoff/SKILL.md`

## Extension points

- Plugins: extension-manifest.json + Extension API (`docs/extension-sdk/`)
- Hooks: documented hooks
- MCP: client=True server=True

## USPs

- Implements Agent Skills as a runtime, not just a pack
- On-disk milestone state is the source of truth
- Scout compresses context for agents who have not seen the files

## Limitations

- README now redirects to open-gsd/gsd-pi; this clone is an archived snapshot (last commit 2026-05-22) — `OS/gsd-2/README.md`
- No company-sim / org-chart / token budgets — `OS/gsd-2/docs/user-docs/working-in-teams.md`

