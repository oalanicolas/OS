# Inventario: Mem0

**Path:** `OS/mem0/`
**Date:** 2026-04-19
**Extraction Method:** filesystem-scan + doc-scan
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | mem0 |
| Source URL | https://github.com/mem0ai/mem0 |
| Primary language | Python |
| Secondary languages | TypeScript, JavaScript, Markdown |
| Stack | Python 3.9+, Node 20/22, FastAPI, Qdrant, pgvector, Neo4j, Pydantic v2, Next.js 15, React 19 |
| License | Apache-2.0 |
| Tagline | Memory layer para AI agents; 91.6 LoCoMo, 93.4 LongMemEval, 64.1 BEAM(1M); hosted + self-hosted; YC S24 |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| LOC (ballpark) | ~125K | `wc -l` em *.py/*.ts (sem embedchain) |
| Files | 1,274 | filesystem scan |
| Top-level dirs | 16 (mem0, mem0-ts, cli, server, openmemory, vercel-ai-sdk, openclaw, evaluation, docs, ...) | filesystem scan |
| Version | 2.0.0 | `pyproject.toml` |
| Last commit | 2026-04-18 | `git log -1` |

## Modules

| Module | Path | Type | LOC estimate | Description |
|--------|------|------|--------------|-------------|
| mem0 | `mem0/` | package | ~60K | Core Python SDK |
| mem0-ts | `mem0-ts/` | package | ~10K | TypeScript SDK |
| cli/python | `cli/python/` | app | ~5K | Typer CLI |
| cli/node | `cli/node/` | app | ~3K | Commander CLI |
| server | `server/` | service | ~4K | FastAPI + PG/pgvector + Neo4j |
| openmemory | `openmemory/` | service | ~15K | FastAPI + Next.js + Qdrant + MCP |
| vercel-ai-sdk | `vercel-ai-sdk/` | package | ~2.5K | @mem0/vercel-ai-provider |
| openclaw | `openclaw/` | package | ~2K | Plugin MCP para Claude/Cursor/Codex |
| evaluation | `evaluation/` | library | ~6K | LOCOMO evals + runner |

## External Dependencies (core + top)

| Package | Version | Purpose |
|---------|---------|---------|
| qdrant-client | >=1.12.0 | vector store default (CORE) |
| openai | >=1.90.0 | LLM + embedding default |
| pydantic | >=2.7.3 | data models |
| posthog | >=4.5.0 | telemetry (core dep) |
| sqlalchemy | >=2.0.31 | metadata SQLite |
| spacy | >=3.7.0 | nlp extra (BM25+entity) |
| chromadb | >=0.4.24 | vector store optional |
| litellm | >=1.74.0 | llms extra (multi-provider) |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| CLI Python | `cli/python/src/mem0_cli/app.py` | `mem0` (pip) |
| CLI Node | `cli/node/src/index.ts` | `mem0` (@mem0/cli npm) |
| HTTP server | `server/main.py` | `uvicorn` + docker-compose |
| OpenMemory API | `openmemory/api/main.py` | FastAPI + Alembic + MCP |
| Library | `mem0/memory/main.py` | `from mem0 import Memory` |

## Capabilities (core)

| Capability | Evidence | Notes |
|------------|----------|-------|
| ADD-only single-pass extraction | `mem0/memory/main.py`, `mem0/configs/prompts.py` | Abril 2026 algo: memories acumulam |
| Multi-signal retrieval (semantic+BM25+entity) | `mem0/utils/scoring.py`, `mem0/utils/lemmatization.py` | `ENTITY_BOOST_WEIGHT` explicito |
| 30 vector stores | `mem0/vector_stores/` | Qdrant, Pinecone, Chroma, Weaviate, Milvus, pgvector, Supabase, Faiss, etc |
| 24 LLM providers | `mem0/llms/` | OpenAI, Anthropic, Bedrock, Groq, Ollama, vLLM, etc |
| 15 embedding providers | `mem0/embeddings/` | OpenAI, Azure, Gemini, HF, FastEmbed, Ollama |
| 4 graph stores | `mem0/graphs/` | Neo4j, Memgraph, Kuzu, Apache AGE |
| 5 rerankers | `mem0/reranker/` | Cohere, HF, LLM-based, ST, Zero Entropy |
| Multi-Level Memory (User/Session/Agent) | `mem0/memory/main.py` | `user_id`/`agent_id`/`run_id` |
| Hosted platform | `mem0/client/` | MemoryClient SaaS |
| OpenMemory self-hosted UI | `openmemory/ui/` | Next.js 15 + Redux Toolkit |
| Vercel AI SDK provider | `vercel-ai-sdk/` | `@mem0/vercel-ai-provider` |
| OpenClaw plugin (9 MCP tools) | `openclaw/`, `mem0-plugin/` | Claude/Cursor/Codex |
| Async APIs | `mem0/memory/main.py` | `AsyncMemory`, `AsyncMemoryClient` |

## Benchmarks published (from README)

| Benchmark | Old | New | Tokens | Latency p50 |
|-----------|-----|-----|--------|-------------|
| LoCoMo | 71.4 | **91.6** | 7.0K | 0.88s |
| LongMemEval | 67.8 | **93.4** | 6.8K | 1.09s |
| BEAM (1M) | — | **64.1** | 6.7K | 1.00s |
| BEAM (10M) | — | **48.6** | 6.9K | 1.05s |

## Tests / Quality

| Signal | Value | Evidence |
|--------|-------|----------|
| Test framework | pytest + jest + vitest | `Makefile`, CI workflows |
| Linter | ruff (120) + Biome + ESLint | varia por pacote |
| CI | GitHub Actions (6 workflows) | `.github/workflows/` |

## Extension Points

| Type | Where | How |
|------|-------|-----|
| Providers | `mem0/{llms,embeddings,vector_stores,graphs,reranker}/base.py` | Abstract + configs |
| MCP tools | `mem0-plugin/`, `openmemory/api/` | 9 tools (add/search/get/update/delete) |
| CLI | `cli/{python,node}/` | Separate entry points |

## Notable Design Decisions

- Provider pattern consistente em 5 categorias (base.py + configs.py)
- Pydantic v2 pra toda config/data
- ADD-only: nao sobrescreve memoria, acumula (Abril 2026)
- Paraphrase-first: LLM extrai fatos (nao verbatim)
- Hosted + self-hosted duais

## Limitations

- Telemetry (posthog) em dependencies core — nao local-first por default
- OpenAI default para LLM + embedding (API key pra caminho happy)
- Paraphrase-first — summarized memories
- Graph memory requer Neo4j/Memgraph externo (nao embutido)

## Unique Selling Points

- Maior ecossistema: 24 LLMs + 30 VS + 15 embeddings + 4 graphs + 5 rerankers
- Hosted + self-hosted + docker-compose OpenMemory full stack
- Arxiv paper + eval framework OSS
- Polyglot: Python core + TS SDK + CLIs + UI + Vercel AI + OpenClaw
- YC S24 + maior stars/downloads do nicho (sinal de comunidade)

---

_Generated by os-bench inventory task | Template v1.0_
