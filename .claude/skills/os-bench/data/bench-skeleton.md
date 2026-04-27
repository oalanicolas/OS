# Benchmark Skeleton (os-bench)

Scaffold canônico do output de um benchmark. Usado como referência ao executar qualquer `*bench-pair`, `*bench-nway` ou `*bench-absorb`.

## 1) Output root

**2-way:** `OS/_bench/{subject_a}-vs-{subject_b}/`
**N-way:** `OS/_bench/{topic}-Nway/`

Regra: slug em kebab-case, sem data, sem versão. O `metadata.json` carrega data e versão.

## 2) Artifact set (2-way)

```
OS/_bench/{a}-vs-{b}/
  ├── metadata.json                    # tipo, dimensões, data, perfil, slug, versão
  ├── inventory-{a}.json               # inventário estruturado A
  ├── inventory-{a}.md                 # idem em prosa
  ├── inventory-{b}.json
  ├── inventory-{b}.md
  ├── comparison-matrix.json           # matriz de features/capabilities
  ├── comparison-matrix.md
  ├── scorecard.json                   # scores por dimensão + pesos
  ├── scorecard.md
  ├── gap-analysis.json                # gaps bidirecionais
  ├── gap-analysis.md
  ├── battle-card.md                   # 1-page resumo
  ├── executive-report.md              # narrativa completa
  └── deep/
      ├── feature-comparison.md        # (opcional) deep dive por feature
      ├── absorption-roadmap.md        # (se *bench-absorb rodou)
      └── migration-playbook.md        # (opcional) passos de migração
```

## 3) Artifact set (N-way)

```
OS/_bench/{topic}-Nway/
  ├── metadata.json
  ├── inventory-{each subject}.{json,md}
  ├── comparison-matrix.{json,md}      # N colunas
  ├── scorecard.{json,md}              # N colunas
  └── executive-report.md
```

Nota: em N-way não geramos `battle-card.md` (não cabe em 1 página) nem `gap-analysis.json` bidirecional por par (seria N² pares — use `*bench-pair` para cada par de interesse).

## 4) Mandatory mapping logic (2-way)

Classes de equivalência por feature comparada:

| Classe | Código | Significado |
|--------|--------|-------------|
| Forte | 5/5 | A e B implementam a mesma capacidade com mesma profundidade |
| Parcial | 3/5 | Implementações equivalentes mas com gap de profundidade/qualidade |
| Sem equivalente | 1/5 | Só um dos lados tem |

Mapeamentos obrigatórios em `comparison-matrix`:

- A → B (para cada capability de A, buscar contraparte em B)
- B-only (capabilities de B sem contraparte em A)
- A-only (capabilities de A sem contraparte em B)
- Diferenciais parciais (onde ambos têm mas um é melhor)

## 5) Scoring

Dimensões carregadas de `data/dimension-packs.yaml` conforme pack escolhido.

- Score 0–100 por dimensão
- Pesos configuráveis por pack (soma = 1.00)
- Cada score precisa de 2+ signals (observações concretas) documentados
- Confidence HIGH/MEDIUM/LOW por dimensão

## 6) Seções mínimas — `comparison-matrix.md`

1. Header (scope, date, type, subjects, pack)
2. Sources (URLs/paths pra dados de cada subject)
3. Method (como os dados foram coletados)
4. Inventory summary dos subjects
5. Feature/capability matrix com scores de equivalência
6. {A}-only capabilities
7. {B}-only capabilities
8. Partial equivalences (notable deltas)
9. Objective reading (strengths de cada)
10. Recommendation/next-depth paths

## 7) Seções mínimas — `scorecard.md`

1. Scoring method + pack usado
2. Lista de dimensões com pesos
3. Tabela per-dimensão (A | B | Delta)
4. Weighted totals
5. Confidence per dimensão
6. Dimension analysis (signals + justificativa)
7. Score distribution (strongest/weakest per subject)
8. Known limitations

## 8) JSON mínimo

### `metadata.json`

```json
{
  "generatedAt": "ISO-8601",
  "comparison_type": "pair | nway",
  "subjects": ["slug_a", "slug_b", "..."],
  "dimension_pack": "coding-agent | memory | ...",
  "scoring_dimensions": ["dim_id_1", "dim_id_2"],
  "profile": "quick | standard | full",
  "skill_version": "1.0.0",
  "output_root": "OS/_bench/{slug}/"
}
```

### `scorecard.json`

```json
{
  "generatedAt": "ISO-8601",
  "comparison_type": "pair | nway",
  "subjects": ["slug_a", "slug_b"],
  "dimension_pack": "memory",
  "dimensions": [
    {
      "id": "recall_accuracy",
      "name": "Recall Accuracy",
      "weight": 0.25,
      "scores": { "slug_a": 92, "slug_b": 96 },
      "signals": { "slug_a": ["..."], "slug_b": ["..."] },
      "confidence": "HIGH",
      "delta": -4
    }
  ],
  "weighted_totals": { "slug_a": 82.3, "slug_b": 79.5 },
  "overall_winner": "slug_a",
  "confidence_overall": "MEDIUM"
}
```

### `comparison-matrix.json`

```json
{
  "generatedAt": "ISO-8601",
  "subjects": ["slug_a", "slug_b"],
  "categories": [
    {
      "name": "Persistence",
      "features": [
        {
          "name": "Verbatim storage",
          "values": { "slug_a": "yes (Chroma)", "slug_b": "no (paraphrased)" },
          "equivalence": 1,
          "delta": "slug_a verbatim, slug_b uses embeddings-only"
        }
      ]
    }
  ],
  "summary": {
    "total_features": 47,
    "forte_count": 18,
    "parcial_count": 12,
    "sem_equiv_count": 17,
    "a_only_count": 9,
    "b_only_count": 8
  }
}
```

### `gap-analysis.json`

```json
{
  "generatedAt": "ISO-8601",
  "subjects": ["slug_a", "slug_b"],
  "a_gaps": [
    {
      "id": "GAP-A-001",
      "name": "Graph support",
      "dimension": "graph_support",
      "severity": "HIGH | MED | LOW",
      "complexity": "HIGH | MED | LOW",
      "strategic_value": "HIGH | MED | LOW",
      "priority": "P0 | P1 | P2 | P3",
      "evidence": "OS/slug_b/src/graph/...",
      "description": "..."
    }
  ],
  "b_gaps": [ "..." ],
  "counts": {
    "a_gaps_total": 9,
    "b_gaps_total": 8,
    "a_p0": 2, "a_p1": 3, "a_p2": 3, "a_p3": 1,
    "b_p0": 1, "b_p1": 2, "b_p2": 4, "b_p3": 1
  }
}
```

## 9) Quality gate

Antes de considerar o benchmark completo:

- [ ] Todos os artefatos canônicos existem (ou marcados como intencionalmente skipped em `metadata.json#skipped_artifacts[]`)
- [ ] Todo JSON é parseable
- [ ] Zero claims inventados — cada assertion tem path real ou URL citada
- [ ] Scoring method disclosed (qual pack, qual label)
- [ ] Confidence level por dimensão + rollup
- [ ] Gaps bidirecionais (mesmo se um lado for 0)
- [ ] Sources citadas pra ambos os subjects
- [ ] Deltas calculados corretamente (verificar aritmética)
- [ ] Nenhuma pasta ou arquivo fora de `OS/_bench/`

## 10) Confidence tagging

Por dimensão:

| Confidence | Critério |
|-----------|----------|
| HIGH | 3+ signals de fonte local (filesystem) + metric quantificado |
| MEDIUM | 2 signals mistos (local + web) ou 1 signal forte |
| LOW | 1 signal apenas ou inferência sem métrica |

Rollup overall:

- Todas HIGH → HIGH
- Qualquer LOW → LOW
- Resto → MEDIUM
