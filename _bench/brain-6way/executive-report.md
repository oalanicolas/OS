# Executive Report: brain-6way

**Date:** 2026-08-06  
**Slug:** brain-6way  
**Subjects:** LifeOS · gbrain · mempalace · mem0 · memori-labs · gsd-2  
**Pack:** memory (quantitativo) + product framing (qualitativo)

---

## 1. One-sentence map

| Subject | Em uma frase |
|---------|----------------|
| **LifeOS** | O **sistema operacional da sua vida** com DA, Cortex e Pulse (voz/dashboard) |
| **gbrain** | O **cérebro de conhecimento** que sintetiza e fecha gaps sobre páginas/entidades |
| **mempalace** | O **arquivo fiel** offline, palavra por palavra |
| **mem0** | O **SDK de memória** para plugar em qualquer stack |
| **memori** | A **memória de ação** do agente (tools, outcomes) |
| **gsd-2** | Memória lateral de um coding agent — não compete |

---

## 2. Scorecard memory pack (quantitativo)

| Rank | Subject | Score |
|-----:|---------|------:|
| 1 | mempalace | **84.23** |
| 2 | gbrain | **78.56** |
| 3 | mem0 | **77.54** |
| 4 | memori-labs | **76.43** |
| 5 | **LifeOS** | **70.58** |
| 6 | gsd-2 | **52.94** |

**LifeOS fica em 5º no pack `memory`** porque:

1. Retrieval é **BM25 em markdown**, não hybrid HNSW com bench público  
2. **Vector support = 42** de propósito (“sem index intermediário”)  
3. Não publica LongMemEval/LoCoMo  

Isso **não** significa que LifeOS seja o pior “brain” no sentido produto — significa que o pack mede store/retrieval, e LifeOS otimiza **operating system**.

### Onde LifeOS pontua bem no pack

| Dim | Score | vs campo |
|-----|------:|----------|
| Schema flexibility | 86 | empatado com mem0, atrás só de memori |
| Graph support | 84 | 2º atrás de gbrain (94) |
| Persistence | 80 | arquivos MD + audit jsonl |
| Local-first | 64 | melhor que mem0/gbrain/memori no eixo “files on disk”; pior que mempalace |

### Onde LifeOS sangra no pack

| Dim | Score | Por quê |
|-----|------:|---------|
| Vector | **42** | design file-first |
| Recall | 68 | sem leaderboard industry; BM25 only |

---

## 3. Product matrix (o que o scorecard não captura)

| Capability | LifeOS | gbrain | mempalace | mem0 | memori |
|------------|:------:|:------:|:---------:|:----:|:------:|
| Life goals / TELOS / Ideal State | ★★★★★ | — | — | — | — |
| Digital Assistant identity | ★★★★★ | ★★ | — | — | ★★ |
| Voice runtime (TTS/Siri/phone) | ★★★★★ | ★★★★ | — | — | — |
| Observability dashboard | ★★★★★ | ★★ | — | ★★★ | ★★ |
| Autonomic memory reviewer | ★★★★★ | ★★★ (dream) | — | ★★ | ★★★ |
| Synthesis + gap analysis | ★★ (via DA) | ★★★★★ | — | — | ★★ |
| Verbatim offline recall | ★★ | ★★ | ★★★★★ | ★ | ★★ |
| Multi-store vector SDK | — | ★ | ★★ | ★★★★★ | ★★ |
| Published recall SOTA | — | ★★ | ★★★★★ | ★★★★★ | ★★★★ |
| Entity people/companies graph | ★★★★ | ★★★★★ | ★★★ | ★★★ | ★★ |
| Install as agent skill pack | ★★★★★ | ★★★★ | ★★★ | ★★★★ | ★★★★ |

---

## 4. LifeOS vs cada peer (head-to-head curto)

### LifeOS vs gbrain (o par mais interessante)

| | LifeOS | gbrain |
|--|--------|--------|
| Metáfora | **OS da vida** + DA | **Cérebro de conhecimento** |
| Storage | markdown + hooks | Postgres/pgvector |
| Query UX | DA na sessão + BM25 context | `think` / search / graph-query |
| Graph | graphology sobre MD | zero-LLM edges + multi-hop SQL |
| Scale story | life ops + skills | 100k+ pages production |
| Voice | Pulse first-class | agent-voice / Twilio |
| Melhor para | “meu assistente que conhece minha vida” | “prepare a call com Alice a partir do corpus” |

**Não são substitutos 1:1.** Overlap em People/Companies. Compose só se aceitar dois SoTs ou sync deliberado.

### LifeOS vs mempalace

| | Winner |
|--|--------|
| Offline / fidelity | **mempalace** |
| Life ops / DA / voice / goals | **LifeOS** |
| Compose? | **Sim** — mempalace cold archive; LifeOS hot OS |

### LifeOS vs mem0

| | Winner |
|--|--------|
| Embutir memória num SaaS multi-tenant | **mem0** |
| Operar a vida de um humano com agent | **LifeOS** |
| Compose? | Raro — eixos diferentes |

### LifeOS vs memori-labs

| | Winner |
|--|--------|
| Tool-call / execution memory | **memori** |
| Identity, TELOS, work, knowledge archive | **LifeOS** |
| Compose? | **Sim** — memori como log de ação do agent; LifeOS como OS |

### LifeOS vs gsd-2

LifeOS engole o use case de “coding agent com memória” e vai muito além. gsd-2 só se você já é GSD-only.

---

## 5. Decision tree

```
Quer só retrieval fiel offline?
  → mempalace

Quer memory SDK no seu produto?
  → mem0

Quer lembrar o que o agente FEZ?
  → memori-labs

Quer knowledge brain (síntese + graph + dream) sobre corpus?
  → gbrain

Quer um LIFE OPERATING SYSTEM (DA, TELOS, voz, dashboard, skills)?
  → LifeOS

Quer coding agent memory only?
  → gsd-2 (ou LifeOS se topa o setup maior)
```

---

## 6. Recommendation (opinionated)

1. **Se o brief era “o cérebro do cara do blog com voz” → LifeOS é o produto certo** — não compete no LongMemEval, compete em **operating the self**.  
2. **Se o brief é “melhor memory layer no pack memory” → mempalace (fidelity) ou gbrain (knowledge ops).**  
3. **Stack ambiciosa:**  
   - **LifeOS** = OS + DA + goals  
   - **mempalace** = archive verbatim  
   - opcional **memori** = execution log  
   - **gbrain** só se precisar de synthesis/gap institutional em Postgres (cuidado com overlap)

4. **Não force LifeOS a ser mem0** (não tem 24 vector stores) nem **mempalace a ser LifeOS** (não tem TELOS/Pulse).

---

## 7. Artefatos

```
OS/LifeOS/                          # clone local
OS/_bench/brain-6way/
├── executive-report.md             ← este
├── scorecard.{md,json}
├── comparison-matrix.md
├── metadata.json
└── _inventories/{LifeOS + 5 peers}/
OS/_bench/_research/obsidian-brain-voice-candidates.md  # confirmado LifeOS
```

---

## 8. Bottom line

> **No pack `memory`, LifeOS é 5º (70.6).**  
> **No espaço “personal AI brain / life OS”, LifeOS é o único full-stack.**  
> **gbrain** continua o melhor *knowledge brain* de produto.  
> **mempalace** continua o melhor *memory fidelity*.  
> **mem0** continua o melhor *memory SDK*.  
> Escolher entre eles é escolher o **job**, não o ranking único.
