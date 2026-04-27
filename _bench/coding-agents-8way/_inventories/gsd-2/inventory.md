# Inventário: gsd-2

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
| Stack | Node >=22, Pi SDK, npm workspaces, MCP SDK |
| License | MIT |
| Tagline | Standalone CLI built on Pi SDK — auto-mode com memória persistente, KG, remote control, self-healing |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| LOC (ballpark) | ~250k TS | find src/packages |
| Files .ts | 1735 | find |
| Top-level dirs | src, packages, studio, web, docs, native, scripts, tests, pkg, mintlify-docs, gitbook, gsd-orchestrator, vscode-extension, docker | ls |
| README length | 855 | wc -l |
| Last commit | 2026-04-19 | git log |
| CI workflows | 11 | .github/workflows |

## Modules / Top-level Structure

| Module | Path | Type | Loc estimate | Description |
|--------|------|------|--------------|-------------|
| src | `src/` | app | ~120k | CLI core, resources/extensions |
| packages/pi-coding-agent | `packages/pi-coding-agent/` | package | ~50k | Coding agent core |
| packages/pi-tui | `packages/pi-tui/` | package | ~20k | Terminal UI |
| packages/pi-ai | `packages/pi-ai/` | package | ~20k | AI providers |
| packages/mcp-server | `packages/mcp-server/` | package | ~5k | MCP server |
| packages/native | `packages/native/` | package | ~10k | Native bindings |
| web | `web/` | app | ~15k | Web host |
| studio | `studio/` | app | ~10k | Studio UI |
| vscode-extension | `vscode-extension/` | package | — | IDE ext |

## External Dependencies (top 10)

| Package | Version | Purpose |
|---------|---------|---------|
| @anthropic-ai/sdk | ^0.90.0 | LLM |
| @anthropic-ai/vertex-sdk | ^0.14.4 | Vertex |
| @aws-sdk/client-bedrock-runtime | ^3.983.0 | Bedrock |
| @google/genai | ^1.40.0 | Gemini |
| @mistralai/mistralai | ^1.14.1 | Mistral |
| @modelcontextprotocol/sdk | ^1.27.1 | MCP |
| @octokit/rest | ^22.0.1 | GitHub |
| ajv | ^8.17.1 | JSON schema |
| chalk | ^5.6.2 | Terminal |
| chokidar | ^5.0.0 | File watch |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| CLI | `dist/loader.js` | `gsd` / `gsd-cli` |
| Web | `web/` | `gsd:web` |
| MCP | `packages/mcp-server/` | `gsd mcp` |

## Capabilities (observed)

### Core Capabilities

| Capability | Evidence | Notes |
|------------|----------|-------|
| Auto-mode | `OS/gsd-2/README.md:14-23` | Roda 1 comando, sai, volta com PR |
| Context mgmt explícito | `OS/gsd-2/README.md:16` | Clear + inject + manage sessions |
| Git branch isolation | `OS/gsd-2/README.md:68` | milestone branch created on entry |
| Stuck-loop detection | `OS/gsd-2/README.md:66` | Detecta repetição; #4414 |
| Memória KG (Phase 1-5) | `OS/gsd-2/README.md:32-38` | capture_thought, memory_query, gsd_graph; scoped/tagged; hybrid retrieval; graph relationships |
| Progressive planning | `OS/gsd-2/README.md:40-43` | Sketch-then-refine; mid-run escalation |
| UOK orchestration kernel | `OS/gsd-2/README.md:80`, `gsd-orchestrator/` | Plan-v2 compile gates, reactive/parallel scheduling |

### Optional/Extensibility

| Capability | Evidence | Notes |
|------------|----------|-------|
| Workflow plugin system | `OS/gsd-2/README.md:46` | /gsd workflow list|run|install|info|validate |
| Extension API | `OS/gsd-2/README.md:82`, `.gsd/extensions/` | 3rd party extensions |
| MCP server | `OS/gsd-2/packages/mcp-server/` | Own MCP crate |
| Remote control | `OS/gsd-2/README.md:51` | Telegram + Slack + Discord |
| Multi-provider | `package.json deps` | 8+ providers |
| Self-healing | `OS/gsd-2/README.md:70` | .gsd staging self-heals; stale OAuth recovery |
| VS Code ext | `OS/gsd-2/vscode-extension/` | IDE |
| Web UI + Studio | `OS/gsd-2/web/`, `studio/` | GUI |

## Tests / Quality Signals

| Signal | Value | Evidence |
|--------|-------|----------|
| Test framework | node --test + c8 | `package.json scripts` |
| Linter | tsc | `tsconfig*.json` |
| CI | GitHub Actions | 11 workflows (ai-triage, build-native, ci, pipeline, pr-risk, prod-release, next-publish etc.) |

## Documentation

| Type | Path | Status |
|------|------|--------|
| README | `README.md` | 855 linhas, change-log-heavy |
| CONTRIBUTING | `CONTRIBUTING.md` | presente |
| Architecture | `mintlify-docs/` + `gitbook/` | presente |
| VISION | `VISION.md` | presente |

## Extension Points

| Extension Type | Where | How to extend |
|----------------|-------|---------------|
| Workflow plugins | `.gsd/extensions/` | Manual install + install remote |
| MCP | `packages/mcp-server/` | Protocol |
| Remote control | Telegram/Slack/Discord | Bot integration |

## Notable Design Decisions

- Auto-mode é centro: milestones auto-advance, cadência sem HITL
- Single-writer DB invariant pra não corromper estado
- DB-authoritative milestone state (#4179)
- Self-healing em symlinks + OAuth + DB
- Stuck-loop detection + model fallback

## Limitations

- Setup pesado (Node + native + web + studio) — package.json 60+ scripts
- README 855 linhas é change-log — onboarding denso

## Unique Selling Points

- Auto-mode end-to-end
- Memória KG completa (5 fases)
- Remote control multi-canal (único do benchmark com Telegram/Slack/Discord)
- Self-healing resilience
- UOK (plan-v2 + reactive scheduling)
- 8+ provedores nativos

---

_Generated by os-bench inventory task | Template v1.0_
