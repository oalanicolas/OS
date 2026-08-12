# VISA-BRAIN × pacote “cérebro da empresa”

**Date:** 2026-08-12  
**Consumer:** kit `VISA-BRAIN/` (product root = `AGENTS.md` + `00-`…`14-`) + skill `$investigate-case-evidence`  
**Pacote de referência:** `_bench/_research/company-brain.md` + Paperclip + gbrain + Superpowers  
**Método:** paths reais no kit e no monorepo de engenharia. Sem dados de caso. Sem paths de máquina.

O VISA-BRAIN **já é um cérebro operacional**. Não é Paperclip e não é gbrain. Avaliar “junto do pacote” exige mapear **qual job** cada pedaço cobre — não um ranking único.

---

## Veredito em uma página

| Job do pacote | VISA-BRAIN | Nota |
|---|---|---|
| **1. Sistema nervoso** (Paperclip) | **Parcial, de propósito** | Tem DAG, gates, portal, aprovações, Action-Register. Não tem empresa de agentes, CEO, budget em tokens, hire. |
| **2. Córtex institucional** (gbrain) | **Mais rigoroso no domínio; mais estreito no mundo** | Epistemologia A/B/C + grafo≠oráculo + Boundary Card > `gbrain think` para prova. Não é wiki de clientes/deals da firma. |
| **3. Memória do empregado** | **Implementado e limpo** | SOUL / USER / MEMORY com budget e *proibição* de prova na Voice Card. |
| **4. Resíduo do trabalho** | **Melhor que Superpowers em enforcement** | Disco é autoridade; extract-before-reviewed é script; ledger hash-encadeado. |

**Não integre gbrain/mempalace/Paperclip como sidecar em cima de dados de caso.** O próprio kit já diz: *no third-party memory SoT*. Isso está certo — e é mais forte que o contrato ainda-em-plano do Paperclip.

**O que absorver do pacote:** pouca doutrina nova. O que falta é **nervoso de escritório** (se um dia houver N casos + N humanos) e **córtex de firma** (conhecimento *entre* casos, fora do vault). O que não falta é “mais grafo”.

---

## O que o VISA-BRAIN *é* no mapa

Pitch (`VISA-BRAIN/PITCH.md`):

> o portal e a conversa são a interface; o repositório é a memória; a IA é quem opera o sistema.

Isso é **case OS**, não **company OS**.

| Paperclip | gbrain | VISA-BRAIN |
|---|---|---|
| A empresa *agora* (quem, custo, goal) | O *mundo* (pessoa, deal, reunião) | O *caso* (fato, prova, claim, decisão) |
| Agentes = empregados | Agentes = clientes do cérebro | Agente = operador do vault |
| Recusa ser memory engine | Recusa ser org-chart | Recusa ser chatbot *e* recusa sidecar de memória de terceiro |
| Heartbeat thin + pull | Push ≤3 páginas + dream | Catalog → extract → P3 packet → promote |

A unidade de isolamento do VISA é o **workspace de caso** (`PRODUCT.yml`, nunca inferir caso global, nunca varrer irmãos). A do gbrain company-brain é **source + OAuth**. A do Paperclip é **companyId**. Três granularidades. A do VISA é a mais fail-closed — correta para processo de alto risco.

---

## Job 1 — Nervoso: o que já existe vs Paperclip

### Já implementado (análogos)

| Paperclip | VISA-BRAIN | Path |
|---|---|---|
| Company goal | Case theory + critério + totality | `01-Strategy-and-Route/Case-Theory.md` |
| Issue ancestry → goal | Claim → EVD → criterion / STD-* | `Epistemology-Layers.md`, `05-Evidence-and-Sources/` |
| Heartbeat protocol | Boot + skills roteados por modo | `AGENTS.md` § Read first / load by mode |
| Board approval | Portal `Aprovacoes.md` + DEC/OUT | `PORTAL-DO-USUARIO/`, `Human-Data-Interface-Contract.md` |
| Status cards | Painel + dashboard gerado | `build_dashboard_projection.py`; Painel ≠ SoT |
| Activity audit | `AI-Action-Log.md` append-only | `11-Communications-and-Decisions/AI-Action-Log.md` |
| Fail-closed freeze | validator `--strict` + freeze | `ENGINEERING-VISA-BRAIN.md`, B-014 |
| Continuation | `open_thread` + “Continuar de onde paramos” | Companion + Painel |

Token hygiene do boot (AGENTS.md) é **melhor** que o preamble do gstack: SOUL + Voice Card + MEMORY ≤2200 + Painel + DAG-DIGEST gerado. Atlas HTML **nunca** entra no contexto. Isso é o always-on vs on-demand do pack, feito direito.

### De propósito ausente

- Org-chart de agentes (CEO/CTO/QA). O “squad” é **skills** (`$visa-brain`, `$investigate`, `$counsel`, `$review-immigration-evidence`), não empregados persistentes.
- Budget mensal / hire / token salary.
- Heartbeat timer acordando um CEO.

**Não copie Paperclip company-sim para dentro do kit.** Um CEO de visto que “delega critério C para o agente 3” quebra a epistemologia (counsel ≠ collector) e o isolamento de workspace.

### Lacuna real (só se o produto for *escritório*, não *caso*)

Se um dia o VISA-BRAIN operar **N casos × N advogados × custo de runtime**:

- binding company-default / agent-override (Paperclip memory-landscape) **fora** do vault — para briefing interno, não para prova
- goal ancestry explícito *do escritório* (pipeline, SLA) separado do goal do *beneficiário* (`goal_one_line` na Voice Card)

Isso é produto novo. Não é gap do case OS.

---

## Job 2 — Córtex: VISA vs gbrain

Aqui o VISA **já pagou as contas que o gbrain ainda ensina com sangue** (`visa-brain-graph-feature-lessons.md`).

### Onde o VISA está à frente

| Doutrina gbrain / pack | VISA |
|---|---|
| Compiled truth + timeline | Hot-index / dashboard = **projeção** com `source_fingerprint`; extracts + registers = evidência. Rebuild se stale. |
| Takes ≠ facts | Camadas A/B/C + Fact / Claim / Inference / AgencyFinding. Categoria-erro *bloqueada* (`Epistemology-Layers.md`). |
| `think` + gaps | Boundary Card obrigatório: estabelecido / não estabelecido / contradições / reopen. P3 fail-closed sem packet. |
| Edges zero-LLM | Candidatos mecânicos no hot-index; papéis evidenciais **só LLM depois de reabrir** o unit. `candidate_edges` ≠ prova. |
| Graph signals reordenam | **Não existem** — correto. Grafo não é gate de verdade. |
| Dual-SoT | Canônico em `00`–`14`; portal/dashboard/DAG-DIGEST são projeções. Kit de produto ≠ workspace de caso (dois-repos do gbrain, só que para *engine vs dossiê*). |
| Isolamento | Workspace explícito; `SAME_ORIGIN_GROUP`; single_source por *grupo*, não por contagem de arquivo. |
| Dream noturno | P3 síntese + P4 gap pursuit + `$counsel` depois do recibo. Não é cron de wiki — é fase com gate. |

`evidence-graph.md`: *“The evidence graph is a relationship index, not a truth oracle.”* Isso é a frase que o gbrain *deveria* ter no `graph-signals.ts` e não tem.

People-Register (`02-People-and-Organizations/People-Register.md`) já faz o que o gbrain faz com `person` pages, com **âncora obrigatória** (INP/SRC). Sem âncora não escreve. Merge só com humano. Sem camada `minds/`. PII mínimo. Isso é **melhor** que notability heurística para um domínio jurídico.

### Onde o gbrain ainda é outro produto

| gbrain | VISA |
|---|---|
| 100k páginas people/companies/deals da *firma* | Um caso. Multi-case é casca opcional (`optional/multi-case/`). |
| `volunteer_context` push ≤3 | Quase só pull + catálogo. Correto: não empurrar dossiê no prompt. |
| Dream 20 fases no corpus inteiro | Fases P0–P7 de *uma* investigação. |
| Company brain = sources + OAuth | Isolamento = workspace. Mais forte, menos “wiki compartilhada do escritório”. |
| `MEMORY_VERBS` plugáveis | Explicitamente: *No third-party memory SoT.* |

**Não** ponha um brain Postgres em cima de `00`–`14`. O lesson pack já disse: sidecar peer sobre dados de caso é anti-goal.

### Lacunas de enforcement (já no gap map 2026-08-06; conferir BACKLOG)

Ainda valem como *hardening*, não como “faltou gbrain”:

- locator/digest em aresta forte (já exigido em doutrina P3; profundidade variável)
- um reconciler para todos os entrypoints
- lifecycle uniforme em toda leitura de grafo
- temporal supersede (B-028 — backlog deliberado, não pular fila)
- health = fingerprint da projeção, não `edge_count` de store (VISA não tem graph DB)

T1 “candidates>0 ⇒ edges>0” **não** deve ser implementado — recria o #3466. Candidatos precisam de disposição (accepted/rejected/ambiguous).

---

## Job 3 — Memória do empregado: já está no pacote OpenClaw/Hermes

`AGENTS.md` + contrato humano:

| Camada pack | Arquivo VISA | Regra |
|---|---|---|
| SOUL | `Partner-Presence-and-Continuity.md` | Parceiro, sem auto-título |
| USER | Voice Card em `Case-Companion-Profile.md` | Estilo, `goal_one_line`, *nunca* prova |
| MEMORY | `Case-Agent-Notes.md` | ≤ ~2200 chars; lição de workflow, não evidência |

Isso é o split OpenClaw (`SOUL`/`USER`/`MEMORY`) + hardline Hermes (card densa, subtrair). Paperclip *colapsou* SOUL no `AGENTS.md` do CEO — o VISA **não** cometeu esse erro no caso.

PARA (`$AGENT_HOME/life`) do Paperclip **não** deve entrar no vault. People-Register já é o “areas/people” com âncora.

---

## Job 4 + Superpowers — processo de trabalho complexo

`$investigate-case-evidence` v4.6 é o SDD do dossiê:

| Superpowers SDD | VISA investigate |
|---|---|
| Ledger sobrevive compactação | Disco = restart authority; SQLite + deltas hash-encadeados |
| Brief por arquivo | `artifacts/units/<id>.md` ≥180 chars + SHA + âncoras |
| Reviewer separado | P6 `$review-immigration-evidence`; depois `$counsel` em sessão limpa |
| Breaker 5 rounds | apply-batch 3 fails → HALT; P6 max 3; verify 2 |
| Controller não implementa | Canonical writes só via `$visa-brain` |
| “Não continue?” | Autônomo até fato do dono / privacidade / counsel |

Aqui o VISA está **mais mecanizado** que Superpowers: `apply-batch` *rejeita* reviewed sem extract. Superpowers depende do modelo obedecer o skill.

Sequence Lock + Post-Phase Verification Gate no investigate é o mesmo espírito do AIOX full-cycle — já no produto.

---

## Mapa honesto: o que você já absorveu do pacote

| Padrão do pacote | Estado no VISA |
|---|---|
| Always-on minúsculo + digest gerado | Sim (`DAG-DIGEST`, Voice Card) |
| Chat ≠ SoT | Sim (repositório = memória) |
| Projeção ≠ autoridade | Sim (dashboard, hot-index, portal) |
| Takes ≠ facts | Sim (e mais: AgencyFinding separado) |
| Grafo ≠ oráculo | Sim (doutrina + P3 estrutural) |
| Dois repos (engine vs conhecimento) | Sim (kit produto vs workspace `PRODUCT.yml`) |
| Isolamento fail-closed | Sim (mais forte que source OAuth) |
| Heartbeat thin | Sim (boot curto; resto on-demand) |
| Goal ancestry | Parcial (teoria + matriz; não é árvore Paperclip) |
| Company-sim / budgets | Não — e não deve |
| Memory provider pluggable | Recusado de propósito |
| Push volunteer_context | Não — e no caso seria rot |
| Org de empregados de IA | Não — skills, não staff |

---

## O que *não* copiar agora

1. **Paperclip Core Exec Team** dentro do caso. Collector ≠ auditor já está no kit (B-018). Um org-chart de agentes reabre self-review.
2. **gbrain dream** no vault inteiro. P3/P4 já são o ciclo com gate. Dream sem perímetro = extract silencioso em escala.
3. **mempalace verbatim como SoT do caso.** Originais + SHA já existem (`hash_originals.py`, `--strict` EXH). O palácio seria dual-SoT.
4. **MEMORY_VERBS** sobre CLM/EVD. O contrato do caso já é INP→SRC→CLM→EVD. Outro verbo = segunda epistemologia.
5. **T1–T22 à letra.** O adendo Codex de 2026-08-06 ainda vale.

---

## Absorção residual (pequena, alinhada ao BACKLOG)

Só o que fecha o pacote *sem* mudar o job do produto:

| Prioridade | Item | De quem | Para onde |
|---|---|---|---|
| P1 | Goal ancestry explícito no Painel: “esta pendência existe porque STD-X / CR-Y” | Paperclip goal tree | projeção do dashboard, não schema novo |
| P1 | Fingerprint da projeção = health (já doutrina; não inventar `edge_count`) | visa-brain lessons T5 corrigido | validator / P3 |
| P2 | PER compiled-truth curto + timeline de episódios (vocês já têm episode vs pattern) | gbrain compiled-truth | `Template-Person.md` / B-045 — sem segunda página |
| P2 | Se existir *escritório* multi-humano: source compartilhado **fora** do vault (playbook, não prova) | gbrain company-brain | monorepo de engenharia / wiki interna |
| P3 | Temporal supersede em campos mutáveis de CLM | mempalace / B-028 | fila existente |

---

## Conclusão

O VISA-BRAIN **já é o cérebro do negócio no sentido que importa para vocês**: memória operacional de um processo de alto risco, com epistemologia mais dura que o gbrain e isolamento mais duro que o company-brain tutorial.

O pacote Paperclip+gbrain descreve **outra empresa** — a que *emprega agentes* e a que *sabe o mercado*. Colar isso no kit do caso seria o mesmo erro que o Paperclip evitou ao recusar ser vector DB, e que o gbrain evitou ao recusar ser org-chart.

O mega-brain-vip é o contraexemplo: recusou recusar, costurou os quatro jobs + fábrica de clones, e virou **Frankenstein declarado** (`_bench/_research/mega-brain-vip-vs-company-brain.md` § Diagnóstico). **Não é fonte de boas práticas** e não é o próximo órgão a enxertar no VISA. É o que acontece quando a recusa some.

Próximo bench útil, se quiser formalizar: **não** `memory` e **não** `harness-structure`. Um pack `case-ops` (epistemologia, projeção, isolamento de workspace, extract-before-reviewed, counsel-vs-collector). Aí o VISA lidera o campo que os peers de OS/ nem tentam.

---

## Fontes

Kit: `VISA-BRAIN/PITCH.md`, `AGENTS.md`, `00-Case-Control/Epistemology-Layers.md`, `Human-Data-Interface-Contract.md`, `knowledge-model.json`, `Partner-Presence-and-Continuity.md`, `01-Strategy-and-Route/Case-Theory.md`, `02-People-and-Organizations/People-Register.md`, `11-Communications-and-Decisions/AI-Action-Log.md`, `.codex/skills/investigate-case-evidence/{SKILL.md,references/evidence-graph.md}`.

Engenharia (fora do kit): `docs/ENGINEERING-VISA-BRAIN.md`, `dev/visa-brain/BACKLOG.md`.

Pacote: `_bench/_research/company-brain.md`, `_bench/_research/mega-brain-vip-vs-company-brain.md` (fusion / Frankenstein — não absorver o corpo), `_bench/brain-6way/visa-brain-graph-feature-lessons.md`.
