# Task: bench-score — Weighted scoring multi-dimensão

## Propósito

Pontuar os subjects nas dimensões do `dimension_pack` escolhido, com pesos, signals documentados e confidence. Output é a scorecard canônica.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `subjects[]` | sim | 2+ slugs |
| `dimension_pack` | sim | pack do `data/dimension-packs.yaml` |
| `comparison_matrix` | opcional | `comparison-matrix.json` pra reforçar scores |
| `output_dir` | sim | `OS/_bench/{slug}/` |

## Outputs

| File | Format |
|------|--------|
| `{output_dir}/scorecard.json` | JSON |
| `{output_dir}/scorecard.md` | MD |

## Pré-condições

- Inventários dos subjects existem
- `data/dimension-packs.yaml` carregado
- `templates/scorecard-tmpl.md` carregado

## Passos

### Passo 1: Validar

```
- Carregar pack → verificar weights somam 1.00 (tolerância 0.01)
- FAIL se weights não somam
- FAIL se pack tem < 3 dimensões
```

### Passo 2: Determinar método de scoring por subject

```
IF inventário.extraction_method == "filesystem-scan" AND confidence == HIGH:
  method = "installed" → "Scored from local filesystem analysis of OS/{subject}/"
ELIF inventário.extraction_method == "filesystem-scan" AND confidence == MEDIUM:
  method = "installed-partial" → "Local scan with some web augmentation"
ELSE:
  method = "estimated" → "Limited local signals, web fallback used"
```

### Passo 3: Scorear cada dimensão

**Este é o passo cognitivo principal.** Para cada dimensão do pack:

```
1. Listar os signals declarados no pack (pack.dimensions[i].signals[])

2. Para cada subject, buscar observações de cada signal no inventário:
   - Capabilities mapping pra signal
   - Quality signals
   - External deps
   - Entry points
   - Extension points
   - Métricas (LOC, stars, contributors, last commit)

3. Consultar scoring_scale declarado no pack (90-100 / 60-89 / 30-59 / 0-29)
   e mapear as observações pra uma banda.

4. Score exato dentro da banda: prose-to-number.
   Ex: banda 60-89 com 3 signals fortes → 82
       banda 60-89 com 1 signal fraco → 62

5. Confidence da dimensão:
   - HIGH: 3+ signals observados com evidence path
   - MEDIUM: 2 signals observados
   - LOW: 1 signal ou só inferência

6. Justificativa: 1 frase por subject explicando o score
```

### Passo 4: Regras de integridade (NON-NEGOTIABLE)

1. **Score ≥90 requer 2+ signals** com evidence path concreto. Falha → rebaixar pra <90.
2. **Score = null** quando zero signals observáveis. Confidence = LOW. NÃO inventar.
3. **Delta honesty**: se B lidera, reportar B lidera.
4. **Sem invenção**: nenhum score/signal pode referenciar path que não existe em `OS/{subject}/`.

### Passo 5: Calcular totais ponderados

```
weighted_total_X = SUM over dimensions: (score_X * weight)

Para cada dim com score=null, distribuir o peso proporcionalmente entre as dims pontuadas (flag isso no output).

Delta = total_A - total_B
Overall winner = A if delta > 0, B if delta < 0, TIE if abs(delta) < 1
```

### Passo 6: Rankings

- A_strongest[]: top 3 dimensões onde A lidera (maior delta positivo)
- B_strongest[]: top 3 dimensões onde B lidera
- Closest[]: dimensões com |delta| < 5 (área competitiva)

### Passo 7: Confidence overall

```
IF todas dimensões HIGH → overall = HIGH
ELIF qualquer LOW → overall = LOW
ELSE → MEDIUM
```

### Passo 8: Montar JSON

```json
{
  "generatedAt": "{ISO-8601}",
  "comparison_type": "pair | nway",
  "subjects": ["{slug_a}", "{slug_b}"],
  "dimension_pack": "{pack_name}",
  "methods": {
    "{slug_a}": "installed | installed-partial | estimated",
    "{slug_b}": "..."
  },
  "dimensions": [
    {
      "id": "{dim_id}",
      "name": "{dim_name}",
      "weight": 0.15,
      "scores": {
        "{slug_a}": 85,
        "{slug_b}": 72
      },
      "signals_observed": {
        "{slug_a}": [
          { "signal": "...", "value": "...", "evidence": "OS/{slug_a}/{path}" }
        ],
        "{slug_b}": []
      },
      "confidence": "HIGH | MEDIUM | LOW",
      "justification": {
        "{slug_a}": "{1_sentence}",
        "{slug_b}": "{1_sentence}"
      },
      "delta": 13,
      "advantage": "{slug_a} | {slug_b} | TIE"
    }
  ],
  "weighted_totals": {
    "{slug_a}": 82.3,
    "{slug_b}": 75.1
  },
  "overall_winner": "{slug_a}",
  "total_delta": 7.2,
  "dimension_wins": {
    "{slug_a}": 5,
    "{slug_b}": 2,
    "ties": 1
  },
  "rankings": {
    "a_strongest": ["{dim_id_1}", "{dim_id_2}"],
    "b_strongest": ["{dim_id_3}"],
    "closest": ["{dim_id_4}"]
  },
  "confidence_overall": "MEDIUM",
  "limitations": ["..."]
}
```

### Passo 9: Renderizar MD

Usar `templates/scorecard-tmpl.md`.

## Veto conditions

- Weights não somam 1.00 → HALT
- >50% das dimensões com score=null → HALT (dados insuficientes)
- Pack pede signals que nenhum subject tem → HALT

## Scoring transparency rules

Repetindo pra clareza:

1. **Todo score tem pelo menos 1 signal com evidence path**
2. **Score 90+ tem 2+ signals com evidence path concreto**
3. **Signal ausente** → `"value": "not_observed"` e score reduzido
4. **Métricas inventadas** → PROIBIDO

## Verificação

- [ ] JSON parseable
- [ ] weighted_totals = recalculados corretamente (verificar)
- [ ] Todo score ≥ 0 e ≤ 100 (ou null)
- [ ] Todo score ≥90 tem 2+ signals com evidence
- [ ] Deltas calculados corretamente (A - B)
- [ ] Confidence overall derivado corretamente
- [ ] Rankings (strongest/closest) derivados dos dados reais
- [ ] MD renderiza sem placeholders

---

_os-bench / bench-score task / v1.0_
