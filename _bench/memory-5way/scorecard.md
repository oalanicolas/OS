# Scorecard: memory-5way

**Date:** 2026-08-06  
**Pack:** memory (8 dimensions, weights sum 1.00)  
**Confidence overall:** HIGH  
**Supersedes:** memory-4way (2026-04-19)

---

## Dimension scores

| Dimension | Weight | gbrain | mempalace | mem0 | memori-labs | gsd-2 | Leader |
|-----------|-------:|:------:|:---------:|:----:|:-----------:|:-----:|:------:|
| Recall Accuracy | 22% | 80 | **93** | 92 | 85 | 38 | mempalace |
| Write Latency | 10% | **82** | 65 | 80 | 76 | 55 | gbrain |
| Read Latency | 12% | **80** | 75 | 74 | 76 | 60 | gbrain |
| Persistence | 12% | 82 | **95** | 72 | 78 | 65 | mempalace |
| Schema Flexibility | 10% | 78 | 80 | 86 | **88** | 55 | memori-labs |
| Local-first | 13% | 58 | **95** | 40 | 55 | 60 | mempalace |
| Vector Support | 11% | 78 | 72 | **98** | 70 | 48 | mem0 |
| Graph Support | 10% | **94** | 86 | 72 | 80 | 55 | gbrain |
| **Weighted total** | **100%** | **78.56** | **84.23** | **77.54** | **76.43** | **52.94** | **mempalace** |

### Weighted totals (sorted)

| Rank | Subject | Score | Dim wins |
|-----:|---------|------:|:--------:|
| 1 | **mempalace** | **84.23** | 3 |
| 2 | **gbrain** | **78.56** | 3 |
| 3 | **mem0** | **77.54** | 1 |
| 4 | **memori-labs** | **76.43** | 1 |
| 5 | **gsd-2** | **52.94** | 0 |

Delta vs memory-4way (same 4 subjects): gbrain 75.89→**78.56** (+2.7); mem0 76.36→**77.54** (+1.2); mempalace 83.14→**84.23** (+1.1); gsd-2 ~flat. **gbrain ultrapassa mem0** no total ponderado (antes 3º).

---

## Score rationales (2+ signals each)

### Recall Accuracy (22%)

| Subject | Score | Signals |
|---------|------:|---------|
| mempalace | 93 | LongMemEval R@5 96.6% raw; hybrid 100% optional — `benchmarks/BENCHMARKS.md` |
| mem0 | 92 | LoCoMo 92.5, LongMemEval 94.4, BEAM 64.1 — `README.md` table |
| memori-labs | 85 | LoCoMo 87% accuracy @ 721 tok; in-repo notebooks — `README.md`, `benchmarks/` |
| gbrain | 80 | R@5 97.9% / P@5 49.1% BrainBench custom — `README.md`; not industry dataset |
| gsd-2 | 38 | no published recall metric |

### Write Latency (10%)

| Subject | Score | Signals |
|---------|------:|---------|
| gbrain | 82 | batch unnest writes; Minions durable queue; pace for backfills — README + CHANGELOG v0.42.49 |
| mem0 | 80 | AsyncMemory; published 0.88–1.09s e2e |
| memori-labs | 76 | Writer path + async API client; background capture |
| mempalace | 65 | incremental; hook budgets; no batch queue |
| gsd-2 | 55 | sync single-writer |

### Read Latency (12%)

| Subject | Score | Signals |
|---------|------:|---------|
| gbrain | 80 | HNSW + hybrid RRF + autocut + explain path — README search section |
| memori-labs | 76 | FAISS + BM25 two-stage hybrid in Rust core — `core/src/search/` |
| mempalace | 75 | Chroma HNSW + budgets |
| mem0 | 74 | e2e includes LLM; store-dependent |
| gsd-2 | 60 | FTS5 / simple embed |

### Persistence (12%)

| Subject | Score | Signals |
|---------|------:|---------|
| mempalace | 95 | explicit VERBATIM policy; no paraphrase |
| gbrain | 82 | compiled_truth + raw_data; page_versions; company isolation |
| memori-labs | 78 | SQL facts + conversations durable; not verbatim-first |
| mem0 | 72 | paraphrase facts; history API |
| gsd-2 | 65 | structured categories only |

### Schema Flexibility (10%)

| Subject | Score | Signals |
|---------|------:|---------|
| memori-labs | 88 | 8+ SQL/NoSQL drivers; entity attribution; KG triples |
| mem0 | 86 | rich metadata + user/agent/run scoping |
| mempalace | 80 | schemaless drawers + entity registry |
| gbrain | 78 | schema packs BYO + frontmatter JSONB (↑ since packs) |
| gsd-2 | 55 | fixed 6-category enum |

### Local-first (13%)

| Subject | Score | Signals |
|---------|------:|---------|
| mempalace | 95 | zero API core; offline; no telemetry |
| gsd-2 | 60 | local SQLite; LLM optional |
| gbrain | 58 | PGLite local DB; embed/rerank keys usual |
| memori-labs | 55 | BYODB local possible; Cloud + LLM default story |
| mem0 | 40 | PostHog client path; hosted Platform first |

### Vector Support (11%)

| Subject | Score | Signals |
|---------|------:|---------|
| mem0 | 98 | 24 vector_store modules; 11 embedding modules |
| gbrain | 78 | multi-provider gateway + pgvector HNSW (↑ from single OpenAI era) |
| mempalace | 72 | 5 backends (chroma/qdrant/milvus/pgvector/sqlite_exact) |
| memori-labs | 70 | FAISS in-proc + SQL embeddings; not multi-store zoo |
| gsd-2 | 48 | optional SQLite embeddings |

### Graph Support (10%)

| Subject | Score | Signals |
|---------|------:|---------|
| gbrain | 94 | zero-LLM typed edges; multi-hop; relational retrieval; Chronicle |
| mempalace | 86 | temporal KG valid_from/to |
| memori-labs | 80 | `memori_knowledge_graph` in Rust migrations + ops |
| mem0 | 72 | optional external graph + LLM extract |
| gsd-2 | 55 | memory_relations only |

---

## Confidence notes

- **HIGH** for mempalace/mem0/gbrain public claims (in-repo docs).
- **MEDIUM** cross-comparing R@5 retrieval (mempalace/gbrain) vs QA accuracy (mem0/memori) — metrics not identical; scores penalize incomparability slightly on gbrain custom corpus.
- memori-labs LoCoMo is strong on **token efficiency** (721 tok) more than raw top-line accuracy vs mem0 92.5.
