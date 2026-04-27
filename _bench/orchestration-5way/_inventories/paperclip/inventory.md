# Inventário: paperclip

**Path:** `OS/paperclip/`
**Date:** 2026-04-19
**Extraction Method:** filesystem-scan + doc-scan
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | paperclip |
| Source URL | https://github.com/paperclipai/paperclip |
| Primary language | TypeScript |
| Secondary languages | React, SQL |
| Stack | Node.js >=20, TypeScript, pnpm monorepo, React, Drizzle ORM, embedded-postgres, tsx, Vitest + Playwright, MCP SDK |
| License | MIT |
| Tagline | Orquestração open-source para 'zero-human companies' — plataforma que coordena agentes heterogêneos (OpenClaw, Claude Code, Codex, Cursor) numa estrutura org-chart com metas, budgets e governança. |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| LOC (TS/TSX) | 279.802 | `wc -l` |
| Files | 1.650 | filesystem scan |
| Top-level dirs | server, ui, cli, packages, docs, tests, evals, skills | `ls` |
| README length | ~500 linhas | `README.md` |
| Docs pages | ~80 | `docs/` mintlify |
| Last commit | 2026-04-17 | `git log -1` |

## Modules / Top-level Structure

| Module | Path | Type | Descrição |
|--------|------|------|-----------|
| @paperclipai/server | `server/` | app | Node HTTP server — routes, services, realtime WS |
| @paperclipai/ui | `ui/` | app | React SPA dashboard |
| @paperclipai/cli | `cli/` | app | `paperclipai` CLI |
| @paperclipai/db | `packages/db/` | package | Drizzle schemas + migrations |
| @paperclipai/mcp-server | `packages/mcp-server/` | package | MCP wrapper sobre REST Paperclip |
| adapters | `packages/adapters/` | package | 7 adapters: claude-local, codex-local, cursor-local, gemini-local, openclaw-gateway, opencode-local, pi-local |
| plugins | `packages/plugins/` | package | Plugin system |
| docker | `docker/` | service | Dockerfile + compose |
| evals | `evals/promptfoo/` | library | Promptfoo smoke evals |
| tests | `tests/` | library | E2E Playwright + release-smoke |

## External Dependencies (top 10)

| Package | Version | Purpose |
|---------|---------|---------|
| @paperclipai/db (drizzle-orm) | workspace | Persistência relacional |
| embedded-postgres | 18.1.0-beta | Postgres embutido dev zero-config |
| typescript | ^5.7.3 | Type system |
| vitest | ^3.0.5 | Unit tests |
| @playwright/test | ^1.58.2 | E2E |
| tsx | vendored | TS runtime |
| esbuild | ^0.27.3 | Bundler |
| @modelcontextprotocol/sdk | mcp-server/package | MCP |
| cross-env | ^10.1.0 | Env vars cross-platform |
| promptfoo | ^0.103.3 | Eval framework |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| CLI | `cli/src/index.ts` | `pnpm paperclipai` |
| HTTP server | `server/src/index.ts` | `pnpm dev:server` |
| MCP server | `packages/mcp-server/src/stdio.ts` | `npx -y @paperclipai/mcp-server` |
| Docker | `Dockerfile` | `docker build .` |

## Capabilities

### Core

| Capability | Evidence | Notes |
|------------|----------|-------|
| Company-sim (org-chart abstraction) | `server/src/services/companies.ts`, `company-member-roles.ts`, `routes/companies.ts`, `routes/org-chart-svg.ts` | Companies, roles, org-chart como abstração de orquestração |
| Heterogeneous agent adapters | `packages/adapters/{claude-local,codex-local,cursor-local,gemini-local,openclaw-gateway,opencode-local,pi-local}/` | 7 runtimes suportados via adapter pattern |
| Execution workspaces (git worktrees) | `server/src/services/execution-workspaces.ts`, `routes/execution-workspaces.ts` | Workspaces isolados por agent/tarefa |
| Routines (cron scheduling) | `server/src/routes/routines.ts`, `server/src/services/cron.ts` | Tasks agendadas recorrentes |

### Governance

| Capability | Evidence | Notes |
|------------|----------|-------|
| Goal + budget governance | `services/budgets.ts`, `goals.ts`, `finance.ts`, `costs.ts` | Budgets + goals + finance — nível empresa |
| Agent approval workflow | `services/approvals.ts`, `routes/approvals.ts` | Human-in-the-loop com aprovação mobile |
| Log redaction + PII | `server/src/{log-redaction,redaction}.ts`, `services/feedback-redaction.ts` | Redação automática de segredos |
| Promptfoo evals | `evals/promptfoo/` | Smoke evals no CI |

### Observability

| Capability | Evidence | Notes |
|------------|----------|-------|
| Heartbeat run summaries | `services/heartbeat-run-summary.ts` | Resumos truncados por run + comments |
| Realtime WebSocket live events | `server/src/realtime/live-events-ws.ts` | WS push pro dashboard/mobile |

### Extensibility / Integration / UX

| Capability | Evidence | Notes |
|------------|----------|-------|
| MCP server surface | `packages/mcp-server/src/tools.ts`, `README.md` | Agentes consomem Paperclip via MCP |
| Plugin system | `packages/plugins/`, `routes/plugins.ts`, `routes/plugin-ui-static.ts` | Server + UI plugins |
| Company portability | `services/company-portability.ts`, `company-export-readme.ts` | Import/export empresas (Clipmart roadmap) |
| Embedded Postgres | `patches/embedded-postgres@18.1.0-beta.16.patch` | DB zero-config |
| Docker deployment | `Dockerfile`, `docker/` | Imagem pronta |
| Mobile-first via Telegram | README 'mobile'; `routes/inbox-dismissals.ts` | Dashboard + Telegram approvals |

## Tests / Quality Signals

| Signal | Value | Evidence |
|--------|-------|----------|
| Test framework | Vitest + Playwright | `package.json`, `tests/e2e/` |
| Test file count | 255 (.test.ts) | find |
| CI/CD | GitHub Actions | `.github/workflows/{pr,release,release-smoke,e2e,docker,refresh-lockfile}.yml` |

## Documentation

| Type | Path | Status |
|------|------|--------|
| README | `README.md` | muito rico, ~500 linhas |
| CONTRIBUTING | `CONTRIBUTING.md` | presente |
| Docs mintlify | `docs/docs.json` | ~80 páginas |
| AGENTS.md | `AGENTS.md` | presente |
| ROADMAP.md | `ROADMAP.md` | presente |

## Extension Points

| Type | Where | How |
|------|-------|-----|
| Adapters | `packages/adapters/` | Adapter pattern por runtime |
| Plugins | `packages/plugins/` + `routes/plugins.ts` | Plugin store + UI |
| MCP server | `packages/mcp-server/` | Expor REST como MCP tools |

## Notable Design Decisions

- **Control-plane, não framework-lib** — orquestra runtimes externos, não reimplementa agents — evidência: `packages/adapters/`
- **Empresa como abstração** — companies/goals/budgets/roles são entidades primeiras — evidência: `server/src/services/companies.ts`
- **Heartbeat como contrato** — "se recebe heartbeat, está contratado" — evidência: `services/heartbeat-run-summary.ts`
- **Mobile-first** — Telegram + dashboard WS — evidência: README + `realtime/live-events-ws.ts`

## Limitations

- Não é framework-lib para criar agents do zero (é control plane)
- TypeScript/Node-only no servidor — sem SDK Python nativo
- Complexidade de stack vs frameworks single-file

## USPs

- **Company-sim**: org-chart + budgets + goals como abstração (diferencial vs chat-centric)
- **Agent-agnostic**: orquestra Claude Code, Codex, Cursor, OpenClaw, HTTP, Bash
- Full-stack pronto para auto-hosting (server+UI+CLI+DB+MCP+Docker)
- Governança embutida (approvals + budgets + audit + cost)
- Mobile-first (Telegram + dashboard responsivo)
- Clipmart roadmap — marketplace de empresas

---

_Generated by os-bench inventory task | Template v1.0_
