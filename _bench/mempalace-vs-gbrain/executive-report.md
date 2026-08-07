# Executive Report: mempalace vs gbrain

**Date:** 2026-08-06  
**Type:** pair (top-2 de memory-5way)  
**Slug:** mempalace-vs-gbrain  
**Pack:** memory  
**Winner (weighted):** mempalace **84.23** vs gbrain **78.56** (Δ **+5.67**)

---

## 1. The real question

Não é “qual é melhor software?” — é **qual job você está comprando?**

| | mempalace | gbrain |
|--|-----------|--------|
| Metaphor | Palácio: guarda o original nas gavetas | Cérebro: lê as gavetas e te conta o que importa |
| Query UX | “Aqui estão os trechos” | “Aqui está a resposta — e o que eu ainda não sei” |
| Cost model | $0 no path raw | API keys embed + LLM synthesis |
| Trust model | Verbatim = auditável | Synthesis = útil, mas interpretada |
| Ops model | CLI + MCP + hooks | Daemon + Minions + dream + doctor |

O scorecard do pack `memory` **foi desenhado** com pesos altos em recall/persistence/local-first (0.22+0.12+0.13 = 47%). Nesse eixo, mempalace é o campeão natural. gbrain otimiza eixos com peso menor (graph 0.10, write 0.10) mas com valor de produto enorme em produção de agentes.

---

## 2. Scorecard head-to-head

| Dimension | W | mempalace | gbrain | Edge |
|-----------|--:|:---------:|:------:|------|
| Recall | 22% | **93** | 80 | LongMemEval público vs BrainBench custom |
| Local-first | 13% | **95** | 58 | **maior delta (+37)** |
| Persistence | 12% | **95** | 82 | Verbatim vs paraphrase+raw |
| Write lat. | 10% | 65 | **82** | Minions + batch |
| Read lat. | 12% | 75 | **80** | Hybrid RRF + autocut |
| Schema | 10% | **80** | 78 | Quase empate |
| Vector | 11% | 72 | **78** | Gateway multi-provider |
| Graph | 10% | 86 | **94** | Auto-wiring zero-LLM |
| **Total** | | **84.23** | **78.56** | mempalace |

**Dim wins 4–4.** Vitória de mempalace é **ponderada**, não unânime.

---

## 3. Architectural contrast

### mempalace path
```
source (chat, file, mine)
  → drawer VERBATIM
  → embed (local Chroma default)
  → search → top-k snippets
  → (optional) hybrid rerank with small LLM
  → agent synthesizes outside
```

### gbrain path
```
source (sync, capture, webhook)
  → page (compiled_truth + raw)
  → zero-LLM edge extract
  → embed (multi-provider gateway)
  → hybrid + graph signals
  → gbrain think → answer + citations + gaps
  → dream/enrich overnight
```

Implicação: **latência cognitiva** do usuário final é menor em gbrain (uma chamada `think`); **fidelidade e custo** favorecem mempalace.

---

## 4. Where each is undefeatable

### mempalace only (prático)
1. Air-gapped / no API budget no hot path  
2. Compliance: “prove as palavras originais”  
3. LongMemEval-class retrieval SOTA sem extraction loss  
4. Claude Code retention (mine + precompact hooks) com UX madura  

### gbrain only (prático)
1. Meeting prep sintético com gap analysis  
2. Graph questions (“who works at X?”, multi-hop) sem Neo4j  
3. Company brain multi-user com write fences  
4. Overnight self-improvement (dream, enrich, doctor remediations)  
5. Production scale story (100k+ pages, dozens of crons)  

---

## 5. Decision matrix (use cases)

| Use case | Winner | Why |
|----------|:------:|-----|
| Personal notes offline | **mempalace** | zero API, verbatim |
| Claude Code session memory | **mempalace** | mine + hooks |
| YC-style people/deals brain | **gbrain** | graph + think |
| Team institutional memory | **gbrain** | company brain |
| Legal/audit transcript store | **mempalace** | verbatim policy |
| OpenClaw/Hermes production brain | **gbrain** | designed for that |
| Lowest token bill | **mempalace** | raw path $0 |
| “What don’t I know?” | **gbrain** | gap analysis |
| Solo privacy maximalist | **mempalace** | local-first |
| Solo leverage maximalist | **gbrain** | synthesis + dream |

---

## 6. Can you run both?

**Yes — recommended for serious setups.**

| Layer | System | Role |
|-------|--------|------|
| Cold | mempalace | Verbatim archive, session mine, offline recall |
| Hot | gbrain | Synthetic working memory, graph, think, crons |

Pattern: periodicamente (ou via agent) promover drawers relevantes → `gbrain put` pages; gbrain nunca vira SoT de fidelidade; mempalace nunca precisa virar company daemon.

**Anti-pattern:** instalar só gbrain e esperar offline zero-cost; instalar só mempalace e esperar gap analysis de board meeting.

---

## 7. If you must pick one

### Pick **mempalace** if…
- Privacy/offline/cost são non-negotiable  
- O agente já é bom em sintetizar; você só precisa de retrieval fiel  
- Caso de uso = coding-agent memory + chat history  

### Pick **gbrain** if…
- Você quer o brain como **produto operacional** (não só store)  
- Workload entity-heavy (people, companies, investments)  
- Team / multi-tenant / overnight autonomy  

### Pack score winner
**mempalace** — para o pack `memory` como definido.  

### Product-brain winner
**gbrain** — se o critério for “substitui o estagiário que lê suas notas”.

---

## 8. Gaps worth closing (see gap-analysis.md)

| Priority | On gbrain | On mempalace |
|:--------:|-----------|--------------|
| P0 | Offline embed path; optional verbatim-primary mode | — |
| P1 | LongMemEval harness; Claude mine hooks | Optional think-lite; zero-LLM edge auto-wire |
| Skip | — | Full multi-tenant (wrong product shape) |

---

## 9. Bottom line

> **mempalace is the better memory. gbrain is the better brain.**

O pack `memory` elege mempalace (+5.7). Um pack hipotético `agent-brain` (synthesis, autonomy, multi-tenant, graph ops) elegeria gbrain com folga.  

**Recommendation final:**  
1. **Solo / privacy / fidelity → mempalace**  
2. **Agent ops / company knowledge → gbrain**  
3. **Ambicioso → ambos em camadas** (não monólito único)

---

## Artefatos deste pair

```
OS/_bench/mempalace-vs-gbrain/
├── battle-card.md          ← 1 página decisória
├── executive-report.md     ← este arquivo
├── scorecard.{md,json}
├── comparison-matrix.{md,json}
├── gap-analysis.md
├── metadata.json
└── _inventories/{mempalace,gbrain}/
```
