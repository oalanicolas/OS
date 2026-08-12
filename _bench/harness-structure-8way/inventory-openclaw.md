# Inventory: openclaw

**Generated:** 2026-08-12T18:00:00Z  
**Path:** `OS/openclaw/`  
**Stack:** gateway, native apps, plugin-sdk, MCP  
**License:** MIT  
**Confidence:** HIGH  
**Extraction:** filesystem-scan

> Personal-agent OS: workspace identity files, multi-root skills, native plugins, and ClawHub.

## Metrics

- Files: 31842 · SKILL.md count: 115 · README lines: 310
- Last commit: `2026-08-12T09:31:23-07:00`
- Source: https://github.com/openclaw/openclaw

## Capabilities

- **Workspace constitution** (core): AGENTS/SOUL/USER/IDENTITY/MEMORY split; subagents get AGENTS.md only. clawd is the reference home. — `OS/openclaw/AGENTS.md`, `OS/clawd/AGENTS.md`
- **Multi-root skill load** (core): Workspace > .agents > ~/.agents > state > bundled > plugin; catalog capped (150 / 18k chars). — `OS/openclaw/docs/tools/skills.md`
- **Native plugin architecture** (extensibility): Manifest validated before executing plugin code; exclusive slots for memory/context-engine. — `OS/openclaw/docs/plugins/architecture.md`, `OS/openclaw/packages/plugin-sdk/`
- **Skill Workshop + ClawHub** (extensibility): Human gate before agent-written skills go live; marketplace verify/scan. — `OS/openclaw/skills/skill-creator/SKILL.md`, `OS/openclaw/docs/clawhub/`
- **TaskFlow durable jobs** (core): stateJson + currentStep for multi-step work; business logic stays in the caller. — `OS/openclaw/skills/taskflow/SKILL.md`
- **Requires gating** (governance): metadata.openclaw.requires.bins/env/os so missing binaries do not pollute the catalog. — `OS/openclaw/docs/tools/skills.md`

## Extension points

- Plugins: openclaw.plugin.json + register(api) (`packages/plugin-sdk/`)
- Hooks: plugin hooks
- MCP: client=True server=True

## USPs

- Richest native plugin model in the set
- Identity files are not skills and not policy
- Catalog budgets with truncation warnings

## Limitations

- Not an SDLC methodology — standing orders + TaskFlow, not specify→plan→ship — `OS/openclaw/docs/tools/skills.md`
- No org-chart / company budget plane (that's Paperclip's job) — `OS/paperclip/README.md`

