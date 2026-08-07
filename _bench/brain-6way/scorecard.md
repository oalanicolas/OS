# Scorecard: brain-6way

**Date:** 2026-08-06  
**Pack:** memory (weights sum 1.00)  
**Subjects:** LifeOS · gbrain · mempalace · mem0 · memori-labs · gsd-2  
**Confidence:** HIGH  

> **Caveat:** o pack `memory` mede **camada de memória**. LifeOS é um **Life OS / harness** com Cortex embutido — o score total **subestima** dashboard, voz, Algorithm, skills e DA. Use a seção “Product jobs” no executive-report.

---

## Ranking (memory pack)

| Rank | Subject | Total | Dim wins |
|-----:|---------|------:|:--------:|
| 1 | **mempalace** | **84.23** | 3 |
| 2 | **gbrain** | **78.56** | 3 |
| 3 | **mem0** | **77.54** | 1 |
| 4 | **memori-labs** | **76.43** | 1 |
| 5 | **LifeOS** | **70.58** | 0* |
| 6 | **gsd-2** | **52.94** | 0 |

\*LifeOS não lidera nenhuma dimensão do pack, mas é #2 em schema e graph, e o único **full life-OS product**.

---

## Dimension table

| Dimension | W | mempalace | gbrain | mem0 | memori | **LifeOS** | gsd-2 | Leader |
|-----------|--:|:---------:|:------:|:----:|:------:|:----------:|:-----:|:------:|
| Recall | 22% | **93** | 80 | 92 | 85 | 68 | 38 | mempalace |
| Write lat. | 10% | 65 | **82** | 80 | 76 | 72 | 55 | gbrain |
| Read lat. | 12% | 75 | **80** | 74 | 76 | 74 | 60 | gbrain |
| Persistence | 12% | **95** | 82 | 72 | 78 | 80 | 65 | mempalace |
| Schema flex. | 10% | 80 | 78 | 86 | **88** | 86 | 55 | memori |
| Local-first | 13% | **95** | 58 | 40 | 55 | 64 | 60 | mempalace |
| Vector | 11% | 72 | 78 | **98** | 70 | 42 | 48 | mem0 |
| Graph | 10% | 86 | **94** | 72 | 80 | 84 | 55 | gbrain |
| **Total** | | **84.23** | **78.56** | **77.54** | **76.43** | **70.58** | **52.94** | |

---

## LifeOS — rationale por dimensão

| Dim | Score | Signals |
|-----|------:|---------|
| Recall | 68 | BM25 + LLM compress; sem LongMemEval/LoCoMo público; hot-layer always-on compensa parcialmente |
| Write | 72 | hooks + set-overwrite hot layer + append knowledge; sem Minions/batch vector |
| Read | 74 | hot-layer free; BM25 top-k + cache 60s; não HNSW |
| Persistence | 80 | markdown durable + audit jsonl; facts curados (não verbatim policy) |
| Schema | 86 | People/Companies/Ideas/Research + proposal kinds + TELOS/USER tree |
| Local-first | 64 | files 100% local; DA precisa LLM cloud no path principal |
| Vector | 42 | **by design** sem vector DB intermediário (`MemorySystem.md`) |
| Graph | 84 | graphology + domains; wikilinks/related; menos auto-wire zero-LLM que gbrain |

---

## Cross-read vs peers

| Se você compara LifeOS com… | Leitura |
|----------------------------|---------|
| **mempalace** | LifeOS perde fidelity/offline; ganha life-ops, DA, dashboard, Algorithm |
| **gbrain** | mais próximo: ambos entity knowledge (people/companies) + agent runtime. gbrain = **knowledge brain product**; LifeOS = **life OS harness** com knowledge folder |
| **mem0** | eixos opostos: mem0 = multi-store SDK; LifeOS = monólito file-first no harness |
| **memori** | memori = agent-action facts SQL; LifeOS = identity + goals + knowledge MD |
| **gsd-2** | ambos “side memory no coding agent”; LifeOS é ordens de magnitude mais completo como OS |
