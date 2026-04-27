# Task: bench-executive-report — Narrativa completa do benchmark

## Propósito

Consolidar todos os artefatos em um relatório narrativo. É o output final, legível de ponta a ponta, adequado pra stakeholder que não vai mergulhar nos JSONs.

Aplica-se a `pair` e `nway`.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `subjects[]` | sim | 2+ slugs |
| `output_dir` | sim | `OS/_bench/{slug}/` |

## Outputs

| File | Format |
|------|--------|
| `{output_dir}/executive-report.md` | MD |

## Pré-condições

Todos os seguintes artefatos já existem em `{output_dir}/`:

- `metadata.json`
- `inventory-{slug}.json` para cada subject
- `comparison-matrix.json`
- `scorecard.json`
- `gap-analysis.json` (opcional em n-way)
- `battle-card.md` (opcional em n-way)

## Passos

### Passo 1: Carregar tudo

```
Read: metadata.json
Read: scorecard.json
Read: comparison-matrix.json
Read: gap-analysis.json (se existir)
Read: inventory-*.json
```

### Passo 2: Executive summary

4–6 frases cobrindo:

- O que foi comparado (subjects, pack)
- Overall winner + delta
- Principal razão do winner ganhar
- Principal força do loser (onde ele brilha)
- Recomendação high-level

### Passo 3: Key metrics

Tabela com:
- Overall winner
- Dimensões analisadas
- Wins por subject
- Ties
- Totals de gaps A e B (apenas em pair)
- Confidence overall

### Passo 4: Scorecard summary

Copiar a tabela principal de scorecard (scores por dimensão + total ponderado).

### Passo 5: Dimension analysis

**Esta é a parte mais longa.** Para cada dimensão:

- Scores A / B / delta
- 3–5 frases de análise narrativa (não é dump da scorecard — é prose que conecta signals ao contexto)
- Key signals (1 por subject, cada com evidence path)
- Gaps na dimensão (se existirem)

### Passo 6: Gap highlights (apenas pair)

- Top N gaps de A
- Top N gaps de B

### Passo 7: Strategic recommendations

3–5 recomendações baseadas em:

- Gaps P0/P1 (derivam de gap-analysis)
- Dimensões onde perdedor tem oportunidade clara
- Sinergias quando cabem

Cada rec:
- Title
- Description (parágrafo)
- Target (A | B | both)
- Expected impact
- Priority

### Passo 8: "When to pick which"

Cenários de escolha (expansão do battle-card):

- Pick A if ... (4–5 cenários concretos)
- Pick B if ... (4–5)
- Consider both (complementary) if ... (2–3)

### Passo 9: Methodology

- Data sources
- Scoring method
- Artifacts generated table
- Limitations

### Passo 10: Appendix

Lista de todos os artefatos em `{output_dir}/`.

### Passo 11: Renderizar

Usar `templates/executive-report-tmpl.md`.

## Regras

1. **Sem dumps**: não copiar JSONs verbatim. O executive report é **narrativa** — prose + tabelas curadas.
2. **Opinionated**: igual ao battle card, toma posição.
3. **Completude**: deve conter info suficiente pra alguém decidir sem ler os JSONs.
4. **Evidence**: quando menciona features específicas, cita paths (`OS/{slug}/...`).

## Verificação

- [ ] MD renderiza sem placeholders
- [ ] Executive summary faz sentido standalone
- [ ] Dimension analysis cobre todas as dimensões do pack
- [ ] Strategic recommendations tem pelo menos 3
- [ ] "When to pick" tem cenários concretos
- [ ] Methodology disclosure completo
- [ ] Appendix lista arquivos que realmente existem

---

_os-bench / bench-executive-report task / v1.0_
