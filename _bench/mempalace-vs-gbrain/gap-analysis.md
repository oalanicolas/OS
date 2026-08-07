# Gap Analysis: mempalace vs gbrain

**Date:** 2026-08-06  
**Pack:** memory  
**Slug:** mempalace-vs-gbrain  
**Confidence:** HIGH  
**Sources:** scorecard, comparison-matrix, inventories, filesystem scan

---

## Executive Summary

Os dois resolvem jobs **complementares**, não o mesmo produto. mempalace é a melhor **camada de fidelidade/retrieval local**; gbrain é o melhor **daemon de conhecimento sintético + grafo + multi-tenant**.  

Gaps de mempalace concentram-se em **síntese, automação noturna e company brain** (HIGH, complexidade alta — são decisões de produto). Gaps de gbrain concentram-se em **verbatim/offline e benchmarks públicos** (HIGH para privacy/audit use cases; complexidade média–alta no verbatim).

| Direction | Total gaps | HIGH | MED | LOW | P0 | P1 | P2 | P3 |
|-----------|:---------:|:----:|:---:|:---:|:--:|:--:|:--:|:--:|
| Gaps de **mempalace** (o que gbrain tem) | 8 | 4 | 3 | 1 | 1 | 3 | 3 | 1 |
| Gaps de **gbrain** (o que mempalace tem) | 7 | 3 | 3 | 1 | 2 | 2 | 2 | 1 |

---

## Gaps de mempalace

O que **gbrain** tem e mempalace não (ou só parcial):

### Missing (Sem_Equiv)

| ID | Capability | Dimension | Impact | Complexity | Priority | Description |
|----|-----------|-----------|:------:|:----------:|:--------:|-------------|
| GAP-A-001 | Synthesis + gap analysis (`think`) | recall / product | HIGH | HIGH | **P1** | Query devolve resposta citada + o que o brain *não* sabe |
| GAP-A-002 | Durable job queue (Minions) | write_latency | HIGH | HIGH | P1 | Subagents/crons crash-safe |
| GAP-A-003 | Company multi-tenant + OAuth fences | schema / product | HIGH | HIGH | P1 | Isolamento por usuário/source em team brain |
| GAP-A-004 | Dream / enrich / doctor overnight loop | ops | HIGH | HIGH | P2 | Consolidação autônoma 24/7 |
| GAP-A-005 | Zero-LLM graph auto-wiring on write | graph_support | MED | MED | P1 | Edges tipadas grátis em cada put |
| GAP-A-006 | Provider-agnostic AI gateway | vector_support | MED | MED | P2 | Multi-embed/rerank sem fork |
| GAP-A-007 | Schema packs agent-evolvable | schema_flexibility | MED | MED | P2 | BYO page types + mutations |
| GAP-A-008 | Self-upgrade + GitHub Releases binaries | ops | LOW | LOW | P3 | `check-update` / `self-upgrade` |

### Partial

| ID | Capability | What A has | What A lacks | Impact | Priority |
|----|-----------|------------|--------------|:------:|:--------:|
| GAP-A-009 | Hybrid graph retrieval | temporal KG as-of | relational boost no hot path de search | MED | P2 |
| GAP-A-010 | Production multi-machine | Docker MCP | Postgres shared engine + HTTP OAuth admin | MED | P2 |

### Detail (P0/P1)

#### GAP-A-001: Synthesis + gap analysis
- **Type:** Missing  
- **Evidence (B):** `OS/gbrain/README.md` (`gbrain think`), synthesis layer docs  
- **Impact HIGH:** sem isso, o agente sempre faz “open 5 drawers e leia” — o job-to-be-done de gbrain  
- **Complexity HIGH:** exige retrieval → LLM compose → citation grounding → hole detection  
- **Priority P1** (P0 só se o produto quiser deixar de ser “palace” e virar “brain”)

#### GAP-A-003: Company multi-tenant
- **Type:** Missing  
- **Evidence (B):** company-brain tutorial, auth slug-prefix write fence v0.42.72  
- **Impact HIGH** para times; **irrelevante** para solo local-first  

#### GAP-A-005: Zero-LLM graph auto-wiring
- **Type:** Missing / Partial  
- **Evidence (B):** link extraction on `put_page`, typed edges  
- **A has:** KG triples explícitos via tools (`tool_kg_add`) — `OS/mempalace/mempalace/mcp_server.py`  
- **Missing:** wiring automático sem LLM em cada write de drawer  

---

## Gaps de gbrain

O que **mempalace** tem e gbrain não (ou só parcial):

### Missing (Sem_Equiv)

| ID | Capability | Dimension | Impact | Complexity | Priority | Description |
|----|-----------|-----------|:------:|:----------:|:--------:|-------------|
| GAP-B-001 | Verbatim-first storage policy | persistence | HIGH | HIGH | **P0** | Nunca paraphrasar como path primário |
| GAP-B-002 | Zero-API core / offline full path | local_first | HIGH | MED | **P0** | Recall sem OpenAI/embed keys |
| GAP-B-003 | LongMemEval (industry) published in-tree | recall_accuracy | HIGH | MED | P1 | Benchmark comparável a peers |
| GAP-B-004 | Pluggable multi-backend zoo (5) | vector_support | MED | MED | P2 | chroma/qdrant/milvus/sqlite além pgvector |
| GAP-B-005 | Wings/rooms spatial UX metaphor | schema | LOW | LOW | P3 | mental model palace |
| GAP-B-006 | Claude session mine + retention hooks | product | MED | LOW | P1 | `mine ~/.claude/projects` + precompact hooks |
| GAP-B-007 | 36 MCP tools surface breadth | extensibility | MED | MED | P2 | palace+KG tool count |

### Partial

| ID | Capability | What B has | What B lacks | Impact | Priority |
|----|-----------|------------|--------------|:------:|:--------:|
| GAP-B-008 | Temporal as-of KG | Chronicle bi-temporal | API `query_entity(as_of=)` first-class e simples | MED | P1 |
| GAP-B-009 | Install friction | agent 30min install | `uv tool install` one-liner | MED | P2 |

### Detail (P0/P1)

#### GAP-B-001: Verbatim-first
- **Type:** Missing (policy)  
- **Evidence (A):** `OS/mempalace/README.md`, `benchmarks/BENCHMARKS.md` thesis  
- **Impact HIGH** se auditoria/legal/“o que eu disse” importa  
- **B has:** raw_data JSONB — partial; primary path is compiled_truth  
- **Priority P0** for privacy/fidelity positioning; P2 if product is intentionally synthetic  

#### GAP-B-002: Zero-API core
- **Type:** Missing  
- **Evidence (A):** 96.6% R@5 raw sem LLM  
- **B:** PGLite ok, mas embed/think dependem de keys  
- **Priority P0** para air-gapped / cost-zero personal  

#### GAP-B-003: LongMemEval in-tree
- **Type:** Missing (public industry suite)  
- **Evidence (A):** `benchmarks/BENCHMARKS.md`  
- **B:** BrainBench custom + gbrain-evals sibling  
- **Priority P1** para credibilidade cross-paper  

#### GAP-B-006: Claude session mine hooks
- **Type:** Missing / weak  
- **Evidence (A):** `mempalace mine`, hooks em `hooks/`, retention docs  
- **B:** capture/MCP, mas mine de transcripts Claude Code é menos first-class  

#### GAP-B-008: Temporal as-of simplicity
- **Type:** Partial  
- **Evidence (A):** `tool_kg_query(..., as_of=)` + `valid_from`/`valid_to`  
- **B:** Chronicle exists (v0.42.56) — menos “one call as_of” no KG path  

---

## Classification

### By Impact

| Impact | Gaps de mempalace | Gaps de gbrain |
|--------|:-----------------:|:--------------:|
| HIGH | 4 | 3 |
| MED | 3 | 3 |
| LOW | 1 | 1 |

### Impact × Complexity (priority heatmap)

| | LOW complexity | MED | HIGH |
|--|----------------|-----|------|
| **HIGH impact** | — | GAP-B-002 offline path | GAP-A-001 think; GAP-B-001 verbatim |
| **MED impact** | GAP-B-006 hooks | GAP-A-005 auto-graph; GAP-B-003 LongMemEval | GAP-A-003 multi-tenant |
| **LOW impact** | GAP-A-008 self-upgrade | GAP-B-005 wings metaphor | — |

---

## Most affected dimensions

### mempalace (gaps from gbrain)

| Dimension | Gap count | Highest priority |
|-----------|:---------:|:----------------:|
| product / synthesis | 1 | P1 (think) |
| write / ops | 2 | P1 (minions, dream) |
| multi-tenant | 1 | P1 |
| graph | 1 | P1 |

### gbrain (gaps from mempalace)

| Dimension | Gap count | Highest priority |
|-----------|:---------:|:----------------:|
| local_first | 1 | **P0** |
| persistence | 1 | **P0** |
| recall_public | 1 | P1 |
| agent-session UX | 1 | P1 |

---

## Action items (absorção seletiva)

| # | Action | Target | Closes | Dim | Priority |
|---|--------|--------|--------|-----|:--------:|
| 1 | Path de embed local (fastembed/ollama) default-able + “offline mode” doctor check | gbrain | GAP-B-002 | local_first | **P0** |
| 2 | Modo `storage.primary=verbatim` (compiled_truth opcional, não default) | gbrain | GAP-B-001 | persistence | **P0** |
| 3 | Publicar LongMemEval harness no tree (ou link gbrain-evals canônico) | gbrain | GAP-B-003 | recall | P1 |
| 4 | `mine claude-sessions` + hooks precompact (copiar shape mempalace) | gbrain | GAP-B-006 | product | P1 |
| 5 | Optional `think`-lite skill (retrieve → compose) atrás de flag LLM | mempalace | GAP-A-001 | product | P1 |
| 6 | Auto-extract lightweight edges on drawer write (regex, zero LLM) | mempalace | GAP-A-005 | graph | P1 |
| 7 | **Não** forçar multi-tenant em mempalace se o produto é personal palace | mempalace | GAP-A-003 | — | skip |

### Recomendação de absorção

- **Se o SoT é gbrain:** absorver P0 de mempalace (offline embed + verbatim mode) — fecha o flanco local-first sem virar outro produto.  
- **Se o SoT é mempalace:** absorver só auto-wiring leve + think opcional; **não** virar Minions/company-brain (mata o simplicidade/offline).  
- **Stack ideal de dois produtos:** mempalace = cold verbatim archive; gbrain = hot synthetic brain. Sync periódico drawers→pages.

---

## Methodology

- Gaps a partir de feature classes Forte/Parcial/Sem_Equiv na matrix  
- Impact ≈ peso da dimensão no pack memory × delta de score  
- Complexity: LOW &lt;1d / MED 1–3d / HIGH arquitetural  
- Confidence HIGH (ambos os trees locais tip atual)
