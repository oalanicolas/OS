# Task: bench-gap — Bidirectional gap analysis

## Propósito

Identificar gaps bidirecionais entre 2 subjects, classificados por severity/complexity/priority. Base pra roadmap de absorção e decisão de adoção.

Esta task aplica-se apenas a `comparison_type=pair`. Em n-way, skip (ou rodar pair-wise separado).

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `subject_a` | sim | primeiro slug |
| `subject_b` | sim | segundo slug |
| `dimension_pack` | sim | pack (pra pesar impacto) |
| `output_dir` | sim | `OS/_bench/{a}-vs-{b}/` |

## Outputs

| File | Format |
|------|--------|
| `{output_dir}/gap-analysis.json` | JSON |
| `{output_dir}/gap-analysis.md` | MD |

## Pré-condições

- `{output_dir}/comparison-matrix.json` existe (gaps derivam da matrix)
- `{output_dir}/scorecard.json` existe (impacto usa pesos do pack + delta de scores)
- `templates/gap-analysis-tmpl.md` carregado

## Passos

### Passo 1: Carregar artefatos

```
Read: {output_dir}/comparison-matrix.json
Read: {output_dir}/scorecard.json
Read: data/dimension-packs.yaml (para weights)
```

### Passo 2: Extrair gaps de A (o que B tem e A não)

```
a_gaps = []

Da comparison-matrix:
  - Todo feature com equivalence="Sem_Equiv" onde só B tem → Missing gap de A
  - Todo feature com equivalence="Parcial" onde B é stronger → Partial gap de A

Para cada gap:
  - Capability name
  - Dimension (category)
  - Evidence em B (path)
  - Target sugerido em A (inferir do módulo análogo em A)
  - Description: 1 frase
```

### Passo 3: Extrair gaps de B (o que A tem e B não)

Espelho do Passo 2. Sempre executar — bidirecional é obrigatório.

### Passo 4: Classificar impact

Para cada gap:

```
impact = função(dimension_weight, score_delta):
  weight = pack.dimensions[dim].weight
  delta = |scorecard.scores.A - scorecard.scores.B|
  impact_score = weight * delta

  HIGH: impact_score >= 8 (peso alto + delta grande)
  MED: 3 <= impact_score < 8
  LOW: impact_score < 3
```

### Passo 5: Classificar complexity

Heurística baseada em tipo de gap:

```
IF a feature existe num único arquivo do source E não tem deps internas:
  complexity = LOW
ELIF feature envolve 2–10 arquivos OU integra com 1 módulo existente:
  complexity = MED
ELSE:
  complexity = HIGH (mudança arquitetural ou cross-module)
```

Estimar olhando o source path e o número de arquivos no módulo de origem.

### Passo 6: Priority matrix

Cruzar impact × complexity:

| Impact \ Complexity | LOW | MED | HIGH |
|---------------------|-----|-----|------|
| HIGH | **P0** | **P1** | P2 |
| MED | P1 | P2 | P3 |
| LOW | P3 | P3 | P3 |

### Passo 7: Contar & agregar

```
counts = {
  a_gaps_total, b_gaps_total,
  a_by_impact: { HIGH, MED, LOW },
  b_by_impact: { HIGH, MED, LOW },
  a_by_priority: { P0, P1, P2, P3 },
  b_by_priority: { P0, P1, P2, P3 },
  most_affected_dims_a: [...],
  most_affected_dims_b: [...]
}
```

### Passo 8: Action items

Pra cada gap P0 ou P1, criar action item:

```
{
  action_title: "Implement {capability} in {target_subject}",
  target: "{A | B}",
  closes_gap: "GAP-{A|B}-{NNN}",
  dimension: "{dim_id}",
  expected_impact: "+{N} pts em {dim}",
  priority: "P0 | P1",
  source_to_copy: "OS/{source_subject}/{path}",
  dependencies: [...]
}
```

### Passo 9: Montar JSON

```json
{
  "generatedAt": "{ISO-8601}",
  "subjects": ["{slug_a}", "{slug_b}"],
  "dimension_pack": "{pack_name}",
  "a_gaps": [
    {
      "id": "GAP-A-001",
      "name": "{capability}",
      "dimension": "{dim_id}",
      "type": "Missing | Partial",
      "severity": "HIGH | MED | LOW",
      "complexity": "HIGH | MED | LOW",
      "strategic_value": "HIGH | MED | LOW",
      "priority": "P0 | P1 | P2 | P3",
      "evidence": "OS/{slug_b}/{path}",
      "target_in_a": "OS/{slug_a}/{suggested_path}",
      "description": "..."
    }
  ],
  "b_gaps": [ "..." ],
  "counts": {
    "a_gaps_total": 0,
    "b_gaps_total": 0,
    "a_p0": 0, "a_p1": 0, "a_p2": 0, "a_p3": 0,
    "b_p0": 0, "b_p1": 0, "b_p2": 0, "b_p3": 0
  },
  "most_affected_dimensions": {
    "a": [ { "dimension": "...", "gap_count": 0, "highest_priority": "P0" } ],
    "b": []
  },
  "action_items": [
    {
      "action_title": "...",
      "target": "A",
      "closes_gap": "GAP-A-001",
      "priority": "P0",
      "source_to_copy": "OS/{slug_b}/{path}"
    }
  ]
}
```

### Passo 10: Renderizar MD

Usar `templates/gap-analysis-tmpl.md`.

## Veto conditions

- `comparison-matrix.json` ausente → HALT
- `scorecard.json` ausente → HALT
- Gaps bidirecionais == 0 de ambos os lados → WARN (produtos idênticos? revisar matrix)
- Algum gap sem evidence path → reportar e excluir

## Verificação

- [ ] JSON parseable
- [ ] Sempre tem tanto a_gaps quanto b_gaps (mesmo que um seja vazio)
- [ ] Toda gap P0/P1 tem action_item correspondente
- [ ] Toda gap tem evidence path real
- [ ] Priorização consistente (HIGH+LOW == P0 sempre, etc)
- [ ] Counts batem com a soma dos arrays
- [ ] MD renderiza sem placeholders

---

_os-bench / bench-gap task / v1.0_
