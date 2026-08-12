# Inventory: paperclip

**Generated:** 2026-08-12T18:00:00Z  
**Path:** `OS/paperclip/`  
**Stack:** Node, React, Postgres/Drizzle, pnpm monorepo  
**License:** MIT  
**Confidence:** HIGH  
**Extraction:** filesystem-scan

> If OpenClaw is an employee, Paperclip is the company — org-chart, budgets, issues, and adapters for heterogeneous agent runtimes.

## Metrics

- Files: 4519 · SKILL.md count: 52 · README lines: 523
- Last commit: `2026-08-12T12:12:55-04:00`
- Source: https://github.com/paperclipai/paperclip

## Capabilities

- **agentcompanies/v1 teams** (core): TEAM.md + AGENTS.md + PROJECT.md + TASK.md packages with manager/includes/requiredSkills. — `OS/paperclip/packages/teams-catalog/catalog/bundled/company-defaults/core-exec-team/TEAM.md`
- **CEO must delegate** (governance): CEO triages and hires; never ICs; child issues carry durable handoff. — `OS/paperclip/packages/teams-catalog/catalog/bundled/company-defaults/core-exec-team/agents/ceo/AGENTS.md`
- **Cross-runtime adapters** (integration): Claude, Codex, Cursor, Gemini, OpenClaw, OpenCode, Pi under one company. — `OS/paperclip/packages/adapters/`
- **Plugin spec** (extensibility): Manifest capabilities, namespaced API routes, UI extensions; current runtime is single-tenant filesystem. — `OS/paperclip/doc/plugins/PLUGIN_SPEC.md`, `OS/paperclip/packages/plugins/`
- **Skills catalog** (core): Bundled vs optional SKILL.md with generated catalog.json. — `OS/paperclip/packages/skills-catalog/`
- **Cost/budget plane** (governance): Company-sim with budgets and board approvals (see also server cost services). — `OS/paperclip/docs/companies/companies-spec.md`

## Extension points

- Plugins: plugin-sdk + PLUGIN_SPEC (`packages/plugins/`)
- Hooks: plugin events/jobs
- MCP: client=True server=True

## USPs

- Only subject with org + money + heterogeneous runtimes
- Issue tree is the coordination bus
- Catalogs for both teams and skills

## Limitations

- Plugin cloud/multi-node install is not ready (PLUGIN_SPEC caveats) — `OS/paperclip/doc/plugins/PLUGIN_SPEC.md`
- Not a coding methodology (no TDD iron law / SDD ledger) — `OS/paperclip/README.md`

