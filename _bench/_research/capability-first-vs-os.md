# Capability-First × o que os clones de OS/ realmente fazem

**Date:** 2026-08-12  
**Referência:** `AIOX-enterprise/docs/architecture/capability-first-and-plugins.md` (guia canônico de leitura; Constituição / ADR-155 / ADR-157)  
**Escopo:** clones em `OS/` + kits externos já mapeados (VISA-BRAIN, mega-brain-vip)  
**Método:** paths reais. Sem score inventado. Sem usar mega-brain-vip como receita.  
**Estado do piloto AIOX:** Code Anatomist é exemplo de *forma física*; migração **não** está aprovada (QG dual-run/cutover aberto). Este memo compara o **modelo do guia**, não um sunset concluído.

---

## Veredito em uma página

**Ninguém em `OS/` está fazendo Capability-First.**

Existe plugin, existe skill, existe squad, existe “capability” — mas as palavras **não nomeiam as mesmas coisas**. O guia AIOX separa seis conceitos; o campo colapsa dois ou três deles, ou usa *capability* para permissão / tipo de registro.

| Conceito AIOX | Existe em OS/? | Quem chega mais perto | O que falta |
|---|---|---|---|
| **Capability** = contrato de produto (`capability.yaml`: purpose, I/O, effects, permissions, compat) | Não | — | Nenhum clone tem esse arquivo como SOT |
| **Plugin** = caixa versionada da capability | Parcial | OpenClaw, Paperclip, BMAD *modules* | Pacote existe; o contrato de *produto* não |
| **Skill** = porta nativa do host (`targets/{runtime}/SKILL.md`) | Parcial | BMAD install → `.claude/skills` + `.agents/skills`; Superpowers / gstack por host | Autoria **nativa** por runtime; AIOX proíbe gerar Claude a partir de Codex |
| **Agent** = papel load-bearing | Sim | BMAD, Paperclip, Superpowers reviewer | Campo cria persona demais (anti-padrão que o guia nomeia) |
| **Squad** = composição *opcional* | Invertido | BMAD modules, mega-brain 88 squads, Paperclip company | Squad ainda é o *contêiner* |
| **Workspace** = dados fora do plugin | Parcial | Paperclip `project_workspaces`; gbrain two-repo; VISA kit≠caso | Sem Workspace Bus (consumir path/schema, não identidade do produtor) |
| **Distribuição ≠ instalação** | Parcial | OpenClaw (pacote inteiro vs map de features); BMAD (módulo npm vs materializar skill); Paperclip (npm vs worker) | Ninguém instala *só* o target e deixa assets no pacote com integridade SHA |
| **Dual-run / cutover / rollback / sunset** | Quase não | Lição *negativa* gsd dual-write (`brain-6way`); Superpowers porting | Zero dual-run de *squad legado × plugin candidato* |

A frase do guia que o campo ainda não implementa:

> Skill é a porta, capability é o contrato do produto, plugin é o pacote e squad só existe quando o trabalho exige um time.

O que o campo implementou, na prática: **skill é o produto, plugin é extensão do host, squad é a pasta, capability é permissão ou tipo de API.**

---

## Três sentidos da palavra “capability” (não misturar)

| Sentido | Onde | O que responde |
|---|---|---|
| **Contrato de produto** | guia AIOX `capability.yaml` | O que o produto promete, I/O, efeitos, permissões, compat |
| **Permissão / grant** | Paperclip `PLUGIN_SPEC.md` §5.7; AGT (narrowing) | O que o *plugin/agente pode chamar* no host |
| **Tipo de registro** | OpenClaw `docs/plugins/architecture.md` “Public capability model” | Provider, channel, speech, search… que o plugin *registra* |

Os três são honestos no seu domínio. Tratar o grant do Paperclip ou o `registerProvider` do OpenClaw como se fossem `capability.yaml` é falso cognato. O `capability-registry.yaml` do mega-brain (capability → tool) é o sentido *grant/mediação* — e o kit está em **quarentena de prática**.

---

## O modelo AIOX (o que estamos procurando)

Fonte: `AIOX-enterprise/docs/architecture/capability-first-and-plugins.md`.

1. Squad-First misturava identidade, versão, comandos, agents, tasks e prompts em `squads/{nome}/`.
2. Capability-First: contrato em `plugins/{id}/capability.yaml`; targets nativos em `targets/claude/SKILL.md` e `targets/codex/SKILL.md`; instalador copia **byte a byte** para `.claude/skills/` e `.agents/skills/`; assets ficam no pacote; workspace fica fora.
3. “Everything enters through a skill; not everything is stored as a skill.”
4. Squad só quando há time real (autor≠avaliador, autoridade exclusiva, handoff persistido).
5. Migração: classificar → baseline → contrato → assets rastreados → targets nativos → **dual-run real** (dois caminhos executáveis, não dois labels) → gate de cutover + owner → sunset.
6. Anti-padrões nomeados: plugin = skill grande; manifesto decorativo; um prompt universal; toda task vira skill; toda persona vira agent; sunset antes do gate; recursos externos implícitos; outputs/segredos no plugin.

Code Anatomist (`AIOX-enterprise/plugins/code-anatomist/`) ilustra a árvore. O próprio guia diz: **não usar como evidência de sunset**. QG de dual-run/cutover aberto.

---

## O que cada clone faz (e o que não faz)

### OpenClaw — plugin de runtime mais rico; capability ≠ contrato

Paths: `OS/openclaw/docs/tools/plugin.md`, `docs/plugins/manifest.md`, `docs/plugins/bundles.md`, `docs/plugins/architecture.md`.

- Pacote instalável (ClawHub / npm / git / path) com `openclaw.plugin.json` validado **antes** de executar código.
- **Capability** = tipo que o plugin registra (`registerProvider`, `registerChannel`, …). Shape `plain-capability` / `hybrid-capability`.
- Bundles Claude / Codex / Cursor / Agent Plugins são **mapeados** para skills/hooks/MCP — não são `targets/{runtime}/` autorados como contrato do *mesmo* produto.
- Distribuição do pacote ≠ enable no Gateway. Rollback = uninstall + restart, não cutover de squad.
- Sem `capability.yaml` de I/O/effects. Sem squad. Sem workspace L0–L4.

Chega perto de **plugin como caixa**. Não chega em **capability como produto**.

### Paperclip — plugin de host; capability = grant

Paths: `OS/paperclip/doc/plugins/PLUGIN_SPEC.md`, `PLUGIN_AUTHORING_GUIDE.md`.

- Plugin instance-wide, worker out-of-process, UI em slot, `apiRoutes` namespaced.
- §5.7: *“A named permission the host grants to a plugin.”*
- Skills vivem noutro sítio (`packages/skills-catalog/`, `requiredSkills` no TEAM.md).
- Workspace = `project_workspaces` (job 1 do company-brain), não Workspace Bus.
- Spec completa é target pós-V1; o guia de authoring admite a superfície alpha.
- Adapters Claude/Codex/… orquestram *agentes*, não instaladores de `targets/*/SKILL.md`.

Chega perto de **plugin ≠ skill** e de **workspace fora**. Não chega em contrato de produto nem targets nativos.

### BMAD — o vizinho mais próximo na *instalação* de skills

Paths: `OS/BMAD-METHOD/tools/docs/native-skills-migration-checklist.md`, `src/core-skills/module.yaml`, `docs/reference/modules.md`, `tools/installer/`.

- Módulo npm (`bmad-builder`, CIS, GDS, TEA) = unidade de **distribuição**.
- Installer materializa skills nativas: Claude → `.claude/skills`; Codex → `.agents/skills` (checklist `refactor/all-is-skills`, itens Claude/Codex marcados).
- Agent = persona load-bearing (architect, PM, QA) — alinhado ao guia.
- Por dentro continua **module/squad-first**: `module.yaml` é config de install, não contrato de I/O/effects.
- Sem dual-run de legado×candidato. Sem `capability.yaml`. Sem “squad só se houver time” — o módulo *é* o time.

Chega perto de **distribuição ≠ superfície do host** e de **targets Claude/Codex**. Ainda é Squad/Module-First com um instalador bom.

### gstack — um source, N hosts *gerados* (o anti-padrão ADR-157)

Path: `OS/gstack/hosts/claude.ts` (e `codex.ts`, `openclaw.ts`, `hermes.ts`).

- Um SKILL.md.tmpl → install gerado por host (`.claude/skills/gstack` vs paths Codex).
- O guia AIOX / ADR-157: *não* traduzir Claude↔Codex; igualdade só se registrada. gstack **gera**. É o inverso consciente: um source, N projeções.

Útil como contraste. Não é Capability-First.

### Superpowers — um corpo, N embalagens

Paths: `OS/superpowers/README.md`, `RELEASE-NOTES.md` (`package-codex-plugin.sh`, `.codex-plugin/plugin.json`).

- Skill-first de processo. Plugin Claude (`.claude-plugin/plugin.json`) e portal Codex separado.
- Mesmo procedimento, embalagem por host. Codex hoje: native discovery em `~/.agents/skills/superpowers/`, sem SessionStart.
- Sem contrato de produto. Sem squad (pipeline de skills + reviewer, não org). Sem dual-run de migração de pasta.

### Hermes, spec-kit, gsd-pi

- Hermes: `plugin.yaml` por *kind* (memory / providers / platforms). Escada “não ponha tool no core”. Capability no sentido de extensão de runtime.
- spec-kit: `extension.yml` + gates. Spec é SoT, não capability.
- gsd-pi / gsd-2: catálogo + `npx skills add` + `.agents/skills/`. Porta Codex-friendly. Sem plugin-contrato.

### VISA-BRAIN (kit externo)

Skill é a porta (`$investigate`, `$counsel`). Workspace de caso ≠ kit de produto. Sem plugin, sem `capability.yaml`, sem multi-runtime targets. Está mais perto da *frase* “entra pela skill” do que qualquer clone — e recusa o resto de propósito.

### mega-brain-vip (kit externo) — **não consultar como prática**

88 squads, `capability-registry.yaml` (grant → tool), KSL + SINKRA + AIOX no mesmo corpo. Diagnóstico: Frankenstein declarado (`_bench/_research/mega-brain-vip-vs-company-brain.md`). **Quarentena.** Não entra na coluna “quem chega perto”.

---

## Matriz compacta

| Sujeito | Contrato de produto | Plugin caixa | Target nativo Claude/Codex | Squad opcional | Dist ≠ install | Dual-run/cutover |
|---|---|---|---|---|---|---|
| **AIOX guia** | `capability.yaml` | `plugins/{id}/` | autorado, byte-a-byte | sim, critério de time | sim | exigido; piloto ainda aberto |
| OpenClaw | não (tipo de registro) | sim | bundles mapeados, não targets irmãos | n/a | sim | uninstall, não cutover |
| Paperclip | não (grant) | sim (alpha) | adapters de agente | company = outro job | sim (npm vs worker) | não |
| BMAD | não (`module.yaml`) | módulo npm | install nativo nas duas superfícies | não — módulo *é* o time | sim | migrate checklist, sem dual-run |
| gstack | não | suíte gerada | **gerado** (anti-ADR-157) | gauntlet, não squad | sim | não |
| Superpowers | não | plugin por host | mesmo corpo, outra caixa | não | parcial | não |
| Hermes / spec-kit / gsd-pi | não | kind / extension / catálogo | superfície do host | não / fábrica | parcial | gsd dual-write = anti-padrão |
| VISA-BRAIN | epistemologia A/B/C, não capability | não | não | skills, não staff | kit ≠ caso | extract/P3, outro job |
| mega-brain-vip | registry de tools | dump | não | 88, obrigatório de fato | doutrina L3 vs dump | WARN, não cutover |

---

## O que o guia AIOX tem e o campo ainda não

1. **Uma SOT de contrato** que não é o `SKILL.md` nem o `squad.yaml`.
2. **Targets irmãos autorados**, com equivalência *registrada* quando for idêntica — não um gerador, não um mapeador de bundle.
3. **Instalador que não traduz** e não despeja a árvore na superfície do host.
4. **Critério positivo para *não* criar squad** (volume de files ≠ colaboração).
5. **Dual-run real + gate de owner** antes de apagar o legado. O único “cutover” documentado em OS/ é o anti-padrão gsd dual-write (`_bench/brain-6way`).

Peças reutilizáveis *do campo* (não do mega-brain), se o AIOX for fechar o piloto:

| Peça | De quem | Para quê no AIOX |
|---|---|---|
| Manifest validado antes de executar código | OpenClaw `openclaw.plugin.json` | evitar `capability.yaml` decorativo |
| Installer que materializa `.claude/skills` *e* `.agents/skills` | BMAD checklist nativo | já é o passo 6 do ciclo AIOX |
| Plugin ≠ skill catalog | Paperclip | não deixar `requiredSkills` redefinir o contrato |
| “Everything is a skill” só na superfície | Superpowers + GSD budget | o guia já diz; o campo confirma o custo |
| Recusa de dual-SoT sem cutover | gsd lessons / VISA projection | o gate que o QG do Code Anatomist ainda cobra |

---

## Conclusão

Capability-First, no sentido do guia AIOX, **ainda é um modelo de um produto** — e o próprio produto marca o piloto como não-aprovado. Os clones de `OS/` resolvem fatias adjacentes (plugin de host, grant, bundle, install multi-IDE, skill-first) sem jamais juntar contrato + caixa + porta nativa + squad opcional + dual-run.

Não há atalho: copiar o plugin do OpenClaw ou o installer do BMAD **não** produz Capability-First. Copiar o mega-brain **piora** — é Squad-First em escala Frankenstein.

Enquanto o dual-run real e o gate de cutover/owner do Code Anatomist estiverem abertos, o guia continua doutrina; o filesystem AIOX ainda não é evidência de sunset. O campo OS/ não fecha esse gap por vocês.

Para **não isolar** o produto num formato só AIOX, a caixa pública é Agent Skills + Agent Plugins 1.0 — ver `_bench/_research/market-compatible-packaging.md`. Capability.yaml / dual-run / squad ficam no namespace `com.aiox.enterprise/`.

---

## Fontes

Guia: `AIOX-enterprise/docs/architecture/capability-first-and-plugins.md` (e, por citação dele, Constituição Art. XI, ADR-155, ADR-157, `plugins/code-anatomist/`, `dual-run-precedence-exit.md`).

OS/: `openclaw/docs/{tools/plugin.md,plugins/manifest.md,plugins/bundles.md,plugins/architecture.md}`; `paperclip/doc/plugins/{PLUGIN_SPEC.md,PLUGIN_AUTHORING_GUIDE.md}`; `BMAD-METHOD/{tools/docs/native-skills-migration-checklist.md,src/core-skills/module.yaml,docs/reference/modules.md}`; `gstack/hosts/claude.ts`; `superpowers/{README.md,RELEASE-NOTES.md}`; `_bench/_research/{skills-squads-plugins.md,company-brain.md,mega-brain-vip-vs-company-brain.md}`; `_bench/brain-6way` (dual-write cutover).
