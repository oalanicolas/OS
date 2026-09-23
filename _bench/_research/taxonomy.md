# Taxonomia — o que é job, o que é protocolo, o que é palavra colidida

**Date:** 2026-09-05 · **Deep:** mesma data  
**Para quê:** índice de *tipos*. Sem score. Sem produto novo.  
**Como ler:** §0 eixos → §1 jobs E/M → §2 protocolos → §3 unidade → §4 colisões → §5 testes → §6 cartas → §7 pares falsos → §8 roteamento → §9 checklist → **§11 etimologia** → **§12 comprar / medir**.

Sem taxonomia uniforme o pack pontua a *palavra*. Sem etimologia no corpus você compra o *metáfora*. Os dois juntos: classifica o ID, mede o pack que o ID admite, recusa o vendor que colou o nome.

`host-protocols.md` classifica *encaixe*. Este arquivo classifica *o que a coisa é*.

---

## 0. Ordem de tipos (classificar nesta ordem)

```
1. KIND        produto | protocolo | pack-score | palavra
2. DOMÍNIO     empresa | pessoa | sessão de código | vida
3. JOB         E1–E4  ou  M1–M5  ou  nenhum (host / processo / life OS)
4. UNIDADE     o objeto do SoT (drawer, page, fact, representation, …)
5. PROTOCOLO   when-to-touch, isolamento, dream, wake, host-role
```

Regra: **não pular 3 para discutir 5.** Volunteer não torna mempalace um córtex. Hub não torna mempalace um nervoso. Slot não torna OpenClaw um store.

```
KIND ─────────────────────────────────────────────
  produto ──► DOMÍNIO ──► JOB ──► UNIDADE ──► protocolos
  protocolo ──► família 2a–2e (nunca “é um cérebro”)
  pack-score ──► dimensão do yaml (recall, local-first, …)
  palavra ──► glossário §4 (não usar como tipo)
```

Um **produto** ocupa *um job dominante num domínio* e implementa *vários protocolos*.  
Setembro copiou protocolos entre produtos **sem** mudar o job — isso é convergência, não fusão taxonômica.

---

## 1. Dois mapas de jobs (não são o mesmo)

`company-brain.md` = o que a **firma** sabe.  
`second-brain-convergence.md` = o que o **produto de store** é.  
Uma lista só foi o ruído.

### 1a. Domínio EMPRESA — jobs E

Pergunta: *o que a empresa sabe, e quem é dono da verdade?*

| ID | Job | Pergunta canônica | SoT | Recusa |
|----|-----|-------------------|-----|--------|
| **E1** Nervoso | Quem faz o quê, por quê, quanto custa, o que está bloqueado? | goal + issue + budget + checkout | wiki, MEMORY.md, org como grafo de pessoas |
| **E2** Córtex | O que é verdade *sobre o mundo* da firma (gente, deal, conta)? | página/entidade + citação + gap | org-chart, folha, verbatim como SoT |
| **E3** Empregado | Como *este agente/humano* trabalha e fala? | SOUL / USER / PARA / `$AGENT_HOME` | heartbeat compartilhado, company DB |
| **E4** Resíduo | O que foi feito *neste* cartão? | issue comment, plan, `.gsd/`, continuation | dossier permanente do mundo |

Quem no OS/: E1 Paperclip · E2 gbrain (company brain) · E3 OpenClaw/LifeOS arquivos de empregado · E4 o próprio issue.

E2 no domínio empresa **é o mesmo trabalho** que M2 no domínio memória, quando o corpus é institucional. E2 pessoal (cérebro do Garry) continua M2, domínio *pessoa*.

### 1b. Domínio MEMÓRIA — jobs M

Pergunta: *que objeto o store guarda, e o que ele se recusa a ser?*

| ID | Job | Pergunta canônica | Unidade | Campeão | Recusa |
|----|-----|-------------------|---------|---------|--------|
| **M1** Arquivo fiel | O que foi *dito*, palavra por palavra? | drawer verbatim | mempalace | síntese, `think` |
| **M2** Córtex | O que *importa*, com gaps? | page + grafo | gbrain | verbatim-as-SoT, E1 |
| **M3** SDK | Como *plugo* memória no *meu* app? | fact + user/run ids | mem0 | ser o cérebro operacional |
| **M4** Log de ação | O que o agente *fez*? | observation / tool outcome | memori | knowledge vault |
| **M5** Peer | O que sei *sobre esta pessoa* ao longo de sessões? | representation + conclusions | honcho | página `people/alice` |

Relações E↔M (não identidade):

| | |
|--|--|
| M2 ≅ E2 | mesmo job quando o corpus é o mundo da firma |
| M1 ⊄ E | a firma não tem job “arquivo fiel”; joga transcrição em E4 (anexo) ou polui E2 |
| M5 ≠ E3 | E3 = *eu, o empregado*. M5 = *modelo do outro* (Alice na terapia ≠ SOUL.md do agente) |
| M3 ∉ E | é *integração*, não saber da firma |
| M4 ≈ E4 | primo: E4 é o cartão; M4 é o rastro do agente. Dois SoTs se os dois guardam o 409 do checkout |

### 1c. Não-jobs (não forçar E nem M)

| Kind | Coisa | Job dominante | Se você pontuar no pack `memory` |
|------|-------|---------------|----------------------------------|
| life OS | LifeOS | nenhum M; Cortex é *módulo* M2-like | subestima TELOS/Pulse (brain-6way já diz) |
| host | OpenClaw | E3 nos arquivos; slots 2e | pack errado |
| observer de sessão | claude-mem | nenhum; sessão de código | pack errado |
| processo | spec-kit, Superpowers, gsd | nenhum; *como construir* | `.gsd/` é E4, o produto não é M |
| E1+E3 colado | Clawith | dois jobs no mesmo produto | risco de MEMORY no heartbeat |

---

## 2. Protocolos (famílias — nunca “espécie de cérebro”)

Setembro moveu **estas** famílias. Copiar uma não muda o ID do job.

### 2a. When-to-touch — *quando o store fala*

| ID | Contrato | Default | Lei |
|----|----------|---------|-----|
| T-pull | question-driven | só se a pergunta *pode* estar lá | mempalace recall-protocol |
| T-sba | search-before-answer | busca, depois fala | honcho workspace chat |
| T-push | reflexive push | default-on, cap 3, gate 0.7 | gbrain volunteer |
| T-inject | start inject + episodic on-demand | core no start | OpenClaw architecture |
| T-skill | skill-gated write | zero `Write` cru no arquivo | LifeOS Cortex |

T-push **não** promove M1→M2. Empurra *ponteiro*, não `synthesize`.

### 2b. When-to-wake — *quando o agente acorda*

| ID | Contrato | Silêncio correto |
|----|----------|------------------|
| W-adapter | janela Paperclip | coalesce; skip blocked |
| W-model | turno OpenClaw | `NO_REPLY` |
| W-delta | `gbrain delta` | cursor; zero LLM |
| W-rare | LifeOS hot-layer | < 0.20 = nothing |
| W-hook | mempalace honra wing | greenfield não busca |
| W-compact | compactação como wake | rehydrate / flush / REFRESH_TURNS |

**Heartbeat** ∈ {W-adapter, W-model, lock-refresh, W-delta}. Quatro tipos, uma palavra.

### 2c. Isolamento — *o que não vaza*

Nenhuma unidade é `user_id`. Nenhuma é automaticamente **auth**.

| ID | Unidade | Auth? | Vaza se |
|----|---------|-------|---------|
| I-source | gbrain source | fence de write; read por source | tratar `world` como internet |
| I-named | honcho named scope | **não** | unscoped request |
| I-allow | honcho allowlist | não; só `explicit` | usar como named (perde inferência) |
| I-hub | `<machine>-<harness>` | coordenação | cursor `since_created_at` |
| I-wing | wing/room | espacial | não é tenant |
| I-prov | OpenClaw provenance | promoção | default `owner` |
| I-ws | workspace/plugin id | serviço | dual-SoT file+Honcho |
| I-sbx | sandbox mode/scope | *onde* a tool corre | `non-main` ≠ main |

### 2d. Dream — *que mutação noturna*

| ID | Loop | Mutação |
|----|------|---------|
| D-cons | gbrain consolidate | **hot facts → cold takes**, uma mão (`takes-vs-facts.md`: never dump takes into facts) |
| D-hygiene | mem0 Dream | merge/prune; conflito → humano |
| D-promo | OpenClaw dreaming | episódico → curated + provenance |
| D-deriver | honcho | representation (peer e named scope) |
| D-route | LifeOS distill | **não muta** o arquivo; roteia |

D-hygiene **não** é `think` (M2). D-route **não** é D-cons.

### 2e. Host-role — *quem monta*

| ID | Papel | Recusa |
|----|-------|--------|
| H-plane | Paperclip control plane | não assemble, não sandboxa |
| H-gw | OpenClaw Gateway | não é o store; Gateway fora do sandbox |
| H-eng | context engine (slot) | não é memory plugin |
| H-mem | memory plugin (slot) | não decide o prompt sozinho |
| H-adp | adapter | não é o control plane |

Um `H-mem`, um `H-eng`. Isso é cardinalidade de encaixe, não job.

---

## 3. Unidade epistêmica (o SoT tem que ser nomeável)

Se não nomeia o objeto, não sabe o job.

| Unidade | Job | Literal? | Reescrita |
|---------|-----|----------|-----------|
| drawer | M1 | sim | ninguém no hot path |
| page (compiled_truth + timeline) | M2/E2 | prova no timeline | think / D-cons |
| fact row | M3 / facts gbrain | extraído | D-hygiene |
| take | gbrain takes | atribuído | **não** → facts direto |
| peer representation | M5 | inferido | D-deriver |
| conclusion explicit/deductive/inductive | M5 | arm | named vs allowlist |
| SOUL.md / USER.md / MEMORY.md | E3 | arquivo | D-promo gated |
| `memory/YYYY-MM-DD.md` | E3 episódico | arquivo | nunca no start |
| note + `related:` | Cortex (módulo LifeOS) | md tipado | só via skill |
| issue + comment + continuation | E4 | cartão | checkout |
| observation / tool outcome | M4 | ação | writer |

Teste da unidade: *apague o store e o que some?*  
Some o texto original → M1. Some a resposta com gaps → M2. Some o perfil da Alice-como-usuária → M5. Some o goal Q3 → E1. Some o 409 do T14 → E4.

---

## 4. Glossário de colisões

Usar o **ID**, não a palavra.

| Palavra | Significados vistos | ID |
|---------|---------------------|-----|
| memory | M1–M5, E3, episódico, hot-layer, H-mem | job ou unidade |
| brain / second brain | M2, LifeOS, “qualquer store” | M2 ou life OS |
| heartbeat | W-adapter, W-model, lock, W-delta | o W-* certo |
| dream | D-* | o D-* certo |
| world | todo agente *neste* brain ≠ internet | `visibility=brain-agents` |
| scope | I-named, I-allow, I-sbx, I-source | o I-* certo |
| sandbox | I-sbx ≠ workspace | sandbox-mode; cwd |
| host | H-* | o H-* certo |
| wake | W-* | o W-* certo |
| volunteer / push | T-push = ponteiro, não think | T-push |
| recall | verbo gbrain / protocolo M1 / chat M5 | citar o contrato |
| compact | W-compact host / rehydrate / REFRESH | o W-compact certo |
| plugin | H-mem/H-eng, MCP, adapter, skill | slot / MCP / adapter / skill |
| company brain | E2 com I-source + OAuth | E2 institucional, não E1 |

---

## 5. Testes (o que a v1 tinha fraco)

O teste único da v1 (“ligar A e B sem dual-SoT”) é necessário e **não suficiente**. Cinco testes; falhar um já classifica.

### 5.1 Dual-SoT (mesmo job)

Se A e B respondem a **mesma pergunta canônica** (§1) sobre o **mesmo objeto**, ligar os dois corrompe. → mesmo job.

“Alice é VP da Acme” em gbrain **e** mempalace como SoT de síntese = dois M2, ou M1 forçado a M2.

### 5.2 Pergunta canônica (job)

Escreva a pergunta. Só um ID a responde sem resto.

| Pergunta | ID |
|----------|-----|
| O que a Alice *disse* na call, palavra por palavra? | M1 |
| O que eu preciso saber antes da call com a Alice? | M2 |
| Como plugo isso no meu SaaS com `user_id`? | M3 |
| Qual tool falhou no turno 12? | M4 |
| O que estressa *esta* usuária na terapia? | M5 |
| Quem é o assignee e qual o goal? | E1 |
| Prefiro diffs pequenos. | E3 |
| O checkout do T14 deu 409. | E4 |

Se a mesma pergunta cabe em dois IDs, a unidade epistêmica ainda não foi escolhida.

### 5.3 Reescrita (M1 vs o resto)

O hot path **pode** parafrasear o objeto?  
Não → M1. Sim → não é M1.  
gbrain compiled_truth = sim. mem0 fact = sim. Honcho representation = sim. drawer = não.

### 5.4 Filho / contexto compartilhado (E3)

O sub-agente ou o grupo **herda** isso no wake?  
Se sim e é preferência/voz → você vazou E3. OpenClaw: MEMORY.md só main privada; sub-agent só AGENTS.md. Paperclip: PARA em `$AGENT_HOME`.

### 5.5 Pack-score (não é taxonomia)

O pack `memory` mede dimensões de **store M** (recall, local-first, grafo, …).  
Não mede E1, T-push, W-model, H-eng.  
LifeOS **fora** do ranking admitido (life-OS). Um score diagnóstico 70.58 **não** é 5º second brain nem 5º store.

### 5.6 Promoção falsa (protocolo fingindo job)

O produto ganhou um protocolo de *outro* job e a marketing colou o nome.

| Ganhou | Não virou | Porque |
|--------|-----------|--------|
| mempalace hub (I-hub) | E1 | frota de agentes ≠ org-chart/budget/checkout |
| mempalace-task | E1 | coordenação de patch ≠ nervoso da firma |
| gbrain volunteer (T-push) | host | ponteiro no prompt ≠ assemble/compact |
| mem0 Dream (D-hygiene) | M2 | merge/prune ≠ gap analysis |
| honcho scopes (I-named) | auth / E1 | recall boundary; unscoped vê tudo |
| OpenClaw memory-wiki | M2 | *ao lado* do slot; não substitui H-mem |
| gbrain company tutorial | E1 | sources+OAuth = E2 institucional, ainda recusa org-chart |

---

## 6. Cartas de classificação (recorte OS/)

Cada carta: domínio, job dominante, unidade, recusas, protocolos que *não* mudam o job.

### mempalace — M1, domínio pessoa (hub = protocolo)

- Unidade: drawer verbatim  
- Recusa: `think`, parafrasear, busca greenfield  
- Protocolos: T-pull, W-hook, I-hub, I-wing; **não** E1  
- Pack `memory`: 1º porque o pack premia M1 (fidelity + local-first)

### gbrain — M2 ≅ E2, domínio pessoa *ou* empresa

- Unidade: page + takes/facts  
- Recusa: E1, M1-as-SoT, `synthesize` no path ambiente  
- Protocolos: T-push, W-delta, I-source, D-cons, H-eng (checkpoint no `assemble`)  
- Company brain = M2 com I-source; **ainda** M2

### mem0 — M3, domínio produto (SaaS)

- Unidade: fact extraído  
- Recusa: ser o córtex operacional  
- Protocolos: D-hygiene, plugins de harness (não H-mem do OpenClaw a menos que ocupe o slot)  
- Dream ≠ M2

### memori-labs — M4

- Unidade: observation / outcome  
- Recusa: vault de conhecimento  
- Primo de E4, SoT diferente (rastro vs cartão)

### honcho — M5, domínio pessoa-como-usuário

- Unidade: representation + conclusions  
- Recusa: ser `people/alice` (M2); ser SOUL (E3)  
- Protocolos: T-sba, I-named ≠ I-allow, D-deriver  
- “O que estressa na terapia” = M5 + I-named, **não** M2

### Paperclip — E1, domínio empresa

- Unidade: agent record + issue + heartbeat-context  
- Recusa: E2 (memory-landscape: contrato *acima* do engine)  
- Protocolos: W-adapter, H-plane, H-adp  
- PARA skill = E3 na borda, `$AGENT_HOME`

### OpenClaw — host (H-gw) + E3 nos arquivos

- Unidade E3: SOUL / USER / MEMORY / daily  
- Recusa: ser M1–M5 (slots *encaixam* um M)  
- Protocolos: T-inject, W-model, D-promo, I-prov, I-sbx, H-eng, H-mem  
- Falha como store; passa como host

### LifeOS — life OS (domínio vida)

- Módulo Cortex ≈ M2-like (note + `related:`) **dentro** de um não-job  
- Recusa: pack `memory` como veredicto de produto  
- Protocolos: T-skill, W-rare, D-route  
- TELOS/Pulse não têm ID E/M — eixos de *vida*, não de store

### claude-mem — observer (domínio sessão de código)

- Nenhum E/M. Sessão ≠ vault ≠ peer.

### gsd-2 / spec-kit / Superpowers — processo

- `.gsd/` e plans = E4. O produto é *como construir*, não M.

### Clawith — E1+E3 colados

- Dois jobs num produto. Risco taxonômico: MEMORY no heartbeat. Não é M2.

---

## 7. Pares falsos (os que mais erram)

| Parece | É | Teste que separa |
|--------|---|------------------|
| M2 e M1 | síntese vs verbatim | 5.3 reescrita |
| M5 e E3 | modelo do outro vs voz do empregado | 5.2 “estressa na terapia” vs “prefiro diffs” |
| M5 e M2 | perfil de sessão vs página institucional | unidade: representation vs `people/alice` |
| M4 e E4 | rastro do agente vs cartão da firma | 409: comment no issue (E4) ou observation (M4) — um SoT |
| E1 e M2 | nervoso vs córtex | “quem é o assignee” vs “quem é a Alice na Acme” |
| E1 e I-hub | org vs frota de CLIs | budget/goal vs `mac-codex` |
| T-push e M2 | ponteiro vs resposta | volunteer cap 3 ≠ `think` |
| D-hygiene e M2 | merge vs gaps | mem0 Dream vs gbrain synthesize |
| H-mem e M2 | slot vs job | Honcho no slot continua M5 |
| life OS e M2 | hill vs arquivo | LifeOS 70.6 no pack ≠ 5º cérebro |
| W-adapter e W-model | CLI sobe/desce vs turno `NO_REPLY` | Paperclip vs OpenClaw “heartbeat” |
| I-named e auth | projeção vs ACL | unscoped vê tudo |
| workspace e I-sbx | cwd vs onde a tool corre | paths absolutos |

---

## 8. Roteamento (informação nova → ID)

Estende `company-brain.md` §4 com os IDs.

| Informação nova | ID | Não |
|-----------------|----|-----|
| “Alice é VP Eng da Acme” | M2/E2 page | E1, E3, M5 |
| Transcrição da call, palavra por palavra | M1 drawer | M2 (só a síntese) |
| “O CEO aprovou a estratégia Q3” | E1 goal + comment | M2 |
| “Prefiro diffs pequenos” | E3 USER.md | M2, heartbeat de grupo |
| “Checkout T14 falhou 409” | E4 comment | M2 dossier |
| “O que os estressa na terapia” | M5 + I-named | allowlist; M2 |
| “Delega o patch para mac-codex” | I-hub logstream (protocolo de M1) | drawer; E1 |
| “Lembrar o grep que quebrou no turno” | M4 | E4 se o SoT da firma é o issue — escolher um |
| “O agente deve ser breve e ter opinião” | E3 SOUL.md | MEMORY.md, M2 |
| “Quem é o assignee e o budget” | E1 `/agents/me` | M2 |

Dois destinos na mesma linha = você ainda não escolheu o SoT.

---

## 9. Checklist (v2)

1. **Kind?** produto / protocolo / pack-score / palavra.  
2. **Domínio?** empresa / pessoa / sessão / vida. “Todos” → host ou Frankenstein.  
3. **Pergunta canônica (§5.2)?** um ID.  
4. **Unidade (§3)?** nomeie o objeto.  
5. **Reescrita (§5.3)?** se o hot path parafraseia, não é M1.  
6. **Filho herda (§5.4)?** se sim e é E3, vazou.  
7. **Protocolos?** T/W/I/D/H — listar *depois* do job.  
8. **Promoção falsa (§5.6)?** hub, Dream, volunteer, wiki, scopes.  
9. **Pack-score?** só se o kind for store M e você aceita o que o yaml mede.

---

## 10. O que ainda é buraco taxonômico

- **Domínio vida** não tem jobs próprios (TELOS, Pulse, Algorithm). LifeOS vive num eixo que este mapa só marca como “não-M”.  
- **M3** é kind *integração* mais que job de saber — talvez saia da lista M num v3.  
- **Clawith** como E1+E3: falta teste de “quando o colado é um produto vs Frankenstein” além do mega-brain-vip.  
- Pack `agent-brain` / `wake` / `host` **não existem**; criar dimensão ≠ criar job.

---

## 11. Etimologia no corpus (de onde veio a palavra, o que o pack mede se você ficar com ela)

Cada entrada: **raiz** → **prior art** (CS / PKM / ops) → **sequestro no OS/** → **medida errada**.

Não é filologia de dicionário. É a linhagem que faz o ID colidir.

### memory

- **Raiz:** lat. *memoria* / *memor* “que se lembra”. Psicologia: encoding → storage → retrieval.
- **Prior art:** CS = RAM vs disco (volátil ≠ durável). IR = *recall@k* (fração do relevante recuperado). PKM = Memex (Bush 1945) → “second brain” (Forte). LLM-product = “memory layer” (mem0).
- **OS/:** M1–M5, E3, episódico OpenClaw, hot-layer LifeOS, **slot** `plugins.slots.memory`.
- **Medida errada:** pack `memory.recall_accuracy` é **IR recall@k**, não “o agente se lembra de mim”. Honcho M5 e LifeOS DA perdem esse pack sem serem stores piores. OpenClaw no pack memory mede o *slot*, não o host.

### brain / second brain

- **Raiz:** órgão do pensamento. Metáfora: o que pensa *por você*.
- **Prior art:** PKM “Building a Second Brain” = arquivo pessoal externo (mais M1 que M2). Neuro: hipocampo (episódico) vs córtex (esquema) — mapa frouxo M1 vs M2.
- **OS/:** gbrain = “brain *layer*” do **agente** (M2). LifeOS = life OS, não cérebro. Marketing cola “second brain” em qualquer store.
- **Medida errada:** ranking único “melhor second brain” mistura M1, M2, life OS e host. Comprar “cérebro” sem ID = comprar a metáfora.

### recall

- **Raiz:** *re- + call*, chamar de volta. Psicologia: retrieval (≠ recognition).
- **Prior art:** IR `R@k`. Legal: citar o original.
- **OS/:** mempalace = retrieval **+** citação verbatim (“never guess”). gbrain `recall()` = verbo de read, distinto de `synthesize()`. Honcho = chat scoped.
- **Medida errada:** somar LME **retrieval** R@k (M1/M2) com LME **QA** (M3) como se fosse a mesma *recall*. O scorecard já avisou; a palavra empurra o erro.

### heartbeat

- **Raiz:** batimento = prova de vida.
- **Prior art:** clusters/SRE: sinal periódico “ainda estou vivo” (liveness probe). Não é um turno de trabalho.
- **OS/:** Paperclip = **janela de adapter** (W-adapter) — o nome veio do probe e virou o *shift* do empregado. OpenClaw = **turno do modelo** que deve dizer `NO_REPLY` (anti-liveness: calar). gbrain = refresh de **lock** (o único próximo da prior art) *e* `delta` de corpus (W-delta).
- **Medida errada:** copiar `intervalSec` do Paperclip para `heartbeat.every` do OpenClaw. Comprar “heartbeat de 5 min” sem W-*.

### dream

- **Raiz:** visão no sono. Neuro: consolidação no sono (replay).
- **Prior art:** “sleep on it” = processar off-path. Não é higiene de dedupe.
- **OS/:** D-cons (hot facts → cold takes), D-hygiene (mem0 merge/prune), D-promo (OpenClaw episódico→core), D-deriver (honcho), D-route (LifeOS distill **sem** mutar).
- **Medida errada:** “tem Dream?” como feature binária. mem0 Dream ≠ gbrain `think`. Pack memory não tem dimensão D-*.

### scope

- **Raiz:** gr. *skopos* “alvo, vigia”. It. *scopo*.
- **Prior art:** lexical scope (quais nomes são visíveis). K8s/docker: quantos objetos compartilham o isolamento.
- **OS/:** I-named (projeção de recall, **não** auth), I-allow (união de sessões, só `explicit`), I-sbx (`agent|session|shared` = quantos *containers*), I-source (gbrain).
- **Medida errada:** “multi-tenant porque tem scopes.” Unscoped honcho vê tudo. Sandbox `scope: shared` não é named-scope.

### sandbox

- **Raiz:** caixa de areia — brincar contido.
- **Prior art:** Java/browser sandbox = execução isolada. “Not a perfect security boundary” é o disclaimer clássico.
- **OS/:** I-sbx = *onde a tool corre*. Workspace = cwd. Elevated = escape. Creator-role required = fail-closed.
- **Medida errada:** “é local-first / é seguro” porque tem sandbox. Sandbox default **off**. `non-main` isola o grupo, não a DM.

### world

- **Raiz:** o mundo = público / internet.
- **Prior art:** ACL `public`.
- **OS/:** gbrain `visibility: world` = todo agente **neste brain**, não a internet (`MEMORY_VERBS`, ambient-writeback).
- **Medida errada:** tratar world-facts como publicáveis. Bug de linguagem, não de feature.

### volunteer / push

- **Raiz:** lat. *voluntarius* — de livre vontade. Quem se oferece.
- **Prior art:** nenhum em IR (retrieval é pull).
- **OS/:** T-push = o *store* toma agência e oferece ponteiros. mempalace recusa (question-driven).
- **Medida errada:** “proativo” como qualidade única. Proativo-errado é pior que pull-calado. `--stats` do gbrain é aproximado de propósito.

### host

- **Raiz:** lat. *hospes* — hóspede **e** anfitrião (mesma raiz de *hostile*).
- **Prior art:** host vs guest VM; process host.
- **OS/:** H-plane (Paperclip) vs H-gw (OpenClaw) vs H-eng vs H-adp. O anfitrião de plugins não é o anfitrião de empregados.
- **Medida errada:** pack personal-assistant vs orchestration no mesmo ranking “de host”.

### plugin / skill

- **Raiz:** *plug in* elétrico. Skill = habilidade.
- **Prior art:** extensões 1970s+; Agent Skills vs Agent Plugins 1.0 (memos de 12 ago).
- **OS/:** H-mem/H-eng (slot exclusivo), MCP tool, Paperclip adapter, skill markdown, marketplace.
- **Medida errada:** “quantos plugins” como extensibility. Slot exclusivo conta **1**. Skills no pack harness-structure, não no pack memory.

### compact

- **Raiz:** lat. *compactus* — apertado junto. ≠ compress (sem perda).
- **Prior art:** GC compaction; LLM context compaction = sumarizar para caber.
- **OS/:** W-compact: flush+summary (OpenClaw), bank+rehydrate (gbrain), REFRESH_TURNS (LifeOS).
- **Medida errada:** “tem compaction” sem perguntar se o verbatim reaparece. Compact sem rehydrate apaga M1.

### wake

- **Raiz:** despertar. CS: wakeup de processo.
- **Prior art:** scheduler wake.
- **OS/:** W-* (§2b). Compact é wake disfarçado.
- **Medida errada:** autonomia do pack `coding-agent` (“30 min sem HITL”) ≠ W-model `NO_REPLY`.

---

## 12. Comprar e medir (o contrato)

### 12.1 Você compra um **ID de job**, não uma palavra

| Quero | Compro | Pack que pode pontuar | Pack que mente |
|-------|--------|----------------------|----------------|
| Texto original, offline | **M1** mempalace | `memory` (persistence, local-first, recall retrieval) | `personal-assistant` |
| Síntese + gaps institucional | **M2/E2** gbrain | `memory` (graph, write) *e* pergunta canônica M2 | `memory` sozinho como “melhor cérebro” |
| Plugar no meu SaaS | **M3** mem0 | `memory` (vector zoo) | “second brain” no README |
| Rastro do que o agente fez | **M4** memori | nenhum pack E; não `memory` como vault | LoCoMo como se fosse M1 |
| Modelo da pessoa ao longo de sessões | **M5** honcho | nenhum pack atual (M5 ≠ IR R@k) | `memory.recall_accuracy` |
| Quem faz o quê / goal / budget | **E1** Paperclip | `orchestration` / `harness-structure` | `memory` |
| Voz e preferência do empregado | **E3** SOUL/USER | nenhum; não injetar em grupo | pack memory |
| Life OS (TELOS, Pulse) | LifeOS (não-M) | nenhum M; product matrix brain-6way | score 70.6 como veredicto |
| Runtime que encaixa os outros | OpenClaw **H-gw** | `personal-assistant` (canais) | `memory` no host |
| Observer de coding session | claude-mem | nenhum | `memory` |

### 12.2 Regra de admissão no pack (uniforme)

Um subject entra no pack **P** só se:

1. O **kind** é o que P declara (`dimension-packs.yaml`).  
2. O **job dominante** é um ID que P sabe medir.  
3. A **unidade epistêmica** produz o *signal* do yaml (R@k, p50, …).

| Pack | Kind admitido | Jobs | Signal que o yaml pede |
|------|---------------|------|------------------------|
| `memory` | store | **M1–M5** (M5 com asterisco: R@k não é representation) | R@k, verbatim vs paraphrase, HNSW, edges |
| `personal-assistant` | host + canais | OpenClaw, Hermes — **não** M2 | channels, cost, privacy |
| `orchestration` | control plane | **E1** (Paperclip, crew, autogen) | topology, delegation |
| `harness-structure` | processo / skills | Superpowers, spec-kit, BMAD, gstack | skill, spine, gates |
| `spec-driven` | processo | spec-kit, gsd, Superpowers | spec format, TDD |
| `case-ops` | epistemologia de caso | VISA-BRAIN vs peers | graph honesty, extract-before-reviewed |
| `workflow-infra` | execução durável | workflow, gh-aw | event log, retry |
| `coding-agent` | agente que edita código | Codex, OpenHands, … | SWE-bench, git, TDD |

**Exclusões obrigatórias do pack `memory`:** LifeOS-as-OS, OpenClaw-as-host, Paperclip-as-E1, claude-mem, gsd-2-as-process. Ranking admitido = M1–M4. M5 sem `recall_accuracy` IR.

M5 no pack `memory`: só dimensões que a unidade produz (schema, maybe graph). **Não** `recall_accuracy` IR contra LME retrieval de M1. Se o yaml não tem signal para representation, o score é `null` + confidence LOW — `bench-score.md` já manda isso. Pontuar 80 “porque parece memória” é medida errada.

### 12.3 Antes de pontuar, a pergunta etimológica

1. Qual palavra o vendor usa?  
2. Qual ID §4 ela mapeia *neste* repo (não no marketing)?  
3. O signal do pack é dessa linhagem? (IR recall ≠ psych recall ≠ `recall()` API)  
4. Se não: `null` ou outro pack. Nunca “ajusta a nota na mão”.

### 12.4 Comprar um compose

Compose legal = **jobs diferentes** + protocolos declarados + um SoT por pergunta canônica (§8).  
Compose suicida = dois produtos no **mesmo ID** (dual-SoT) ou a mesma *palavra* cobrindo W-adapter e W-model.

Você não “compra um second brain”. Compra M1 **e/ou** M2 **e/ou** M5 **e** um H-gw, cada um medido no pack que admite o ID.

---

## 13. Namespace de IDs

Job IDs `M1`–`M5` / `E1`–`E4` **não** são âncoras Markdown. O arquivo `_research/second-brain-convergence.md` (revisão VISA/MKT) usa `[M1]`/`[M2]` como citações de paths em `MKT-LENDARIO`. São namespaces diferentes. Neste cluster: `job:M1`, nunca `[M1]` como link.

---

## Relação

| Artefato | Tipo |
|----------|------|
| **este** | taxonomia + etimologia + contrato de medida |
| `company-brain.md` | jobs **E** + roteamento da firma |
| `second-brain-convergence.md` | jobs **M** + movimento de protocolo |
| `second-brain-protocols.md` | T, I, D |
| `wake-protocols.md` | W |
| `host-protocols.md` | H |
| `memory-5way` / `brain-6way` | pack-score sobre **M** (LifeOS no 6-way = exceção documentada, não norma) |
| `data/dimension-packs.yaml` | o que cada pack *pode* medir — filtrar por §12.2 |

---

_os-bench research memo (taxonomy v2) | 2026-09-05_
