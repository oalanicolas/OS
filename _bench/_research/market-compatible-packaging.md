# Empacotar no mercado, não num formato só nosso

**Date:** 2026-08-12  
**Pedido:** criar algo compatível com o mercado, não isolado no vocabulário AIOX  
**Lê junto:** `_bench/_research/plugin-vs-skill-vs-squad.md` (definições) · `_bench/_research/capability-first-vs-os.md`  
**Não usar:** mega-brain-vip como receita

---

## Veredito

A unidade pública **já existe**. Não inventar `capability.yaml` / `targets/claude` / `squads/` como o que o mundo instala.

| Camada | Padrão de mercado (2026) | O que o host lê |
|---|---|---|
| Porta | **Agent Skills** — `skills/{id}/SKILL.md` ([agentskills.io](https://agentskills.io/specification)) | Claude, Codex (`~/.agents/skills` / `.agents/skills`), Cursor, Copilot, OpenClaw, BMAD installer, gsd-pi |
| Caixa | **Agent Plugins 1.0** — `plugin.json` + `skills/` + `mcp.json` opcional ([agent-plugins.org](https://agent-plugins.org/)) | OpenClaw já mapeia; TSC: Amazon, Cursor, Microsoft, OpenAI, Vercel (ago/2026) |
| I/O determinístico | **MCP** — `mcp.json` no mesmo pacote | o que não é procedimento |
| Extra de um host | namespace `com.{vendor}.{product}/` | quem não conhece **ignora** |

Capability-First continua válido **por dentro** (contrato, permissões, dual-run, squad opcional). Por fora, isso não pode ser o formato. Se o pacote só abre com `npm run capability:validate` e um instalador AIOX, está isolado.

A frase compatível:

> O mercado instala um **Agent Plugin** que contém **Agent Skills** (e MCP se houver I/O). Squad, capability.yaml e dual-run são governança nossa, no namespace `com.aiox.enterprise/`, invisíveis para quem não somos nós.

---

## O que o mercado *não* vai adotar

Isto é o que o guia AIOX trata como arquitetura-alvo — e o que os clones recusam ou nomeiam diferente:

| Peça só nossa | Por que isola |
|---|---|
| `plugins/{id}/capability.yaml` como SOT pública | Zero hosts validam esse schema. Paperclip/OpenClaw usam “capability” para *grant* ou *tipo de registro* |
| `targets/claude/SKILL.md` + `targets/codex/SKILL.md` como irmãos públicos | O padrão é **um** `SKILL.md` Agent Skills. Extra de host vai no namespace, não em dois contratos |
| Gerar Claude a partir de Codex (gstack) | Falsa equivalência — certo recusar; a resposta de mercado não é dois targets, é um core portátil + extras |
| `squads/` como unidade de distribuição | BMAD ainda faz module-first; o resto do mercado não. Squad = composição interna |
| Instalador que só o AIOX entende | Claude marketplace, ClawHub, `npx skills add`, `openclaw plugins install`, BMAD `npx bmad-method install` já existem |

O piloto Code Anatomist (QG aberto) **não** deve ser o artefato que vocês publicam. Publicar a árvore Capability-First como se fosse o produto é exatamente o isolamento.

---

## O que criar (formato, não produto novo)

Um **perfil de empacotamento** — um plugin de referência que qualquer cliente Agent Plugins / Agent Skills carrega, e o AIOX ainda consegue governar.

```text
{plugin-id}/
├── plugin.json                 # Agent Plugins 1.0 (obrigatório)
├── README.md
├── skills/
│   └── {skill-id}/
│       ├── SKILL.md            # Agent Skills (name + description no frontmatter)
│       ├── scripts/            # determinístico
│       ├── references/         # on-demand
│       └── assets/
├── mcp.json                    # só se houver tool I/O
├── com.anthropic.claude/       # opcional: hooks, .claude-plugin extras
├── com.openai.codex/           # opcional: .codex-plugin extras
└── com.aiox.enterprise/        # SÓ NOSSO — hosts de mercado ignoram
    ├── capability.yaml         # contrato interno (I/O, effects, owner)
    ├── dual-run/               # evidência; não é runtime
    └── squad/                  # só se houver time real
```

`plugin.json` mínimo (o piso da spec, não um schema AIOX):

```json
{
  "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
  "name": "example-capability"
}
```

Regras:

1. **O que viaja para o operador** é `plugin.json` + `skills/` (+ `mcp.json` se precisar). Sem isso, não é produto.
2. **`SKILL.md` é a porta.** Description = quando abrir. Corpo = como. Scripts fazem o determinístico. Não despejar tasks/templates como skills públicas.
3. **Um skill portátil, não dois targets.** Se Claude ou Codex precisarem de hook/manifest próprio, isso vive em `com.anthropic.claude/` / `com.openai.codex/`. O core não é traduzido.
4. **`com.aiox.enterprise/capability.yaml` é interno.** Pode validar CI AIOX, permissões, owner, dual-run. Um `openclaw plugins install` ou um `npx skills add` **não** depende dele.
5. **Squad não embarca** a menos que o plugin realmente tenha autor≠avaliador / autoridade exclusiva / handoff. Volume de ficheiros ≠ time.
6. **Workspace fica fora do pacote.** Outputs, credenciais, BUs, casos — nunca dentro do plugin. Isso o mercado e o vosso guia já concordam.
7. **Instalar = o que o host já faz.** Não exigir o CLI AIOX para um dev no Codex ou no OpenClaw usar a skill.

---

## Como isso mapeia o guia sem o isolar

| Guia AIOX | Superfície de mercado | Fica interno |
|---|---|---|
| Capability (contrato) | `plugin.json` `name` + `SKILL.md` description | `com.aiox.enterprise/capability.yaml` |
| Plugin (caixa) | diretório Agent Plugin 1.0 | — |
| Skill (porta) | `skills/{id}/` Agent Skills | extras em `com.*.*/` |
| Agent load-bearing | persona só se o host tiver agents; senão é texto no SKILL | `agents/` no namespace AIOX |
| Squad opcional | não viaja | `com.aiox.enterprise/squad/` |
| Workspace | fora; o SKILL aponta paths do operador | L0–L4 no repo do cliente |
| Dist ≠ install | o host instala o pacote e carrega `skills/` / MCP; não copia a árvore toda para o prompt | checksum/CI AIOX |
| Dual-run / cutover | sem equivalente público — e não precisa | pasta `dual-run/` + QG vosso |

“Everything enters through a skill; not everything is stored as a skill” **já é a doutrina do mercado** (Agent Skills + progressive disclosure). Não é uma invenção AIOX. Podem repetir essa frase em público.

ADR-157 (não sincronizar/gerar um host a partir do outro) **mantém-se** como regra de qualidade dos extras. Não justifica dois `SKILL.md` públicos.

---

## Canais de distribuição (usar os que existem)

Ordem de alcance, não de orgulho:

1. **Pasta Agent Skills** — o menor artefato; funciona com symlink/`npx skills add`/`.agents/skills`.
2. **Agent Plugin 1.0** (git, tarball, npm) — OpenClaw `plugins install`; qualquer cliente que implemente a spec.
3. **Claude marketplace / `.claude-plugin`** — só o que for extra Claude, no namespace.
4. **Codex plugin portal** — idem, namespace Codex (Superpowers já faz essa embalagem sem mudar o corpo da skill).
5. **BMAD module** — só se o público for quem já instala BMAD; o módulo deve *conter* skills nativas, não substituí-las.

Não criar um quarto marketplace AIOX até os três primeiros carregarem o mesmo pacote sem patch.

---

## O que *não* criar agora

- Um “padrão AIOX de plugins” concorrente do Agent Plugins.
- Instalador único que reescreve SKILL para cada host (gstack).
- Publicar Code Anatomist / árvore `plugins/{id}/targets/...` como o formato.
- Tirar lição de empacotamento do mega-brain-vip.
- Esperar o sunset do dual-run para ter um artefato instalável. O artefato de mercado **não depende** do dual-run. O dual-run governa a *migração interna* squad→plugin.

---

## Primeiro artefato concreto (quando disserem GO)

Um plugin **mínimo** (uma skill, zero MCP, zero squad) no layout acima, instalável por:

- `openclaw plugins install ./the-plugin` (ou o path que o host aceitar)
- copiar/symlink `skills/{id}` → `.claude/skills/{id}` e `.agents/skills/{id}`

Aceite: Claude e Codex descobrem a skill **sem** código AIOX no PATH. O `capability.yaml` no namespace pode existir no mesmo commit e ser ignorado pelos dois.

Isso prova compatibilidade. O resto (MCP, extras de host, contrato interno, dual-run) acrescenta-se depois, sem mudar a caixa.

---

## Fontes

Mercado: [agentskills.io/specification](https://agentskills.io/specification); [agent-plugins.org](https://agent-plugins.org/) (v1.0.0, ago/2026); MCP spec.

OS/: `openclaw/docs/plugins/bundles.md` (mapeia Agent Plugins + Claude + Codex + Cursor); `BMAD-METHOD/tools/docs/native-skills-migration-checklist.md`; `superpowers/RELEASE-NOTES.md` (portal Codex, mesmo corpo); `gstack/hosts/*.ts` (anti-padrão a não copiar); `paperclip/doc/plugins/PLUGIN_SPEC.md` (capability = grant).

Casa: `AIOX-enterprise/docs/architecture/capability-first-and-plugins.md` (doutrina interna; piloto não-aprovado). `_bench/_research/capability-first-vs-os.md`.
