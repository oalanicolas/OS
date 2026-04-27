# Gap Analysis: {SUBJECT_A} vs {SUBJECT_B}

**Date:** {DATE}
**Dimension pack:** {PACK_NAME}
**Slug:** {SLUG}
**Source artifacts:** `comparison-matrix.json`, `scorecard.json`, `inventory-{a}.json`, `inventory-{b}.json`

---

## Executive Summary

{GAP_EXECUTIVE_SUMMARY_3_5_FRASES}

| Direction | Total gaps | HIGH | MED | LOW | P0 | P1 | P2 | P3 |
|-----------|:---------:|:----:|:---:|:---:|:--:|:--:|:--:|:--:|
| Gaps de {SUBJECT_A} (o que {B} tem e {A} não) | {A_TOTAL} | {HIGH_A} | {MED_A} | {LOW_A} | {P0_A} | {P1_A} | {P2_A} | {P3_A} |
| Gaps de {SUBJECT_B} (o que {A} tem e {B} não) | {B_TOTAL} | {HIGH_B} | {MED_B} | {LOW_B} | {P0_B} | {P1_B} | {P2_B} | {P3_B} |

---

## Gaps de {SUBJECT_A}

O que {SUBJECT_B} tem que {SUBJECT_A} não tem (ou tem parcialmente):

### Missing Capabilities (Sem_Equiv)

| ID | Capability | Dimension | Impact | Complexity | Priority | Description |
|----|-----------|-----------|:------:|:----------:|:--------:|-------------|
| GAP-A-{NNN} | {CAPABILITY} | {DIM} | {HIGH/MED/LOW} | {HIGH/MED/LOW} | {P0/P1/P2/P3} | {1_LINE} |

### Partial Gaps ({SUBJECT_B} Stronger)

| ID | Capability | What {A} has | What {A} lacks | Impact | Priority |
|----|-----------|-------------|-----------------|:------:|:--------:|
| GAP-A-{NNN} | {CAPABILITY} | {A_COVERS} | {WHAT_MISSING} | {IMPACT} | {PRIORITY} |

### Gap Detail

<!-- Uma seção por gap -->

#### GAP-A-{NNN}: {CAPABILITY}

- **Type:** {Missing | Partial}
- **Dimension:** {DIM}
- **Impact:** {HIGH/MED/LOW} — {WHY}
- **Complexity:** {HIGH/MED/LOW} — {WHY}
- **Priority:** {P0/P1/P2/P3}
- **Evidence (B has):** `OS/{B_SLUG}/{PATH}`
- **Target (where to add in A):** `OS/{A_SLUG}/{SUGGESTED_PATH}`
{IF_PARTIAL}
- **What {A} has:** {COVERAGE}
- **What's missing:** {DELTA}
{END_IF}

---

## Gaps de {SUBJECT_B}

O que {SUBJECT_A} tem que {SUBJECT_B} não tem (ou tem parcialmente):

### Missing Capabilities (Sem_Equiv)

| ID | Capability | Dimension | Impact | Complexity | Priority | Description |
|----|-----------|-----------|:------:|:----------:|:--------:|-------------|
| GAP-B-{NNN} | {CAPABILITY} | {DIM} | {HIGH/MED/LOW} | {HIGH/MED/LOW} | {P0/P1/P2/P3} | {1_LINE} |

### Partial Gaps ({SUBJECT_A} Stronger)

| ID | Capability | What {B} has | What {B} lacks | Impact | Priority |
|----|-----------|-------------|-----------------|:------:|:--------:|
| GAP-B-{NNN} | {CAPABILITY} | {B_COVERS} | {WHAT_MISSING} | {IMPACT} | {PRIORITY} |

### Gap Detail

#### GAP-B-{NNN}: {CAPABILITY}

- **Type:** {Missing | Partial}
- **Dimension:** {DIM}
- **Impact:** {HIGH/MED/LOW} — {WHY}
- **Complexity:** {HIGH/MED/LOW} — {WHY}
- **Priority:** {P0/P1/P2/P3}
- **Evidence (A has):** `OS/{A_SLUG}/{PATH}`
- **Target (where to add in B):** `OS/{B_SLUG}/{SUGGESTED_PATH}`

---

## Classification Matrix

### By Impact

| Impact | Gaps de {A} | Gaps de {B} |
|--------|:-----------:|:-----------:|
| HIGH | {H_A} | {H_B} |
| MED | {M_A} | {M_B} |
| LOW | {L_A} | {L_B} |

### By Complexity

| Complexity | Gaps de {A} | Gaps de {B} |
|------------|:-----------:|:-----------:|
| LOW | {LC_A} | {LC_B} |
| MED | {MC_A} | {MC_B} |
| HIGH | {HC_A} | {HC_B} |

### By Priority

| Priority | Gaps de {A} | Gaps de {B} |
|----------|:-----------:|:-----------:|
| P0 (crítico) | {P0_A} | {P0_B} |
| P1 (alto) | {P1_A} | {P1_B} |
| P2 (médio) | {P2_A} | {P2_B} |
| P3 (baixo) | {P3_A} | {P3_B} |

### Impact × Complexity Heatmap

```
              LOW complexity    MED complexity    HIGH complexity
HIGH impact   P0 (quick win)    P1 (invest)       P2 (strategic)
MED impact    P1 (easy win)     P2 (moderate)     P3 (hard/moderate)
LOW impact    P3 (trivial)      P3 (low value)    P3 (avoid)
```

---

## Most Affected Dimensions

### Para {SUBJECT_A}

| Dimension | Gap count | Highest priority | Cumulative impact |
|-----------|:---------:|:----------------:|:-----------------:|
| {DIM} | {N} | {P0} | {IMPACT_SCORE} |

### Para {SUBJECT_B}

| Dimension | Gap count | Highest priority | Cumulative impact |
|-----------|:---------:|:----------------:|:-----------------:|
| {DIM} | {N} | {P0} | {IMPACT_SCORE} |

---

## Action Items

Gaps P0 e P1 que merecem atenção imediata:

| # | Action | Target | Closes gap | Dimension | Expected impact | Priority |
|---|--------|--------|-----------|-----------|-----------------|:--------:|
| 1 | {ACTION_TITLE} | {A | B} | {GAP_ID} | {DIM} | +{N} pts | P0 |

### Action Detail

#### 1. {ACTION_TITLE}

- **Target:** {SUBJECT_A | SUBJECT_B}
- **Closes gap:** {GAP_ID} ({CAPABILITY})
- **Description:** {WHAT_TO_DO}
- **Expected score improvement:** +{N} em {DIM}
- **Dependencies:** {LIST_OR_NONE}
- **Source to copy/adapt:** `OS/{source_slug}/{PATH}`

---

## Methodology

- **Gap identification:** baseado em `comparison-matrix.json` (classes Forte/Parcial/Sem_Equiv)
- **Impact:** derivado dos pesos do dimension pack + score delta
- **Complexity:**
  - LOW: mudança em 1–3 arquivos, <1 dia
  - MED: 4–15 arquivos ou integração com módulo, 1–3 dias
  - HIGH: mudança arquitetural ou múltiplos módulos, >3 dias
- **Priority matrix:** impact × complexity (ver heatmap)
- **Confidence:** {HIGH/MED/LOW}

---

_Generated by os-bench bench-gap task | Template v1.0_
