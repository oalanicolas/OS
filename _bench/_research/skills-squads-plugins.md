# Skills, squads e plugins — como os harnesses dão contexto e estrutura a trabalho complexo

**Date:** 2026-08-12
**Escopo:** clones em `OS/` após sync do `repos.tsv` (skills, squads, plugins, contexto)
**Método:** leitura de arquivos reais + triangulação com `orchestration-5way`, `coding-agents-8way`, `spec-driven-3way`, `personal-assistant-3way`
**Não é um bench canônico** — é um mapa de paradigmas. Sem score inventado.

---

## Tese

Quase todos adotaram o mesmo átomo: **uma pasta + `SKILL.md` com YAML `name`/`description`**. O que muda — e o que decide se o agente consegue trabalho de horas, não de um turno — é a **teoria de controle**:

| Teoria | Quem | Unidade | O que o agente faz quando o trabalho cresce |
|---|---|---|---|
| Disciplina | superpowers | process skill + hook de bootstrap | Invoca skill antes de qualquer ação; subagente fresco por tarefa; ledger em disco |
| Playbook executável | gstack | skill gerada = programa | Passos numerados, seções com STOP, `/autoplan` sequencial, `/ship` como máquina de release |
| OS de ciclo de vida | get-shit-done, gsd-2 | comando/fase + artefato | discuss → plan → execute → verify; estado em `.planning/` ou `.gsd/` |
| Catálogo + runtime | hermes-agent, openclaw | skill indexada + tools | Índice compacto sempre; corpo on-demand; bundles / `$refs` / TaskFlow |
| Empresa simulada | paperclip, Clawith | empregado + org-chart | CEO delega, budgets, heartbeats, issues com handoff durável |
| Spec como SoT | spec-kit | comando + workflow YAML | specify → gate → plan → tasks → implement |
| Identidade de workspace | clawd, LifeOS | SOUL / USER / MEMORY / ISA | Quem você é + o que já sabe; skills moram em outro lugar |
| Governança overlay | agent-governance-toolkit | identidade + policy | Não define o PM; define quem pode o quê, fail-closed |

Mesmo formato de arquivo. Cinco teorias de controle. Misturar sem escolher a teoria produz um prompt inchado que o modelo ignora.

---

## 1. O modelo de 4 camadas (convergência real)

Todo sistema que escala trabalho complexo acabou na mesma pilha:

```
Camada 0  Catálogo          name + description          sempre no prompt, minúsculo
Camada 1  SKILL.md          procedimento + gates        carrega no invoke
Camada 2  references/       domínio, fases, prompts     Read sob demanda
Camada 3  scripts/          trabalho determinístico     executa, não gasta tokens
```

Evidência:

- gsd-2 injeta só o XML `<available_skills>` (`packages/pi-coding-agent/src/core/skills.ts`); o Skill tool lê o corpo.
- OpenClaw capia o catálogo (`maxSkillsInPrompt` 150, `maxSkillsPromptChars` 18k).
- Hermes indexa description ≤ 60 chars (o índice trunca em 57 + `...`); corpo via `skill_view` ou slash.
- GSD mediu o orçamento: 66 skills ≈ 60% do 1% de listing do Claude (~2k tokens). Solução: **menos skills no catálogo**, não descriptions mais curtas (`get-shit-done/docs/research/2026-05-12-skill-surface-budget.md`).
- Superpowers proíbe `@arquivo` no skill — force-load queima contexto.

**Regra:** description responde “devo abrir isto agora?”. Corpo responde “como executar”. Scripts fazem o que o modelo geraria mal.

---

## 2. Skills — como organizam

### 2.1 Formato canônico (Agent Skills)

```
skill-name/
  SKILL.md              # obrigatório
  references/           # só se > ~100–200 linhas
  scripts/              # só se determinístico
  templates/            # contratos de output
```

Frontmatter mínimo: `name`, `description`. Quem cresceu o schema:

| Extra | Quem | Pra quê |
|---|---|---|
| `triggers` / `allowed-tools` | gstack, GSD | invoke + sandbox |
| `requires:` / `benefits-from` | GSD, gstack | composição / perfil de install |
| `platforms` / `related_skills` | hermes | gating OS + grafo de skills |
| `metadata.openclaw.requires.bins` | openclaw, gsd-orchestrator | não listar skill se o binário não existe |
| `disable-model-invocation` | skills pack, openclaw | setup humano; slash ainda funciona |
| `preamble-tier` | gstack | quanto de bootstrap o SKILL.md gerado carrega |

### 2.2 Duas escolas de `description`

**Escola Superpowers (SDO):** description = *quando usar*, nunca o workflow. Se o description resume o fluxo, o agente segue o resumo e **pula o corpo**. Caso documentado: “code review between tasks” fez o agente revisar uma vez, embora o flowchart mandasse duas.

**Escola catalog (GSD / skills.sh / Hermes):** description = *o que faz + when*. Hermes é o extremo: ≤ 60 chars, um período, sem marketing. GSD capia em 100 chars no CI.

As duas escolas concordam no essencial: **description é o único texto pago em todo turno**. Workflow no description é atalho que o modelo toma.

### 2.3 Onde as skills moram

| Repo | Layout | Instalação |
|---|---|---|
| superpowers | `skills/<name>/SKILL.md` (flat) | plugin Claude + hooks; portado pra Codex/Gemini/Pi/OpenCode |
| skills (mattpocock) | `skills/{engineering,productivity,misc}/` | `link-skills.sh` achata em `~/.claude/skills/` |
| gstack | cada pasta raiz é uma skill (`ship/`, `autoplan/`, …) | `~/.claude/skills/gstack/` gerado de `SKILL.md.tmpl` |
| hermes | `skills/<categoria>/<name>/` vs `optional-skills/` | bundled vs `hermes skills install official/…` |
| openclaw | 6 raízes com precedência (workspace > `.agents` > `~/.agents` > state > bundled > plugin) | ClawHub + Skill Workshop |
| gsd-2 | `~/.agents/skills/` + `.agents/skills/` + bundled | `npx skills add`; catálogo por stack no `gsd init` |
| get-shit-done | `commands/gsd/*.md` vira skill do host | perfis `core` / `standard` / `full` |
| paperclip | `packages/skills-catalog/` + `.agents/skills/` | bundled vs optional; `requiredSkills` no TEAM.md |
| BMAD | `src/{bmm-skills,core-skills}/<skill>/` | skill = persona **ou** workflow com `steps/` |
| LifeOS | um install skill unpack 49 skills + hooks | opt-in; CLAUDE.md é routing table |

Precedência que virou padrão de fato: **workspace > projeto > pessoal > bundled**.

### 2.4 Como forçam o agente a usar a skill

Esperar que o modelo “note” o catálogo não funciona. Quem leva a sério **injeta um bootstrap**:

1. **superpowers** — hook `SessionStart` injeta o corpo inteiro de `using-superpowers`. Regra: “1% de chance de aplicar → MUST invoke”. Tabela de racionalizações. Testado com pressure scenarios.
2. **gstack** — skill router na raiz + oferta de gravar `## Skill routing` no `CLAUDE.md`.
3. **LifeOS** — `CLAUDE.md` é uma tabela de `@`-imports, não a biblioteca.
4. **gbrain** — triggers MECE + `routing-eval.jsonl` (≥5 intents) por skill; `volunteer_context` empurra ≤3 páginas.

Sem bootstrap, o pack é inerte.

### 2.5 Como estruturam trabalho complexo *dentro* da skill

| Padrão | Onde | Mecânica |
|---|---|---|
| Pipeline de skills | superpowers | brainstorm (hard-gate) → writing-plans → SDD |
| Seções com STOP | gstack | `sections/*.md` + `manifest.json`; “não trabalhe de memória” |
| Router → workflows | gsd-2, gsd-orchestrator | SKILL.md só roteia; `workflows/*.md` tem process + success criteria |
| Comando fino + `@include` | GSD | `commands/gsd/plan-phase.md` puxa `workflows/plan-phase.md` |
| Persona + menu | BMAD | `customize.toml` `[[agent.menu]]` dispara outra skill |
| Procedure + critério checável | hermes | cada passo termina com completion criterion |
| YAML workflow + gate | spec-kit | `type: gate` approve/reject entre specify e plan |

Composição boa: **Read o outro SKILL.md e pule o preamble compartilhado** (gstack `/autoplan`). Composição ruim: skill-router cujo único conteúdo é “vá pra skill X” (Hermes proíbe). Superpowers nomeia `REQUIRED SUB-SKILL` sem `@` (não force-load).

---

## 3. Squads — cinco modelos mentais

Não há um “melhor”. Cada um decompõe trabalho complexo por uma unidade diferente.

### 3.1 Pipeline ágil + sala de papéis — BMAD

- Personas nomeadas: Winston (architect), John (PM), Amelia (UX), etc.
- Cada uma = `SKILL.md` + `customize.toml` (role, identity, principles, `persistent_facts`, menu).
- Merge em 3 camadas: skill default → `_bmad/custom/{skill}.toml` (time) → `.user.toml`.
- Trabalho flui por **artefatos**: análise → PRD/UX/SPEC → architecture/epics → build.
- Party Mode: `session` (uma mente, várias vozes) · `auto` · `subagent` (mentes independentes) · `agent-team` (time persistente no Claude Code).
- Memória da party é `.memlog.md` (dinâmica, não transcript).
- Governança: humano em cada gate de fase. Sem budget de tokens.

**Quando brilha:** SDLC editorial. O humano quer falar com o arquiteto, não com um “agente 3”.

### 3.2 Company-sim — paperclip e Clawith

**Paperclip** é o control plane mais completo:

- Pacote `agentcompanies/v1`: `TEAM.md` + `AGENTS.md` + `PROJECT.md` + `TASK.md` + `SKILL.md`.
- Core Exec Team: CEO → CTO → QA. CEO **não faz IC**; delega; contrata se o report não existe.
- Árvore de issues (`parentId`), checkout atômico (409 se dois claimam), budgets mensais em cents, board (hire/pause/reassign).
- Handoff durável no issue: objetivo, owner, acceptance, blocker, next action.
- 7 adapters (Claude, Codex, Cursor, Gemini, OpenClaw, OpenCode, Pi) — a empresa orquestra **runtimes heterogêneos**.

**Clawith** é o mesmo metáfora com runtime social:

- `meta.yaml` + `soul.md` por cargo (20+ templates).
- A2A: `notify` | `consult` | `task_delegate`.
- Autonomia L1 auto / L2 notify / L3 approval (`modify_soul` e financeiro = L3).
- Filesystem privado por empregado (`soul`, `memory`, `skills`, `workspace`).

**Quando brilha:** frota persistente, custo, auditoria, “quem reporta pra quem”.

### 3.3 Fábrica de milestones — gsd-2 / get-shit-done

- GSD: 60+ slash commands + 33 subagentes tipados (`gsd-planner`, `gsd-executor`, `gsd-verifier`…).
- gsd-2: `scout` → `planner` → N `worker` em worktrees → gates → 3 reviewers (requirements / integration / acceptance).
- Contexto default = `fresh`. Filho **não herda** o chat do pai. Scout comprime pra quem não viu os arquivos.
- Estado em disco: `STATE.md`, `T##-PLAN.md` / `T##-SUMMARY.md`, `DECISIONS.md`, `KNOWLEDGE.md`.
- Parallel: leases + fencing + overlap de arquivos. Filho com `GSD_SUBAGENT_CHILD=1` não respawna.

**Quando brilha:** “uma spec, anda embora, volta com o projeto”. Autonomia longa.

### 3.4 Especialistas sequenciais — gstack

Não é empresa. É uma **gauntlet de papéis no mesmo humano**:

```
/office-hours → /spec → /autoplan (CEO → Design → Eng → DX) → implement → /review → /qa → /ship
```

- Fases **não rodam em paralelo** — cada uma constrói na anterior.
- Independência via voz dupla: subagente Claude (sem contexto da fase anterior) + Codex `exec`, depois tabela de consenso.
- Especialistas de review são checklists JSON (`review/specialists/{security,red-team,testing,…}.md`).
- Artefatos em `~/.gstack/projects/<slug>/` (decisions, learnings, timeline, checkpoints).

**Quando brilha:** um founder/dev quer taste + rigor sem contratar um org de agentes.

### 3.5 Conversação / crew / governança

- **crewAI:** YAML `role/goal/backstory` + `Process.sequential|hierarchical`. Próxima task recebe output da anterior. Sem org, sem budget.
- **autogen:** RoundRobin / Selector / Swarm / Magentic-One / GraphFlow. Transcript compartilhado. Caps de turn/stall. Biblioteca, não produto.
- **AGT:** não interpreta o PM. Interpreta *quem pode o quê*: delegação com narrowing monotônico de capabilities, DID, policy fail-closed.
- **OpenHands (este checkout):** control plane de conversas + automações. Sem primitiva de squad.

---

## 4. Plugins — o que um pacote pode acrescentar

Três famílias. Misturá-las no core é o anti-pattern mais caro (cada tool do core é pago em **todo** turno).

### 4.1 Plugin de processo (ensina a trabalhar)

- **superpowers:** `.claude-plugin/plugin.json` + `skills/` + um hook `SessionStart`. Zero deps. Skills nomeiam **ações**, nunca tools do host. Domain skills são rejeitadas do core (94% PR reject é feature).
- **gstack:** não é plugin nativo — é uma suíte gerada por host (`hosts/claude.ts`, `codex.ts`, `openclaw.ts`, `hermes.ts`…). Um source, N instalações.
- **spec-kit:** `extension.yml` → comandos `speckit.<ext>.<cmd>` + hooks `after_specify|plan|tasks|implement`. Bundles = extensions + presets + workflows. Catálogo community = discovery only.

### 4.2 Plugin de runtime (acrescenta capacidade)

- **openclaw:** o modelo mais rico. Manifest validado **antes** de executar código. Pode registrar providers, channels, tools, hooks, HTTP, skills, MCP, e **slots exclusivos** `memory` | `context-engine`. Bundles Claude/Codex/Cursor entram com trust boundary mais estreito.
- **hermes:** `plugin.yaml` por kind (`memory/`, `model-providers/`, `platforms/`, `context_engine/`). Escada oficial: estender código → CLI+skill → tool com gate → plugin → MCP → tool de core (último recurso).
- **paperclip:** plugin com UI, API routes namespaced, capabilities no worker. Ainda single-tenant / filesystem (spec completa é target, não o de hoje).

### 4.3 Pack de contexto (quem você é / o que já sabe)

- **gbrain:** plugin OpenClaw (context engine + MCP + ~40 skills) **e** skillpack. Cérebro (páginas) ≠ repo do agente (código/skills/identidade). `volunteer_context` empurra ≤3 páginas.
- **mempalace:** L0 identidade (~100 tokens) + L1 história (500–800) sempre; L2/L3 via search. Verbatim. PreCompact flush.
- **clawd / LifeOS / OpenClaw workspace:** `SOUL.md` (voz) ≠ `AGENTS.md` (regras) ≠ `USER.md` (o humano) ≠ `MEMORY.md` (curado) ≠ `memory/YYYY-MM-DD.md` (log). Subagente leva **só** `AGENTS.md`.

### 4.4 MCP é o primitivo, não o produto

`mcp-servers` expõe tools/resources/prompts. Todo mundo acima **embrulha** MCP. Ninguém sério trata MCP como substituto de skill: skill é procedimento + julgamento; MCP é I/O.

### 4.5 Capability-First (AIOX) — ninguém em OS/ faz isso

O guia `AIOX-enterprise/docs/architecture/capability-first-and-plugins.md` separa **capability** (contrato de produto) · **plugin** (caixa) · **skill** (porta nativa do host) · **agent** (papel load-bearing) · **squad** (composição opcional) · **workspace** (dados fora).

Em `OS/` as mesmas palavras significam outra coisa: capability = grant (Paperclip) ou tipo de registro (OpenClaw); plugin = extensão do host; squad = pasta. Nenhum clone tem `capability.yaml` + `targets/{claude,codex}/SKILL.md` autorados + dual-run/cutover.

Vizinhos (não equivalentes): BMAD installer nativo nas duas superfícies; OpenClaw bundles; gstack *gera* hosts (o inverso do ADR-157). mega-brain-vip **não entra** — quarentena de prática.

Memo: `_bench/_research/capability-first-vs-os.md`. Caixa pública: `_bench/_research/market-compatible-packaging.md`. Definições + comparação por clone (skill = porta, plugin = caixa, squad-como-pasta = legado): `_bench/_research/plugin-vs-skill-vs-squad.md`.

---

## 5. Contexto — o que fica sempre ligado

Always-on tem que caber em poucos mil tokens. Isso é o padrão mais consistente do conjunto.

| Sempre ligado | Função | Quem |
|---|---|---|
| `AGENTS.md` | regras operacionais, standing orders | OpenClaw, Codex, Hermes, OpenHands |
| `CLAUDE.md` | o mesmo, sabor Claude; frequentemente routing | Superpowers, gstack, LifeOS, gbrain |
| `SOUL.md` | voz/persona — **não** policy | OpenClaw, Hermes, Clawith |
| `IDENTITY.md` | nome, vibe, ~100 tokens | OpenClaw, MemPalace L0 |
| `USER.md` | modelo do humano | OpenClaw, LifeOS |
| Bootstrap skill | “cheque skill antes de agir” | Superpowers, gstack router |
| Catálogo de skills | name+description | todos os runtimes Agent Skills |

**On-demand:** corpo da skill, specs, plans, ISA, drawers, páginas gbrain, MCP resources.

Limites observados:

- OpenClaw: 20k chars/arquivo, 60k total no bootstrap; aviso se truncar (não drop silencioso).
- Hermes: 20k no project-context; first-match `.hermes.md` → `AGENTS.md` → `CLAUDE.md`; **não compacta mensagem do usuário**.
- MemPalace wake-up: 600–900 tokens.
- gstack preamble gerado é o outlier (grande). Funciona, mas é o oposto do bootstrap mínimo do Superpowers.

### Como lutam contra context rot

| Tática | Fonte | Por que importa |
|---|---|---|
| Subagente fresco + handoff por **arquivo** | superpowers SDD | Paste de histórico chegou a 42k chars, 99% recap |
| Ledger em disco | `.superpowers/sdd/<plan>/progress.md` | Compactação apaga a conversa; controllers sem ledger re-despacharam tasks já feitas |
| Compaction + PreCompact flush | OpenClaw, MemPalace | Memória sai do chat antes do corte |
| Micro-compaction (nunca a mensagem do user) | Hermes | Intent do humano é SoT; narração do agente é descartável |
| Checkpoint / context-save | gstack `~/.gstack/projects/<slug>/checkpoints/` | Resume cross-session e cross-workspace |
| Artefatos de fase | GSD `.planning/`, gsd-2 `.gsd/`, spec-kit `spec.md`/`plan.md`/`tasks.md` | Chat é scratch buffer |
| Compiled truth + log append-only | gbrain, LifeOS ISA, OpenClaw MEMORY vs daily | Não reler o diário inteiro |

**A falha mais cara documentada (superpowers):** conversa não sobrevive compactação. Sem ledger, o controller reexecuta o plano.

---

## 6. A espinha do trabalho complexo (nomes diferentes, mesmo osso)

```
intent → shape/spec → plan (gate) → implement (TDD / task loop)
      → review (contexto separado) → fix loop com teto → ship → persistir memória
```

| Estágio | Superpowers | gstack | GSD / gsd-2 | spec-kit | paperclip |
|---|---|---|---|---|---|
| Shape | `brainstorming` (hard-gate) | `/office-hours` | `discuss-phase` / scout | `/speckit.specify` | CEO + `task-planning` |
| Spec | `docs/superpowers/specs/` | `/spec` (issue) | `REQUIREMENTS.md` / SPEC | `spec.md` + constitution | issue + plan doc |
| Plan | `writing-plans` | `/autoplan` 4 fases | `plan-phase` + checker | `plan.md` + `tasks.md` | child issues |
| Execute | SDD: 1 implementer / task | implement + `/qa` | workers em worktree | `/speckit.implement` | CTO via adapter |
| Gate | review spec+quality, 5 rounds, breaker | AskUserQuestion + `/codex` | verify / 3 reviewers | `type: gate` + checklists | `in_review` + board |
| Persist | git + ledger | decisions/learnings/gbrain | STATE / SUMMARY / KNOWLEDGE | feature dir | issue comments + artifacts |

### Gates que de fato funcionam

1. **Humano só em porta de mão única** — Superpowers empacota contradições do plano *antes* da Task 1; não pergunta “continuar?”. gstack auto-decide perguntas de duas vias (`/plan-tune`); taste vai pro humano.
2. **Reviewer é outro contexto** — controller não implementa, não “conserta rápido”. Re-review é scoped no diff do fix.
3. **Breaker** — 5 rounds e adjudica no ledger. Loop infinito de review é o outro jeito de queimar o run.
4. **Completeness no artefato**, não no “o modelo disse done” — checklists spec-kit, coverage do `/ship`, spec ✅ + quality approved.
5. **Constraints globais copiadas verbatim** no brief da task — o implementer **não** lê o plano inteiro.

### O que carrega contexto entre agentes

| Mecanismo | Quem |
|---|---|
| Artefato de fase (PRD, SPEC, plan file) | BMAD, gstack, GSD, spec-kit |
| Grafo de issues + comments | paperclip, Clawith |
| soul/memory FS privado | Clawith |
| Transcript compartilhado | autogen, BMAD party, Clawith group |
| Output da task → próxima | crewAI, GraphFlow, gsd-2 `{previous}` |
| Scout comprimido / `continue.md` | gsd-2 |
| Heartbeat / API pull | paperclip |
| Ticket criptográfico de delegação | AGT |

Chat compartilhado escala mal. Arquivo nomeado escala.

---

## 7. O que vale absorver (stack recomendada)

Se o alvo é um harness (AIOX / sinkra / um gstack-like) que precise de contexto e estrutura pra trabalho de verdade:

1. **Process plugin no formato Superpowers**
   - Zero-dep, SessionStart bootstrap, skills nomeiam ações, SDD com ledger + reviewer separado + breaker.
   - Description = trigger only. Sem `@` force-load.

2. **Runtime plugin no formato OpenClaw**
   - Manifest-first (valida sem executar). Slots exclusivos de memory/context-engine. Bundles de Claude/Codex como trust menor.

3. **Conhecimento no formato gbrain + MemPalace**
   - Compiled truth + gavetas verbatim. Push de poucas páginas. Nunca dump do palácio. Dois repos: agente ≠ cérebro.

4. **Overlay de projeto no formato spec-kit / LifeOS / GSD**
   - Constitution + spec/plan/tasks **ou** ISA **ou** `.gsd/` em disco.
   - `AGENTS.md`/`CLAUDE.md` é routing table com marcadores gerenciados, não a enciclopédia.

5. **Host adapters no formato gstack**
   - Um source de skill, install gerado por host, prefixo opcional (`gstack-*`).

6. **Company-sim só se houver frota heterogênea**
   - paperclip (org + budget + adapters) quando o problema é governar muitos agentes de stacks diferentes. Não use isso pra um dev solo fazer um PR.

7. **Governança AGT em volta, não no lugar**
   - Identity + narrowing + audit quando “quem pode o quê” precisa fail-closed. Não substitui skill/squad.

### Superfície de skill: o orçamento é o produto

GSD já bateu na parede (66 skills = 60% do listing). Levers que funcionam:

- Perfis de install (`core` / `full`).
- Routers de namespace (6 meta-skills em vez de 60 no catálogo).
- Cap duro de description + lint no CI.
- `disable-model-invocation` pra setup.
- Gating por binário/OS (OpenClaw) pra não poluir o índice.

Não funciona: encolher description de 72 → 50 chars. O próximo corte é **emitir menos skills**.

---

## 8. Anti-patterns (não copiar)

| Anti-pattern | Evidência | Dano |
|---|---|---|
| Biblioteca inteira no system prompt | LifeOS 49 skills always-on; MEMORY.md gigante | Rot + truncagem silenciosa |
| Workflow no `description` | Superpowers SDO | Agente segue o resumo, ignora o corpo |
| Chat como fonte da verdade | SDD sem ledger | Re-despacho de tasks feitas pós-compaction |
| Colar histórico no próximo subagente | dispatch de 42k, 99% recap | Context bloat + custo |
| Controller “conserta rápido” | Superpowers rationalization table | Pula review, polui o coordenador |
| Domain skill no plugin core | Superpowers rejeita no PR | Core vira monólito |
| Tool novo no core por feature | Hermes AGENTS.md | Pago em todo turno pra sempre |
| Auto-executar runbook de install | gbrain recusa `bootstrap.md` | Supply chain |
| Escrever no config global do user | Superpowers porting guide | Integração frágil e hostil |
| Sumarizar memória do usuário | MemPalace reject; Hermes não compacta user | Perde a SoT |
| Search de memória em todo turno | MemPalace recall skill | Mata latência / “parece instantâneo” |
| Fusion Squad-First em escala (88 squads + 5 núcleos) | mega-brain-vip (Frankenstein declarado) | Circulação ≠ doutrina; **não usar como prática** |
| Um SKILL gerado para todos os hosts | gstack `hosts/*.ts` | Falsa equivalência Claude↔Codex (ADR-157) |
| Skill-router vazio | Hermes hardline | Hop inútil + description duplicada |
| Preamble gerado enorme sem budget | gstack SKILL.md | Oposto do bootstrap mínimo |
| Persona-only sem catálogo | claude-remote-manager | Serve bot 24/7; não é plataforma |

---

## 9. Mapa rápido por repo

| Repo | Skills | Squads | Plugins | Contexto always-on | Espinha do trabalho |
|---|---|---|---|---|---|
| superpowers | 14 process skills, flat | SDD: implementer + reviewer | Claude plugin + hook | `using-superpowers` | brainstorm → plan → SDD ledger |
| gstack | 40+ playbooks gerados | gauntlet CEO/Design/Eng/DX | host adapters | router + CLAUDE.md + `~/.gstack/projects/` | office-hours → autoplan → ship |
| get-shit-done | 60+ commands | 33 subagentes tipados | install profiles | listing budget | discuss → plan → execute → verify |
| gsd-2 | Agent Skills runtime + orchestrator | scout/planner/worker/reviewer | Extension API + MCP | `.gsd/` artifacts | milestone DAG + worktrees |
| BMAD | skill = persona **ou** workflow | 5 agentes + party modes | customize.toml 3 camadas | `persistent_facts` + project-context | PRD → arch → stories → build |
| paperclip | catalog bundled/optional | org-chart + hire | plugin spec + 7 adapters | issue + heartbeat | CEO delega na árvore de issues |
| Clawith | skills por empregado | A2A + group @ | templates de cargo | soul.md privado | workplace social + L1–L3 |
| hermes | bundled vs optional, ≤60c desc | `delegate_task` + plan skill | `plugin.yaml` kinds | SOUL + project-context 20k | /plan → `.hermes/plans/` |
| openclaw | 6 raízes, ClawHub, Workshop | TaskFlow children | native plugin + bundles | AGENTS/SOUL/USER + skill *list* | standing orders + daily memory |
| spec-kit | *não tem skills* — commands | handoffs entre commands | extension.yml + bundles | constitution + managed block | specify → gate → plan → tasks |
| skills pack | práticas pequenas | nenhum | `npx skills add` | CONTEXT.md + ADRs | grill → tdd → triage |
| LifeOS | 49 skills unpack | nenhum org | um install skill | constitution + routing table + USER/ISA | TELOS → ISA → Algorithm |
| clawd | nenhum | nenhum | nenhum | SOUL/USER/MEMORY | continuidade, não grafo |
| crewAI / autogen | n/a (code/YAML) | crew / group chat | library | transcript / memory tiers | task list ou speaker policy |
| AGT | n/a | delegation chain | host hooks | identity YAML | authz, não planning |
| gbrain / mempalace | recall / skillpacks | n/a | OpenClaw plugin / MCP | compiled truth / L0–L1 | push context / search-before-answer |

---

## 10. Fontes (paths no clone)

- `superpowers/skills/writing-skills/SKILL.md` — SDO, TDD de skill, anti-`@`
- `superpowers/skills/using-superpowers/SKILL.md` — bootstrap / 1% rule
- `superpowers/skills/subagent-driven-development/SKILL.md` — ledger, brief-por-arquivo, breaker
- `gstack/docs/skills.md` — mapa da suíte e o ciclo office-hours → ship
- `gstack/ARCHITECTURE.md` — “browser é o difícil; o resto é Markdown”
- `gsd-2/docs/user-docs/skills.md` — Agent Skills + `~/.agents/skills/`
- `gsd-2/gsd-orchestrator/SKILL.md` — GSD como subprocesso (exit 0/1/10/11)
- `get-shit-done/docs/research/2026-05-12-skill-surface-budget.md` — orçamento de listing
- `BMAD-METHOD/src/core-skills/bmad-party-mode/SKILL.md` — 4 modos de party
- `BMAD-METHOD/src/bmm-skills/agents/bmad-agent-architect/` — persona + customize.toml
- `paperclip/packages/teams-catalog/catalog/bundled/company-defaults/core-exec-team/`
- `paperclip/doc/plugins/PLUGIN_SPEC.md`
- `hermes-agent/skills/software-development/hermes-agent-skill-authoring/SKILL.md`
- `spec-kit/spec-driven.md` + `spec-kit/extensions/EXTENSION-DEVELOPMENT-GUIDE.md`
- `clawd/AGENTS.md` — ritual de sessão (SOUL → USER → daily → MEMORY)
- `_bench/orchestration-5way/executive-report.md`
- `_bench/coding-agents-8way/executive-report.md`
- `_bench/CROSS-BENCH-SYNTHESIS.md` §6 (patterns a absorver)

---

_Pesquisa 2026-08-12. Para scores e dimensões, os benches canônicos em `_bench/{slug}/`. Este memo não inventa ranking._
