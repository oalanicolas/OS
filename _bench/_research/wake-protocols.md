# Wake protocols — o que entra no turno

**Date:** 2026-09-05  
**Nível:** irmão de `second-brain-protocols.md` (when-to-touch da *memória*)  
**Pergunta:** o agente acorda com o wiki, com 3 páginas, com o goal do issue, ou com o soul?  
**Método:** arquivos-lei nos clones. Sem score. Sem pack novo.

`second-brain-protocols.md` §3 parou em *quando tocar o store*. Este memo cobre o **turno inteiro**: quem dispara o wake, o que é injetado, o que é recusado, o que acontece depois de compactar.

---

## 1. Arquivos-lei

| Sistema | Lei | Promessa congelada |
|---------|-----|-------------------|
| Paperclip runtime | `OS/paperclip/docs/agents-runtime.md` | Agentes **não rodam contínuos**. Heartbeat = janela curta. |
| Paperclip skill | `OS/paperclip/skills/paperclip/SKILL.md` §Heartbeat Procedure | Identity → inbox-lite → checkout **obrigatório** → `heartbeat-context` compacto |
| Paperclip tese | `OS/paperclip/doc/GOAL.md` | Control plane **não executa** o agente. Orchestrates. |
| Paperclip memória | `OS/paperclip/doc/memory-landscape.md` | Menor contrato *acima* de vários engines; não virar um |
| OpenClaw heartbeat | `OS/openclaw/docs/gateway/heartbeat.md` | Turno periódico na **main session**; `NO_REPLY` se nada; **não** inferir tarefas velhas |
| OpenClaw workspace | `OS/openclaw/docs/concepts/agent-workspace.md` | `SOUL.md` toda sessão; `MEMORY.md` só sessão **main privada** |
| OpenClaw system prompt | `OS/openclaw/docs/concepts/system-prompt.md` | Bootstrap caps 20k/60k; sub-agent só `AGENTS.md` |
| OpenClaw context engine | `OS/openclaw/docs/concepts/context-engine.md` | Ingest → Assemble → Compact → After turn |
| OpenClaw compaction | `OS/openclaw/docs/concepts/compaction.md` | Flush de memória **antes**; falha **não** descarta o turno |
| gbrain placement | `OS/gbrain/docs/guides/ambient-recall.md` | Start/`compact` = `context_pack`; heartbeat = `delta`; **nunca** `synthesize` no path ambiente |
| mempalace | `OS/mempalace/integrations/shared/recall-protocol.md` L31 | On wake-up: honrar wing do hook; depois recall **question-driven** |
| LifeOS SessionStart | `OS/LifeOS/LifeOS/install/hooks/LoadContext.hook.ts` | Constituição no system prompt; hook só **dinâmico**; skip subagent |
| LifeOS cada prompt | `OS/LifeOS/LifeOS/install/hooks/MemoryTurnStart.hook.ts` | Hot-layer **não** é todo prompt; BM25 fail-open, threshold 0.20 = nada |

Se o plugin restata o procedimento em vez de linkar o skill/doc, o fio já driftou. Paperclip scoped-wake é o anti-drift: **pula steps 1–4**.

---

## 2. O que *é* um wake

Cinco metáforas, nenhum é “o agente está sempre ligado”.

| Sistema | Unidade de wake | Disparos | Se já está rodando |
|---------|-----------------|----------|-------------------|
| **Paperclip** | heartbeat = start adapter → prompt → exit/timeout → gravar | `timer` · `assignment` · `on_demand` · `automation` | **coalesce** — não lança duplicata (`agents-runtime.md` §2) |
| **OpenClaw heartbeat** | turno na main session (não cria task record) | cadence (`30m`, `1h` se Anthropic OAuth); event-driven; manual | defere se a main/automation/target session está busy |
| **OpenClaw user turn** | assemble do context engine | mensagem do humano | — |
| **gbrain** | *placement* de verbo, não processo | SessionStart, PreCompact, heartbeat do *host* | `delta` avança cursor; não há push de heartbeat |
| **LifeOS** | SessionStart (LoadContext) + UserPromptSubmit (MemoryTurnStart) | abrir sessão Claude / cada prompt | hot-layer gated; BM25 por query |
| **mempalace** | hook de session-start + recall por pergunta | wake do harness | honra wing; não busca greenfield |

Paperclip `GOAL.md`: *The control plane doesn't run agents. It orchestrates them.* OpenClaw heartbeat **é** um turno do modelo. São jobs diferentes com a mesma palavra.

---

## 3. O que entra no contexto (e o que é recusado)

### Paperclip — puxar fino, checkout grosso

Procedimento (`SKILL.md`):

1. `GET /api/agents/me` — id, role, chain of command, budget  
2. approval follow-up se houver  
3. `inbox-lite` — **não** a issue list completa  
4. pick: `in_progress` → `in_review` (se comentário) → `todo`; skip `blocked`  
5. **MUST checkout** (run ID header)  
6. `GET /api/issues/{id}/heartbeat-context` — estado compacto, ancestrais, goal/project, **comment cursor** — *without forcing a full thread replay*

**Scoped-wake fast path:** se a mensagem traz `Paperclip Resume Delta` / `Wake Payload` com issue, **skip 1–4**. Não chamar `/agents/me`. Não pegar inbox. Não escolher trabalho.

Recusa: wiki da empresa, MEMORY.md pessoal, replay do thread.

### OpenClaw user turn — bootstrap + on-demand

Injetado sempre (Project Context, com caps):

| Arquivo | Quando | Recusa |
|---------|--------|--------|
| `AGENTS.md` | toda sessão, **inclusive sub-agent** | — |
| `SOUL.md` | sessão normal | não é handbook (`soul.md`: short beats long) |
| `USER.md` | se existe; cap 4k chars | — |
| `MEMORY.md` | **só main privada**; curated summary | **não** em shared/group; daily `memory/*.md` **não** entra no bootstrap |
| skills | inject vs on-demand | ver `context.md` |

Truncation: notice in-prompt de que algo foi cortado; arquivo no disco intacto. Missing file → marker, continua. Sub-agent: **só `AGENTS.md`**.

Heartbeat (outro contrato): prompt verbatim *“If nothing needs attention, reply NO_REPLY. Do not infer or repeat old tasks from prior chats.”*  
`lightContext: true` → **pula bootstrap** (sem SOUL/MEMORY).  
`isolatedSession: true` → sessão fresca, ~100K → 2–5K tokens.

### gbrain — placement, não dump

`ambient-recall.md` é o Pareto explícito:

| Momento | Verbo | LLM? |
|---------|-------|------|
| mensagem com entidade | `entity(name)` | zero, p99 < 100ms |
| **session start** | `context_pack` | zero |
| **depois de compactar** | `context_pack` (rehidrata o que o summary dropou) | zero |
| **heartbeat** | `delta(session_id)` | zero; O(changes); cursor |
| pergunta explícita | `recall` | +1 embed se query |
| raciocínio cross-page | `synthesize` | **NUNCA no path ambiente** |

Push heartbeat **deliberadamente não existe**. Claude Code: hook SessionStart + PreCompact. Codex/MCP: pull. OpenClaw: context engine `assemble()` injeta o checkpoint.

Pack default = `world` only (pode ir para cloud). `include_private` só `remote === false`; MCP remoto **nunca** alarga, mesmo pedindo.

### LifeOS — constituição sempre; hot-layer rara

v5.0 (`LoadContext.hook.ts`):

| Camada | Onde | Quando |
|--------|------|--------|
| Constituição | `LIFEOS_SYSTEM_PROMPT.md` via `--append-system-prompt-file` | sempre |
| Operação + knowledge | `CLAUDE.md` @imports nativos | sempre (Claude Code) |
| Dinâmico | este hook: relationship, learning, advisory, work 48h | SessionStart; **skip subagent**; blocking <50ms |

`MemoryTurnStart` (UserPromptSubmit) — o comentário de 2026-07-11 é a lei:

> `<lifeos-memory>` ~1.5K tokens; injetar **todo** prompt duplicava dezenas de vezes.

Policy: primeiro prompt da sessão, **ou** os arquivos mudaram, **ou** `REFRESH_TURNS` (backstop pós-compact). BM25 todo turno, mas score < 0.20 → **inject NOTHING**. Fail-open: erro do retriever **nunca** bloqueia o prompt. Exit 0 sempre.

### mempalace — honrar o hook, depois calar

On wake-up: se o hook injetou wing / `additional_context`, honrar. Depois: recall **só** se a pergunta puder estar no palácio. Greenfield = não busca.

---

## 4. Cinco recusas (o coração do memo)

| Recusa | Quem escreveu | O oposto consciente |
|--------|---------------|---------------------|
| **Não rodar contínuo** | Paperclip runtime | OpenClaw user session *é* contínua até compactar |
| **Não inferir tarefa velha no poll** | OpenClaw `NO_REPLY` | Paperclip “act in the same heartbeat” (`agents-runtime.md` §7.1) |
| **Não dump do wiki** | Paperclip `heartbeat-context` + gbrain `context_pack` budget | injetar `MEMORY.md` enorme (OpenClaw avisa: distille) |
| **Não synthesize no ambiente** | gbrain ambient-recall | volunteer default-on é *push de ponteiro*, não `think` |
| **Não injetar hot-layer todo prompt** | LifeOS MemoryTurnStart | gbrain volunteer *é* todo prompt (com dedupe de slug) |
| **Não MEMORY.md em grupo** | OpenClaw workspace | honcho/gbrain `world` facts visíveis a todo agente do brain |
| **Não replay do thread** | Paperclip comment cursor | OpenClaw heartbeat *default* manda o histórico da main session (daí `isolatedSession`) |
| **Não dual wake** | Paperclip coalesce | dois plugins de heartbeat no mesmo agente |

OpenClaw `isolatedSession: true` **quebra** o cursor `gbrain delta --session-id` se o id não for estável entre wakes. Os dois docs pedem o contrário: um quer sessão fresca para baratear; o outro quer cursor. Compose legal = `session_id` explícito, não o id da sessão isolada.

---

## 5. Compactação é um wake disfarçado

Quem compacta **apaga verbatim**. Os protocolos que sobreviveram trataram isso como *boundary*, não como GC.

| Sistema | Antes de compactar | Depois |
|---------|-------------------|--------|
| OpenClaw | silent **memory flush** para disco; falha não reseta a sessão | summary; notice se flush esgotou (`notifyUser`) |
| gbrain | PreCompact **bank** das entidades + spool da janela | SessionStart `source=compact` injeta `context_pack` + links `## Compaction checkpoints` |
| LifeOS | — | `REFRESH_TURNS` re-injeta hot-layer (compaction backstop) |
| Paperclip | session ID reuse; **reset** se “stale or confused” | humano decide; não há rehydrate automático |
| mempalace | drawers no SQLite independem do HNSW | índice corrompido ≠ memória perdida |

Gbrain: *the misses come from moments when no question fires* (`ambient-recall.md` L9–10). Compact é um desses momentos. OpenClaw princípio 5 (failures never block replies) aplica: flush falhou → turno segue, talvez degradado.

---

## 6. Sub-agente / scoped-wake — o filho não herda o pai

| Sistema | O que o filho vê | O que o filho **não** vê |
|---------|------------------|--------------------------|
| OpenClaw | `AGENTS.md` | SOUL, USER, MEMORY, daily notes |
| LifeOS | skip LoadContext | relationship/learning/work do SessionStart |
| Paperclip | checkout **subtree-scoped**; 3 canais canônicos de report | o inbox do pai; scoped-wake já nomeou a issue |
| gbrain volunteer | hook só no host; `--harness` por canal | pack com `include_private` via MCP remoto |

O anti-pattern clássico (MEMORY.md do CEO no heartbeat do estagiário, `company-brain.md`) é exatamente **não** filtrar o filho.

---

## 7. Heartbeat ≠ cron ≠ volunteer

Três relógios, três recusas.

| Relógio | Job | Silêncio correto |
|---------|-----|------------------|
| OpenClaw heartbeat | “precisa de atenção **agora**?” | `NO_REPLY`; tarefas recorrentes = **automations**, não scratch |
| Paperclip timer | “tem assignment?” | skip `blocked` sem contexto novo; coalesce |
| gbrain `delta` | “o **corpus** mudou desde o último wake?” | `has_more` + cursor; não é pergunta ao modelo |
| gbrain volunteer | “esta **fala** aponta para uma página?” | confidence < 0.7 ou ambiguidade → nada |
| LifeOS BM25 | “este **prompt** tem hit no arquivo?” | score < 0.20 → nada |

OpenClaw: *Recurring tasks are automations; create or change their schedules with the automations tool, not heartbeat scratch.* Misturar checklist de cron no prompt de heartbeat é o que o default tenta matar.

---

## 8. Compose legal vs suicida

Legal (os docs já se encaixam):

```
Paperclip heartbeat
    → GET me + inbox-lite + checkout + heartbeat-context
    → NÃO puxa MEMORY.md / gbrain synthesize

OpenClaw user turn
    → SOUL + AGENTS (+ MEMORY se main privada)
    → memory_search on demand
    → gbrain context_pack no SessionStart / pós-compact (zero LLM)
    → volunteer só no UserPromptSubmit, cap 3, dedupe

OpenClaw heartbeat
    → isolatedSession + lightContext
    → gbrain delta --session-id <id estável, NÃO o id isolado>
    → NO_REPLY se o delta veio vazio e o scratch está quieto

LifeOS
    → constituição always-on
    → hot-layer rara (first / changed / REFRESH_TURNS)
    → BM25 fail-open
```

Suicida:

1. Heartbeat OpenClaw **sem** `isolatedSession` + SOUL + MEMORY + volunteer + `synthesize` no mesmo poll.  
2. `isolatedSession: true` + `gbrain delta` usando o session id descartável.  
3. `lightContext: true` (sem SOUL) **e** esperar personalidade no poll.  
4. Paperclip scoped-wake **e** ainda assim chamar inbox (o skill **proíbe**).  
5. Injetar `MEMORY.md` em grupo (OpenClaw) **e** gbrain `world` facts no mesmo turno compartilhado.  
6. LifeOS hot-layer every-prompt (já medido: 1.5K × dezenas) **mais** gbrain volunteer every-prompt sem dedupe.  
7. Dois heartbeats (Paperclip timer + OpenClaw cadence) no mesmo empregado sem coalesce.

---

## 9. Falhas que o protocolo já confessou

| Classe | Onde | Não fazer |
|--------|------|-----------|
| ☠️ dual wake | Paperclip coalesce | não lançar segundo heartbeat |
| ☠️ inferência de chat velho | OpenClaw `NO_REPLY` prompt | scratch ≠ inbox de tarefas |
| ☠️ cursor vs sessão fresca | gbrain `delta` × OpenClaw `isolatedSession` | `session_id` estável, explícito |
| 🔒 MEMORY em grupo | OpenClaw workspace | só main privada |
| 🔒 private no MCP | gbrain `include_private` fail-closed | remoto nunca alarga |
| 🔁 compact sem rehydrate | gbrain `source=compact`; OpenClaw flush | compactar e torcer |
| 📊 hot-layer spam | LifeOS 1.5K × N | gate first/changed/REFRESH |
| 🧭 heartbeat palavra | Paperclip = janela de adapter; OpenClaw = turno do modelo | não copiar config entre os dois |
| 🧭 control plane executa | `GOAL.md` recusa | adapter lá fora, phone home |

---

## 10. O que ainda não medimos

- Token real de um heartbeat OpenClaw default vs `isolatedSession+lightContext` (o doc cita ~100K → 2–5K; não re-rodamos)
- Precision do `gbrain delta` com `has_more` em produção
- Se Paperclip `heartbeat-context` comment cursor perde comentários quando o agente reseta sessão
- LifeOS `REFRESH_TURNS` vs gbrain PreCompact: dois backstops no mesmo Claude Code
- `personal-assistant-3way` (abril) vs este fio — o bench de canais não viu `NO_REPLY` nem `context_pack`

Candidatos a dimensão se um pack `wake` nascer: `payload_thinness`, `silence_correctness`, `compaction_rehydrate`, `child_filter`, `coalesce`. Não criar o pack agora.

---

## Relação com os outros artefatos

| Artefato | Papel |
|----------|--------|
| `second-brain-protocols.md` | when-to-touch do **store** |
| **este** | when-to-wake do **agente** |
| `company-brain.md` | nervoso (Paperclip) vs córtex (gbrain); §7 itens 12–14 |
| `memory-5way` / `brain-6way` | scores de store, não de turno |
| `personal-assistant-3way` | abril/2026; **stale** relativo a este memo |
| `_research/host-protocols.md` | quem assemble/compact/sandbox; slots exclusivos |

---

_os-bench research memo (wake layer) | 2026-09-05_
