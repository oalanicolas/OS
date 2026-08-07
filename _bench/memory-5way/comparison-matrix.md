# Comparison Matrix: memory-5way

**Date:** 2026-08-06  
**Type:** nway  
**Pack:** memory  
**Subjects:** gbrain · mempalace · mem0 · memori-labs · gsd-2

---

## Method

Matriz a partir de scan local em `OS/{subject}/`. Claims de benchmark só com fonte no tree ou README citando paper. memori-labs entra como 5º sujeito (ausente no memory-4way de 2026-04-19).

## Inventory snapshot

| Metric | gbrain | mempalace | mem0 | memori-labs | gsd-2 |
|--------|--------|-----------|------|-------------|-------|
| Version | 0.42.73.2 | 3.6.0 | 2.0.17 | 3.3.7 | 3.0.0 (gsd-pi) |
| Primary lang | TypeScript | Python | Python+TS | Python+TS+Rust | TypeScript |
| License | MIT | MIT | Apache-2.0 | Apache-2.0 | MIT |
| Memory = core product? | YES | YES | YES | YES | NO (side-feature) |
| Last commit (clone) | 2026-08-05 | 2026-07-17 | 2026-08-06 | 2026-07-28 | 2026-05-22 |

---

## Feature matrix by category

### Recall Accuracy

| Item | gbrain | mempalace | mem0 | memori-labs | gsd-2 |
|------|--------|-----------|------|-------------|-------|
| Public bench | BrainBench custom R@5 **97.9%**, P@5 49.1% | LongMemEval R@5 **96.6%** raw / 100% hybrid | LoCoMo **92.5**, LongMemEval **94.4**, BEAM1M **64.1** | LoCoMo **87%** QA @ 721 tok | none |
| Industry datasets | no (custom Opus corpus) | YES (LongMemEval) | YES (LoCoMo, LongMemEval, BEAM) | YES (LoCoMo notebooks) | — |
| Metric type | retrieval P/R@k | retrieval R@5 | end-to-end QA-style scores | end-to-end accuracy | — |
| Eval harness in-repo | yes (`evals/`, `docs/eval*`) | yes (`benchmarks/`) | yes (`evaluation/`) | yes (`benchmarks/*.ipynb`) | no |

**Leaders:** mempalace + mem0 (rigor público); gbrain (retrieval max no corpus próprio); memori (forte em token-efficiency).

### Write / Read latency

| Item | gbrain | mempalace | mem0 | memori-labs | gsd-2 |
|------|--------|-----------|------|-------------|-------|
| Batch / async write | YES (unnest batch + Minions) | incremental | YES AsyncMemory | Writer + async API | sync single-writer |
| Durable job queue | YES Minions | no | no | background capture | no |
| Published p50 | no | budgets &lt;500ms hooks | 0.88–1.09s e2e | 721 tok/query cost focus | no |
| Index / read path | HNSW pgvector + hybrid RRF | Chroma/HNSW + BM25 rerank | per-store | FAISS + BM25 hybrid (Rust) | FTS5 + optional embed |

**Leaders:** gbrain (batch+queue), mem0 (p50 published), memori (hybrid core).

### Persistence (verbatim vs paraphrase)

| Item | gbrain | mempalace | mem0 | memori-labs | gsd-2 |
|------|--------|-----------|------|-------------|-------|
| Strategy | paraphrase (`compiled_truth`) + raw JSONB | **VERBATIM** non-negotiable | LLM fact extract (paraphrase) | structured facts + conversations | 6-category structured |
| Durable backend | PGLite / Postgres | Chroma + SQLite KG (+ more backends) | many vector DBs | multi SQL + Mongo | SQLite |
| Versioning | page_versions | append-only drawers | memory history API | entity facts + sessions | superseded chains |

**Leader (fidelity):** mempalace.

### Schema flexibility

| Item | gbrain | mempalace | mem0 | memori-labs | gsd-2 |
|------|--------|-----------|------|-------------|-------|
| Model | pages/chunks/links/timeline + **schema packs** | drawers schemaless + entity registry | memories + metadata + user/agent/run | entity attribution + facts + KG triples | enum 6 categories |
| Multi-tenant | company brain + source isolation + write fence | wings/rooms scope | user/agent/run_id | entity_id attribution | project-scoped |

**Leaders:** memori-labs (BYODB breadth + attribution), mem0 (metadata scoping).

### Local-first

| Item | gbrain | mempalace | mem0 | memori-labs | gsd-2 |
|------|--------|-----------|------|-------------|-------|
| Zero API core path | NO (embed/rerank keys typical) | **YES** | NO | partial (SQLite BYODB; LLM usual) | hybrid |
| Offline | partial | **YES** | partial | partial | partial |
| Telemetry | none observed | zero policy | PostHog in client | cloud API path | RTK flag |

**Leader:** mempalace.

### Vector support

| Item | gbrain | mempalace | mem0 | memori-labs | gsd-2 |
|------|--------|-----------|------|-------------|-------|
| Stores | pgvector (PGLite/PG) | chroma, qdrant, milvus, pgvector, sqlite_exact | **24** modules | SQL store + FAISS in-process | SQLite embeddings |
| Embed providers | multi via AI gateway (OpenAI, Voyage, ZE, …) | default Chroma + pluggable | **11** modules | HF/ONNX/TEI/API embeddings | via Pi model discovery |
| Index | HNSW | HNSW (Chroma) etc. | per provider | IndexFlatIP + BM25 | flat/FTS |

**Leader:** mem0.

### Graph support

| Item | gbrain | mempalace | mem0 | memori-labs | gsd-2 |
|------|--------|-----------|------|-------------|-------|
| Auto-wiring | **zero-LLM** typed edges on write | temporal KG | LLM + external graph DB | `memori_knowledge_graph` tables (Rust) | memory_relations |
| Traversal | `graph-query` multi-hop + relational retrieval | as-of temporal queries | depends on backend | entity/subject/predicate/object | limited |
| Temporal | Life Chronicle bi-temporal | valid_from/to first-class | limited | session/conversation time | hit-count decay |

**Leader:** gbrain.

---

## Positioning one-liners

| Subject | One-liner |
|---------|-----------|
| **gbrain** | Institutional knowledge brain: synthesis + zero-LLM graph + dream cycle |
| **mempalace** | Verbatim local palace: max recall fidelity, zero API |
| **mem0** | Universal memory SDK: any vector store, any embedder, hosted option |
| **memori-labs** | Agent-action memory: what the agent *did*, SQL-native, OpenClaw/Hermes |
| **gsd-2** | Coding-agent tribal memory only — not a memory product |
