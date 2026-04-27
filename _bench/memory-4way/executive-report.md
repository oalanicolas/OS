# Executive Report: memory-4way (gbrain vs mempalace vs mem0 vs gsd-2)

**Date:** 2026-04-19
**Type:** nway
**Slug:** memory-4way
**Dimension pack:** memory

---

## Executive Summary

Esta comparacao analisa quatro projetos opensource que oferecem camadas de memoria para agentes de IA: **gbrain** (Postgres-native, PGLite default), **mempalace** (verbatim local-first Python), **mem0** (ecossistema mais amplo, YC S24, hosted+OSS), e **gsd-2** (memoria como extension dentro de um coding agent). Em scoring ponderado pelo pack `memory` (8 dimensoes, pesos somando 1.00), **mempalace lidera com 83.14/100**, vencendo por Recall Accuracy + Persistence (verbatim) + Local-first. **mem0** (76.36) vence Vector Support e Schema Flexibility com o maior ecossistema de providers. **gbrain** (75.89) vence Graph Support (zero-LLM auto-wiring) e Latencia de Write/Read. **gsd-2** (51.95) nao e memory-first — e um coding agent com memoria como feature lateral, reflete em scores baixos em Recall e Vector Support. A decisao entre os tres lideres depende de qual eixo pesa: **verbatim + local-first** (mempalace), **ecossistema + hosted** (mem0), **graph Postgres-native** (gbrain).

---

## Key Metrics

| Metric | Value |
|--------|-------|
| Overall Winner | **mempalace** (83.14/100) |
| Runners-up | mem0 (76.36), gbrain (75.89), gsd-2 (51.95) |
| Dimensions analyzed | 8 (memory pack v1.0) |
| gbrain dim wins | 3 (graph, write_latency, read_latency) |
| mempalace dim wins | 3 (recall, persistence, local_first) |
| mem0 dim wins | 2 (vector, schema_flex) |
| gsd-2 dim wins | 0 |
| Features compared | 14 across 8 categories |
| Confidence overall | HIGH |

---

## Scorecard Summary

| Dimension | Weight | gbrain | mempalace | mem0 | gsd-2 |
|-----------|:------:|:------:|:---------:|:----:|:-----:|
| Recall Accuracy | 22% | 78 | **92** | 90 | 35 |
| Write Latency | 10% | **80** | 65 | 78 | 55 |
| Read Latency | 12% | **78** | 75 | 72 | 60 |
| Persistence | 12% | 80 | **95** | 72 | 65 |
| Schema Flexibility | 10% | 75 | 80 | **85** | 55 |
| Local-first | 13% | 55 | **95** | 40 | 60 |
| Vector Support | 11% | 72 | 65 | **98** | 45 |
| Graph Support | 10% | **92** | 85 | 70 | 55 |
| **Weighted Total** | **100%** | **75.89** | **83.14** | **76.36** | **51.95** |

---

## Dimension Analysis

### Recall Accuracy (22%)

**mempalace 92 | mem0 90 | gbrain 78 | gsd-2 35**

mempalace e mem0 publicam em benchmarks de industria padrao (LongMemEval, LoCoMo). mempalace relata **96.6% R@5 raw** em LongMemEval 500q sem nenhum LLM + **98.4% hybrid v4 held-out** (benchmarks/BENCHMARKS.md). mem0 relata **93.4 LongMemEval**, **91.6 LoCoMo**, **64.1 BEAM (1M)** apos algoritmo novo (Abril 2026, README.md). gbrain mostra **R@5 83 -> 95%** com hybrid+graph no BrainBench proprio, mas o corpus Opus-generated e customizado e limita comparabilidade. gsd-2 nao publica recall.

Key signals:
- mempalace: `OS/mempalace/benchmarks/longmemeval_bench.py` + resultados em `benchmarks/results_*.jsonl`
- mem0: README tabela "New Memory Algorithm April 2026" + `OS/mem0/evaluation/`
- gbrain: `OS/gbrain/docs/benchmarks/2026-04-18-brainbench-v1.md`

### Write Latency (10%)

**gbrain 80 | mem0 78 | mempalace 65 | gsd-2 55**

gbrain combina **batch-write via unnest** (4-5 array params independente do tamanho) com **Minions durable job queue** (753ms production vs 10s+ gateway timeout em sub-agents, conforme benchmark). mem0 tem **AsyncMemory/AsyncMemoryClient** + p50 end-to-end 0.88-1.09s publicado. mempalace declara **budget hooks <500ms** mas nao tem batch/async explicit. gsd-2 e sync com single-writer invariant.

### Read Latency (12%)

**gbrain 78 | mempalace 75 | mem0 72 | gsd-2 60**

gbrain tem HNSW via pgvector + `statement_timeout` scoped per-transaction (v0.12.3 evita leaks no pool postgres.js) + `clampSearchLimit` per-operation. mempalace tem budget `<100ms` startup injection + BM25 re-rank sobre candidate small. mem0 p50 e end-to-end (inclui LLM). gsd-2 e SQLite local simples.

### Persistence (12%)

**mempalace 95 | gbrain 80 | mem0 72 | gsd-2 65**

Esta dimensao separa os projetos pela fidelidade ao conteudo original:

| Subject | Strategy | What is stored |
|---------|----------|----------------|
| **mempalace** | **VERBATIM** | palavras exatas em drawers (policy nao-negociavel) |
| gbrain | paraphrase + raw backup | `compiled_truth` primario + `raw_data` JSONB |
| mem0 | paraphrase (LLM facts) | ADD-only single-pass extraction, accumulates |
| gsd-2 | structured category+content | 6 categorias enum, nao conversa |

mempalace e o unico com politica explicita "nao summarizamos, nao paraphrasamos, retornamos palavras exatas" (CONTRIBUTING). Todos tem durable backend.

### Schema Flexibility (10%)

**mem0 85 | mempalace 80 | gbrain 75 | gsd-2 55**

mem0 vence por metadata Pydantic + multi-level scoping (user_id/agent_id/run_id) + graph Neo4j opcional. mempalace tem drawers schemaless + entity registry. gbrain tem schema rigido + frontmatter JSONB. gsd-2 tem **6 categorias enum fixas** (architecture/convention/gotcha/preference/environment/pattern) — mais restritivo.

### Local-first (13%)

**mempalace 95 | gsd-2 60 | gbrain 55 | mem0 40**

Esta e a maior separacao no scorecard. **mempalace** e o unico 100% local-first por design: zero API keys no core path, zero telemetry policy, works offline, data ownership explicit. **mem0** tem **PostHog em dependencies core** + OpenAI default obrigatorio — hibrido local+cloud. **gbrain** tem DB local (PGLite WASM) mas requer OpenAI pra embeddings. **gsd-2** forces `RTK_TELEMETRY_DISABLED=1` e tem SQLite local mas LLM depende de provider.

### Vector Support (11%)

**mem0 98 | gbrain 72 | mempalace 65 | gsd-2 45**

mem0 domina absolutamente: **30 vector stores** (Qdrant, Pinecone, Chroma, Weaviate, Milvus, MongoDB, Redis, ES, pgvector, Supabase, Faiss, ...) + **15 embedding providers** (OpenAI, Azure, Gemini, HF, FastEmbed, Together, Bedrock, Ollama, VertexAI, ...) + HNSW/IVF per-provider. gbrain tem HNSW + lock-in em OpenAI. mempalace tem ChromaDB default + pluggable interface. gsd-2 usa SQLite simples.

### Graph Support (10%)

**gbrain 92 | mempalace 85 | mem0 70 | gsd-2 55**

gbrain lidera com **zero-LLM auto-wiring**: heuristicas regex extraem typed edges (`attended`, `works_at`, `invested_in`, `founded`, `advises`, `source`, `mentions`) em cada write sem chamar LLM. 3+ hop traversal via `gbrain graph-query --depth N --direction in/out/both`. mempalace tem **temporal KG** unico com `valid_from`/`valid_to` (`query_entity(as_of=date)`). mem0 tem graph mas requer **backend externo** (Neo4j/Memgraph/Kuzu/AGE) + extraction **LLM-based**. gsd-2 tem memory relations (Phase 4).

---

## Strategic Recommendations

### 1. Use mempalace como baseline para "memoria fiel local"

mempalace e a escolha default quando o requisito e: verbatim storage + 100% local + sem API keys + benchmarks publicos reproduziveis. O compromisso e: Python-only, single embedding provider default, sem batch write explicit.

- **Target:** time que prioriza privacidade + fidelidade semantica (o agente retorna o que o usuario disse)
- **Addresses:** Persistence + Local-first + Recall
- **Expected impact:** memoria agentica auditavel, sem vendor lock-in, com recall publicado
- **Priority:** P0

### 2. Use mem0 como stack padrao para producao multi-provider

mem0 e a escolha quando o requisito e: escalabilidade via ecossistema + SDK duais (Python+TS) + platform hosted + SDK Vercel AI. Trade-off: telemetry default on, paraphrase-first, OpenAI default.

- **Target:** times enterprise / multi-tenant / hosted-first
- **Addresses:** Vector Support + Schema Flexibility + Integration breadth
- **Expected impact:** deploy rapido com qualquer stack existente (Qdrant/Pinecone/Neo4j/OpenAI/Gemini/Bedrock)
- **Priority:** P0

### 3. Use gbrain quando o core do workload e knowledge-graph heavy

gbrain entrega graph auto-wiring sem LLM + traversal 3+ hop + durable job queue em Postgres, tudo em um runtime contract-first. E a escolha quando se quer relacionamentos tipados sem custo de LLM em cada write, e quando se tolera OpenAI embeddings.

- **Target:** times com corpora entidade-pesados (pessoas, empresas, deals)
- **Addresses:** Graph Support + Write Latency + Integration MCP
- **Expected impact:** auto-linking gratis, queries graph tipadas no hot path
- **Priority:** P1

### 4. gsd-2 nao e memory system standalone — considere apenas se ja usa o coding agent

As tres tools (`capture_thought`, `memory_query`, `gsd_graph`) sao uteis dentro do workflow do GSD, mas nao sao competitivos como memory product. Se voce quer memoria pra um coding agent standalone, use mempalace + mem0 + gbrain via MCP no Claude Code/Cursor.

- **Target:** apenas usuarios existentes do GSD coding agent
- **Addresses:** memory como side-feature, nao product
- **Priority:** P3

### 5. Hibridizacao: mempalace + gbrain como memoria stack complementar

As forcas sao ortogonais: mempalace domina verbatim+local, gbrain domina graph+Postgres. Ambos expoem MCP server. Um deployment hybrido pode usar mempalace como storage verbatim + gbrain como graph layer com auto-wiring — mas exige codigo de sync que nenhum dos dois oferece hoje.

- **Target:** times com recursos de engenharia pra glue
- **Addresses:** compensar weaknesses (vector no mempalace, local-first no gbrain)
- **Priority:** P2

---

## When to Pick Which

### Choose mempalace if...
- Privacy / local-first / sem API keys e requisito duro
- Precisa retornar palavras exatas do usuario (verbatim)
- Time e Python-first e trabalha com Claude Code / MCP
- Benchmark recall publicado e requerido pra compliance
- Temporal validity de fatos importa (valid_from/valid_to)

### Choose mem0 if...
- Ecossistema (30+ vector stores, multi-LLM) e crucial
- Usa Vercel AI SDK / Next.js stack
- Precisa de hosted platform option
- Quer SDK TypeScript nativo alem de Python
- Aceita telemetry + OpenAI default

### Choose gbrain if...
- Stack ja Postgres (quer pgvector + hybrid search + graph no mesmo DB)
- Graph de entidades tipadas e core (pessoas, empresas, deals)
- Quer job queue durable junto com memoria (Minions)
- Tolera lock-in em OpenAI embeddings
- Trabalha com agentes pessoais estilo YC / Garry Tan (pra quem o repo foi construido)

### Choose gsd-2 if...
- Ja usa GSD coding agent (v2.76+)
- Memoria e lateral ao workflow de coding, nao product

### Consider both (complementary) if...
- mempalace (verbatim layer) + gbrain (graph layer) via MCP: fidelidade + relacoes
- mempalace (local) + mem0 (cloud fallback) via backend abstraction
- gbrain (source of truth) + mem0 (indexing rich) via sync job

---

## Methodology

### Data Sources

| Subject | Source | Method | Confidence |
|---------|--------|--------|------------|
| gbrain | `OS/gbrain/` + `CLAUDE.md` + `docs/benchmarks/` | filesystem-scan + doc-scan | HIGH |
| mempalace | `OS/mempalace/` + `CLAUDE.md` + `benchmarks/BENCHMARKS.md` | filesystem-scan + doc-scan | HIGH |
| mem0 | `OS/mem0/` + `CLAUDE.md` (AGENTS.md) | filesystem-scan + doc-scan | HIGH |
| gsd-2 | `OS/gsd-2/` + `README.md` + `src/resources/extensions/gsd/memory-*` | filesystem-scan + code-scan | MEDIUM |

### Scoring Method

- **Dimension pack:** memory v1.0 (8 dimensoes: recall, write_latency, read_latency, persistence, schema_flex, local_first, vector, graph)
- **Pesos:** soma = 1.00 (recall 0.22 e maior, local_first 0.13 segundo maior)
- **Score range:** 0-100
- **Regras de integridade:** score >=90 requer 2+ signals com evidence path concreto; signal ausente -> reduzir score + flag
- **Confidence rollup:** HIGH se todas HIGH/MEDIUM; MEDIUM caso contrario

### Artifacts Generated

| Artifact | File | Status |
|----------|------|:------:|
| Metadata | `metadata.json` | OK |
| Inventory gbrain | `_inventories/gbrain/inventory.{json,md}` | OK |
| Inventory mempalace | `_inventories/mempalace/inventory.{json,md}` | OK |
| Inventory mem0 | `_inventories/mem0/inventory.{json,md}` | OK |
| Inventory gsd-2 | `_inventories/gsd-2/inventory.{json,md}` | OK |
| Comparison Matrix | `comparison-matrix.{json,md}` | OK |
| Scorecard | `scorecard.{json,md}` | OK |
| Executive Report | `executive-report.md` | OK |

### Limitations

- Benchmarks de recall sao self-reported (citados apenas quando tem evidence path)
- gsd-2 nao expõe metricas de memoria — penalizado por ausencia de measurement, nao por performance ruim
- Latency p50 do mem0 e end-to-end (inclui LLM), nao write/read puro
- gbrain BrainBench usa corpus customizado (nao LongMemEval/LoCoMo padrao)
- Scoring "Local-first" combina 3 criterios (API keys, telemetry, offline) ponderados iguais

---

## Appendix: Source Artifacts

Todos os artefatos em `OS/_bench/memory-4way/`:

| # | File | Type | Format |
|---|------|------|--------|
| 1 | `metadata.json` | Metadata | JSON |
| 2 | `_inventories/gbrain/inventory.json` | Inventory | JSON |
| 3 | `_inventories/gbrain/inventory.md` | Inventory | MD |
| 4 | `_inventories/mempalace/inventory.json` | Inventory | JSON |
| 5 | `_inventories/mempalace/inventory.md` | Inventory | MD |
| 6 | `_inventories/mem0/inventory.json` | Inventory | JSON |
| 7 | `_inventories/mem0/inventory.md` | Inventory | MD |
| 8 | `_inventories/gsd-2/inventory.json` | Inventory | JSON |
| 9 | `_inventories/gsd-2/inventory.md` | Inventory | MD |
| 10 | `comparison-matrix.json` | Matrix | JSON |
| 11 | `comparison-matrix.md` | Matrix | MD |
| 12 | `scorecard.json` | Scoring | JSON |
| 13 | `scorecard.md` | Scoring | MD |
| 14 | `executive-report.md` | Report | MD |

---

_Generated by os-bench bench-executive-report task | Template v1.0_
