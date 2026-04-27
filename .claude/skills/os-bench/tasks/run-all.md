# Task: run-all — Executa os 6 benchmarks canônicos em sequência

## Propósito

Rodar em sequência os 6 benchmarks planejados pra cobrir as categorias principais do repositório `OS/`. Cada um produz um set canônico em `OS/_bench/{slug}/`.

## Inputs

Nenhum — a lista é fixa (ver Plano abaixo). Pode passar `--skip <slug>` pra pular um.

## Plano

| # | Slug | Pack | Subjects | Tipo | Notes |
|---|------|------|----------|------|-------|
| 1 | `coding-agents-8way` | `coding-agent` | claude-code-main, codex, aider, OpenHands, gsd-2, gstack, superpowers, ai-website-cloner-template | nway | 8 agents; foco em autonomia/TDD/multi-agent |
| 2 | `memory-4way` | `memory` | gbrain, mempalace, mem0, gsd-2 | nway | 4 memory systems; local-first vs cloud |
| 3 | `orchestration-5way` | `orchestration` | BMAD-METHOD, crewAI, autogen, paperclip, claude-remote-manager | nway | 5 orchestration frameworks |
| 4 | `spec-driven-3way` | `spec-driven` | spec-kit, get-shit-done, superpowers | nway | 3 approaches a spec-driven dev |
| 5 | `personal-assistant-3way` | `personal-assistant` | openclaw, hermes-agent, gbrain | nway | 3 personal assistants |
| 6 | `workflow-infra-2way` | `workflow-infra` | workflow, gh-aw | pair | durable workflows: Vercel vs GitHub Actions agentic |

## Pré-condições

- Todos os 18 subjects únicos existem em `OS/`
- A skill está completa (tasks, templates, data)

## Passos

### Passo 1: Validar subjects

```
unique_subjects = union de todos os subjects dos 6 benchmarks
= { claude-code-main, codex, aider, OpenHands, gsd-2, gstack, superpowers,
    ai-website-cloner-template, gbrain, mempalace, mem0, BMAD-METHOD,
    crewAI, autogen, paperclip, claude-remote-manager, spec-kit,
    get-shit-done, openclaw, hermes-agent, workflow, gh-aw }

Para cada: Bash "ls OS/{subject}"
FAIL_IF: algum falta → HALT listando os faltantes
```

### Passo 2: Inventário em batch

```
Para cada subject único:
  IF OS/_bench/_inventories/{subject}/inventory.json existe E tem <7 dias:
    SKIP (cache hit)
  ELSE:
    Rodar tasks/inventory.md {subject} (profile=quick)

Log: "{subject}: cached | regenerated | failed"
```

### Passo 3: Executar os 6 benchmarks

Em sequência (NÃO paralelo — cada bench pode ser custoso em tokens):

#### Bench 1: coding-agents-8way

```
output_dir = OS/_bench/coding-agents-8way/
subjects = [claude-code-main, codex, aider, OpenHands, gsd-2, gstack, superpowers, ai-website-cloner-template]
pack = coding-agent

Etapas:
  1. Escrever metadata.json
  2. Copiar inventários para output_dir
  3. Rodar tasks/bench-matrix.md (nway)
  4. Rodar tasks/bench-score.md (nway)
  5. Rodar tasks/bench-executive-report.md (nway)
  6. (SKIP gap-analysis em nway)
  7. (SKIP battle-card em nway)
  8. Validar quality gate

Se Bench 1 já existe (INDEX.md lista) → ASK user: regenerar ou skip
```

#### Bench 2: memory-4way

Idem estrutura, pack=`memory`, 4 subjects.

#### Bench 3: orchestration-5way

Idem, pack=`orchestration`, 5 subjects.

#### Bench 4: spec-driven-3way

Idem, pack=`spec-driven`, 3 subjects.

#### Bench 5: personal-assistant-3way

Idem, pack=`personal-assistant`, 3 subjects.

#### Bench 6: workflow-infra-2way (pair)

Único `pair` — roda full pipeline:

```
output_dir = OS/_bench/workflow-infra-2way/
subjects = [workflow, gh-aw]
pack = workflow-infra

Etapas:
  1. metadata.json
  2. inventories
  3. tasks/bench-matrix.md
  4. tasks/bench-score.md
  5. tasks/bench-gap.md
  6. tasks/bench-battle-card.md
  7. tasks/bench-executive-report.md
  8. Quality gate
```

### Passo 4: Atualizar INDEX.md

Regenerar `OS/_bench/INDEX.md` listando os 6 benchmarks novos + qualquer pré-existente.

### Passo 5: Relatório final

Imprimir ao usuário:

```
run-all report:
  [1/6] coding-agents-8way     — OK   (artifacts: 4, quality_gate: PASS)
  [2/6] memory-4way            — OK   (artifacts: 4, quality_gate: PASS)
  [3/6] orchestration-5way     — FAIL (quality_gate: scorecard score 91 sem signals)
  [4/6] spec-driven-3way       — OK
  [5/6] personal-assistant-3way — OK
  [6/6] workflow-infra-2way    — OK

Total: 5/6 passed. Next: fix orchestration-5way scoring or re-run with --redo 3.
```

## Flags suportadas

- `--skip <N>` — pular o benchmark N do plano (1–6)
- `--redo <N>` — forçar re-execução mesmo se já existe
- `--profile <quick|standard|full>` — default: standard
- `--dry-run` — mostrar plano sem executar

## Veto conditions

- Algum subject essencial falta → HALT
- Qualidade: se 3+ benchmarks falham o quality gate → HALT (problema sistêmico na skill)

## Verificação

- [ ] `OS/_bench/INDEX.md` atualizado
- [ ] Para cada bench concluído, todos os artefatos canônicos do profile estão presentes
- [ ] Todo JSON gerado parseia
- [ ] Relatório final mostra status de cada bench

---

_os-bench / run-all task / v1.0_
