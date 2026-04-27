# Task: bench-absorb — Roadmap de absorção

## Propósito

Gerar um roadmap priorizado de features do `source_subject` pra absorver em `target_subject`. Baseado nos gaps identificados em `gap-analysis.json`.

Aplica-se a `pair`. Precisa que o bench-pair completo já tenha rodado.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `source_subject` | sim | De onde vêm as features |
| `target_subject` | sim | Onde absorver |
| `bench_dir` | sim | `OS/_bench/{a}-vs-{b}/` |

## Outputs

| File | Format |
|------|--------|
| `{bench_dir}/deep/absorption-roadmap.md` | MD |

## Pré-condições

- `{bench_dir}/gap-analysis.json` existe (gaps de target = features de source pra absorver)
- `{bench_dir}/comparison-matrix.json` existe
- Inventário do source existe
- `templates/absorption-roadmap-tmpl.md` carregado

## Passos

### Passo 1: Determinar direção

```
IF source == subject_a AND target == subject_b:
  features_to_absorb = gap-analysis.b_gaps  (o que A tem e B não)
ELSE IF source == subject_b AND target == subject_a:
  features_to_absorb = gap-analysis.a_gaps  (o que B tem e A não)
ELSE:
  HALT — source/target não batem com o bench-pair
```

### Passo 2: Deep-analyze cada feature

Pra cada feature em `features_to_absorb`:

```
1. Read: o arquivo no source (evidence path da gap)
2. Extract:
   - O que a feature faz (2–3 frases técnicas)
   - Como está implementada (key code pattern, max 20 linhas de snippet)
   - Dependências transitivas (imports, libs externas)
3. Assess:
   - Valor para target (3 benefits concretos)
   - Complexidade de absorção (Baixa/Média/Alta) com estimativa de #arquivos afetados
   - Prioridade (P0/P1/P2/P3) — herdar de gap-analysis mas pode refinar
4. Target path:
   - Onde no target_subject implementar (inferir módulo análogo)
```

### Passo 3: Agrupar em fases

```
Fase 1 (Quick Wins): complexidade Baixa E prioridade P0/P1
Fase 2 (Core): complexidade Média E prioridade P0/P1
Fase 3 (Advanced): complexidade Alta E prioridade P0/P1
Fase 4 (Future): prioridade P2/P3 qualquer complexidade
```

### Passo 4: Dependências entre fases

Identificar:
- Features de Fase 2 que dependem de features de Fase 1 → documentar ordem
- Features com dependências externas (lib, service) → listar separado

### Passo 5: Métricas de sucesso

Pra cada fase, definir:
- KPI quantificável (ex: "+X pts em dimensão Y no próximo re-score")
- KPI qualitativo (ex: "target passa a ter paridade em capability Z")

### Passo 6: Executable backlog

Gerar JSON inline (embutido no MD, como bloco de código) — pronto pra importar em task tracker:

```json
{
  "generatedAt": "{ISO-8601}",
  "source_subject": "...",
  "target_subject": "...",
  "total_items": N,
  "items": [
    {
      "id": "ABS-001",
      "title": "...",
      "phase": 1,
      "priority": "P0",
      "complexity": "LOW",
      "source_reference": "OS/{source}/{path}",
      "target_reference": "OS/{target}/{suggested_path}",
      "acceptance_criteria": ["..."]
    }
  ]
}
```

### Passo 7: Renderizar

Usar `templates/absorption-roadmap-tmpl.md`. Preencher cada seção.

Criar o diretório `{bench_dir}/deep/` se não existir antes de escrever.

## Regras

1. **Source code verbatim**: snippets citados devem ser copiados literalmente do source, com path preciso. Nunca paráfrase.
2. **Target path sugerido**: inferir módulo análogo. Se não houver análogo, propor criação de novo módulo com nome explícito.
3. **Acceptance criteria**: cada item do backlog tem 2+ ACs mensuráveis.
4. **Sem duplicação**: uma feature pertence a exatamente 1 fase.

## Veto conditions

- Gap-analysis ausente → HALT
- 0 features pra absorver → gerar report mínimo "nothing to absorb" e SAIR
- Source e target são o mesmo subject → HALT

## Verificação

- [ ] Toda feature do gap analysis foi endereçada
- [ ] Snippets são cópia verbatim de paths reais
- [ ] Cada item tem valor + complexidade + prioridade
- [ ] Fases não duplicam features
- [ ] Executable backlog JSON é parseable
- [ ] Métricas de sucesso são mensuráveis
- [ ] MD renderiza sem placeholders

---

_os-bench / bench-absorb task / v1.0_
