# Task: bench-matrix — Comparison matrix (2-way ou n-way)

## Propósito

Gerar a matriz de comparação de features/capabilities entre 2 ou mais subjects. Para cada item da matriz, classificar em `Forte | Parcial | Sem_Equiv`.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `subjects[]` | sim | 2+ slugs de subjects com inventários prontos |
| `dimension_pack` | sim | pack do `data/dimension-packs.yaml` |
| `output_dir` | sim | `OS/_bench/{slug}/` |

## Outputs

| File | Format |
|------|--------|
| `{output_dir}/comparison-matrix.json` | JSON |
| `{output_dir}/comparison-matrix.md` | MD |

## Pré-condições

- Inventários de todos os subjects existem em `OS/_bench/_inventories/{subject}/`
- `data/dimension-packs.yaml` contém o pack solicitado
- `templates/comparison-matrix-tmpl.md` carregado

## Passos

### Passo 1: Carregar inputs

```
Read: OS/_bench/_inventories/{subject_a}/inventory.json
Read: OS/_bench/_inventories/{subject_b}/inventory.json
Read: data/dimension-packs.yaml
```

Para cada subject, extrair:
- capabilities[]
- quality_signals
- extension_points
- modules

### Passo 2: Construir universo de capabilities

Unir capabilities de todos os subjects. Canonicalizar nomes similares (ex: "plugin system" ≡ "plugin support" ≡ "extensibility.plugins"):

```
Para cada capability de cada subject:
  - Normalizar nome (lowercase, stripped, sem plurals)
  - Agrupar sinônimos em um "canonical capability"
  - Anexar evidence paths

Resultado: lista unificada de ~30–80 capabilities distintas
```

### Passo 3: Agrupar por categoria

Usar as dimensões do `dimension_pack` como categorias principais. Cada capability é roteada pra uma categoria:

```
Para cada canonical capability:
  - Mapear pra uma dimension do pack
  - Se não bate: colocar em "General / Other"
```

### Passo 4: Classificar equivalência (2-way)

Para cada feature em cada categoria:

```
FOR each feature:
  A_value = inventário de A tem essa capability?
  B_value = inventário de B tem essa capability?

  IF both have AND depth/breadth is comparable:
    equivalence = "Forte" (5/5)
  ELSE IF both have BUT one is noticeably stronger (coverage/depth/signals):
    equivalence = "Parcial" (3/5)
  ELSE IF only one has:
    equivalence = "Sem_Equiv" (1/5)
    mark which side is only

  STORE delta: 1-line describing the difference
```

**Regra crítica:** classificação é sobre dados observáveis (evidence paths). Nunca "adivinhe" que um subject tem algo sem evidence.

### Passo 5: N-way matrix

Para N ≥ 3:

- Gerar tabela com N+1 colunas (feature name + N subjects)
- Cada cell: `yes (detail)` | `no` | `partial (detail)`
- Skipar a classificação Forte/Parcial/Sem_Equiv (só faz sentido pair-wise)
- Ao invés, gerar ranking por feature: quantos subjects têm, quais são os "líderes" por feature

### Passo 6: Montar JSON

```json
{
  "generatedAt": "{ISO-8601}",
  "comparison_type": "pair | nway",
  "subjects": ["{slug_a}", "{slug_b}", "..."],
  "dimension_pack": "{pack_name}",
  "categories": [
    {
      "name": "{category_name}",
      "features": [
        {
          "name": "{feature_name}",
          "values": {
            "{slug_a}": "{detail_or_no}",
            "{slug_b}": "{detail_or_no}"
          },
          "evidence": {
            "{slug_a}": ["OS/{slug_a}/{path}"],
            "{slug_b}": ["OS/{slug_b}/{path}"]
          },
          "equivalence": "Forte | Parcial | Sem_Equiv",
          "delta": "{1-line}"
        }
      ]
    }
  ],
  "summary": {
    "total_features": 0,
    "forte_count": 0,
    "parcial_count": 0,
    "sem_equiv_count": 0,
    "a_only_count": 0,
    "b_only_count": 0
  },
  "subject_only_capabilities": {
    "{slug_a}": [
      { "name": "{cap}", "category": "{cat}", "evidence": "OS/{slug_a}/{path}" }
    ],
    "{slug_b}": []
  }
}
```

### Passo 7: Renderizar MD

Usar `templates/comparison-matrix-tmpl.md` preenchendo:
- Header, sources, method
- Inventory summary (puxar das métricas de cada inventário)
- Feature matrix por categoria
- {A}-Only, {B}-Only
- Partial equivalences notáveis (Parcial com delta > "minor")
- Objective reading (prose derivada dos dados)
- Method disclosure

## Veto conditions

- Inventário de algum subject não existe → HALT
- Pack não existe em `data/dimension-packs.yaml` → HALT
- Total de features comparadas < 10 → WARN (baixa granularidade)
- Alguma evidência cita path que não existe → WARN e marcar confidence LOW na cell

## Verificação

- [ ] JSON parseable
- [ ] Total features ≥ 10
- [ ] Toda classificação Forte tem evidence em ambos os lados
- [ ] Toda Sem_Equiv aparece em {subject}-only no output
- [ ] Contagens batem com a soma (forte + parcial + sem_equiv == total)
- [ ] Nenhum evidence path inventado
- [ ] MD renderiza sem placeholders

---

_os-bench / bench-matrix task / v1.0_
