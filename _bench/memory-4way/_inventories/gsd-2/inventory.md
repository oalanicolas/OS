# Inventario: GSD 2

**Path:** `OS/gsd-2/`
**Date:** 2026-04-19
**Extraction Method:** filesystem-scan + doc-scan
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | gsd-2 |
| Source URL | https://github.com/gsd-build/GSD-2 |
| Primary language | TypeScript |
| Secondary languages | JavaScript, Markdown, Python |
| Stack | Node 22+, Pi SDK (pi-mono), SQLite (`gsd.db`), tsup, node:test / vitest, Next.js (web) |
| License | MIT |
| Tagline | GSD 2 (Get Shit Done): standalone coding agent com Pi SDK; memoria persistente v2.76 (capture_thought, memory_query, gsd_graph) |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| LOC (ballpark) | ~548K | `wc -l` (inclui generated, web, vscode) |
| Files | 2,937 | filesystem scan |
| Top-level dirs | 14 (src, packages, studio, web, native, docs, gitbook, mintlify-docs, ...) | filesystem scan |
| Version | 2.76.0 | `package.json` |
| Last commit | 2026-04-19 | `git log -1` |

## Modules

| Module | Path | Type | LOC estimate | Description |
|--------|------|------|--------------|-------------|
| src/resources/extensions/gsd | `src/resources/extensions/gsd/` | library | ~80K | Extension GSD com memory-store, memory-tools, memory-relations |
| packages/pi-coding-agent | `packages/pi-coding-agent/` | package | ~30K | Agent harness core |
| packages/native | `packages/native/` | package | ~5K | Native bindings |
| studio | `studio/` | package | ~10K | Studio TUI/frontend |
| web | `web/` | app | ~20K | Web UI |
| vscode-extension | `vscode-extension/` | app | ~5K | VS Code sidebar |

## External Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| Pi SDK (pi-mono) | workspace | Agent harness TS-native |
| @gsd/pi-tui | workspace | TUI |
| @gsd/pi-ai | workspace | AI/LLM |
| @gsd/pi-coding-agent | workspace | Coding agent core |
| @gsd-build/mcp-server | workspace | MCP server workflow |
| RTK binary | external (managed) | Shell output compression (opt-out) |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| CLI | `dist/loader.js` | `gsd` / `gsd-cli` |
| MCP server | `packages/mcp-server/` | Workflow tools over MCP |

## Capabilities (memory-relevant)

| Capability | Evidence | Notes |
|------------|----------|-------|
| capture_thought / memory_query / gsd_graph | `src/resources/extensions/gsd/tools/memory-tools.ts`, `bootstrap/memory-tools.ts` | v2.76 Phase 1 |
| Scoped memories + tags | `src/resources/extensions/gsd/memory-store.ts` | project/milestone/slice scopes |
| Hybrid retrieval (kw + semantic) | `src/resources/extensions/gsd/commands-memory.ts` | Phase 3 |
| Knowledge graph relationships | `src/resources/extensions/gsd/tests/memory-relations.test.ts` | Phase 4 (memory edges feed planning) |
| Cap cascade + decay + export/import | `src/resources/extensions/gsd/memory-store.ts` | Phase 5 maintenance |
| Structured fields (ADR-013) | `src/resources/extensions/gsd/memory-store.ts` | optional payload para decisions |
| Extract learnings | `src/resources/extensions/gsd/commands-extract-learnings.ts` | LEARNINGS.md |
| Single-writer DB invariant | `src/resources/extensions/gsd/db-writer.ts` | previne corruption em gsd.db |
| DB-authoritative milestone state | `src/resources/extensions/gsd/` | v2.74 |
| UOK (plan-v2 compile gates) | `src/resources/extensions/gsd/` | v2.75 default |
| Workflow plugin system | `src/resources/extensions/gsd/` | install/run/validate |
| Extension API | `src/resources/extensions/` | .gsd/extensions/ loader |
| MCP server (workflow tools) | `packages/mcp-server/` | slice replan, milestone, ask user |

## Tests / Quality

| Signal | Value | Evidence |
|--------|-------|----------|
| Test framework | node:test + vitest + tsx | `package.json` scripts |
| Test coverage | c8: 40% stmts/lines, 20% branches/fns | `package.json` |
| Linter | — (sem explicit root) | — |
| CI | GitHub Actions | `.github/workflows/` |

## Extension Points

| Type | Where | How |
|------|-------|-----|
| Extensions | `.gsd/extensions/` | GSD Extension API |
| Workflow hooks | `src/resources/extensions/gsd/` | before_model_select + slice hooks |
| MCP | `packages/mcp-server/` | client + server |

## Notable Design Decisions

- Memoria como **layer** dentro do coding agent (nao produto standalone)
- Pi SDK direct control: context windows, sessions, execution sob controle TS
- Single-writer SQLite (`gsd.db`) enforcement contra corruption
- 5-phase memory roadmap: capture → scope → hybrid → KG → maintenance
- Graceful degradation: DB unavailable retorna empty, nao throw

## Limitations

- Memoria e side-feature (coding-agent-first), nao memory-first
- Sem benchmarks publicos de recall/latencia comparados a mem0/mempalace
- Requer `.gsd/` project inicializado (caso contrario db_unavailable)
- RTK binary introduz dependencia externa (opt-out via env)

## Unique Selling Points

- Coding agent-integrated memory (memory feeds planning/dispatch direto)
- One-command walk-away auto-mode com stuck detection e recovery
- 30+ skill packs cobrindo frameworks, databases, clouds
- Remote control via Telegram/Slack/Discord
- VS Code sidebar com SCM provider, checkpoints, activity feed

---

_Generated by os-bench inventory task | Template v1.0_
