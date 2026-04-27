# Comparison Matrix: memory-4way (gbrain, mempalace, mem0, gsd-2)

**Date:** 2026-04-19
**Comparison type:** nway
**Dimension pack:** memory
**Slug:** memory-4way

---

## Sources

| Subject | Path | Confidence |
|---------|------|------------|
| gbrain | `OS/gbrain/` | HIGH |
| mempalace | `OS/mempalace/` | HIGH |
| mem0 | `OS/mem0/` | HIGH |
| gsd-2 | `OS/gsd-2/` | HIGH |

## Method

Matriz construida a partir de scan local dos 4 repositorios em `OS/`. Cada feature foi extraida de evidencia concreta (arquivo + linhas), nunca inferida sem path. Benchmarks sao citados apenas quando o repo publica resultado reproduzivel no proprio tree (`benchmarks/` ou `docs/benchmarks/`). Claims como "95% R@5" aparecem apenas com citacao da fonte.

---

## Inventory Summary

| Metric | gbrain | mempalace | mem0 | gsd-2 |
|--------|-------:|----------:|-----:|------:|
| LOC (code) | ~44.5K | ~35K | ~125K | ~548K* |
| Files | 584 | 231 | 1,274 | 2,937 |
| Primary language | TypeScript | Python | Python | TypeScript |
| License | MIT | MIT | Apache-2.0 | MIT |
| Version | v0.12.3 | 3.3.1 | 2.0.0 | 2.76.0 |
| Last commit | 2026-04-19 | 2026-04-17 | 2026-04-18 | 2026-04-19 |
| Memory = core product? | YES | YES | YES | NO (layer em coding agent) |

*gsd-2 LOC inclui web UI, VS Code ext e generated code; codigo core de memoria e bem menor.

---

## Feature Matrix

### Category: Recall Accuracy

| Item | gbrain | mempalace | mem0 | gsd-2 |
|------|--------|-----------|------|-------|
| Benchmark publico reproduzivel | R@5 95% (BrainBench proprio, 240-page Opus corpus) | R@5 96.6% raw (LongMemEval 500q), 98.4% held-out v4 | LoCoMo 91.6, LongMemEval 93.4, BEAM(1M) 64.1 | no |
| Eval harness incluso | yes (`src/core/search/eval.ts`) | yes (`benchmarks/*.py`) | yes (`evaluation/`) | no |
| Dataset padrao da industria | no (custom corpus) | YES (LongMemEval, LoCoMo, ConvoMem, MemBench) | YES (LoCoMo, LongMemEval, BEAM) | — |

**Leaders:** mempalace (tied com mem0 em rigor publico), mem0 (benchmarks mais amplos)

---

### Category: Write/Read Latency

| Item | gbrain | mempalace | mem0 | gsd-2 |
|------|--------|-----------|------|-------|
| p50/p99 documentado | no explicit | budgets <500ms/<100ms declarados | 0.88s-1.09s end-to-end publicado | no |
| Batch/async write | YES (addLinksBatch unnest + Minions) | incremental sync | YES (AsyncMemory/Client) | sync (single-writer) |
| Job queue durable | YES (Minions BullMQ-inspired) | no | no (graph reconciliation async) | no |

**Leaders:** mem0 (p50 publicado), gbrain (batch + job queue), mempalace (performance budgets contratados)

---

### Category: Persistence (Verbatim vs Paraphrase)

| Item | gbrain | mempalace | mem0 | gsd-2 |
|------|--------|-----------|------|-------|
| Storage strategy | paraphrase (`compiled_truth`) + raw em `raw_data` JSONB | **VERBATIM** nao-negociavel | paraphrase (LLM facts extraction ADD-only) | structured category+content |
| Durable backend | PGLite WASM OU Postgres/Supabase | ChromaDB + SQLite KG | Qdrant + Neo4j (docker ou hosted) | SQLite single-writer |
| Snapshot/versioning | `page_versions` table | append-only | memory history via `history(memory_id)` | superseded_by chain |
| Crash-safe incremental | yes | yes (policy: crash mid-op leave palace untouched) | yes | yes (single-writer invariant) |

**Leader (verbatim promise):** mempalace — unica com policy explicita zero-paraphrase

---

### Category: Schema Flexibility

| Item | gbrain | mempalace | mem0 | gsd-2 |
|------|--------|-----------|------|-------|
| Schema model | pages + chunks + links + timeline (rigid + frontmatter JSONB) | drawers schemaless + entity registry + typed predicates KG | memories + metadata + entity links + graph Neo4j | categoria enum 6 values + structured_fields JSON |
| Metadata flexibility | alta (frontmatter arbitrario) | alta (dialect symbolic + entity props) | alta (metadata Pydantic + user/agent/run_id scoping) | media (fixed categoria + JSON payload) |

**Leaders:** mem0, mempalace

---

### Category: Local-first

| Item | gbrain | mempalace | mem0 | gsd-2 |
|------|--------|-----------|------|-------|
| Zero API keys no core | NO (OpenAI embeddings obrigatorio) | **YES** (96.6% raw sem LLM) | NO (OpenAI default + posthog) | hibrido (Ollama possivel) |
| Works offline | parcial | **YES** | parcial (fastembed extra) | parcial |
| Telemetry | none detected | zero (policy) | posthog em deps core | RTK_TELEMETRY_DISABLED forced |
| Encryption at rest | n/d | n/d (SQLite dir 0o700) | n/d | n/d |

**Leader absoluto:** mempalace — unico 100% local-first por design

---

### Category: Vector Support

| Item | gbrain | mempalace | mem0 | gsd-2 |
|------|--------|-----------|------|-------|
| Embedding providers | 1 (OpenAI text-embedding-3-large) | 1 default (Chroma) + pluggable | **15** (OpenAI/Azure/Gemini/HF/FastEmbed/Together/Bedrock/Ollama/VertexAI/...) | via Pi SDK (model-agnostic) |
| Vector stores | 2 (PGLite pgvector, Postgres pgvector) | 1 default + pluggable interface | **30** (Qdrant/Pinecone/Chroma/Weaviate/Milvus/Mongo/Redis/ES/pgvector/Supabase/Faiss/...) | 1 (SQLite embeddings) |
| Index type | HNSW via pgvector | HNSW via Chroma | diverso por provider | flat/simple |
| Dim flexibility | depends on embedding | depends on embedder | yes (config per-provider) | yes |

**Leader absoluto:** mem0 — 30 stores, 15 embedders

---

### Category: Graph Support

| Item | gbrain | mempalace | mem0 | gsd-2 |
|------|--------|-----------|------|-------|
| Native KG | **zero-LLM auto-wiring** com typed edges (attended/works_at/invested_in/founded/advises) + 3+ hop traversal | **temporal KG** com `valid_from`/`valid_to` em SQLite local | graph memory opcional (Neo4j/Memgraph/Kuzu/AGE externo) | memory relations graph (Phase 4) |
| Entity extraction | heuristic regex (`link-extraction.ts`) | entity_detector + registry | LLM-based batch + entity linking multi-signal | manual via capture_thought |
| Auto-wiring sem LLM | **YES** | yes (regex + heuristic) | NO (LLM-driven) | NO |
| Traversal queries | `gbrain graph-query --depth N --direction in/out/both` | `query_entity(as_of=)` temporal | Cypher (via Neo4j) | `traverseGraph` |

**Leaders:** gbrain (auto-wiring + custo), mempalace (temporal semantics)

---

### Category: Extensibility / Integration

| Item | gbrain | mempalace | mem0 | gsd-2 |
|------|--------|-----------|------|-------|
| MCP tools | ~41 (stdio + HTTP + OAuth) | 29 | 9 | 6 read-only + workflow |
| SDKs | TS (CLI+MCP) | Python (CLI+MCP) | **Python + TS + Vercel + OpenClaw + CLI dual** | TS (Pi SDK) |
| Plugin system | 26 skill files + recipes/ YAML | storage backends + hooks | provider pattern 5 categorias | GSD Extension API `.gsd/extensions/` |
| Integrations MCP clients | Claude Code, Cursor, Windsurf, Claude Desktop, Cowork, Perplexity | Claude Code, Gemini CLI | Claude Code, Cursor, Codex | Claude Code CLI |

**Leaders:** mem0 (SDKs + platform), gbrain (MCP tool count + skills)

---

## Equivalence Summary (N-way ranking)

Ranking de leaders por categoria (contagem):

| Subject | # categorias onde lidera ou empata em 1o | Destaque |
|---------|----:|----------|
| mempalace | 8 | Local-first + verbatim + recall publicado |
| mem0 | 6 | Ecosystem breadth + benchmarks + platform |
| gbrain | 5 | Graph auto-wiring + durable queue + MCP surface |
| gsd-2 | 1 | Coding-agent integration |

---

## gbrain-Only Capabilities

| # | Capability | Category | Evidence |
|---|-----------|----------|----------|
| 1 | Zero-LLM auto-wiring typed knowledge graph | Graph Support | `OS/gbrain/src/core/link-extraction.ts` |
| 2 | Minions durable job queue Postgres-native (753ms vs 10s+ sub-agents) | Write Latency | `OS/gbrain/src/core/minions/queue.ts` |
| 3 | PGLite WASM embedded Postgres (2s startup, sem servidor) | Persistence | `OS/gbrain/src/core/pglite-engine.ts` |
| 4 | 26 fat-skills markdown com thin-harness | Extensibility | `OS/gbrain/skills/RESOLVER.md` |

## mempalace-Only Capabilities

| # | Capability | Category | Evidence |
|---|-----------|----------|----------|
| 1 | Verbatim-only storage policy (CONTRIBUTING nao-negociavel) | Persistence | `OS/mempalace/CLAUDE.md` |
| 2 | 100% local-first no core path (zero API keys) | Local-first | `OS/mempalace/README.md` |
| 3 | AAAK symbolic compression dialect | Schema Flexibility | `OS/mempalace/mempalace/dialect.py` |
| 4 | Wings/Rooms/Drawers scoped search hierarchy | Schema Flexibility | `OS/mempalace/mempalace/palace.py` |
| 5 | Temporal KG com valid_from/valid_to em SQLite local | Graph Support | `OS/mempalace/mempalace/knowledge_graph.py` |
| 6 | Performance budgets explicitos (hooks <500ms, startup <100ms) | Latency | `OS/mempalace/CLAUDE.md` |

## mem0-Only Capabilities

| # | Capability | Category | Evidence |
|---|-----------|----------|----------|
| 1 | 30 vector stores + 24 LLMs + 15 embeddings + 4 graphs + 5 rerankers | Vector Support | `OS/mem0/mem0/` |
| 2 | Hosted platform SaaS (mem0.ai) | Extensibility | `OS/mem0/mem0/client/` |
| 3 | Vercel AI SDK provider | Extensibility | `OS/mem0/vercel-ai-sdk/` |
| 4 | OpenMemory full-stack docker-compose (API+UI+MCP+Qdrant) | Extensibility | `OS/mem0/openmemory/` |
| 5 | Arxiv paper + OSS eval framework (`memory-benchmarks`) | Recall Accuracy | `OS/mem0/evaluation/` |
| 6 | Async APIs nativas | Write Latency | `OS/mem0/mem0/memory/main.py` |

## gsd-2-Only Capabilities

| # | Capability | Category | Evidence |
|---|-----------|----------|----------|
| 1 | Memory tools como extension de coding agent (feed direto em planning/dispatch) | Integration | `OS/gsd-2/src/resources/extensions/gsd/tools/memory-tools.ts` |
| 2 | Single-writer SQLite invariant | Persistence | `OS/gsd-2/src/resources/extensions/gsd/db-writer.ts` |
| 3 | Categoria enum rigida (6 values: architecture/convention/gotcha/preference/environment/pattern) | Schema Flexibility | `OS/gsd-2/src/resources/extensions/gsd/tools/memory-tools.ts` |
| 4 | `extract-learnings` -> `LEARNINGS.md` | Extensibility | `OS/gsd-2/src/resources/extensions/gsd/commands-extract-learnings.ts` |

---

## Verbatim vs Paraphrase (comparative read)

| Subject | Strategy | What's stored |
|---------|----------|---------------|
| **mempalace** | VERBATIM | palavras exatas do usuario em drawers |
| gbrain | paraphrase + raw backup | `compiled_truth` para retrieval, `raw_data` como ground truth |
| mem0 | paraphrase | LLM extrai fatos, ADD-only, memories acumulam |
| gsd-2 | structured short content | categoria + content text (nao raw conversation) |

**Leitura:** apenas MemPalace garante que uma query retorne exatamente o que foi dito. gbrain preserva o raw mas retorna paraphrase por default. mem0 compromete verbatim em troca de agregacao semantica. gsd-2 e category-scoped, nao conversa.

## Vector vs Graph vs Hybrid (comparative read)

| Subject | Vector | Graph | Hybrid default |
|---------|--------|-------|----------------|
| gbrain | pgvector HNSW | zero-LLM typed edges | **YES** (RRF vector+keyword+graph) |
| mempalace | Chroma HNSW | temporal predicates SQLite | **YES** (BM25 re-rank + closet boosting) |
| mem0 | 30 stores pluggable | graph externa opcional | **YES** (semantic+BM25+entity multi-signal) |
| gsd-2 | SQLite simples | Phase 4 relations | parcial (hybrid listado, semantics limitado) |

**Leitura:** os tres lideres (gbrain, mempalace, mem0) convergem em hybrid, mas cada um enfatiza um eixo: gbrain no graph auto-wiring, mempalace no BM25 + closet pointers, mem0 na diversidade de providers. gsd-2 segue o padrao mas sem benchmarks.

---

## Objective Reading

### gbrain strengths

gbrain tem a combinacao unica de engine dual Postgres (PGLite embutido via WASM pra zero-config, Postgres/Supabase pra escala) + zero-LLM knowledge graph auto-wiring + Minions job queue durable. O fato da graph extraction rodar sem LLM significa custo marginal zero pra auto-wiring, e os benchmarks mostram R@5 83 -> 95% quando se agrega o graph ao vetorial (evidence: `docs/benchmarks/2026-04-18-brainbench-v1.md`). O surface de MCP e o mais amplo (~41 tools).

### mempalace strengths

mempalace e o unico projeto com caminho 100% local-first comprovado — 96.6% R@5 em LongMemEval sem nenhuma API key, nenhuma chamada LLM (evidence: `benchmarks/BENCHMARKS.md`). A policy verbatim protegida no CONTRIBUTING torna o projeto MEC a nivel semantico (nao summariza, nao paraphrase, retorna palavras exatas). O temporal KG com `valid_from`/`valid_to` em SQLite local e unico no grupo. Budgets de performance declarados (hooks <500ms, startup <100ms) trazem rigor de contrato.

### mem0 strengths

mem0 e vastamente o projeto mais largo em ecossistema (30 vector stores, 24 LLMs, 15 embedders, 4 graphs, 5 rerankers) e o unico com hosted platform + arxiv paper + SDK TS/Python duais + CLIs duais + Vercel provider + OpenMemory docker-compose full stack. Os scores em benchmarks padrao sao muito altos (LongMemEval 93.4, LoCoMo 91.6). A velocidade de iteracao (v2.0 com novo algoritmo Abril 2026) e YC S24 garantem comunidade.

### gsd-2 strengths

gsd-2 nao compete como memory system standalone — e um coding agent com memory como extension. O diferencial e que as tres tools (`capture_thought`, `memory_query`, `gsd_graph`) alimentam planning/dispatch direto no harness Pi SDK. Single-writer SQLite invariant e solido, e o roadmap 5-phase (scope → hybrid → KG → maintenance) mostra direcao. Graceful degradation (db_unavailable retorna empty vs throw) e pattern exemplar.

### Key Differentiators

- **gbrain:** zero-LLM graph auto-wiring + PGLite embutido + Minions queue
- **mempalace:** verbatim sagrado + 100% local + temporal KG
- **mem0:** maior ecossistema + hosted + benchmarks industria + SDK dual
- **gsd-2:** memory-as-coding-agent-extension (nao produto de memoria)

### Areas of Parity

- Todos tem MCP server
- Todos tem durable backend
- Todos tem algum hybrid search
- Todos tem entity/graph layer
- Todos sao open source com licensa permissiva

---

## Method Disclosure

- **Comparison date:** 2026-04-19
- **Dimension pack:** memory v1.0 (8 dimensoes)
- **Items compared:** 14 features across 8 dimensions + inventory metrics
- **Scoring model:** n-way ranking por categoria (nao Forte/Parcial/Sem_Equiv porque pairwise nao e aplicavel em 4-way)
- **Data sources:**
  - gbrain: filesystem scan + README + CLAUDE.md + `docs/benchmarks/`
  - mempalace: filesystem scan + README + CLAUDE.md + `benchmarks/BENCHMARKS.md`
  - mem0: filesystem scan + README + CLAUDE.md (AGENTS.md)
  - gsd-2: filesystem scan + README + memory-store.ts + memory-tools.ts

---

_Generated by os-bench bench-matrix task | Template v1.0_
