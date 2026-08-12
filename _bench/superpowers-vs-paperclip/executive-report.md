# Executive Report: superpowers vs paperclip

**Date:** 2026-08-12  
**Type:** pair  
**Slug:** superpowers-vs-paperclip  
**Pack:** harness-structure  
**Parent n-way:** harness-structure-8way

---

## Executive Summary

Este pair isola o empate técnico do 8-way (#1 vs #2, Δ 1.86). **superpowers (85.74) vence paperclip (83.88)** no pack de estrutura de harness — não porque é “melhor produto”, e sim porque o pack mede *como um agente executa trabalho complexo de software*. Superpowers é um plugin de processo. Paperclip é uma empresa de agentes.

A leitura útil: **5 dimensões para Superpowers (gates, skill, context, spine, handoff), 3 para Paperclip (squad, plugin, governance)**. O penhasco de governance (−37) não vira o total porque o peso é 6%. O penhasco de gates (+17) pesa 10% e decide.

**Recomendação:** compor. Paperclip emprega. Superpowers é o `requiredSkills` de quem escreve código. Não inverter. Não fundir os cores.

---

## Key Metrics

| | |
|---|---|
| Winner | superpowers (+1.86) |
| Dim wins | 5–3 |
| Features | 21 (Forte 6 · Parcial 11 · Sem_Equiv 4) |
| Gaps | A 4 (3× P3) · B 4 (3× P1) |
| Confidence | HIGH |

---

## Scorecard Summary

| Dim | W | SP | PC | Δ |
|---|---:|---:|---:|---:|
| Skill System | 16% | **92** | 78 | +14 |
| Squad Model | 14% | 78 | **94** | −16 |
| Plugin Ext. | 12% | 82 | **86** | −4 |
| Context | 16% | **86** | 76 | +10 |
| Spine | 16% | **90** | 84 | +6 |
| Gates | 10% | **95** | 78 | +17 |
| Handoff | 10% | **93** | 90 | +3 |
| Governance | 6% | 55 | **92** | −37 |
| **Total** | | **85.74** | 83.88 | **+1.86** |

---

## Dimension Analysis

### Skill System (+14 SP)

SessionStart injeta `using-superpowers` (`OS/superpowers/hooks/session-start`). SDO proíbe workflow no description (`OS/superpowers/skills/writing-skills/SKILL.md`). Paperclip tem catálogo e `requiredSkills` no TEAM.md, mas o heartbeat *nomeia* uma skill — não força a leitura do corpo. Testes: SP mede compliance do agente; PC mede o arquivo do catálogo.

### Squad Model (−16 PC)

Única org de verdade no pair. `TEAM.md` CEO→CTO/QA e a regra “CEO must not IC” (`OS/paperclip/packages/teams-catalog/.../agents/ceo/AGENTS.md`). Superpowers tem papéis de *task* (implementer/reviewer), não empregados.

### Plugin Extensibility (−4 PC)

Paperclip é um runtime de plugin (`OS/paperclip/doc/plugins/PLUGIN_SPEC.md`) + 7 adapters. Superpowers *é* um plugin de host (`.claude-plugin/plugin.json`) e recusa MCP. Quase empate: PC mais profundo, SP mais portátil.

### Context Architecture (+10 SP)

Always-on do Superpowers é um corpo pequeno. Paperclip puxa contexto pelo issue/heartbeat e colapsou SOUL/HEARTBEAT em AGENTS.md (o próprio TEAM.md admite). Nenhum dos dois chega no split OpenClaw.

### Complex-Work Spine (+6 SP)

Superpowers: design assinado → plano júnior-proof → SDD por horas (`OS/superpowers/README.md`). Paperclip: grafo de issues e pipelines (`OS/paperclip/docs/pipelines-tutorial.md`). Ambos persistem artefatos; só um é metodologia de construção.

### Gates & Discipline (+17 SP)

Decide o ranking. TDD iron law + reviewer separado + breaker de 5 rounds. Paperclip tem status `in_review` e um agente QA. Isso governa o *cartão*, não o *diff*.

### Handoff & State (+3 SP)

Quase Forte. Superpowers: scripts `task-brief` / `review-package` depois de um paste de 42k. Paperclip: comment com objetivo/owner/acceptance/blocker. Ambos isolam execução (worktree vs execution workspace).

### Governance (−37 PC)

Decide o *produto*, não o total. Budgets + board vs disciplina de prompt. Peso 6% de propósito: o pack não é “quem opera uma empresa”.

---

## Gap Highlights

**Paperclip P1 (3):** bootstrap, TDD/breaker, file briefs. Tudo cabe como pack, sem mudar o control plane.

**Superpowers P3 (3):** org, money, MCP. Fora de escopo. Absorver isso mata o zero-dep.

---

## Strategic Recommendations

1. **P1 — Paperclip requiredSkills pack** com using-pack + SDO + TDD + SDD. Source: `OS/superpowers/skills/`.
2. **P1 — Heartbeat bootstrap** no CEO/CTO: injetar o corpo, não o nome da skill.
3. **P1 — Issue attachments** carregam brief + review-package (paths, não paste).
4. **P3 — Superpowers permanece processo.** Host adapters, não org-chart.

---

## When to pick which

- **Só Superpowers:** um dev, um host, um PR difícil.
- **Só Paperclip:** frota heterogênea, custo, quem reporta pra quem — e aceitar código sem iron law.
- **Os dois:** Paperclip é a empresa; cada engineer-agent carrega o pack Superpowers.
- **Nenhum dos dois:** spec-kit (SoT é a spec) ou OpenClaw (o produto é o empregado pessoal).

---

## Methodology

Filesystem local, pack `harness-structure`, scores iguais ao 8-way (mesmos signals). Todo score ≥90 tem ≥2 evidence paths. Sem stars. Sem paths de máquina.

## Appendix

```
OS/_bench/superpowers-vs-paperclip/
  metadata.json
  inventory-{superpowers,paperclip}.{json,md}
  comparison-matrix.{json,md}
  scorecard.{json,md}
  gap-analysis.{json,md}
  battle-card.md
  executive-report.md
  deep/absorption-roadmap.md
```
