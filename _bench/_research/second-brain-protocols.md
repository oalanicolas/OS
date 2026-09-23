# Second-brain protocols — o fio, não o produto

**Date:** 2026-09-05  
**Nível:** abaixo dos jobs de `second-brain-convergence.md` e `company-brain.md`  
**Método:** leitura dos protocolos canônicos nos clones (não CHANGELOG)  
**Não pontua.** Sem pack novo. Sem score.

Os benches de setembro dizem *quem ganhou o pack*. Este memo diz **o que cada um recusa no fio** — o contrato de verbo, isolamento, push e sonho. É aqui que a convergência de produto ainda **não** unificou.

---

## 1. Achar o protocolo

Cada sistema tem um arquivo que *é* a lei. Skills/plugins devem linkar, não recontar.

| Sistema | Arquivo-lei | Promessa congelada |
|---------|-------------|-------------------|
| gbrain | `OS/gbrain/docs/protocol/MEMORY_VERBS_v1.md` | 5 verbos + `context_pack`/`delta`; visibility `world`≠internet |
| gbrain push | `OS/gbrain/docs/guides/push-context.md` | volunteer zero-LLM, cap 3, gate 0.7 |
| gbrain writeback | `OS/gbrain/docs/guides/ambient-writeback.md` | TTL no **read**; quem nunca é perguntado |
| gbrain episteme | `OS/gbrain/docs/takes-vs-facts.md` | takes frios ≠ facts quentes; consolidate é ponte de uma mão |
| mempalace recall | `OS/mempalace/integrations/shared/recall-protocol.md` | **100% recall, verbatim, never guess** |
| mempalace frota | `OS/mempalace/integrations/shared/coordination-protocol.md` | memory ≠ coordination; cursor = `since_event_id` |
| honcho scopes | `OS/honcho/docs/v3/documentation/features/advanced/scopes.mdx` | scope = **projeção**, não partição; **não é auth** |
| OpenClaw | `OS/openclaw/docs/concepts/memory-architecture.md` | 5 princípios; write path = security boundary |
| OpenClaw×Honcho | `OS/openclaw/docs/concepts/memory-honcho.md` | Honcho é **engine plugável**, não o workspace |
| mem0 Dream | `OS/mem0/integrations/mem0-plugin/skills/dream/SKILL.md` | merge / contradict / prune; conflito pede humano |
| LifeOS Cortex | `OS/LifeOS/LifeOS/install/skills/Cortex/SKILL.md` | never write `KNOWLEDGE/` direto; ripple no ingest |

Se um plugin restata o protocolo em vez de linkar, o fio já driftou. Mempalace diz isso na linha 5 de `recall-protocol.md`.

---

## 2. Epistemologia — o que *é* uma memória

Não são o mesmo objeto. Colapsar o nome “memory” é o erro de agosto, agora com prova no fio.

| Sistema | Unidade | SoT | O modelo pode inventar? |
|---------|---------|-----|-------------------------|
| **mempalace** | drawer verbatim | texto original no SQLite/Chroma | **Não.** Quote exact words. Empty → say so (`recall-protocol.md` §Unhappy paths) |
| **gbrain** | page = compiled_truth + timeline | síntese reescrita + prova append-only | `synthesize` devolve answer+gaps; facts `world` default |
| **gbrain facts/takes** | `facts` quente vs `takes` frio | dono vs atribuído a terceiros | **Never dump takes into facts** (`takes-vs-facts.md`) |
| **honcho** | peer representation + conclusions | deriver/dreamer async | named scope tem `deductive`/`inductive`; allowlist só `explicit` |
| **OpenClaw builtin** | files + SQLite index | `MEMORY.md`/`USER.md` curated; `memory/YYYY-MM-DD.md` episodic | Promotion gated; untrusted never defaults to `owner` |
| **mem0** | extracted fact rows | paraphrase + metadata user/run | Dream merge deixa o texto *mais* específico — ainda não é verbatim |
| **LifeOS Cortex** | markdown note tipada + `related:` | arquivo no `KNOWLEDGE/` | Ingest **ripple** atualiza notas ligadas; distill é router, não destino |
| **memori** | SQL entity facts + tool outcomes | o que o agente *fez* | (pack; sem protocolo de verbo neste refresh) |

**Implicação:** “Dream” em mem0 **reescreve** fatos. “Dream” em OpenClaw **promove** episódico → curated core. “Dream” em gbrain **promove hot facts → cold takes** (nunca o inverso). Três verbos, uma palavra.

---

## 3. Quando tocar a memória (o contrato mais diferente)

Este é o eixo que o pack `memory` não mede.

| Contrato | Quem | Reflexo default | Greenfield |
|----------|------|-----------------|------------|
| **Question-driven pull** | mempalace `recall-protocol.md` | Só se a pergunta *pode* estar no palácio. Rename de variável → **não busca**. | Silêncio correto |
| **Search-before-answer** | honcho workspace chat; mempalace *quando* a pergunta é sobre o passado | Busca primeiro, depois fala | Honcho: chat do workspace |
| **Reflexive push** | gbrain volunteer | Default-on no plugin host. Cap 3 páginas, gate 0.7. Ambiguidade → **injeta nada**. | Kill switch `retrieval_reflex_volunteer` |
| **Session-start inject + on-demand episodic** | OpenClaw architecture | Curated core no start (budgeted, provenance-eligible). Episódico **nunca** injetado; só search/escalation. | Falha de memória **não bloqueia o turno** |
| **Skill-gated write** | LifeOS Cortex | Toda escrita passa pelo skill. `cp` em `KNOWLEDGE/` é corrupção silenciosa do grafo. | Distill semanal, não por turno |

Dois defaults opostos, ambos conscientes:

- mempalace: *recall is question-driven, not reflexive* (`recall-protocol.md` L25–27)
- gbrain: *pull needs the agent to know to ask; push is the other direction* (`push-context.md` L3–6)

Quem copiar os dois sem escolher o default gera o pior dos mundos: push barulhento **e** pull que o agente esquece.

Gbrain já admite que stats de volunteer são **aproximados de propósito** (`used` = `last_retrieved_at > volunteered_at`, falso negativo por throttle de 5 min). Não tratar `--stats` como KPI de produto.

---

## 4. Isolamento — cinco unidades, nenhum é `user_id`

| Unidade | Dono | O que isola | O que **não** isola | Armadilha |
|---------|------|-------------|---------------------|-----------|
| **Source** (gbrain) | company brain | leitura por source; write fence por prefixo | `visibility: world` = todo agente *neste* brain | `world` ≠ internet (`ambient-writeback.md`, `MEMORY_VERBS`) |
| **Scope** (honcho) | named set of sessions | recall através do scope | **não é authorization** — unscoped request vê tudo | escolher allowlist (`explicit` only) quando queria named scope (inferência) |
| **Hub identity** (mempalace) | `<machine>-<harness>` | coordenação + palace compartilhado | embedder drift entre client/hub | misturar drawer com logstream; cursor `since_created_at` **pula evento** |
| **Wing/room** (mempalace) | spatial | recall scoped | não é tenant | acordar sem honrar o hook de wing |
| **Provenance class** (OpenClaw) | `owner`/`agent`/`untrusted`/`system` | o que pode ser promovido ao core | cron/heartbeat/sub-agent **não** geram candidato durável | defaultar origem desconhecida para `owner` — o doc **proíbe** |
| **Workspace/plugin** (OpenClaw×Honcho) | `workspaceId: "openclaw"` | isolamento Honcho | arquivos `USER.md` originais **não são apagados** na migração | dual-SoT file + Honcho se os dois ficarem vivos |

Honcho é o único que escreve a frase letal na docs:

> Scopes are a recall boundary, not an authorization boundary.

Gbrain `include_private` é fail-closed no `context_pack`/`delta`. Remote nunca vê `visibility=private`. Isso é o par de honcho “named scope” — profundidade com observador trocado — não o par de “lista de session ids”.

Mempalace coordination: **Resume with `since_event_id`. Never resume with `since_created_at`.** Relógios divergem entre réplicas; cursor de wall-clock **silencia** evento. Classe ☠️ do `graph-pitfalls` (falha silenciosa), agora no logstream.

---

## 5. Verbos — o fio congelado do gbrain vs o menu do palácio

### gbrain MEMORY_VERBS v1

| Verbo | Classe | LLM? | Nota |
|-------|--------|------|------|
| `recall` | read | retrieval | facts[] + `fact_id` opaco para `forget` |
| `remember` | write | — | `visibility` default **world** (todo agente no brain) |
| `entity` | read | **zero LLM**, p99 < 100ms | miss = `found:false`, não erro |
| `synthesize` | read | **EXPENSIVE** | `{answer, sources[], gaps[], cost}` |
| `forget` | write | — | |
| `context_pack` | read | zero LLM | `include_private` fail-closed |
| `delta` | read | zero LLM | cursor `(source_id, client_id, session_id)` |

Trust boundary no próprio spec: OAuth write-scope em `remember`/`forget`; per-source isolation em todo read; remote só `world`.

### mempalace tool menu (recall-protocol)

`mempalace_search` → `mempalace_kg_query` / `_supersede` / `_invalidate` / `_add` / `_timeline` / diary. Temporal é **first-class no menu**, não um afterthought. Unhappy path de índice Chroma corrompido: drawers intactos no SQLite; rebuild do HNSW; **agente não repara in-process**.

### honcho two arms

| Arm | O que troca | Conclusões |
|-----|-------------|------------|
| `scope="therapy"` (named, um nome) | o **observador** — view do scope, deriver já backfillou | `explicit` + `deductive`/`inductive` *dentro* do scope |
| `sessions=[…]` ou `scope=["a","b"]` | o **peer** continua observador; união de sessões | **só `explicit`** — dream não atribui a uma sessão |

Copiar “scopes” sem copiar os dois braços produz inferência vazando entre therapy e billing — o exemplo canônico do próprio doc.

---

## 6. Quatro “dreams” (não são o mesmo loop)

| | Gatilho | Mutação | Humano no loop | Evidência |
|--|---------|---------|----------------|-----------|
| **gbrain consolidate** | overnight + write-path | **hot facts → cold takes** (uma mão). Takes de terceiros **nunca** voltam para facts | dono do cérebro | `OS/gbrain/docs/takes-vs-facts.md` |
| **mem0 Dream skill** | `/mem0:dream` ou `--auto` | merge duplicata, prune stale; **contradiction skip + reminder** | sim, se conflito | `skills/dream/SKILL.md` L119, L210–221 |
| **OpenClaw dreaming** | background pass, fora do reply path | promoção episódico → curated core com provenance | review em `DREAMS.md` | `memory-architecture.md` princípios 2–4 |
| **honcho deriver/dreamer** | async Insights queue | representation + conclusions por peer e por **named scope** | — | README Architecture; scopes.mdx “Two Arms” |
| **LifeOS distill** | semanal | **não muta** `KNOWLEDGE/`; roteia para o SoT dono; digest ≤10 itens | digest é índice | Cortex SKILL.md `distill` |

Regra de absorção: se o target precisa de **higiene de store**, copie mem0 Dream. Se precisa de **promoção com provenance**, copie OpenClaw. Se precisa de **takes≠facts**, copie gbrain. Se precisa de **não criar dual-SoT no digest**, copie LifeOS distill.

---

## 7. OpenClaw é o host de composição (o achado que os benches não tinham)

`OS/openclaw/docs/concepts/memory.md` §Memory engines:

| Engine | Papel |
|--------|--------|
| **Builtin** (default) | SQLite + files; architecture.md |
| **Honcho** | plugin `@honcho-ai/openclaw-honcho`; user/agent models; `honcho_ask` |
| **LanceDB** | embeddings OpenAI-compatible |
| **memory-wiki** (ao lado, não no lugar) | vault compilado; **não substitui** o plugin ativo de recall/dream |

Princípios do architecture.md que nenhum vault do pack `memory` escreve tão seco:

1. **No hidden state** — só o que está em arquivo no workspace  
2. **Writing is the hard part** — cita LongMemEval arXiv:2410.10813: o que foi *escrito* importa mais que o índice  
3. **Write path = security boundary** — não dá para detectar poison depois  
4. Gates determinísticos; LLM só dentro deles  
5. **Failures never block replies**

Migração Honcho: *non-destructive* — files sobem, originais ficam. Isso **cria dual-SoT** se ninguém desligar o builtin. O doc não escolhe o SoT pós-migração. Classe 🔁.

Gbrain no OpenClaw é o outro braço: `openclaw.plugin.json` + volunteer default-on. Três plugins de memória no mesmo assistente (builtin + honcho + gbrain) sem regra de roteamento é o mega-brain-vip em miniatura.

---

## 8. Grafo no write vs grafo no skill

| | Quando liga a aresta | Se o humano furar |
|--|----------------------|-------------------|
| gbrain | **todo `put_page`**, zero LLM, regex+tipo | extract silencioso (já minerado em `graph-pitfalls`) |
| LifeOS Cortex | **todo ingest/add via skill**; `related:` 2–4 obrigatório; ripple nas notas ligadas | `cp` em `KNOWLEDGE/` = *phantom entries retrieval misses* — o skill **nomeia** a classe ☠️ |
| mempalace | **explícito** `kg_add` / `supersede` / `invalidate` | não inventa `works_at` por pasta |
| honcho | deriver no background sobre sessões do scope | allowlist corta inferência de propósito |

LifeOS e gbrain concordam no diagnóstico (write-time graph ou o grafo mente) e discordam no enforcement: gbrain é código no `put`; LifeOS é disciplina de skill (quebrável por `Write` direto — Gotchas admitem exception do Algorithm LEARN).

---

## 9. Falhas que o protocolo já confessou

| Classe | Onde está escrito | Não fazer |
|--------|-------------------|-----------|
| ☠️ cursor de relógio | mempalace coordination `since_created_at` | watcher tem que persistir `since_event_id` |
| ☠️ volunteer KPI | gbrain push `--stats` approximate | não usar como precision de produto |
| ☠️ índice ≠ drawers | mempalace Chroma compaction | rebuild from SQLite; agente não “conserta” |
| 🔒 scope ≠ auth | honcho scopes Warning | unscoped request vê tudo |
| 🔒 world ≠ internet | gbrain MEMORY_VERBS / writeback | não expor `world` facts em canal público |
| 🔒 provenance default | OpenClaw: unknown → `untrusted`/`system`, never `owner` | |
| 🔁 dual-SoT na migração | OpenClaw honcho setup keeps files | escolher um SoT depois |
| 🔁 distill dual-write | LifeOS: distill **não** edita KNOWLEDGE | |
| 📊 expansion LME | gbrain CHANGELOG 0.48.2 `tokenmax` 54.89% | `search.mode balanced` |
| 🧭 two arms | honcho lista de scopes = allowlist, **não** N named scopes | |

`graph-pitfalls-and-lessons.md` (ago) continua a mina de extract/`works_at`. Este memo **não a substitui**; adiciona a camada de *protocolo de sessão* que aquela mina não cobriu (logstream, scopes, volunteer, provenance).

---

## 10. Compose legal vs compose suicida

Legal (os próprios docs pedem):

```
OpenClaw builtin files     → memória do empregado (soul / USER.md)
        + honcho plugin    → peer model cross-session (job 5)
        + gbrain plugin    → córtex do mundo (job 2), volunteer cap 3
        + mempalace hub    → arquivo fiel + coordenação de frota (job 1 + logstream)
Paperclip heartbeat        → nervoso (job 1 company-brain.md)
```

Cada seta precisa de **um SoT por tipo de fato**. Teste:

| Fato novo | Onde o protocolo manda |
|-----------|------------------------|
| “Alice é VP da Acme” | gbrain page / mempalace drawer+KG — **um** dos dois |
| “Prefiro diffs pequenos” | OpenClaw `USER.md` / honcho user model — **não** gbrain |
| “Checkout T14 falhou 409” | issue/comment (Paperclip) ou mempalace diary — **não** curated MEMORY.md |
| “Delegar o patch para mac-codex” | mempalace **logstream event**, não drawer |
| “O que os estressa na terapia” | honcho `scope="therapy"` named, **não** allowlist, **não** gbrain |

Suicida: ligar volunteer gbrain **e** session-start MEMORY.md **e** honcho_ask **e** mempalace_search no mesmo turno sem budget. OpenClaw princípio 5 (fail open no reply) mascara o spam até o contexto explodir.

---

## 11. O que ainda não medimos

- Precision real do volunteer (gbrain admite que `--stats` mente um pouco)
- Named-scope vs allowlist em honcho com o mesmo corpus (o doc descreve; não há receipt in-tree no clone)
- Dual-SoT pós `openclaw honcho setup` em produção
- LifeOS ripple vs gbrain extract no mesmo corpus (write-time graph, dois enforcements)
- Pack `memory` sem dimensão de **when-to-touch** e **isolation-unit**

Candidatos a dimensão se um pack `agent-brain` nascer: `when_to_touch`, `isolation_honesty`, `dream_directionality`, `provenance_gate`, `fail_open_on_reply`. Não criar o pack neste refresh — falta eval comparável.

---

## Relação com os outros artefatos

| Artefato | Papel |
|----------|--------|
| `second-brain-convergence.md` | movimento de produto (push/dream/fleet/plugin) |
| **este** | contratos de fio |
| `company-brain.md` | quatro jobs da empresa + §7 |
| `memory-5way` / `brain-6way` | scores do pack `memory` |
| `graph-pitfalls-and-lessons.md` | extract/over-typing (ago; ainda válido) |
| `visa-brain-graph-feature-lessons.md` | consumer VISA; clean-room |
| `_research/wake-protocols.md` | when-to-wake do **agente** (irmão deste: when-to-touch do store) |
| `_research/host-protocols.md` | slots `memory` ≠ `contextEngine`; quarantine; workspace ≠ sandbox |

---

_os-bench research memo (protocol layer) | 2026-09-05_
