# Plugin ≠ skill. Squad como caixa é legado.

**Date:** 2026-08-12  
**Para:** vocabulário público e de produto (compatível com o mercado)  
**Padrões:** Agent Skills ([agentskills.io](https://agentskills.io/specification)) · Agent Plugins 1.0 ([agent-plugins.org](https://agent-plugins.org/))  
**Não usar:** mega-brain-vip como receita. `squads/` como unidade de distribuição.

---

## Três perguntas, três coisas

| | **Skill** | **Plugin** | **Squad** (sentido legado) |
|---|---|---|---|
| Pergunta | Como *este* host começa o trabalho? | Como o valor *viaja* e se instala? | Em que pasta morava “a feature”? |
| Unidade | procedimento invocável | pacote versionado | diretório `squads/{nome}/` |
| Forma | `skills/{id}/SKILL.md` | `plugin.json` + `skills/` + `mcp.json?` | agents + tasks + workflows + skills misturados |
| Quem lê | Claude, Codex, Cursor, OpenClaw, Copilot | instalador / marketplace / `plugins install` | só o nosso monorepo |
| Obrigatório? | sim, se o host for executar | sim, se for distribuir mais que um ficheiro solto | **não** — e não é o formato |

Uma frase:

> **Skill é a porta. Plugin é a caixa. Squad era a gaveta onde metíamos as duas — e o time, e os dados, e o prompt.**

---

## Skill

Uma skill é o contrato que o **runtime** abre. O mercado chama a isto Agent Skill.

```text
skills/review-pr/
├── SKILL.md          # frontmatter name + description; corpo = como
├── scripts/          # determinístico (o modelo não deve gerar)
├── references/       # domínio, só se o corpo pedir
└── assets/
```

Ela responde:

- quando o agente deve abrir isto (`description` — o único texto pago em todo turno);
- o que fazer a seguir (corpo);
- o que é script, não prosa.

Ela **não** responde:

- versão do produto, permissões globais, lista de efeitos, compatibilidade de framework;
- como o pacote se instala noutro computador;
- quem é o time.

Por isso uma skill sozinha pode viver (symlink para `.claude/skills` ou `.agents/skills`). Isso já é produto mínimo. Superpowers, gsd-pi, o installer BMAD e o OpenClaw tratam *isto* como a superfície.

Regra de superfície (mercado e guia AIOX dizem o mesmo):

> Everything enters through a skill; not everything is stored as a skill.

Tasks, templates, rubrics, dados e personas **não** viram skills públicas. Isso explode o catálogo (GSD mediu: 66 skills ≈ 60% do listing).

---

## Plugin

Um plugin é o **pacote**. O mercado chama a isto Agent Plugin 1.0.

```text
review-assistant/
├── plugin.json                 # identidade do pacote (spec pública)
├── skills/
│   └── review-pr/SKILL.md      # uma ou mais portas
├── mcp.json                    # opcional: I/O de tool
├── com.anthropic.claude/       # extra de um host; os outros ignoram
└── com.aiox.enterprise/        # contrato interno nosso; o mercado ignora
```

Ele responde:

- o que se distribui junto (skills + MCP + extras);
- que versão do *pacote* é esta;
- o que o instalador valida sem executar código (`plugin.json`).

Ele **não** é:

- uma skill grande com outro nome;
- um squad zipado;
- a pasta onde moram dados de negócio.

Analogia que o guia AIOX já usa e o mercado aguenta: **capability/produto no rótulo, plugin na caixa, skill na tampa que se abre.** No formato público, o rótulo é o `plugin.json` + a `description` das skills — não um `capability.yaml` que nenhum host valida.

Distribuir ≠ instalar:

- **Distribuir** = o tarball/npm/git leva a caixa inteira.
- **Instalar** = o host põe as skills na superfície dele (`.claude/skills`, `.agents/skills`, loader OpenClaw) e, se houver, sobe o MCP. Não despeja tasks/templates no prompt.

OpenClaw já instala esta caixa (`plugins install` + bundles). Claude marketplace e Codex portal são *outra embalagem do mesmo miolo* (`SKILL.md`), não outro produto.

---

## Por que a confusão é cara

| Confusão | O que acontece |
|---|---|
| Plugin = skill grande | Mudou a pasta, não o contrato. O host ainda vê um `SKILL.md` gordo; versão/permissões continuam implícitas |
| Toda task vira skill | Superfície explode; o modelo escolhe pelo resumo e ignora o corpo |
| Plugin = extensão só do *nosso* runtime | Isolamento. Paperclip/OpenClaw usam “plugin” para *estender o host*; o mercado de agentes usa Agent Plugin para *levar skills* |
| Capability = plugin = skill | Três palavras, uma pasta. Ninguém sabe o que versionar |

No campo `OS/`, “capability” ainda significa **grant** (Paperclip) ou **tipo de registro** (OpenClaw). Não usar essa palavra na boca do operador. Na boca do operador: *skill* (uso) e *plugin* (install).

---

## Por que squad é legado

“Squad” misturou **dois significados** no mesmo diretório `squads/{nome}/`:

1. **Caixa de software** — identidade, versão, comandos, skills, tasks, templates, prompts de Claude e de Codex.
2. **Time multiagente** — papéis, handoff, autor ≠ avaliador.

O primeiro sentido é o que o mercado **não tem** e o que nos isolou. Esse sentido é **legado**.

### O que a gaveta `squads/` fazia de errado

1. **O contrato era a pasta.** Não havia um ficheiro que dissesse o que o produto promete. Versionar era “o commit da árvore”.
2. **Distribuir era clonar o monorepo** (ou um extract frágil). O consumidor não podia levar *uma* capacidade. Agent Plugins existe exactamente para isto.
3. **Claude e Codex eram projeções de um prompt universal** (ou de um gerador). O mercado resolve com *um* `SKILL.md` + extras em `com.*`. Dois targets irmãos públicos são dialecto nosso.
4. **Assets internos viravam superfície.** Tudo que estava no squad parecia porta. O catálogo inchava.
5. **“Squad” queria dizer pacote *e* time.** Volume de ficheiros era tratado como colaboração. 88 pastas não são 88 times — são 88 gavetas (o anti-exemplo mega-brain-vip; não copiar).

BMAD ainda distribui *modules* que são times. Isso é um produto de SDLC editorial, não o formato do mercado de skills. Não é o alvo.

### O que *não* morreu

Papéis load-bearing e composição de time **continuam válidos** quando o trabalho *é* um time:

- autor e avaliador independentes;
- autoridade exclusiva (só devops publica);
- handoff persistido;
- convergência de decisões distintas.

Isso não se chama mais “o squad do produto X” como pasta canónica. Chama-se **composição**, mora *dentro* do plugin (ou no namespace `com.aiox.enterprise/squad/`) e **não é o que se instala**. O operador instala o plugin; o host abre a skill; o time, se existir, é um detalhe de execução.

Teste de uma linha:

> Se apagar a pasta `squads/{nome}` e o valor ainda puder viajar como `plugin.json` + `skills/`, o squad era caixa. Caixa é legado.  
> Se apagar e *perder* a separação autor/avaliador ou uma autoridade exclusiva, havia um time. O time fica — sem ser a unidade de distribuição.

### Por que “legado” e não “proibido”

Porque ainda há árvores `squads/` a migrar. Legado significa:

- **não** criar squad novo como forma de empacotar uma feature;
- **não** publicar `squads/` como o artefato;
- migrar gaveta → plugin + skill (dual-run é *nosso* gate interno, não o formato);
- só preservar composição quando o teste de time passar.

Sunset da pasta é o último passo, não o primeiro. O formato-alvo no dia 1 é skill (porta) + plugin (caixa).

---

## Como cada OS em `OS/` usa as três palavras

Nenhum clone usa o trio do mercado (porta / caixa / composição) de forma limpa. Quase todos **colapsam duas palavras numa pasta** ou usam a mesma palavra para jobs diferentes.

Ler a tabela assim:

- **Skill (deles)** = o que o repo *chama* skill, command, extension command.
- **Porta** = o que o host de facto abre (SKILL.md, slash, comando).
- **Plugin (deles)** = o que o repo *chama* plugin / extension / module / bundle.
- **Caixa** = o que *viaja* e se instala.
- **Time** = se há papéis load-bearing com handoff — independentemente do nome.

Nenhum tem `squads/` no filesystem. “Squad” no campo aparece como *module*, *company*, *party*, *gauntlet*, *subagents*, *crew* — ou não aparece.

### Matriz

| Sujeito | Porta (o que o host abre) | Caixa (o que viaja) | Time / composição | Colapso |
|---|---|---|---|---|
| **superpowers** | 14 `skills/*/SKILL.md` de *processo* | `.claude-plugin/plugin.json` + irmãos `.codex-plugin` / `.cursor-plugin` / `.kimi-plugin` — **mesma caixa, N embalagens** | SDD: implementer ≠ reviewer; sem org | Plugin = envelope do pack de skills. Sem squad-pasta |
| **openclaw** | skills em 6 raízes (workspace > `.agents` > `~/.agents` > state > bundled > plugin) | `openclaw.plugin.json` nativo **ou** bundle Claude/Codex/Cursor/Agent Plugins | sem primitiva de squad | “Capability” = tipo que o plugin *registra* (provider, channel…). Plugin = extensão do **host**, não só caixa de skills |
| **paperclip** | `packages/skills-catalog/` + skills *dentro* de plugins (`plugin-llm-wiki/skills/`) + `requiredSkills` no `TEAM.md` | `packages/plugins/*` — worker + UI + grant; npm | company-sim: CEO/CTO/QA, hire, budget | Plugin ≠ skill (bem separado). Plugin = extensão do **control plane**. Time = empresa, não pasta |
| **BMAD** | skill = **persona** *ou* workflow (`src/{core,bmm}-skills/*/SKILL.md` + `customize.toml`) | **module** npm (`bmad-builder`, TEA, …) + installer → `.claude/skills` e `.agents/skills` | Party Mode / agent-team; o módulo *é* o time | Skill = papel. Module = squad-caixa com outro nome. Mais perto do legado |
| **gstack** | cada pasta raiz é uma skill (`ship/`, `autoplan/`, …) gerada de `SKILL.md.tmpl` | suíte gerada por `hosts/{claude,codex,openclaw,hermes}.ts` — **não** Agent Plugin | gauntlet sequencial (CEO→Design→Eng→DX), não paralelo | Sem plugin de mercado. Um source, N projeções (anti-ADR-157) |
| **gsd-pi** | `gsd-orchestrator/SKILL.md` roteia para `workflows/`; + skills no engine | `extensions/*/extension-manifest.json` (tier, provides) | scout → planner → workers + 3 reviewers | Skill = router. Extension = plugin do *produto GSD*, não Agent Plugin |
| **gsd-2** | catálogo Agent Skills + `npx skills add` | o próprio repo / skills.sh | fábrica worktree (scout/planner/worker) | Porta alinhada ao mercado. Sem caixa Agent Plugin |
| **get-shit-done** | **0** `SKILL.md`; porta = `commands/gsd/*.md` (60+) | install que *vira* skill do host | 33 ficheiros em `agents/gsd-*` (planner, verifier, …) | Command ≈ skill. Agents ≈ papéis de subagente, não squad-pasta |
| **hermes-agent** | ~194 `SKILL.md` em `skills/` + `optional-skills/` | `plugins/{kind}/…/plugin.yaml` (`kind: platform`, memory, image_gen…) | subagents / MoA; sem squad | Plugin = **adapter de runtime** (DingTalk, TTS). Skill = procedimento. Dois mundos no mesmo repo |
| **spec-kit** | 1 `SKILL.md`; porta real = `templates/commands/*.md` + `extensions/*/commands/` | `extension.yml` + `preset.yml` + `bundle.yml` | sem time; pipeline specify→plan→tasks | Extension = caixa de *comandos*, não de skills. Spec é a SoT |
| **gbrain** | ~93 skills de knowledge-ops | `openclaw.plugin.json` (`family: bundle-plugin`) + MCP `gbrain serve` + skillpack | sem squad | Plugin OpenClaw = caixa + context-engine. Skill = porta para o cérebro. Dois repos (brain ≠ agent) |
| **mempalace** | 12 skills de recall/verbatim | `.claude-plugin` + `.codex-plugin` + `.cursor-plugin` + `.antigravity-plugin` (mesmo padrão Superpowers) | sem time | Pack de contexto. Plugin = envelope multi-host |
| **LifeOS** | ~53 skills unpack no install; `CLAUDE.md` é routing | sidecar Hermes `plugin.yaml` (hooks de segredo) | sem squad; identidade = SOUL/TELOS | Skill = biblioteca da vida. Plugin = guarda, não caixa do produto |
| **clawd** | 0 `SKILL.md` | sem plugin | sem squad | Só identidade de workspace (SOUL/USER/MEMORY). Skills moram noutro sítio |
| **AGT** | 1 skill | `.claude-plugin` + exemplos de marketplace `plugin.json` | sem squad; *capability* = IAM | Plugin Claude = envelope de policy. Capability ≠ produto |
| **OpenHands / crewAI / autogen** | 0 `SKILL.md` neste checkout | sem Agent Plugin | crew/conversation/graph — time de *biblioteca*, não de pasta | Fora do formato de mercado. Não copiar como caixa |
| **VISA-BRAIN** (fora de OS/) | `$investigate`, `$counsel` — skill como porta | kit ≠ workspace de caso; sem plugin | skills, não staff | Melhor *recusa* de squad-caixa. Sem caixa de mercado |
| **mega-brain-vip** (fora; **não prática**) | 483 skills + KSL | dump do monorepo | 88 `squads/` = gavetas | Colapso total: skill + plugin + squad + workspace na mesma árvore |

Contagens de `SKILL.md` (sem `node_modules`): superpowers 14 · paperclip 52 · openclaw 115 · BMAD 58 · gstack 59 · gsd-pi 55 · gsd-2 38 · GSD 0 · hermes 194 · spec-kit 1 · gbrain 93 · LifeOS 53 · mempalace 12 · AGT 1.

### Quatro famílias de “plugin” no campo

Não são o mesmo objecto. Usar a palavra sem a família é o isolamento.

| Família | O que a caixa *acrescenta* | Quem | Compatível com Agent Plugins 1.0? |
|---|---|---|---|
| **A. Envelope de skills** | o mesmo `SKILL.md` em N marketplaces | Superpowers, mempalace, AGT | Quase: é `.claude-plugin` / `.codex-plugin`, não ainda `plugin.json` no root da spec 1.0 |
| **B. Extensão do host** | provider, channel, UI, sandbox, grant | OpenClaw, Paperclip, Hermes `kind:` | OpenClaw *consome* 1.0 como bundle; o nativo dele é outro schema. Paperclip/Hermes = outro planeta |
| **C. Módulo de processo / time** | personas + workflows + installer | BMAD module, spec-kit extension/preset | Não. BMAD *emite* skills nativas no install — o módulo não é a caixa pública |
| **D. Suíte gerada** | um source → N hosts | gstack | Não. É o anti-padrão de target gerado |

O alvo de mercado é **A** (caixa = skills + MCP opcional). B é produto de plataforma (não é o que *nós* devemos inventar). C é o squad-legado com outro nome. D não copiar.

### Cinco substitutos de “squad”

Ninguém (excepto o mega-brain) usa a pasta `squads/`. O *job* “vários papéis no trabalho complexo” aparece assim:

| Substituição | Quem | É time de verdade? | É caixa? |
|---|---|---|---|
| Company-sim (empregado + goal + budget) | Paperclip, Clawith | Sim — org persistente | Não; a empresa não se instala como skill |
| Module + party / agent-team | BMAD | Sim — SDLC editorial | Sim — o módulo *é* a unidade de distribuição |
| Fábrica (scout/planner/worker + reviewers) | gsd-pi, gsd-2, GSD `agents/` | Parcial — papéis de pipeline, não cargos | Não |
| Gauntlet sequencial no mesmo humano | gstack `/autoplan` | Não — vozes, não empregados | Não |
| Subagente fresco + reviewer | Superpowers SDD | Sim no teste autor≠avaliador | Não — são skills compostas |

O único que ainda trata o **time como caixa instalável** é BMAD (module). Por isso o guia AIOX pode herdar o *installer* BMAD (materializar `.claude/skills` + `.agents/skills`) e **não** o módulo-como-produto.

### Quem separa bem (e o que copiar da *separação*, não do produto)

| Separação | Quem acerta | Lição |
|---|---|---|
| Skill ≠ plugin | Paperclip (`skills-catalog` vs `packages/plugins`); Hermes (`skills/` vs `plugins/{kind}`) | Dois diretórios, dois jobs. Manter |
| Plugin = envelope, skill = porta | Superpowers, mempalace | Um corpo de skill, N `plugin.json` de host |
| Kit ≠ dados | gbrain (brain repo ≠ agent repo); VISA (kit ≠ caso) | Workspace fora da caixa |
| Time ≠ pasta de feature | Paperclip (company); Superpowers (reviewer é skill, não pasta) | Composição sem `squads/` |
| Superfície pequena | Superpowers (14 skills, rejeita domain no core); GSD (orçamento medido) | Não um SKILL por persona |

| Separação | Quem falha | Porquê |
|---|---|---|
| Skill = persona | BMAD | Catálogo = org-chart. O mercado instala procedimentos, não cargos |
| Plugin = host inteiro | OpenClaw nativo, Paperclip | Correcto *para eles* (são a plataforma). Errado como formato *nosso* de distribuição |
| Command = skill, sem SKILL.md | GSD, spec-kit | Porta existe, mas não é Agent Skills até o install projectar |
| Um source, N SKILL gerados | gstack | Falsa equivalência de hosts |
| Tudo na mesma árvore | mega-brain-vip | Skill + plugin + 88 squads + workspace. Quarentena |

### Leitura por sujeito (o essencial)

**Superpowers.** O produto *é* um conjunto de skills de disciplina. O “plugin” é só como o pack chega ao Claude/Codex/Cursor/Kimi. Time = SDD (implementer / reviewer) via skills compostas, não via pasta. Mais perto do alvo de mercado (família A). Falta o `plugin.json` Agent Plugins 1.0 no root — têm um manifest por host.

**OpenClaw.** Duas camadas: (1) skills que qualquer bundle traz; (2) plugins nativos que *são* o runtime (WhatsApp, providers). Bundles 1.0 já entram. Não criar um OpenClaw nativo nosso; *caber* no bundle.

**Paperclip.** Plugin estende o tabuleiro (UI, worker, sandbox). Skill diz ao empregado o que fazer. Company é o time. Três objectos distintos — e nenhum é Agent Plugin 1.0. Se o AIOX for *plataforma*, estudar Paperclip. Se o AIOX for *pacote que o mercado instala*, Paperclip é o sítio errado para copiar a caixa.

**BMAD.** Skill = Winston / John / o workflow `bmad-help`. Module = o squad-legado oficial do campo. Installer é o único pedaço alinhado (emite portas nativas). Não publicar módulos como se fossem plugins de mercado.

**gstack.** Skill-first até à raiz do repo. Sem caixa padrão. Geração por host. Gauntlet ≠ squad. Útil como playbook; inútil como formato.

**GSD / gsd-2 / gsd-pi.** Porta = comando ou skill-router; estado em `.planning/` / `.gsd/`. “Agents” são tipos de subagente. gsd-2 já fala Agent Skills (`npx skills add`). gsd-pi “extension” é plugin do *engine*, família B.

**Hermes.** Separação limpa skill vs plugin-de-plataforma. 194 skills é o aviso de catálogo. Plugin.yaml `kind: platform` não é Agent Plugin.

**spec-kit.** A SoT é a spec. Extension/preset/bundle carregam *comandos* `speckit.*`. Quase não há SKILL.md. Migrar um squad para “extension spec-kit” continua isolado do mercado de skills.

**gbrain / mempalace / LifeOS / clawd.** Packs de *contexto*, não de processo. gbrain e mempalace já usam envelope multi-host. LifeOS plugin é um hook de segredo. clawd não tem skill — e está certo: identidade ≠ porta.

**VISA.** Skill é porta; workspace é o caso; sem plugin de mercado (de propósito). Não é o formato a publicar para o mundo; é a recusa correcta de squad-caixa em domínio de prova.

---

## Quadro de decisão

| Situação | O que é | O que criar |
|---|---|---|
| Um procedimento que o host deve saber abrir | skill | `skills/{id}/SKILL.md` |
| Esse procedimento + scripts + talvez MCP, para outra máquina | plugin | Agent Plugin 1.0 |
| Muitas tasks/templates, um executor | plugin asset-heavy; **uma** skill pública | não squad |
| Dois papéis com autoridade distinta e handoff real | composição *dentro* do plugin | não `squads/{nome}` como caixa |
| Dados do operador / BU / caso | workspace, fora do pacote | nunca no plugin nem no squad |
| “Vamos fazer um squad para esta feature” | reflexo legado | perguntar: qual é a skill? qual é a caixa? |

---

## Anti-padrões (nomear e recusar)

| Não | Porquê |
|---|---|
| Renomear `squads/foo` para `plugins/foo` sem `plugin.json` + `skills/` | mudança de pasta, não de modelo |
| Um `SKILL.md` por persona do antigo squad | catálogo = org-chart; o mercado não instala isto |
| Dois `SKILL.md` públicos (Claude vs Codex) como contrato | dialecto; extra vai em `com.*` |
| Plugin sem skill | caixa sem tampa — o host não entra |
| Skill que é o zip do squad (tudo no corpo) | porta entupida |
| Criar squad “porque tem muitos ficheiros” | volume ≠ time |
| Usar mega-brain / 88 squads como padrão | Frankenstein; quarentena de prática |

---

## O que o campo autoriza (e o que não)

Do filesystem, não da doutrina:

1. **A porta que o mercado já abre é `SKILL.md`.** Quem ainda vive em `commands/*.md` (GSD, spec-kit) projecta isso no install. Não inventar uma terceira porta.
2. **A caixa pública é um envelope de skills (família A),** eventualmente Agent Plugins 1.0. Superpowers/mempalace já fazem o miolo; falta o manifest único da spec.
3. **Plugin de host (família B) é trabalho de plataforma.** OpenClaw, Paperclip, Hermes. Só fazer se formos a plataforma — não para distribuir uma capacidade.
4. **Module/extension de processo (família C) é o squad-legado com outro nome.** BMAD e spec-kit. Não é o artefato.
5. **Ninguém precisa de `squads/` para ter time.** Paperclip tem empresa, Superpowers tem reviewer, GSD tem factory. A pasta é o que o mega-brain hipertrofiou.

---

## Relação com os outros memos

- Empacotar no mercado: `_bench/_research/market-compatible-packaging.md`
- Ninguém em OS/ faz Capability-First: `_bench/_research/capability-first-vs-os.md`
- Quatro camadas de skill (catálogo → corpo → refs → scripts): `_bench/_research/skills-squads-plugins.md`
- Guia interno AIOX (doutrina; piloto não-aprovado): `AIOX-enterprise/docs/architecture/capability-first-and-plugins.md`

Se as três palavras colidirem num doc ou num ADR, este ficheiro vence para o sentido *público*. Capability.yaml e dual-run continuam vocabulário interno, no namespace `com.aiox.enterprise/`.
