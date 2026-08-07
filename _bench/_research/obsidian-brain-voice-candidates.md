# Candidatos: cérebro OSS + Obsidian + voz + criador de conteúdo

**Status:** ✅ **RESOLVIDO** — o alvo era **LifeOS** (`danielmiessler/LifeOS`)  
**Date:** 2026-08-06 (parking) · **Resolved:** 2026-08-06  
**Context:** busca por “opensource de cérebro de um americano com blog, modo de voz, usa Obsidian, canal YouTube, cria muito conteúdo”.  
**Descartes explícitos:** OpenClaw (Peter Steinberger / steipete.me), GBrain (Garry Tan), Khoj + shortlist abaixo (Cole, SystemSculpt, Note Companion…).

---

## ✅ Confirmado pelo Alan: LifeOS (Daniel Miessler)

| Campo | Valor |
|-------|--------|
| **Repo** | https://github.com/danielmiessler/LifeOS |
| **Site** | https://ourlifeos.ai · docs: https://docs.ourlifeos.ai |
| **Autor** | **Daniel Miessler** (americano) |
| **Blog** | https://danielmiessler.com |
| **X** | [@danielmiessler](https://twitter.com/danielmiessler) |
| **Walkthrough** | https://youtu.be/Le0DLrn7ta0 |
| **Nome anterior** | PAI — Personal AI Infrastructure (renomeado LifeOS ~v6) |
| **Licença** | MIT |
| **Stack** | TypeScript + Bun; harness-agnostic (principal path: Claude Code); skills, hooks, Algorithm, Pulse |
| **Voz** | **Pulse** daemon (voz, hooks, cron, dashboard); DA interview escolhe voice; TTS (ex. Google Cloud TTS community); roadmap outbound phone |
| **Memória** | **Cortex** — hot-layer memory + Knowledge Archive (People, Companies, Ideas, Research) |
| **Obsidian** | não é “plugin Obsidian”; knowledge/wiki layer + vault markdown; comunidade combina com Obsidian |
| **Install** | Prompt: `Read https://ourlifeos.ai/install and install LifeOS for me.` · ou `curl -fsSL https://ourlifeos.ai/install.sh \| bash` |
| **Relacionado** | Fabric (prompts/patterns) — https://github.com/danielmiessler/fabric |

### Por que batia o brief

- Americano com **blog massivo** (danielmiessler.com) + conteúdo contínuo  
- **LifeOS / “Life Operating System”** no GitHub (“git LifeOS”)  
- **Modo de voz** first-class no Pulse / DA  
- Cérebro persistente (Cortex, TELOS, Ideal State), não só chat  
- Open source MIT  

### Relação com nossos benches

| Bench | Nota |
|-------|------|
| memory-5way | LifeOS compete no eixo **personal OS / agent memory**, não 1:1 com mempalace/mem0 |
| personal-assistant-3way | mais próximo de openclaw/hermes+gbrain como *harness + brain* |
| parking shortlist | manteve valor histórico; não era o alvo |

**Próximo passo opcional:** clonar em `OS/LifeOS` (ou path do manifesto) + inventário os-bench / comparar com gbrain no pack personal-assistant ou memory.

**Feito 2026-08-06:** comparação n-way em `OS/_bench/brain-6way/` (LifeOS + gbrain + mempalace + mem0 + memori-labs + gsd-2).

---

## Shortlist histórica (não era o alvo — manter para referência)

---

## Por que esta lista

Foram os matches mais próximos **depois** dos descartes. Nenhum foi reconhecido. Servem como shortlist para:

1. Conferir depois se algum era o alvo  
2. Eventual inventário / bench `memory` ou `personal-assistant` se valer absorver  
3. Não perder o rastro da conversa de 2026-08-06

---

## Shortlist (salvar / revisitar)

### 1. Cole Medin — second brain + Claude Code + Obsidian

| Campo | Valor |
|-------|--------|
| Canal | https://www.youtube.com/@ColeMedin |
| OSS | https://github.com/coleam00/second-brain-starter |
| Relacionado | `coleam00/second-brain-skills` |
| Comunidade | https://dynamous.ai |
| Stack | Claude Code + markdown memory + Obsidian vault |
| Voz | fraca como feature nativa; stack costuma usar dictation externa |
| Por que listar | volume alto de conteúdo; OSS explícito de “AI second brain”; Obsidian no centro |
| Quando re-checar | se a memória for “cara gringo de AI agents / Claude Code / Dynamous” |

### 2. SystemSculpt (Mike) — plugin Obsidian AI + voz

| Campo | Valor |
|-------|--------|
| Canal | https://www.youtube.com/@SystemSculpt (ou SystemSculpt) |
| Site / blog | https://systemsculpt.com/blog |
| OSS / plugin | https://github.com/systemsculpt/obsidian-systemsculpt-ai |
| Stack | Obsidian plugin: chat, semantic search, transcription, workflows |
| Voz | **forte** — voice query, TTS, audio/YouTube transcription |
| Licença | freemium / license activation (não MIT “puro”) |
| Por que listar | melhor match em **voz dentro do Obsidian** + YouTube + blog |
| Quando re-checar | se a memória for “plugin no Obsidian com microfone / TTS e canal diário” |

### 3. Note Companion (ex File Organizer 2000)

| Campo | Valor |
|-------|--------|
| Canal | https://www.youtube.com/@note-companion |
| Site | https://www.notecompanion.ai |
| OSS | https://github.com/Nexus-JPF/note-companion |
| Stack | Obsidian plugin: organize, chat, YouTube → notes |
| Voz | Voice Chat (Whisper), meeting recorder |
| Quem | iniciativa open source (dois irmãos) |
| Por que listar | voz + YouTube capture + OSS; menos “blog de autor solo americano” |
| Quando re-checar | se a memória for “plugin que organiza arquivos sozinho + voice chat” |

### 4. Brian Petro — Smart Connections

| Campo | Valor |
|-------|--------|
| GitHub | https://github.com/brianpetro/obsidian-smart-connections |
| Stack | embeddings + related notes + Smart Chat no Obsidian |
| YouTube | fraco (walkthroughs pontuais) |
| Por que listar | clássico “second brain” no ecossistema Obsidian AI |
| Quando re-checar | se a memória for “Smart Connections / wfhbrian” |

### 5. Stephen G. Pope — Shockwave

| Campo | Valor |
|-------|--------|
| Canal | https://www.youtube.com/@StephenGPope (ou Stephen G. Pope) |
| OSS | https://github.com/stephengpope/shockwave |
| Stack | clone OSS de Obsidian + AI coding agent embutido |
| Twitch | twitch.tv/stephengpope |
| Por que listar | OSS “substitui Obsidian”, conteúdo frequente |
| Quando re-checar | se a memória for “clone do Obsidian open source com agent” |

### 6. Eugeniu Ghelbur — obsidian-second-brain

| Campo | Valor |
|-------|--------|
| OSS | https://github.com/eugeniughelbur/obsidian-second-brain |
| Stack | persistent memory para Claude Code / Codex / Gemini em vault Obsidian |
| Voz | voice memo ingest (`/obsidian-ingest meeting.m4a` + Whisper local) |
| YouTube | autor pouco “creator massivo”; viralizou via Instagram/reels de terceiros |
| Por que listar | voice memo + YouTube link + screenshot → vault; stars relevantes |
| Quando re-checar | se a memória for “drop voice note / YT link e o vault se organiza” |

### 7. Outros (baixa prioridade nesta busca)

| Projeto | Notas |
|---------|--------|
| Logan Yang — Copilot for Obsidian | 1M+ downloads; Seattle; **pouco** YouTube (ele mesmo disse) |
| AgriciDaniel/claude-obsidian | self-organizing second brain; stars altos; creator YT? a validar |
| Matt Paige | Substack forte sobre Karpathy LLM wiki + Obsidian; não é “seu” OSS de cérebro |
| Vault Brain (plugin) | multimodal local + voice memos; criador pouco “canal massivo” |
| Smart Second Brain / Smart2Brain | plugin OSS “talk to notes”; autores Leo310 / nicobrauchtgit |

---

## Critérios que o alvo **deve** bater (checklist)

Usar quando reabrir a busca:

- [ ] Open source (ou source-available claro)
- [ ] Usa **Obsidian** (plugin, vault, ou clone)
- [ ] **Modo de voz** (não só “brand voice” de conteúdo)
- [ ] Autor com **blog**
- [ ] Canal **YouTube** com volume alto de conteúdo
- [ ] Perfil lembrado como **americano** (pode ser impreciso — ex. Peter era austríaco)
- [ ] **Não** é: OpenClaw, GBrain, Khoj, Cole, SystemSculpt, Note Companion (já negados)

---

## Relação com benches existentes

| Bench | Link | Relevância |
|-------|------|------------|
| memory-5way | `OS/_bench/memory-5way/` | memória/RAG/KG (gbrain, mempalace, mem0, memori, gsd-2) |
| mempalace-vs-gbrain | `OS/_bench/mempalace-vs-gbrain/` | H2H top-2 memory |
| personal-assistant-3way | `OS/_bench/personal-assistant-3way/` | openclaw, hermes, gbrain |

Estes candidatos **não** entraram nos scores. Se um for o alvo, considerar:

- inventário em `OS/_bench/_inventories/{slug}/` após clonar em `OS/` ou pasta dedicada  
- pack `memory` ou `personal-assistant` conforme o job (vault fidelity vs assistant)

---

## Log

| Data | Evento |
|------|--------|
| 2026-08-06 | Lista criada a partir da conversa de busca; nenhum item confirmado pelo Alan |
| 2026-08-06 | Alan: “não é nenhum destes mas vale salvar no relatório para conferir depois” |
| 2026-08-06 | Alan: “é o git lifeOS” → **danielmiessler/LifeOS** confirmado; parking lot marcado RESOLVIDO |

---

_Arquivo de parking lot — não é veredito de bench._
