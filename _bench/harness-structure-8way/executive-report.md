# Executive Report: harness-structure-8way

**Date:** 2026-08-12  
**Type:** nway (8 subjects)  
**Slug:** harness-structure-8way  
**Dimension pack:** harness-structure (new pack: Skill System, Squad Model, Plugin Extensibility, Context Architecture, Complex-Work Spine, Gates & Discipline, Handoff & State, Governance)

---

## Executive Summary

Oito harnesses foram comparados na pergunta que o estudo anterior abriu: **como organizar skills, squads e plugins para um agente ter contexto e estrutura em trabalho complexo**. O pack novo `harness-structure` (pesos = 1.00) mede isso — não coding depth, não recall, não canais.

**superpowers vence o ranking ponderado (85.74)**, +1.86 sobre paperclip (83.88) e +2.58 sobre gsd-pi (83.16). A vitória é de categoria: é o único processo que *força* o uso de skills (SessionStart), *proíbe* workflow no `description` (SDO), e *sobrevive compactação* (ledger + brief por arquivo + breaker de 5 rounds). paperclip é o único company-sim completo (org + budget + 7 adapters). gsd-pi é o generalista — zero wins de dimensão, terceiro no total — e o clone local está **arquivado** (README aponta para `open-gsd/gsd-pi`).

Não existe um vencedor universal. Existe uma **teoria de controle**. Colar as oito no mesmo `CLAUDE.md` é o anti-pattern que o próprio GSD mediu: 66 skills = 60% do orçamento de listing.

**Recomendação high-level:** processo Superpowers + host OpenClaw (ou Claude) + company-sim Paperclip só se houver frota + spec-kit quando a SoT precisa ser a spec, não a skill.

---

## Key Metrics

| Metric | Value |
|---|---|
| Overall winner | **superpowers** (85.74) |
| Runner-up | paperclip (83.88) |
| Generalist | gsd-pi (83.16, 0 dim wins) |
| Floor (honest contrast) | spec-kit (69.52) — commands, not skills |
| Dimensions | 8 |
| Features in matrix | 21 |
| Field gaps | 24 (P0=1, P1=10) |
| Confidence | HIGH |
| Profile | full |

---

## Scorecard Summary

| Dim | W | SP | gstack | gsd-pi | BMAD | paperclip | hermes | openclaw | spec-kit |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Skill System | 16% | **92** | 84 | 88 | 80 | 78 | 91 | 88 | 42 |
| Squad Model | 14% | 78 | 72 | 82 | 90 | **94** | 62 | 58 | 48 |
| Plugin Ext. | 12% | 82 | 80 | 78 | 68 | 86 | 88 | **94** | 84 |
| Context | 16% | 86 | 74 | 84 | 70 | 76 | 90 | **93** | 72 |
| Spine | 16% | 90 | **91** | 90 | 88 | 84 | 78 | 70 | 90 |
| Gates | 10% | **95** | 82 | 80 | 76 | 78 | 80 | 62 | 78 |
| Handoff | 10% | **93** | 84 | 88 | 80 | 90 | 72 | 74 | 82 |
| Governance | 6% | 55 | 62 | 60 | 60 | **92** | 70 | 84 | 68 |
| **Total** | 100% | **85.74** | 79.84 | 83.16 | 78.04 | 83.88 | 80.08 | 78.20 | 69.52 |

---

## Dimension Analysis

### Skill System — superpowers 92 / hermes 91 / spec-kit 42

O átomo compartilhado é `SKILL.md`. O que decide o score é **descoberta + orçamento + bootstrap**.

Superpowers ganha porque o hook `OS/superpowers/hooks/session-start` injeta o corpo de `using-superpowers` e a regra SDO em `OS/superpowers/skills/writing-skills/SKILL.md` impede o agente de seguir o resumo e pular o corpo. Hermes chega a 91 com 194 skills e description ≤ 60 chars (`OS/hermes-agent/skills/software-development/hermes-agent-skill-authoring/SKILL.md`) — o maior catálogo com a barra de review mais dura. spec-kit 42 é o contraste honesto: `OS/spec-kit/templates/commands/specify.md` é comando, não skill. GSD-2 implementa o *runtime* Agent Skills (`OS/gsd-pi/packages/pi-coding-agent/src/core/skills.ts`) e por isso fica em 88 mesmo sem bootstrap de SessionStart.

### Squad Model — paperclip 94 / BMAD 90 / openclaw 58

Só dois sujeitos têm pessoas persistentes. paperclip com `TEAM.md` + CEO que **não faz IC** (`OS/paperclip/packages/teams-catalog/catalog/bundled/company-defaults/core-exec-team/agents/ceo/AGENTS.md`). BMAD com Winston/John e Party Mode em quatro runtimes (`OS/BMAD-METHOD/src/core-skills/bmad-party-mode/SKILL.md`). gstack e Superpowers são especialistas sequenciais / papéis de task — não empregados. openclaw 58: identidade de workspace não é roster.

### Plugin Extensibility — openclaw 94 / hermes 88 / BMAD 68

OpenClaw valida o manifest **antes** de executar código (`OS/openclaw/docs/plugins/architecture.md`) e reserva slots exclusivos de memory/context-engine. spec-kit 84 prova que extensão de verdade não exige SKILL.md (`extension.yml`). Superpowers 82 é um *process plugin* zero-dep — marketplace oficial, sem MCP próprio, de propósito. BMAD 68 customiza persona, não tem runtime de plugin.

### Context Architecture — openclaw 93 / hermes 90 / gstack 74

A regra mais consistente do conjunto: always-on minúsculo. OpenClaw capia 20k/arquivo e 60k total e lista skills, não corpos. Hermes recusa compactar a mensagem do usuário (`OS/hermes-agent/docs/micro-compaction.md`). Superpowers 86 porque o bootstrap é pequeno mas a identidade fica no host. gstack 74: o preamble gerado é o outlier caro (`OS/gstack/SKILL.md`).

### Complex-Work Spine — gstack 91 / SP·gsd-pi·spec-kit 90

Cinco spines completos, nomes diferentes. gstack ganha por um ponto porque o produto *é* a sequência office-hours → autoplan → ship (`OS/gstack/docs/skills.md`). spec-kit empata em 90 sem ter skills — a spec é a SoT (`OS/spec-kit/spec-driven.md`). openclaw 70: TaskFlow não é SDLC.

### Gates & Discipline — superpowers 95 / openclaw 62

Único com TDD iron law + reviewer separado + breaker. O breaker existe porque loops de review não convergem. paperclip tem `in_review` e QA, não TDD. openclaw Workshop gateia *skill nova*, não implementação.

### Handoff & State — superpowers 93 / paperclip 90 / gsd-pi 88

Superpowers documentou a falha: controller sem ledger re-despachou tasks prontas após compactação. Por isso `task-brief` e `review-package` são scripts, não prosa. paperclip coloca o contrato no comment da issue. gsd-pi usa `continue.md` + leases de worktree (`OS/gsd-pi/docs/dev/ADR-001-branchless-worktree-architecture.md`).

### Governance — paperclip 92 / openclaw 84 / superpowers 55

Única dimensão em que Superpowers é o piso entre os líderes. Correto: um plugin de processo não deve ter board. paperclip é o plano de dinheiro. openclaw é o plano de confiança (allowlist, `requires.bins`, ClawHub).

---

## Gap Highlights

P0 único: **P0 do gsd-pi arquivado foi fechado com gsd-pi**. Absorver deste clone sem olhar `open-gsd/gsd-pi` é erro.

P1 que importam para um harness próprio:

1. Bootstrap tamanho Superpowers (gstack/hermes/gsd-pi).
2. Breaker de review (gstack, paperclip, openclaw).
3. Listing budget (BMAD, paperclip).
4. Adapter Agent Skills para spec-kit (senão some no host).
5. Process pack (TDD/SDD) como `requiredSkills` no paperclip — não no core.

---

## Strategic Recommendations

### 1. Monte a pilha em camadas, não em um monólito — P0

Process plugin (Superpowers) + runtime plugin (OpenClaw) + knowledge (gbrain/MemPalace, fora deste bench) + overlay de projeto (spec-kit ou `.gsd/`). Company-sim só com frota.

**Target:** both · **Impact:** evita o estouro de listing que GSD mediu.

### 2. Description é produto — P0

SDO (trigger only) **ou** cap duro (Hermes 60 / GSD 100) + lint no CI. Nunca workflow no frontmatter.

**Source:** `OS/superpowers/skills/writing-skills/SKILL.md`

### 3. Progresso em arquivo — P0

Ledger / STATE.md / issue. Chat é scratch. Handoff é path.

**Source:** `OS/superpowers/skills/subagent-driven-development/SKILL.md`

### 4. Humano só em porta de mão única — P1

Superpowers empacota contradições do plano antes da Task 1. gstack auto-decide duas vias. spec-kit `type:gate`. Não perguntar “continuar?”.

### 5. Trate gsd-pi como snapshot — P1

Clone `open-gsd/gsd-pi` antes de portar o runtime de skills. O score 83.16 é do tree de maio/2026.

---

## When to pick which

**Pick superpowers if** você precisa que o agente *não pule* TDD, review e o plano, em qualquer host.

**Pick paperclip if** você opera vários runtimes (Claude+Codex+Cursor) como uma empresa, com budget.

**Pick gsd-pi / gsd-pi if** o modo é “uma spec, anda embora”.

**Pick gstack if** um founder quer taste (office-hours, CEO review) e um browser persistente.

**Pick BMAD if** o humano quer falar com o arquiteto, e o desacordo é feature (Party Mode).

**Pick openclaw if** o produto é o agente pessoal: canais, plugins, identidade, ClawHub.

**Pick hermes if** o produto é o catálogo + hibernação + o agente escrever skills.

**Pick spec-kit if** a spec precisa ser a fonte da verdade, e skills seriam um atalho perigoso.

**Use both** Superpowers + spec-kit quando o time quer SDD *e* disciplina de implementação. Superpowers + paperclip quando a empresa precisa de empregados que saibam construir.

---

## Methodology

- **Sources:** filesystem de `OS/{subject}/` após `./update.sh` em 2026-08-12. Zero claims sem path.
- **Pack:** `harness-structure` adicionado em `.claude/skills/os-bench/data/dimension-packs.yaml`.
- **Scoring:** banda do pack → número; ≥90 exige 2+ signals; aritmética gerada por script.
- **N-way extras:** gap-analysis de campo, battle-card de paradigma, `deep/` de absorção — marcados em `metadata.json`.
- **Limitations:** gsd-pi arquivado; stars não pontuadas; LifeOS e get-shit-done fora do score (apêndice).

---

## Appendix — artifacts

```
OS/_bench/harness-structure-8way/
  metadata.json
  inventory-{8 subjects}.{json,md}
  comparison-matrix.{json,md}
  scorecard.{json,md}
  gap-analysis.{json,md}
  battle-card.md
  executive-report.md
  deep/feature-comparison.md
  deep/absorption-roadmap.md
```

Inventários canônicos também em `OS/_bench/_inventories/{subject}/`.

### Parked (não pontuados)

| Subject | Por que ficou de fora |
|---|---|
| get-shit-done | README: repositório arquivado; sucessor é GSD Core / gsd-pi |
| LifeOS | Pólo personal-OS (ISA/USER/Pulse), não harness de trabalho de software |
| Clawith / crewAI / autogen / AGT | Já cobertos em orchestration-5way; AGT é overlay de authz |

---

_Gerado por os-bench v1.0.0 · pack harness-structure · profile full._
