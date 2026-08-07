# Scorecard: mempalace vs gbrain

**Date:** 2026-08-06  
**Pack:** memory  
**Confidence:** HIGH  
**Slug:** mempalace-vs-gbrain

---

## Dimension scores

| Dimension | Weight | mempalace | gbrain | Δ | Winner |
|-----------|-------:|:---------:|:------:|--:|:------:|
| Recall Accuracy | 22% | **93** | 80 | +13 | mempalace |
| Write Latency | 10% | 65 | **82** | −17 | gbrain |
| Read Latency | 12% | 75 | **80** | −5 | gbrain |
| Persistence | 12% | **95** | 82 | +13 | mempalace |
| Schema Flexibility | 10% | **80** | 78 | +2 | mempalace (narrow) |
| Local-first | 13% | **95** | 58 | +37 | mempalace |
| Vector Support | 11% | 72 | **78** | −6 | gbrain |
| Graph Support | 10% | 86 | **94** | −8 | gbrain |
| **Weighted total** | **100%** | **84.23** | **78.56** | **+5.67** | **mempalace** |

**Dim wins:** mempalace 4 · gbrain 4 — empate em contagem; mempalace vence no peso (recall + local-first + persistence).

---

## Why each dimension

### Recall (+13 mempalace)
- mempalace: LongMemEval R@5 **96.6% raw** (zero LLM) — `OS/mempalace/benchmarks/BENCHMARKS.md`
- gbrain: BrainBench R@5 **97.9%** mas corpus Opus custom; não industry-standard — `OS/gbrain/README.md`
- Score penaliza gbrain na comparabilidade, não no número bruto

### Write latency (+17 gbrain)
- gbrain: batch `unnest` + Minions durable queue + pace — `README.md`, CHANGELOG v0.42.49
- mempalace: incremental drawers; hook budgets; sem job queue durable

### Read latency (+5 gbrain)
- gbrain: HNSW pgvector + hybrid RRF + autocut + explain
- mempalace: Chroma HNSW + hybrid opcional; muito rápido no path raw

### Persistence (+13 mempalace)
- mempalace: **VERBATIM** non-negotiable (CONTRIBUTING/README)
- gbrain: `compiled_truth` paraphrase + raw JSONB backup

### Schema (+2 mempalace)
- mempalace: drawers schemaless + wings/rooms + entity registry
- gbrain: schema packs BYO (v0.39+) + frontmatter — quase empatado; slight edge mempalace por zero friction

### Local-first (+37 mempalace) — maior delta
- mempalace: zero API no core, offline, zero telemetry
- gbrain: PGLite local, mas embeddings/rerank/synthesis exigem API keys

### Vector (+6 gbrain)
- gbrain: multi-provider AI gateway + pgvector HNSW
- mempalace: 5 backends (chroma/qdrant/milvus/pgvector/sqlite_exact) mas embed path mais simples

### Graph (+8 gbrain)
- gbrain: zero-LLM typed edges on write + multi-hop + relational retrieval + Chronicle
- mempalace: temporal KG first-class (`valid_from`/`valid_to`, `as_of`) — excelente, mas wiring não é free no write path da mesma forma
