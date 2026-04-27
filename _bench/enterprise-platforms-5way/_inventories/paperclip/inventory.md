# Inventory — paperclip

**Path:** `OS/paperclip/`
**Profile:** quick
**License:** MIT (`OS/paperclip/README.md#L309`)

## Positioning

> "If OpenClaw is an _employee_, Paperclip is the _company_. Paperclip is a Node.js server and React UI that orchestrates a team of AI agents to run a business."
> (`OS/paperclip/README.md#L30-L32`)

Company-sim puro: "It looks like a task manager — but under the hood it has org charts, budgets, governance, goal alignment, and agent coordination." (`#L35`)

## Stack

- **Node.js 20+, TypeScript** (`OS/paperclip/package.json` engines)
- **pnpm 9.15.4** monorepo com `pnpm-workspace.yaml`
- **PostgreSQL** embedded (patch `embedded-postgres@18.1.0-beta.16` em `patches/` para zero-setup first run)
- **Vitest** unit tests + **Playwright** e2e/release-smoke/multiuser-authenticated
- **promptfoo** em `evals/promptfoo/`

## Top-level

```
README.md  ROADMAP.md  AGENTS.md  CONTRIBUTING.md  SECURITY.md  LICENSE
Dockerfile  adapter-plugin.md  package.json  pnpm-workspace.yaml
tsconfig.json  tsconfig.base.json  vitest.config.ts
cli/  server/  ui/  packages/  skills/  evals/
doc/  docs/  docker/  tests/  scripts/  patches/  releases/  report/
```

## Packages

`adapter-utils`, `adapters`, `db`, `mcp-server`, `plugins`, `shared`.

## Server routes (`OS/paperclip/server/src/routes/`)

`companies.ts`, `org-chart-svg.ts`, `goals.ts`, `projects.ts`, `agents.ts`, `issues.ts`, `issues-checkout-wakeup.ts`, `approvals.ts`, `costs.ts`, `routines.ts`, `dashboard.ts`, `authz.ts`, `access.ts`, `secrets.ts`, `assets.ts`, `adapters.ts`, `plugins.ts`, `company-skills.ts`, `execution-workspaces.ts`, `workspace-command-authz.ts`, `workspace-runtime-service-authz.ts`, `instance-settings.ts`, `inbox-dismissals.ts`, `llms.ts`, `sidebar-badges.ts`, `sidebar-preferences.ts`, `activity.ts`.

## Skills shipped

`skills/paperclip`, `skills/paperclip-create-agent`, `skills/paperclip-create-plugin`, `skills/para-memory-files`.

## Capacidades observaveis (subject-only highlights)

- **Company-sim paradigm** — org charts, CEO/CTO/engineers, reporting lines, job descriptions (`OS/paperclip/README.md#L117-L123`).
- **True multi-company isolation**: "Every entity is company-scoped, so one deployment can run many companies with separate data and audit trails" (`#L155`).
- **Atomic task checkout + budget enforcement** — "no double-work and no runaway spend" (`#L149`).
- **Heartbeat-based agents (BYOA)**: OpenClaw, Claude Code, Codex, Cursor, Bash, HTTP — "If it can receive a heartbeat, it's hired" (`#L54-L63`).
- **Goal-aware execution** — tasks carry full goal ancestry (`#L153`).
- **Portable company templates** via `companies.sh` com secret scrubbing + collision handling (`#L154`; ROADMAP shipped).
- **Governance with rollback** — approval gates + revisioned config (`#L152`).
- **Adapter plugin system** (`OS/paperclip/adapter-plugin.md`).
- **Bind presets**: local loopback / lan / tailnet (Tailscale-friendly para mobile) (`#L181-L187`).
- **Evals via promptfoo** (`OS/paperclip/evals/promptfoo/`).

## Observacao de escopo — ROADMAP gaps

Marcados como ⚪ (nao-shipped) no ROADMAP (`OS/paperclip/README.md#L249-L272`):

- Multiple Human Users
- Cloud / Sandbox agents (Cursor / e2b)
- Artifacts & Work Products
- **Memory / Knowledge** (grande gap — paperclip nao tem memory nativa)
- Enforced Outcomes
- Deep Planning, Work Queues, Self-Organization
- Automatic Organizational Learning
- CEO Chat, Cloud deployments, Desktop App

Paperclip e **orquestracao pura** — nao tenta ser memory infra, nem model provider, nem framework de agentes. Tem `skills/para-memory-files` (memory-files based) mas nao memory estruturada.
