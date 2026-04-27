# Task: bench-battle-card — 1-page resumo executivo

## Propósito

Gerar um battle-card de 1 página que resume o benchmark pra decisão rápida. Formato MD único, sem JSON.

Aplica-se apenas a `comparison_type=pair`. Em n-way, skip.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `subject_a` | sim | |
| `subject_b` | sim | |
| `output_dir` | sim | `OS/_bench/{a}-vs-{b}/` |

## Outputs

| File | Format |
|------|--------|
| `{output_dir}/battle-card.md` | MD (≤ ~200 linhas) |

## Pré-condições

- `{output_dir}/scorecard.json` existe
- `{output_dir}/comparison-matrix.json` existe
- Inventories existem
- `templates/battle-card-tmpl.md` carregado

## Passos

### Passo 1: Quick specs

Puxar de cada inventory:

- Stack
- Primary language
- LOC estimate
- License
- GitHub stars (se disponível)
- Last commit date
- Local-first: yes/no (baseado em capabilities)

### Passo 2: Score table

Da scorecard:

- Linha por dimensão com scores A | B | winner icon
- Linha final com weighted totals

### Passo 3: Strengths & Weaknesses

Da scorecard `rankings`:

- A strengths: top 3 dimensões onde A lidera (usar justification como fonte)
- A weaknesses: top 2 dimensões onde A perde com maior delta
- B strengths: top 3 dimensões onde B lidera
- B weaknesses: top 2 dimensões onde B perde com maior delta

### Passo 4: "When to pick"

Prose curta (2–3 frases por lado) — cenário concreto de escolha.

Derivar de:
- Strengths de cada lado
- Capabilities únicas em {subject}-only
- Trade-offs observados (ex: "A = local-first" → "pick A if privacy-sensitive")

### Passo 5: TL;DR Verdict

Um parágrafo curto com a conclusão executiva. Evitar "depende" — tomar posição baseada no weighted total e contexto.

Seguido de 1 linha "Recommendation:".

### Passo 6: Renderizar

Usar `templates/battle-card-tmpl.md`. Manter enxuto — battle card é 1 página.

## Regras

1. **Opinionated**: o battle card toma posição. "Depende" só é aceitável se realmente são empatados (|delta| < 3 pts).
2. **Evidência implícita**: battle-card não cita paths (diferente da scorecard/matrix). Assume que o scorecard/matrix têm as evidências.
3. **Limite**: ~200 linhas MD. Se passar, enxugar.

## Verificação

- [ ] MD renderiza sem placeholders
- [ ] Todos os scores batem com scorecard.json
- [ ] "When to pick A" e "When to pick B" são distintos e não triviais
- [ ] TL;DR toma posição (não "ambos são bons")
- [ ] ≤ ~200 linhas

---

_os-bench / bench-battle-card task / v1.0_
