# O cérebro da empresa — o que esses harnesses realmente modelam

**Date:** 2026-08-12 · **Refresh:** 2026-09-05  
**Escopo:** Paperclip (control plane), gbrain (knowledge ops), bordas (PARA, wiki plugin, LifeOS, mempalace, Superpowers, honcho)  
**Método:** leitura de paths reais + triangulação com `brain-6way`, `harness-structure-8way`, `superpowers-vs-paperclip`  
**Não é um bench canônico** — é o mapa do *job* “cérebro de negócio”. Sem score inventado.  
**Delta set/2026:** ver §7. Tese dos quatro jobs **não muda**. O que muda é a pressão para colapsá-los.

---

## Tese

“Cérebro da empresa” não é uma feature. São **quatro jobs** que as pessoas colapsam numa palavra só. Quem mistura os quatro no mesmo store perde SoT, vaza privacidade e acha que o agente “sabe a empresa” quando ele só leu o último issue.

| Job | Metáfora | Quem no OS/ | O que a empresa *sabe* |
|---|---|---|---|
| **1. Sistema nervoso** | control plane | **Paperclip** | Quem faz o quê, por quê (goal), quanto custa, o que está bloqueado |
| **2. Córtex institucional** | knowledge brain | **gbrain** | Pessoas, empresas, deals, reuniões — síntese citada + gaps |
| **3. Memória do empregado** | soul / PARA / MEMORY.md | OpenClaw, LifeOS, skill PARA do Paperclip | Padrões do *humano* ou do *agente*, não da firma |
| **4. Resíduo do trabalho** | working memory | issues, PRDs, `.gsd/`, plans | O que foi feito *neste* cartão — não sintetizado |

Paperclip **recusa** ser o job 2. gbrain **recusa** ser o job 1. Essa recusa é o design.

---

## 1. Paperclip — o nervoso, não o hipocampo

Fonte de produto: `OS/paperclip/doc/GOAL.md`.

> Paperclip is not the company. Paperclip is what makes the companies possible. We are the control plane, the nervous system.

### O que a empresa *é*

Uma company tem: **goal**, empregados (agentes), org-chart, budget em cents, hierarquia de issues que sobe até o goal (`OS/paperclip/docs/start/core-concepts.md`).

Pacote portátil (`agentcompanies/v1`): `COMPANY.md` + `TEAM.md` + `AGENTS.md` + `PROJECT.md` + `TASK.md` + `SKILL.md` (`OS/paperclip/docs/companies/companies-spec.md`). Runtime é mais fino: a row de company no DB não guarda um blob de missão — direção vive em `goals[]` + árvore `goals` + corpo do CEO.

### O que o agente *sabe* ao acordar

Não o cérebro inteiro. Um **heartbeat** é uma janela curta (`OS/paperclip/docs/agents-runtime.md`):

1. Identidade (`/agents/me` — role, chain of command, budget)
2. Por que acordou (assignment, @mention, timer, approval)
3. `heartbeat-context` — issue + ancestrais + **goal/project** + cursor de comments + `continuation_summary`
4. Puxa o resto (plan doc, search, cases)

Default sofisticado: **thin ping + skill Paperclip**, não fat payload. O agente *consulta* a empresa; a empresa não despeja o wiki no prompt.

### Onde mora a “memória” de negócio (hoje)

| Superfície | Path | Papel |
|---|---|---|
| Árvore de goals | `OS/paperclip/packages/db/src/schema/goals.ts` | “por que este task existe” |
| Issues + comments | schema `issues` / `issue_comments` | canal de comunicação = SoT operacional |
| Documentos revisionados | `documents.ts` (`plan`, `continuation_summary`) | plano vivo no cartão |
| Summary slots / status cards | `summary_slots.ts`, skill `summarize-status` | verdade compilada para o board |
| Activity log | audit | proveniência de mutação |
| Budget / spend | `budget_policies.ts`, `cost_events.goalId` | salário em tokens, não P&L |

Não há tipo OKR. Alinhamento = **ancestralidade do issue até o company goal**.

### O que Paperclip recusa ser

`OS/paperclip/doc/memory-landscape.md`:

> The question is not "which memory project wins?" It is "what is the smallest Paperclip contract that can sit above several very different memory systems?"

Core **não** é knowledge base. Wiki/vector-DB são anti-goal do core (`SPEC.md` §11). Contrato futuro: binding company-default / agent-override + proveniência (issue/comment/run) + custo. Provider dono de extract/embed/forget.

Implementado na borda, não no core:

- **PARA** (`OS/paperclip/skills/para-memory-files/SKILL.md`) — `$AGENT_HOME/life/`, **privado do agente**
- **LLM Wiki plugin** — distila issues → `wiki/projects/<slug>/{standup,index,decisions}.md`, opt-in, default off

### Built-ins `briefs` e `learning`

`OS/paperclip/docs/built-in-agents.md` — agentes de sistema company-scoped (não passam por hire approval do board). Primeiro cheiro de “a empresa tem um funcionário cuja função é lembrar/aprender”. Ainda não é gbrain.

---

## 2. gbrain — o córtex (conhecimento do mundo)

Fonte: `OS/gbrain/docs/tutorials/company-brain.md` (receita explícita para 10–50 pessoas, <$100/mês).

### O que uma página *é*

Um arquivo markdown = uma entidade. Duas zonas (`OS/gbrain/docs/guides/compiled-truth.md`):

- **Compiled truth** — síntese reescrita (estado atual em 30 segundos)
- **Timeline** — evidência append-only (a prova)

Epistemologia (`OS/gbrain/docs/takes-vs-facts.md`):

| Camada | Quem fala | Quando |
|---|---|---|
| **Facts** (quente) | o dono do cérebro, na conversa | tempo real |
| **Takes** (frio) | qualquer holder (Alice, o mundo, o brain) | extração + dream |

Nunca despejar take dos outros na tabela de facts do dono. Dream `consolidate` é a ponte de uma mão.

### Dois repos — o teste de fronteira

`OS/gbrain/docs/guides/repo-architecture.md`:

> Isto é sobre como o agente opera, ou sobre o mundo?

- Pessoa / empresa / deal / reunião / ideia → **brain repo**
- SOUL, skill, cron, preferência, heartbeat → **agent repo**

Trocar de agente não mata o conhecimento. Trocar de ferramenta de knowledge não mata o SOUL.

### Como a empresa usa (não é outro binário)

O tutorial de company brain é o cérebro pessoal **com três acréscimos**:

1. **Várias sources** no mesmo DB (wiki compartilhada, caderno de cada um, internal/legal)
2. **OAuth por pessoa** — Alice escreve no source dela, lê o shared; Bob não vê o de Alice
3. **Pastas/crons/skills por pessoa** no agent repo

Privacidade de leitura é **por source**, não por prefixo. Precisa de sigilo → source próprio. Fences de prefixo são de *write*.

Verbos congelados (`OS/gbrain/docs/protocol/MEMORY_VERBS_v1.md`): `recall` · `remember` · `entity` · `synthesize` · `forget`. Memórias default são visíveis a **todo agente ligado naquele brain** (`visibility: private` para fato local).

### Push, não só pull

`volunteer_context` / hooks empurram ≤3 páginas de alta confiança (`OS/gbrain/docs/guides/push-context.md`). De noite, `gbrain dream` fecha buracos, reescreve compiled truth, promove facts, detecta contradição.

`gbrain think` devolve resposta **citada** + **gaps** (stale, sem citação, contradição). Bench `visa-brain-graph-feature-lessons.md`: o array de gaps existe; o loop multi-round ainda não é first-class. Grafo **reordena** top-K — não prova claim.

### Grafo barato (e as armadilhas)

Edges zero-LLM (regex + tipo de página) em todo `put_page` (`OS/gbrain/src/core/link-extraction.ts`). Barato e perigoso: `works_at` por adjacência de pasta, extract silencioso, health mentiroso. Não copiar sem receipt de extract.

### O que gbrain não é

Não é org-chart. Não é budget de empresa (só cap de token do dream). Não é arquivo verbatim (mempalace ganha). Não é sessão. Não é HRIS.

---

## 3. As outras camadas (para não confundir)

| Sistema | Job | Por que não é “cérebro da empresa” |
|---|---|---|
| LifeOS | OS da *vida* (TELOS, Pulse, DA) | Pessoa, não firma (`brain-6way`) |
| mempalace | arquivo fiel offline | Fidelity, não síntese institucional |
| mem0 | SDK multi-tenant | Pluga num produto; não opera a empresa |
| memori | o que o agente *fez* | Execution log |
| Superpowers / gsd-pi | como *construir* | Processo; `.gsd/` é resíduo de um projeto |
| OpenClaw MEMORY.md | continuidade do empregado | Vazaria em contexto compartilhado |
| PARA no Paperclip | caderno do agente | `$AGENT_HOME`, não company DB |

---

## 4. Como um agente “sabe o negócio” de verdade

Pilha que os próprios docs pedem (não um monólito):

```
Board / humano
    │  goal + aprovação de estratégia
    ▼
Paperclip  ──────── sistema nervoso
    │  heartbeat: quem sou, qual issue, qual goal, quanto gastei
    │  issues/comments/plan = working memory
    │
    ├── puxa ──► gbrain think / recall     córtex (mundo: cliente, deal, pessoa)
    ├── puxa ──► requiredSkills (Superpowers / spec-kit)   como construir
    └── NÃO puxa MEMORY.md pessoal em contexto compartilhado
```

Teste de roteamento (gbrain `brain-vs-memory` + Paperclip memory-landscape):

| Informação nova | Onde vai |
|---|---|
| “Alice é VP Eng da Acme, lidera a migração GraphQL” | **gbrain** page `people/alice` + timeline |
| “O CEO aprovou a estratégia Q3” | **Paperclip** goal + comment no issue + activity |
| “Prefiro diffs pequenos” | **agent MEMORY** / USER.md |
| “Checkout do T14 falhou com 409” | **issue comment** (resíduo); não vira dossier |
| Transcrição da call, palavra por palavra | **mempalace** (ou anexo); gbrain só a síntese |

---

## 5. O que vale absorver se você está montando o cérebro da *sua* empresa

### Do Paperclip (nervoso)

1. Goal ancestry em todo task — o agente responde “por que estou fazendo isto?”
2. Heartbeat thin + pull — ninguém acorda com o wiki
3. Contrato de memória *acima* do engine (binding + proveniência + custo)
4. Compiled views para humano (status card, continuation_summary), não para o prompt inteiro
5. PARA / MEMORY no `$AGENT_HOME`, nunca no DB da company

### Do gbrain (córtex)

1. Compiled truth + timeline (síntese ≠ prova)
2. Takes vs facts (crença atribuída ≠ fato do dono)
3. Dois repos (agente substituível, mundo permanente)
4. Company brain = mesmo runtime + sources + OAuth — não um produto novo
5. `think` com citação + gap explícito (“não temos página da Sarah”)
6. Push de poucas páginas, dream de noite
7. Source = fronteira de privacidade

### Não absorver

- Paperclip virar vector DB
- gbrain virar org-chart / folha de pagamento
- Um store só para os quatro jobs
- Grafo como oráculo (visa-brain já pagou essa conta)
- MEMORY.md do CEO no heartbeat do estagiário
- Dual-SoT (wiki plugin + gbrain + PARA sem dizer quem ganha)
- **Costurar os quatro jobs + fábrica de clones num repo só** — o caso concreto é `mega-brain-vip` (diagnóstico: Frankenstein declarado; **não é fonte de boas práticas**; ver `_bench/_research/mega-brain-vip-vs-company-brain.md`)

---

## 6. Relação com os benches que já existem

| Bench | O que mediu | O que *não* mediu |
|---|---|---|
| `harness-structure-8way` | skills / squads / plugins | o que a empresa *sabe* |
| `superpowers-vs-paperclip` | processo × empresa-como-OS | knowledge ops |
| `brain-6way` | memory pack + LifeOS-as-OS | company tenancy, goal ancestry, heartbeat |
| `mempalace-vs-gbrain` | fidelity × synthesis | control plane |
| `_research/visa-brain-vs-company-brain` | case OS × quatro jobs | holding / clones |
| `_research/mega-brain-vip-vs-company-brain` | holding OS + clones; **fusion Frankenstein** (NÃO prática) | case-ops canônico (leitura informal só) |
| `_research/capability-first-vs-os` | contrato/plugin/skill/squad vs clones OS/ | sunset AIOX (piloto ainda aberto) |

O buraco entre “Paperclip 83.88” e “gbrain 78.56 no pack memory” é exatamente este memo: **um é o nervoso, o outro é o córtex**. Nenhum dos dois sozinho é o cérebro da empresa.

O mega-brain-vip é o contraexemplo vivo da linha “um store só para os quatro jobs”: recusou recusar, declarou a fusion (BMAD · Spec-Kit · Claude Code · Foundry · SINKRA · AIOX · JARVIS · KSL) e ficou com cinco control planes e membros `declared_gap` sob pele de produto. Não é o cérebro da empresa. É o corpo inteiro sem um coração único.

---

## 7. Delta setembro 2026 (após o pull)

Tips: gbrain **0.48.2.0**, mempalace **3.9.0**, mem0 **2.0.20**, honcho **3.1.1**. Pack `memory` re-score em `memory-5way` / `brain-6way`. Memo irmão: `_research/second-brain-convergence.md`.

A recusa Paperclip≠gbrain **sobrevive**. O que o pull fez foi aproximar os *bordas* do córtex:

| Job | O que o pull tentou colar em cima | Por que ainda não é o job 2 |
|-----|-----------------------------------|-----------------------------|
| 1 Nervoso (Paperclip) | runner recovery, `agent.task_run`, GPT-6 Astra — control plane, não wiki | Continua recusando vector DB |
| 2 Córtex (gbrain) | LME público 93.19/95.32; volunteer OpenClaw; ambient writeback | Continua recusando verbatim e org-chart |
| 3 Memória do empregado | OpenClaw memory ranking; Clawith soul/memory; claude-mem observer | Continua privado do agente |
| 4 Resíduo | spec-kit workflow slots, superpowers SDD workspace | Continua cartão, não dossier |
| *Novo 2b. Peer identity* | **honcho** scopes + Qdrant + dialectic search-before-answer | Não é página de empresa; é “o que sei sobre Alice” |
| *Novo 1b. Fleet archive* | **mempalace 3.9 hub** | Frota de agentes ≠ OAuth de funcionário |

### O que absorver a mais (além da §5)

8. **Volunteer de poucas páginas, com kill switch** — gbrain `retrieval_reflex_volunteer` / `docs/guides/push-context.md`. Paperclip heartbeat thin continua o modelo; o córtex *oferece*, o nervoso *não despeja*.
9. **Recall ≠ coordenação** — mempalace `mempalace-task` vs skill de recall. Se a empresa copiar um hub, não misturar “quem tem a vez” com “o que foi dito”.
10. **Scopes, não prefixos** — honcho: session ∈ vários scopes; peer unificado. Casa com gbrain “privacidade por source, não por prefixo”.
11. **Dream é higiene, `think` é resposta** — mem0 Dream (merge/prune) não substitui gap analysis. Não promover o skill Dream a córtex.
12. **When-to-touch é um contrato, não uma feature** — mempalace é question-driven (não busca greenfield); gbrain volunteer é reflexivo default-on. Ligar os dois no mesmo turno sem budget. Ver `_research/second-brain-protocols.md` §3.
13. **OpenClaw já é o host** — engines builtin \| Honcho \| LanceDB + wiki ao lado (`OS/openclaw/docs/concepts/memory.md`). Migração Honcho é non-destructive → dual-SoT se o builtin ficar ligado. Gbrain plugin no mesmo assistente precisa de regra de roteamento, senão é mega-brain-vip em miniatura.
14. **Scope ≠ auth** — honcho `scopes.mdx`: unscoped request vê tudo. Não usar scope como ACL de empresa.
15. **Wake ≠ dump** — Paperclip `heartbeat-context` + gbrain `context_pack`/`delta` + OpenClaw `NO_REPLY`. Compactação é wake disfarçado. Ver `_research/wake-protocols.md`.
16. **Host ≠ store** — um slot `memory`, um slot `contextEngine`; plugin quebra → quarantine + `legacy`. Workspace não é sandbox. Ver `_research/host-protocols.md`.

### O que o pack `memory` agora diz (e o que não diz)

gbrain 78.56 → **81.60** porque publicou LME, não porque virou nervoso. mempalace 84.23 → **85.10** porque o hub melhorou schema/vector, não porque virou company brain. A distância caiu (+5.67 → **+3.50**) e **local-first ainda desempata**. Honcho fora do pack de propósito.

`graph-pitfalls-and-lessons.md` **não foi reescrito**: extract silencioso e `works_at` por adjacência continuam as armadilhas; um R@5 público não as apaga.

Stack honesta:

```
Paperclip          = agora (quem, custo, goal)
gbrain             = o que o mundo é (cliente, deal, pessoa)
Superpowers/spec   = como construir
mempalace          = arquivo (compliance / legal)
memori             = o que os agentes fizeram
VISA-BRAIN         = o caso (fato, prova, claim) — fora de OS/
mega-brain-vip     = fusion holding+clones — quarentena de prática; anti-exemplo, não receita
```

---

## Fontes

- `OS/paperclip/doc/GOAL.md`
- `OS/paperclip/docs/start/core-concepts.md`
- `OS/paperclip/docs/agents-runtime.md`
- `OS/paperclip/doc/memory-landscape.md`
- `OS/paperclip/docs/companies/companies-spec.md`
- `OS/paperclip/docs/built-in-agents.md`
- `OS/paperclip/skills/para-memory-files/SKILL.md`
- `OS/gbrain/docs/guides/compiled-truth.md`
- `OS/gbrain/docs/takes-vs-facts.md`
- `OS/gbrain/docs/guides/repo-architecture.md`
- `OS/gbrain/docs/guides/brain-vs-memory.md`
- `OS/gbrain/docs/tutorials/company-brain.md`
- `_bench/_research/visa-brain-vs-company-brain.md`
- `_bench/_research/mega-brain-vip-vs-company-brain.md` (diagnóstico Frankenstein; **não é fonte de prática**; kit externo `mega-brain-vip/`)
- `_bench/_research/capability-first-vs-os.md`
- `OS/gbrain/docs/protocol/MEMORY_VERBS_v1.md`
- `OS/gbrain/docs/guides/push-context.md`
- `OS/_bench/brain-6way/executive-report.md`
- `OS/_bench/brain-6way/visa-brain-graph-feature-lessons.md`

---

_Pesquisa 2026-08-12. Contraexemplo de fusion: `_research/mega-brain-vip-vs-company-brain.md` (Frankenstein declarado; **não usar como boa prática**). Capability-First vs campo: `_research/capability-first-vs-os.md`. Próximo bench possível: `company-brain-Nway` (Paperclip × gbrain × Clawith × LifeOS) — só se o pack for novo (`company-ops`), não `memory` nem `harness-structure`. Não incluir mega-brain-vip nesse n-way sem pack `holding-ops`._
