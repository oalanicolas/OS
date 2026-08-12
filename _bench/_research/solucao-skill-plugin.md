# Solução: o que construir

**Date:** 2026-08-12  
**Decisão.** Não é mais um mapa — é o alvo.

---

## A solução em quatro linhas

1. **Skill** = porta Agent Skills (`skills/{id}/SKILL.md`). É o que Claude, Codex, Cursor e OpenClaw já abrem.
2. **Plugin** = caixa Agent Plugins 1.0 (`plugin.json` + `skills/` + `mcp.json` se houver I/O). É o que se instala.
3. **Squad-como-pasta** = legado. Não criar, não publicar. Time de verdade (autor≠avaliador, autoridade exclusiva) vira *composição dentro do plugin*, se o teste de time passar.
4. **Capability.yaml, dual-run, L0–L4, ontologia** = governança AIOX em `com.aiox.enterprise/`. Hosts de mercado ignoram. Nenhum install depende disso.

Uma frase:

> Publicamos um Agent Plugin cujo miolo são Agent Skills. Não publicamos squads, não publicamos `capability.yaml` como formato, não publicamos o mega-brain.

---

## O que *não* é a solução

| Tentação | Porquê recusar |
|---|---|
| Capability-First como formato público (`plugins/{id}/capability.yaml` + dois targets) | Zero hosts validam. Isola |
| Squad-First / 88 gavetas | Frankenstein. Quarentena |
| Plugin estilo OpenClaw/Paperclip (estender o *host*) | Isso é ser plataforma, não distribuir uma capacidade |
| Module BMAD / extension spec-kit como artefato | Squad-legado com outro nome |
| Gerar Claude a partir de Codex (gstack) | Falsa equivalência |
| Esperar dual-run/sunset do Code Anatomist para ter algo instalável | Dual-run governa *migração interna*. A caixa de mercado não depende dele |
| Quarto marketplace AIOX | Claude / ClawHub / `npx skills add` / `openclaw plugins install` já existem |

---

## Forma física do artefato

```text
{id}/
├── plugin.json                 # Agent Plugins 1.0
├── README.md
├── skills/
│   └── {porta}/
│       ├── SKILL.md            # name + description; corpo = como
│       ├── scripts/
│       └── references/
├── mcp.json                    # só se houver tool I/O
├── com.anthropic.claude/       # extra opcional
├── com.openai.codex/           # extra opcional
└── com.aiox.enterprise/        # interno; o mercado não lê
    ├── capability.yaml
    └── dual-run/               # se houver migração de squad
```

Aceite: `openclaw plugins install ./the-plugin` **ou** symlink de `skills/{porta}` para `.claude/skills` e `.agents/skills` funciona **sem** CLI AIOX no PATH.

---

## Primeiro passo (um plugin, não um framework)

Um pacote **mínimo**: uma skill, zero MCP, zero squad, zero persona.

Prova em três hosts no mesmo tarball. Só depois: MCP, extras `com.*`, contrato interno, migração de uma gaveta `squads/` com dual-run *nosso*.

Não começar pelo Code Anatomist nem por um “kit completo”.

---

## De quem copiar a *separação* (não o produto)

| Copiar | De quem | Não copiar |
|---|---|---|
| Um `SKILL.md`, N envelopes de host | Superpowers, mempalace | o processo SDD inteiro, salvo se for o job |
| Skill ≠ plugin no disco | Paperclip, Hermes | o plugin-de-host / company-sim |
| Kit ≠ dados | gbrain, VISA | o cérebro/caso como caixa |
| Installer que *emite* `.claude/skills` + `.agents/skills` | BMAD | o module como produto |
| Superfície pequena | Superpowers (14 skills; domain fora do core) | 194 skills Hermes / 483 mega-brain |

---

## Fontes da decisão

`_bench/_research/plugin-vs-skill-vs-squad.md` · `market-compatible-packaging.md` · `capability-first-vs-os.md` · `mega-brain-vip-vs-company-brain.md` (anti-exemplo).
