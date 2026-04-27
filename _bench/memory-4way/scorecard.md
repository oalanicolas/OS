# Scorecard: memory-4way (gbrain vs mempalace vs mem0 vs gsd-2)

**Date:** 2026-04-19
**Dimension pack:** memory (8 dimensoes)
**Slug:** memory-4way
**Overall Confidence:** HIGH

---

## Scoring Method

- Score range: 0-100 por dimensao
- Pesos do pack `memory` (soma = 1.00): recall_accuracy 0.22, write_latency 0.10, read_latency 0.12, persistence 0.12, schema_flexibility 0.10, local_first 0.13, vector_support 0.11, graph_support 0.10
- Cada score derivado de 2+ signals documentados com evidence path
- Signal ausente -> score reduzido e confidence rebaixada
- Fonte primaria: filesystem (`OS/{subject}/`)

---

## Dimension Scores (N-way)

| Dimension | Weight | gbrain | mempalace | mem0 | gsd-2 | Confidence | Leader |
|-----------|-------:|:------:|:---------:|:----:|:-----:|:----------:|:------:|
| Recall Accuracy | 22% | 78 | **92** | 90 | 35 | HIGH | mempalace |
| Write Latency | 10% | **80** | 65 | 78 | 55 | MEDIUM | gbrain |
| Read Latency | 12% | **78** | 75 | 72 | 60 | MEDIUM | gbrain |
| Persistence | 12% | 80 | **95** | 72 | 65 | HIGH | mempalace |
| Schema Flexibility | 10% | 75 | 80 | **85** | 55 | HIGH | mem0 |
| Local-first | 13% | 55 | **95** | 40 | 60 | HIGH | mempalace |
| Vector Support | 11% | 72 | 65 | **98** | 45 | HIGH | mem0 |
| Graph Support | 10% | **92** | 85 | 70 | 55 | HIGH | gbrain |

---

## Weighted Total

| Subject | Weighted Score | Dim wins |
|---------|:-------------:|:--------:|
| **mempalace** | **83.14/100** | 3 (recall, persistence, local-first) |
| **mem0** | **76.36/100** | 2 (schema, vector) |
| **gbrain** | **75.89/100** | 3 (write, read, graph) |
| **gsd-2** | **51.95/100** | 0 |

**Overall Winner:** mempalace (+6.78 vs mem0, +7.25 vs gbrain, +31.19 vs gsd-2)

---

## Dimension Analysis

### Recall Accuracy (22%)

**gbrain: 78 | mempalace: 92 | mem0: 90 | gsd-2: 35** | Confidence: HIGH

mempalace e mem0 publicam benchmarks industria-padrao (LongMemEval, LoCoMo) com metricas reproduziveis. mempalace lidera levemente com 96.6% R@5 raw sem LLM + 98.4% held-out. mem0 tem scores fortes em tres benchmarks (93.4 LongMemEval, 91.6 LoCoMo, 64.1 BEAM 1M) e publica arxiv paper. gbrain usa corpus Opus proprio (BrainBench) — R@5 vai de 83% -> 95% com hybrid+graph, mas a comparabilidade com peers e limitada porque o dataset e idiosincratico. gsd-2 nao publica metrica de recall.

**Key signals:**
- gbrain: R@5 95% BrainBench proprio — `OS/gbrain/docs/benchmarks/2026-04-18-brainbench-v1.md`
- mempalace: R@5 96.6% raw LongMemEval — `OS/mempalace/benchmarks/BENCHMARKS.md`
- mem0: LongMemEval 93.4, LoCoMo 91.6, BEAM(1M) 64.1 — `OS/mem0/README.md`
- gsd-2: not_observed

---

### Write Latency (10%)

**gbrain: 80 | mempalace: 65 | mem0: 78 | gsd-2: 55** | Confidence: MEDIUM

gbrain tem batch-write via `unnest` (4-5 params regardless de tamanho, evita o cap de 65535 parametros do Postgres) + Minions job queue durable (753ms vs 10s+ em sub-agents conforme benchmark de producao). mem0 tem AsyncMemory/AsyncMemoryClient full async + p50 publicado end-to-end. mempalace declara budgets mas nao tem batch/async explicito. gsd-2 e sync com single-writer invariant (correto, nao performante).

**Key signals:**
- gbrain: addLinksBatch via unnest — `OS/gbrain/src/core/postgres-engine.ts`
- mem0: AsyncMemory + p50 0.88-1.09s — `OS/mem0/mem0/memory/main.py`
- mempalace: hooks <500ms budget — `OS/mempalace/CLAUDE.md`
- gsd-2: sync writes — `OS/gsd-2/src/resources/extensions/gsd/db-writer.ts`

---

### Read Latency (12%)

**gbrain: 78 | mempalace: 75 | mem0: 72 | gsd-2: 60** | Confidence: MEDIUM

gbrain tem HNSW via pgvector + statement_timeout scoped per transaction (v0.12.3) + clampSearchLimit per-operation caps — sinais solidos de tuning. mempalace tem budget <100ms startup injection e BM25 re-rank sobre small candidate set. mem0 p50 publicado e end-to-end (inclui LLM). gsd-2 e SQLite local simples.

**Key signals:**
- gbrain: statement_timeout scoping — `OS/gbrain/src/core/postgres-engine.ts`
- mempalace: startup <100ms budget — `OS/mempalace/CLAUDE.md`
- mem0: p50 1.00s-1.09s end-to-end — `OS/mem0/README.md`
- gsd-2: SQLite queries — `OS/gsd-2/src/resources/extensions/gsd/memory-store.ts`

---

### Persistence (12%)

**gbrain: 80 | mempalace: 95 | mem0: 72 | gsd-2: 65** | Confidence: HIGH

Esta dimensao separa os projetos pela politica de storage. mempalace tem a melhor pontuacao porque combina verbatim obrigatorio + durable backend (ChromaDB+SQLite) + append-only + crash-safe explicito. gbrain preserva raw em JSONB mas retorna paraphrase (compiled_truth) por default. mem0 e paraphrase-first puro (LLM extrai fatos, nao guarda conversa). gsd-2 e category-scoped (nao guarda conversa inteira, so "architecture/convention/gotcha" etc).

**Key signals:**
- mempalace: verbatim policy + crash-safe — `OS/mempalace/CLAUDE.md`
- gbrain: compiled_truth + raw_data JSONB — `OS/gbrain/src/core/operations.ts`
- mem0: LLM facts ADD-only — `OS/mem0/mem0/configs/prompts.py`
- gsd-2: structured content — `OS/gsd-2/src/resources/extensions/gsd/memory-store.ts`

---

### Schema Flexibility (10%)

**gbrain: 75 | mempalace: 80 | mem0: 85 | gsd-2: 55** | Confidence: HIGH

mem0 lidera com metadata Pydantic + multi-level scoping (user_id/agent_id/run_id) + graph opcional Neo4j. mempalace tem drawers schemaless + entity registry com disambiguation. gbrain tem schema rigido mas frontmatter JSONB permite extensao. gsd-2 tem 6 categorias enum fixas (architecture/convention/gotcha/preference/environment/pattern) com `structured_fields` JSON opcional — mais restritivo.

---

### Local-first (13%)

**gbrain: 55 | mempalace: 95 | mem0: 40 | gsd-2: 60** | Confidence: HIGH

mempalace e o unico 100% local-first por design: 96.6% R@5 raw sem nenhuma API key, zero telemetry policy, works offline, data ownership explicit. mem0 tem posthog em dependencies core + OpenAI obrigatorio default (score mais baixo). gbrain tem DB local (PGLite WASM) mas embedding requer OpenAI — quebra local-first puro. gsd-2 tem SQLite local + RTK_TELEMETRY_DISABLED forced mas LLM depende de provider.

**Key signals:**
- mempalace: zero API core + zero telemetry — `OS/mempalace/README.md`, `OS/mempalace/CLAUDE.md`
- mem0: posthog em deps core — `OS/mem0/pyproject.toml`
- gbrain: OpenAI embedding required — `OS/gbrain/src/core/embedding.ts`
- gsd-2: RTK telemetry disabled forced — `OS/gsd-2/README.md`

---

### Vector Support (11%)

**gbrain: 72 | mempalace: 65 | mem0: 98 | gsd-2: 45** | Confidence: HIGH

mem0 domina absolutamente com 30 vector stores + 15 embedding providers + HNSW/IVF per-provider + dim flexibility. gbrain tem HNSW via pgvector mas lock-in em OpenAI text-embedding-3-large. mempalace tem ChromaDB default + pluggable interface (1 provider default limita o score). gsd-2 usa SQLite simples pra memorias de coding agent.

---

### Graph Support (10%)

**gbrain: 92 | mempalace: 85 | mem0: 70 | gsd-2: 55** | Confidence: HIGH

gbrain lidera com zero-LLM auto-wiring (heuristicas regex pra typed edges attended/works_at/invested_in/founded/advises/source/mentions) + 3+ hop traversal via `gbrain graph-query`. mempalace tem temporal KG em SQLite local com valid_from/valid_to — unico com temporal semantics. mem0 graph e forte mas requer backend externo (Neo4j/Memgraph/Kuzu/AGE) + extraction LLM-based. gsd-2 tem memory relations simples (Phase 4).

**Key signals:**
- gbrain: zero-LLM link-extraction — `OS/gbrain/src/core/link-extraction.ts`
- mempalace: temporal valid_from/valid_to — `OS/mempalace/mempalace/knowledge_graph.py`
- mem0: Neo4j/Memgraph/Kuzu/AGE externos — `OS/mem0/mem0/graphs/`
- gsd-2: Phase 4 traverseGraph — `OS/gsd-2/src/resources/extensions/gsd/tools/memory-tools.ts`

---

## Score Distribution

### gbrain Profile
- Strongest: **Graph Support** (92) + Write Latency (80) + Persistence (80)
- Weakest: **Local-first** (55) pela dependencia em OpenAI embeddings
- Weighted: 75.89

### mempalace Profile
- Strongest: **Local-first** (95) + Persistence (95) + Recall Accuracy (92)
- Weakest: **Vector Support** (65) pelo single-provider default
- Weighted: 83.14

### mem0 Profile
- Strongest: **Vector Support** (98) + Recall Accuracy (90) + Schema Flexibility (85)
- Weakest: **Local-first** (40) pela telemetria core + OpenAI default
- Weighted: 76.36

### gsd-2 Profile
- Strongest: **Read Latency** (60) + Schema Flexibility + Persistence (ambos 65)
- Weakest: **Recall Accuracy** (35) e **Vector Support** (45) — nao e memory-first
- Weighted: 51.95

### Competitive Dimensions (|delta| < 5)
- **Recall Accuracy**: mempalace 92 vs mem0 90 (delta 2)
- **Write Latency**: gbrain 80 vs mem0 78 (delta 2)
- **Read Latency**: gbrain 78 vs mempalace 75 (delta 3)

---

## Confidence Disclosure

| Subject | Confidence | Reason |
|---------|-----------|--------|
| gbrain | HIGH | README, CLAUDE.md, 4 benchmarks docs, codigo rico |
| mempalace | HIGH | CLAUDE.md detalhado, benchmarks in-tree reproduziveis |
| mem0 | HIGH | README rich + polyglot structure mapeada, arxiv paper |
| gsd-2 | MEDIUM | Memoria e side-feature, sem benchmarks publicos de memoria |

### Sources

- **gbrain**: filesystem `OS/gbrain/` + `CLAUDE.md` + `docs/benchmarks/`
- **mempalace**: filesystem `OS/mempalace/` + `CLAUDE.md` + `benchmarks/BENCHMARKS.md`
- **mem0**: filesystem `OS/mem0/` + `CLAUDE.md` (AGENTS.md)
- **gsd-2**: filesystem `OS/gsd-2/` + `README.md` + `memory-store.ts`

### Dimension Pack

| Pack | Version | Designed For |
|------|---------|-------------|
| memory | 1.0 | Sistemas de memoria, RAG, knowledge graphs |

### Scoring Transparency

Todos os scores acima derivam de signals documentados na seção "Signals observed" do JSON. Nenhum score >= 90 foi atribuido sem 2+ signals verificaveis com evidence path. Quando um signal nao pode ser observado (gsd-2 sem recall benchmark), o score foi reduzido e marcado "not_observed".

### Known Limitations

- Benchmarks de recall citados sao self-reported pelos projetos (gbrain BrainBench proprio, mempalace LongMemEval in-tree, mem0 README)
- gsd-2 nao expõe p50/p99 nem metrica de recall, penalizando por ausencia de measurement
- Latency p50 do mem0 e end-to-end (inclui LLM), nao write/read puro
- "Local-first" foi pontuado por zero API keys + zero telemetry + offline — mempalace lidera nos tres

---

_Generated by os-bench bench-score task | Template v1.0_
