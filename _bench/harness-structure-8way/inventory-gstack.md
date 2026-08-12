# Inventory: gstack

**Generated:** 2026-08-12T18:00:00Z  
**Path:** `OS/gstack/`  
**Stack:** Bun, Chromium/CDP, Claude Code skills  
**License:** MIT  
**Confidence:** HIGH  
**Extraction:** filesystem-scan

> Opinionated software factory of slash-command specialists (CEO, eng, design, QA, ship) plus a persistent browser daemon.

## Metrics

- Files: 1177 · SKILL.md count: 59 · README lines: 491
- Last commit: `2026-08-08T09:28:45-07:00`
- Source: https://github.com/garrytan/gstack

## Capabilities

- **Generated skill suite** (core): Each top-level folder is a SKILL.md generated from templates with shared preamble. — `OS/gstack/docs/skills.md`, `OS/gstack/SKILL.md.tmpl`
- **Office-hours to ship spine** (core): office-hours → spec → autoplan → implement → review → QA → ship. — `OS/gstack/docs/skills.md`, `OS/gstack/ship/SKILL.md`
- **Sequential specialist pipeline** (core): CEO → Design → Eng → DX must run in order; dual-voice Claude+Codex per phase. — `OS/gstack/autoplan/SKILL.md`
- **Host adapters** (extensibility): One skill source rewritten per host (Claude, Codex, OpenClaw, Hermes, Cursor, …). — `OS/gstack/hosts/claude.ts`, `OS/gstack/hosts/openclaw.ts`, `OS/gstack/hosts/hermes.ts`
- **Persistent browser daemon** (ux): Long-lived Chromium over localhost HTTP; ~100–200ms after first start. — `OS/gstack/ARCHITECTURE.md`
- **Context save/restore** (core): Checkpoints under ~/.gstack/projects/ for cross-session resume. — `OS/gstack/context-save/SKILL.md`

## Extension points

- Plugins: host-generated skill install, not a native plugin runtime (`hosts/`)
- Hooks: Claude host hooks
- MCP: client=False server=False

## USPs

- Markdown is the program; browser is the hard part
- Specialist gauntlet without standing employees
- Multi-host generation from one source

## Limitations

- Generated SKILL.md preamble is large (opposite of Superpowers tiny bootstrap) — `OS/gstack/SKILL.md`
- No org-chart, hire, or cost budgets — `OS/gstack/docs/skills.md`

