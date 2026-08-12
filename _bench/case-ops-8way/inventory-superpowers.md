# Inventory: superpowers

**Generated:** 2026-08-12T18:00:00Z  
**Path:** `OS/superpowers/`  
**Stack:** Claude Code plugin, Codex plugin, Gemini extension, OpenCode, Cursor, Copilot  
**License:** MIT  
**Confidence:** HIGH  
**Extraction:** filesystem-scan

> Complete software-development methodology for coding agents built on composable skills plus bootstrap instructions that force the agent to use them.

## Metrics

- Files: 179 · SKILL.md count: 14 · README lines: 281
- Last commit: `2026-07-28T12:25:36-07:00`
- Source: https://github.com/obra/superpowers

## Capabilities

- **SessionStart bootstrap** (core): Injects using-superpowers body so the agent must invoke skills before any action. — `OS/superpowers/hooks/session-start`, `OS/superpowers/skills/using-superpowers/SKILL.md`
- **SDO skill descriptions** (core): Description is trigger-only; workflow summaries are forbidden because agents skip the body. — `OS/superpowers/skills/writing-skills/SKILL.md`
- **Subagent-driven development** (core): Fresh implementer per task, file-only briefs, 5-round fix loop with breaker, plan-scoped ledger. — `OS/superpowers/skills/subagent-driven-development/SKILL.md`
- **TDD iron law** (governance): Red/green/refactor enforced as a skill, tested with pressure scenarios. — `OS/superpowers/skills/test-driven-development/SKILL.md`
- **Skill TDD authoring** (extensibility): Skills are written only after a failing pressure-scenario baseline. — `OS/superpowers/skills/writing-skills/SKILL.md`, `OS/superpowers/tests/explicit-skill-requests/`
- **Multi-host plugin pack** (extensibility): Same skills packaged for Claude, Codex, Gemini, OpenCode, Cursor, Copilot, Pi. — `OS/superpowers/.claude-plugin/plugin.json`, `OS/superpowers/gemini-extension.json`

## Extension points

- Plugins: Claude plugin.json + per-host adapters (`.claude-plugin/plugin.json`)
- Hooks: SessionStart
- MCP: client=False server=False

## USPs

- Process plugin that forces skill use via hook, not hope
- Ledger + file handoff designed after compaction re-dispatched finished tasks
- Zero-dep; domain skills rejected from core

## Limitations

- No org-chart, budgets, or plugin marketplace of its own — `OS/superpowers/README.md`
- Depends on host context files (CLAUDE.md/AGENTS.md) for identity — `OS/superpowers/skills/using-superpowers/SKILL.md`

