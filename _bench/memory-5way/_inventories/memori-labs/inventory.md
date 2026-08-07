# Inventario: Memori (memori-labs)

**Path:** `OS/memori-labs/`  
**Date:** 2026-08-06  
**Extraction Method:** filesystem-scan + doc-scan  
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | memori-labs |
| Source URL | https://github.com/MemoriLabs/Memori |
| Primary language | Python (+ TypeScript SDK + Rust core) |
| Stack | SQL multi-dialect, FAISS, BM25 hybrid, ONNX/embeddings, OpenClaw/Hermes plugins |
| License | Apache-2.0 |
| Version | 3.3.7 (`pyproject.toml`) |
| Last commit | 2026-07-28 |
| Tagline | Memory from what agents **do**, not just what they say |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| LOC (py+ts+rs ballpark) | ~69K | `wc -l` |
| Code files | ~472 | filesystem |
| LoCoMo accuracy | **87%** overall | `README.md` L128–134 |
| Tokens per query | **721** (~2.8% full-context) | `README.md` |
| Paper | arxiv.org/abs/2603.19935 | README |

## Modules

| Module | Path | Description |
|--------|------|-------------|
| Python SDK | `memori/` | Agent, Writer, search, storage drivers, LLM adapters |
| TypeScript SDK | `memori-ts/` | Paridade TS (sqlite/postgres/mysql/cockroach examples) |
| Rust core | `core/src/` | Hybrid search, augmentation, knowledge_graph storage ops |
| Benchmarks | `benchmarks/` | LoCoMo notebooks (FAISS+BM25) |
| Integrations | `docs/memori-cloud/openclaw`, `hermes` | Drop-in memory for OpenClaw & Hermes |

## Storage backends (BYODB)

Evidence: `memori/storage/drivers/` + `docs/memori-byodb/databases/`

- sqlite, postgresql, mysql, tidb, oracle, oceanbase, mongodb, cockroachdb
- adapters: sqlalchemy, django, dbapi, mongodb

## Capabilities (core)

| Capability | Evidence | Notes |
|------------|----------|-------|
| Auto capture conversation | `memori/agent.py`, README quickstart | LLM register → background persist |
| Agent-controlled recall | `Agent.recall` / `recall_summary` | explicit tools for Hermes |
| Hybrid search | `core/src/search/` (dense + BM25), `memori/search/_faiss.py` | FAISS IndexFlatIP + BM25 rerank |
| Knowledge graph tables | `core/src/storage/migrations/*` `memori_knowledge_graph` | entity/subject/predicate/object |
| Entity attribution | `memori/__init__.py` `attribution(entity_id, …)` | multi-user scoping |
| Cloud + BYODB | README Memori Cloud vs docs/memori-byodb | dual path |
| OpenClaw plugin | README L138–156 | tool calls, decisions, outcomes |
| Hermes provider | README L158–175 | `memory.provider memori` |

## Persistence model

- **Structured facts** extracted/augmented (not verbatim policy like mempalace)
- Conversations persisted; entity facts + embeddings in SQL
- Advanced Augmentation pipeline (docs + rust `augmentation/`)

## Local-first stance

- BYODB SQLite works offline for storage
- Extraction/augmentation typically needs LLM API keys
- Default product path emphasizes Memori Cloud (`MEMORI_API_KEY`)

## Not observed

- Industry multi-bench suite beyond LoCoMo (no LongMemEval/BEAM published in-repo like mem0/mempalace)
- 30-provider vector-store surface (uses SQL + FAISS, not Qdrant/Pinecone zoo)
- Zero-LLM graph auto-wiring (KG exists; extraction path is LLM-centric)
