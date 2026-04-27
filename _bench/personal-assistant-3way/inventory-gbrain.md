# Inventário: GBrain

**Path:** `OS/gbrain/`
**Date:** 2026-04-19
**Extraction Method:** filesystem-scan + doc-scan
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | gbrain |
| Source URL | https://github.com/garrytan/gbrain |
| Primary language | TypeScript (Bun runtime) |
| Secondary languages | SQL, Markdown (skills) |
| Stack | Bun, TypeScript, PGLite (embedded Postgres via WASM), Postgres+pgvector (Supabase), OpenAI text-embedding-3-large, MCP (stdio+HTTP) |
| License | MIT |
| Version | 0.12.3 |
| Tagline | Your AI agent is smart but forgetful. GBrain gives it a brain — hybrid RAG + self-wiring knowledge graph |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| TS files (src) | 1,703 | filesystem scan |
| Bundled skills | 26 | `skills/` |
| CLI commands | 34 | `src/commands/` |
| MCP operations | 41 | `src/core/operations.ts` |
| Integration recipes | 7 | `recipes/` |
| Published benchmarks | 4 | `docs/benchmarks/` |
| Last commit | 2026-04-19 | `git log -1` |

## Modules / Top-level Structure

| Module | Path | Type | Description |
|--------|------|------|-------------|
| src/core | `src/core/` | library | Operations contract, engines (PGLite + Postgres), hybrid search, chunkers, embeddings |
| src/commands | `src/commands/` | app | 34 CLI subcommands |
| src/mcp | `src/mcp/` | service | MCP stdio server generated from contract |
| src/core/minions | `src/core/minions/` | library | Durable Postgres-native job queue |
| skills | `skills/` | package | 26 skills + RESOLVER.md routing |
| recipes | `recipes/` | library | 7 integration recipes |
| docs | `docs/` | library | MCP deploy, benchmarks, architecture, ethos, guides, designs |
| templates | `templates/` | library | SOUL/USER/ACCESS_POLICY/HEARTBEAT templates |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| CLI | `src/cli.ts` | `gbrain <cmd>` |
| MCP stdio | `src/mcp/server.ts` | `gbrain serve` |
| MCP HTTP | `src/mcp/server.ts` | `gbrain serve --http 8787` (via ngrok + token) |

## Capabilities (observed)

### Core Capabilities

| Capability | Evidence | Notes |
|------------|----------|-------|
| Hybrid search (vector + keyword + RRF) | `src/core/search/`, `src/core/search/intent.ts`, `src/core/search/expansion.ts`, `src/core/search/eval.ts` | Multi-query expansion + dedup + intent classifier |
| Self-wiring knowledge graph (zero-LLM) | `src/core/link-extraction.ts`, `src/commands/extract.ts`, `src/commands/graph-query.ts` | Typed edges: attended/works_at/invested_in/founded/advises/source/mentions |
| Pluggable engines (PGLite / Postgres) | `src/core/engine.ts`, `src/core/engine-factory.ts`, `src/core/pglite-engine.ts`, `src/core/postgres-engine.ts` | Bidirectional migration via `gbrain migrate` |
| Contract-first ops (~41 shared) | `src/core/operations.ts` (1137 LOC), `src/mcp/server.ts`, `src/cli.ts` | CLI + MCP from single source |
| Minions durable job queue | `src/core/minions/queue.ts`, `src/core/minions/worker.ts`, `src/core/minions/attachments.ts`, `src/commands/jobs.ts` | Postgres-native, BullMQ-inspired, cascade-kill, idempotency |
| Tiered enrichment | `src/core/enrichment-service.ts`, `skills/enrich/` | Auto-escalation by mention frequency |
| 3-tier chunking | `src/core/chunkers/` | Recursive, semantic, LLM-guided |
| Retrieval eval harness | `src/core/search/eval.ts`, `src/commands/eval.ts`, `docs/benchmarks/2026-04-18-brainbench-v1.md` | P@k, R@k, MRR, nDCG@k; BrainBench v1 R@5 83→95% |

### Optional/Extensibility Capabilities

| Capability | Evidence | Notes |
|------------|----------|-------|
| MCP stdio + HTTP | `src/mcp/server.ts`, `docs/mcp/{DEPLOY,CLAUDE_CODE,CLAUDE_DESKTOP,CLAUDE_COWORK,PERPLEXITY}.md` | Remote MCP with Bearer token |
| 26 skills | `skills/signal-detector/`, `skills/brain-ops/`, `skills/query/`, `skills/enrich/`, `skills/minion-orchestrator/`, `skills/RESOLVER.md` | Fat markdown skills + resolver |
| 7 recipes | `recipes/calendar-to-brain.md`, `recipes/email-to-brain.md`, `recipes/twilio-voice-brain.md`, `recipes/x-to-brain.md` | YAML+MD, trust-tagged |
| 4-tier identity (SOUL/USER/ACCESS/HEARTBEAT) | `skills/soul-audit/SKILL.md`, `templates/` | 6-phase interview |
| Publish (password-HTML, zero LLM) | `src/commands/publish.ts` | Deterministic |
| Universal migration | `skills/migrate/`, `src/commands/migrate-engine.ts` | Obsidian/Notion/Logseq/Roam/CSV/JSON/MD |
| Doctor + reliability checks | `src/commands/doctor.ts` | jsonb_integrity, markdown_body_completeness |
| Voice transcription (Groq Whisper default, OpenAI fallback) | `src/core/transcription.ts` | ffmpeg segmentation for >25 MB |
| Trust boundary (remote flag) | `src/core/operations.ts` OperationContext.remote | Tightens filesystem confinement for untrusted agent callers |

## Tests / Quality Signals

| Signal | Value | Evidence |
|--------|-------|----------|
| Unit tests | ~75 files, 1412 pass | `test/` |
| E2E tests | 8 files, 119 when `DATABASE_URL` set | `test/e2e/` |
| Test framework | bun test | `bun test` |
| CI/CD | GitHub Actions | `.github/workflows/` |
| Benchmarks published | Yes (BrainBench v1, Minions prod/lab, tweet ingestion) | `docs/benchmarks/` |

## Documentation

| Type | Path | Status |
|------|------|--------|
| README | `README.md` | Present (detailed tables + benchmarks) |
| CLAUDE.md | `CLAUDE.md` | 39 KB detailed architecture notes |
| CHANGELOG | `CHANGELOG.md` | 100 KB |
| Ethos | `docs/ethos/THIN_HARNESS_FAT_SKILLS.md`, `docs/ethos/MARKDOWN_SKILLS_AS_RECIPES.md` | Present |
| Benchmarks | `docs/benchmarks/2026-04-18-brainbench-v1.md` + 3 others | Reproducible |
| MCP guides | `docs/mcp/` | Per-client setup |
| Install for agents | `INSTALL_FOR_AGENTS.md` | Agent-driven install |

## Extension Points

| Extension Type | Where | How to extend |
|----------------|-------|---------------|
| Skills | `skills/` + RESOLVER.md | Fat markdown + conformance test (skill-creator) |
| Recipes | `recipes/` | YAML frontmatter + MD |
| Engines | `src/core/engine.ts` interface | pglite / postgres (bidirectional migrate) |
| Storage | `src/core/storage.ts` | S3, Supabase Storage, local |
| MCP | `src/mcp/server.ts` | 41 operations auto-exposed |
| Plugin handlers | `docs/guides/plugin-handlers.md` | Host-specific (RCE-safe): migration emits structured TODOs |

## Notable Design Decisions

- **Thin harness, fat skills** — evidence: `docs/ethos/THIN_HARNESS_FAT_SKILLS.md` (intelligence in skills, not runtime)
- **Contract-first** — evidence: `src/core/operations.ts` defines ~41 shared ops; CLI + MCP are generated from it
- **Engine pluggable from day one** — evidence: `src/core/engine-factory.ts` dynamic import of `pglite` or `postgres`
- **Benchmarks are first-class** — evidence: `docs/benchmarks/` with reproducible harnesses, published numbers
- **Trust boundary explicit** — evidence: `OperationContext.remote` flag; SSRF helpers in `src/commands/integrations.ts`
- **Not a standalone assistant** — evidence: README "Designed to be installed and operated by an AI agent" (OpenClaw / Hermes recommended)

## Limitations / Known Issues

- Not a standalone assistant — brain layer under an agent platform — `README.md`
- No built-in messaging channels — channels come from host (OpenClaw/Hermes)
- MCP remote HTTP requires manual ngrok + token (not hosted) — `README.md`
- ChatGPT MCP requires OAuth 2.1 (not yet implemented) — `README.md`

## Unique Selling Points

- Self-wiring knowledge graph with zero-LLM auto-link
- Hybrid RAG with published benchmark (R@5 83→95%, graph-only F1 86.6%)
- Pluggable engines (PGLite zero-config OR Postgres+pgvector)
- Contract-first: 41 ops drive both CLI and MCP
- Minions durable Postgres-native job queue
- Trust boundary: CLI vs agent callers treated differently
- Installed by an agent (~30 min agent-driven install)
- Designed as brain layer under OpenClaw or Hermes

---

## Extraction Notes

- Scanned: `src/`, `skills/`, `recipes/`, `docs/`, `templates/`
- Skipped: `node_modules`, `.git`, `bun.lock`
- Data sources: filesystem 100%
- Tools used: `ls`, `find`, `grep`, README/CLAUDE read

---

_Generated by os-bench inventory task | Template v1.0_
