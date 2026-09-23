# Host protocols — quem monta o turno

**Date:** 2026-09-05  
**Nível:** terceiro da série  
- store → `second-brain-protocols.md`  
- turno → `wake-protocols.md`  
- **host → este**  
**Pergunta:** quem decide o que o modelo *vê*, onde as tools *correm*, e o que acontece quando o plugin quebra?  
**Método:** arquivos-lei. Sem score.  
**Não é taxonomia de cérebros.** Jobs E/M e o glossário estão em `_research/taxonomy.md`. Este memo é só o eixo host (2e).

Os dois memos anteriores assumem um host. Este nomeia o host e o que ele **recusa ser**.

---

## 1. Arquivos-lei

| Sistema | Lei | Promessa |
|---------|-----|----------|
| OpenClaw context engine | `OS/openclaw/docs/concepts/context-engine.md` | Assemble/compact/subagent são um **slot exclusivo**; default `legacy`; falha → **quarantine + fallback** |
| OpenClaw system prompt | `OS/openclaw/docs/concepts/system-prompt.md` | Bootstrap caps; sub-agent só `AGENTS.md`; heartbeat scratch **não** entra no system prompt |
| OpenClaw workspace | `OS/openclaw/docs/concepts/agent-workspace.md` | Workspace = cwd default, **não** sandbox |
| OpenClaw sandbox | `OS/openclaw/docs/gateway/sandboxing.md` | Gateway **sempre no host**; só tool execution move |
| Sandbox vs policy vs elevated | `OS/openclaw/docs/gateway/sandbox-vs-tool-policy-vs-elevated.md` | Três camadas independentes; `explain` nomeia qual bloqueou |
| Plugin slots | `OS/openclaw/docs/plugins/manifest.md` | `kind: memory` → `slots.memory` (default `memory-core`); `kind: context-engine` → `slots.contextEngine` (default `legacy`) |
| Memory engines | `OS/openclaw/docs/concepts/memory.md` | builtin \| Honcho \| LanceDB; wiki **ao lado**, não no slot |
| Paperclip GOAL | `OS/paperclip/doc/GOAL.md` | Control plane **não executa** agentes |
| Hermes | `OS/hermes-agent/plugins/context_engine/__init__.py` | Um engine ativo; default `compressor`; separado do plugin system geral |
| gbrain placement | `OS/gbrain/docs/guides/ambient-recall.md` | No OpenClaw, o **context engine** roda o checkpoint lane (`assemble` injeta o pack) |

---

## 2. Três papéis que a palavra “host” mistura

| Papel | Quem é | Recusa |
|-------|--------|--------|
| **Control plane** | Paperclip | Não monta prompt, não compacta, não sandboxa. Heartbeat = invocar adapter. |
| **Gateway / runtime** | OpenClaw Gateway | Monta prompt, compacta, aplica sandbox **nas tools**. Processo do Gateway **nunca** entra no sandbox. |
| **Context engine** | slot `contextEngine` | Decide *quais mensagens* o modelo vê. **Não** é o memory plugin. |
| **Memory plugin** | slot `memory` | Search/retrieval. **Não** controla o que entra no prompt — a menos que o engine chame `buildMemorySystemPromptAddition`. |
| **Adapter** | Paperclip `claude_local` / `openclaw_gateway` / Hermes | Executa o turno noutro processo. Phone home. |

Paperclip e OpenClaw não são dois hosts do mesmo tipo. Um orquestra empregados; o outro *é* o runtime do empregado. Ligar os dois sem essa frase produz heartbeat duplicado (`wake-protocols.md` §8.7).

---

## 3. Slots exclusivos — um de cada, não um bazar

`manifest.md`:

> Exclusive plugin kinds are selected through `plugins.slots.*`

| Slot | Default | Kind | Uninstall |
|------|---------|------|-----------|
| `plugins.slots.memory` | `memory-core` | `memory` | reset para default |
| `plugins.slots.contextEngine` | `legacy` | `context-engine` | reset para `legacy` |

`context-engine.md` L403: o slot é exclusivo **em runtime** — só um engine resolvido por run/compaction. Outros `kind: "context-engine"` podem *carregar*; só o selecionado é *resolvido*.

`memory-lancedb.md`: se outro plugin dono do memory slot, **é desabilitado com warning**.

Isso mata o compose suicida “builtin + Honcho + LanceDB + gbrain todos no slot de memória”. Honcho e gbrain no mesmo assistente só são legais se **um** está no `slots.memory` e o outro é tool/MCP **fora** do slot — e aí o roteamento é o problema de `second-brain-protocols.md` §7, não do host.

Hermes replica o padrão: `plugins/context_engine/<name>/`, *only one is active*, default `compressor`.

---

## 4. Ciclo de vida do context engine (quatro pontos + um opcional)

Toda run (`context-engine.md`):

| Ponto | Quando | Pode |
|-------|--------|------|
| **1. Ingest** | nova mensagem na sessão | indexar no store do engine |
| **2. Assemble** | antes do model run | devolver mensagens ordenadas + `systemPromptAddition` no budget |
| **3. Compact** | janela cheia ou `/compact` | sumarizar o velho |
| **4. After turn** | run completa | persistir, compactar em background, atualizar índice |
| **maintain()** | pós-bootstrap / turno / compact | rewrite de transcript; `turnMaintenanceMode: "background"` para **não** bloquear o reply |

Sub-agent: `prepareSubagentSpawn` opcional. Codex nativo: o host projeta o assemble em developer instructions; **Codex ainda dono** do thread e do compact nativo.

`ownsCompaction`:

- `true` — o engine admite o prompt; auto-compact in-attempt do runtime **desliga**
- `false` / unset — **não** cai no compact do `legacy` sozinho. Tem que `delegateCompactionToRuntime(...)` ou implementar o próprio e pôr `true`

Quem seta `ownsCompaction: false` e não delega **perde compactação**. Classe ☠️.

---

## 5. Três camadas de “por que a tool bloqueou”

`sandbox-vs-tool-policy-vs-elevated.md` — a ordem importa. `openclaw sandbox explain` nomeia a camada.

```
1. Sandbox     → ONDE a tool corre (backend vs host)
2. Tool policy → QUAIS tools existem/são allowed
3. Elevated    → escape hatch de exec; não fura creator-role required sandbox
```

Sandbox (`sandboxing.md`):

- **Off por default.** “Not a perfect security boundary.”
- Gateway **sempre no host**. Só `exec/read/write/edit/apply_patch/process` (+ browser opcional) entram.
- Mode: `off` | `non-main` | `all`
- **`non-main` é a surpresa:** grupos/canais **sempre** non-main → sandboxed; a main key `agent:<id>:main` não é. DM do dono e o grupo **não** compartilham o mesmo chão.
- Scope: `agent` | `session` | `shared` (quantos containers)
- `workspaceAccess`: `none` (default, workspace do agente **não** aparece) | `ro` | `rw`
- Creator role `sandbox: "required"` é **imutável** na sessão; backend indisponível **fail-closed**; elevated **não** bypassa

Workspace (`agent-workspace.md`):

> The workspace is the **default cwd**, not a hard sandbox. Absolute paths still reach the host unless sandboxing is enabled.

Três recusas:

1. Workspace ≠ sandbox  
2. Tool policy ≠ sandbox (MCP some no sandbox se `alsoAllow` não lista o prefixo)  
3. Elevated ≠ “desliga o jail do creator”

`docker.binds` **fura** o filesystem do sandbox. Bind de `/var/run/docker.sock` = host control. O doc grita.

---

## 6. Falha do plugin: quarantine, não crash do turno

`context-engine.md` Failure isolation + Tips:

- Engine missing / contract inválido / throw no factory / throw no lifecycle → **quarantine** no processo atual do Gateway  
- User turns caem no `legacy` para **a reply continuar**  
- Doctor lista `contextEngineQuarantines`  
- Embedding provider configurado mas plugin não registrado → recall semântico cai em **keyword/FTS sem avisar o turno** (`status-plugin-health.ts` — “silently falls back”)

Espelha OpenClaw princípio 5 (`memory-architecture.md`): *failures never block replies*. O custo é **silêncio**: o operador acha que o lossless-claw está ativo e está no `legacy`. `openclaw doctor` é o único honesto.

Uninstall do plugin no slot → reset automático para default. Sem edit manual. Dois slots (`memory` e `contextEngine`) compartilham essa regra.

Sessões antigas **não** migram de engine: “existing sessions continue with their current history. The new engine takes over for future runs.”

---

## 7. O que o host recusa ser

| Recusa | Onde | O oposto consciente |
|--------|------|---------------------|
| **Não ser o memory store** | slot `memory` ≠ `contextEngine` | engine que “também” indexa sem estar no slot (dual-SoT) |
| **Não executar o empregado** | Paperclip GOAL | OpenClaw Gateway *é* o runtime |
| **Não sandboxar o Gateway** | sandboxing.md | tools no backend; Gateway no host |
| **Não injetar daily notes no bootstrap** | system-prompt.md | `memory/*.md` on demand; `/new` é a exceção one-shot |
| **Não pôr heartbeat scratch no system prompt** | system-prompt.md L126 | scratch só na user message do poll |
| **Não um bazar de engines** | slots exclusivos | N `kind: memory` enabled, um só resolvido — os outros carregam e mentem |
| **Não compactar duas vezes** | `ownsCompaction` | engine `true` + runtime in-attempt = double summary |
| **Não fail-closed no reply** | quarantine → legacy | Hermes/gstack fail-closed no *exec*; o host OpenClaw fail-*open* no *texto* |

Gbrain no OpenClaw: o path legal é o **engine** chamar o checkpoint no `assemble()` (`ambient-recall.md` “Engine-internal”). Não é segundo memory slot.

---

## 8. Hermes no mesmo desenho, outro chão

`hermes-agent/plugins/context_engine/__init__.py`:

- Engines **no repo**, não no plugin system geral  
- Um ativo (`context.engine` no yaml)  
- Default `"compressor"` (ContextCompressor)  
- Load falhou → `None` (caller decide)

OpenClaw externaliza o engine (npm plugin, quarantine, doctor). Hermes embute e troca por nome. Mesmo slot-mental, enforcement diferente: OpenClaw **isola falha do turno**; Hermes **deixa o loader retornar vazio**.

Paperclip não tem context engine. O adapter (Claude/Codex/Hermes/OpenClaw) monta o que quiser. O control plane só vê status/tokens/logs.

---

## 9. Compose legal vs suicida

Legal:

```
Paperclip                  → control plane (checkout, budget, goal)
    adapter openclaw_gateway
        OpenClaw Gateway   → host (prompt, compact, sandbox tools)
            slots.contextEngine = legacy | lossless-claw | gbrain-checkpoint
            slots.memory        = memory-core | honcho | lancedb   # UM
            sandbox.mode        = non-main | all
            workspace           ≠ sandbox
        gbrain volunteer       → hook/MCP fora do memory slot
        mempalace hub          → MCP tools, recall protocol
```

Suicida:

1. Dois `kind: memory` “enabled” e achar que os dois retrievam. O slot pega um; o outro pode só registrar tools e duplicar.  
2. `slots.memory = honcho` **e** deixar `USER.md`/`MEMORY.md` vivos (migração non-destructive). Dual-SoT (`second-brain-protocols.md` §7).  
3. Plugin context engine com `ownsCompaction: false` sem `delegateCompactionToRuntime` — compact some.  
4. `sandbox.mode: non-main` achando que o grupo está tão exposto quanto a DM. O grupo **é** sandboxed; a main **não**.  
5. `workspaceAccess: none` + paths absolutos no prompt — o modelo “lê” o workspace no texto e escreve no sandbox vazio.  
6. `docker.binds: /var/run/docker.sock` e chamar isso de jail.  
7. Trocar context engine e esperar que sessões velhas re-assemblem o histórico com a estratégia nova.  
8. Quarantine silenciosa: lossless-claw quebrado, `legacy` servindo, doctor ignorado.  
9. Paperclip timer **e** OpenClaw heartbeat no mesmo empregado (`wake-protocols.md`).  
10. `synthesize` no `assemble()` do context engine — gbrain **proíbe** no path ambiente.

---

## 10. Falhas que o protocolo já confessou

| Classe | Onde | Não fazer |
|--------|------|-----------|
| ☠️ compact sumiu | `ownsCompaction: false` sem delegate | implementar ou delegar |
| ☠️ recall semântico mudo | embedding provider sem plugin | doctor “Configured memory provider not registered” |
| ☠️ dual-SoT pós-migrate | honcho setup keeps files | escolher SoT |
| 🔒 sandbox surpresa | `mode: non-main` | grupos ≠ main |
| 🔒 workspace ≠ sandbox | agent-workspace.md | absolute paths |
| 🔒 elevated vs required | creator role immutable | não é override de operador |
| 🔁 dois compactadores | ownsCompaction true + runtime | um dono |
| 📊 engine que você acha que está ativo | quarantine → legacy | `openclaw doctor` |
| 🧭 slot vs kind | vários plugins carregam; um resolve | |

---

## 11. Trilogia (como ler os três)

```
STORE     second-brain-protocols   o que é uma memória; when-to-touch
TURN      wake-protocols           o que dispara o wake; o que entra
HOST      este                     quem assemble/compact/sandbox; um slot
```

Regra que atravessa os três: **silêncio correto > dump**.  
Store: empty palace → say so.  
Turn: `NO_REPLY` / inject nothing < 0.20.  
Host: engine quebra → legacy, reply segue; compact falha → conversa intacta.

O preço do silêncio no host é o único que o operador **não** vê no chat: quarantine. Por isso doctor é parte do protocolo, não ops opcional.

---

## 12. O que ainda não medimos

- Token real `legacy` vs `lossless-claw` no mesmo corpus  
- Quantas sessões em produção ficam em `legacy` por quarantine sem o dono saber  
- Hermes `compressor` vs OpenClaw `legacy` no mesmo transcript  
- Paperclip `openclaw_gateway` + `slots.memory=honcho` + gbrain volunteer — o compose legal, em um único empregado, com budget  
- `personal-assistant-3way` (abril) vs este fio — o pack de canais não viu slots

Não reescrever `personal-assistant-3way` neste refresh: o pack mede channels/cost/privacy, não assemble/sandbox/slot. Este memo é o substituto de *protocolo*; o bench de produto continua stale.

---

## Relação

| Artefato | Papel |
|----------|--------|
| `second-brain-protocols.md` | store |
| `wake-protocols.md` | turno |
| **este** | host |
| `company-brain.md` | nervoso vs córtex |
| `personal-assistant-3way` | abril; canais; **stale** para slots |

---

_os-bench research memo (host layer) | 2026-09-05_
