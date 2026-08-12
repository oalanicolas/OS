# Formato público de empacotamento — decisão pós-lançamento do Agent Plugins 1.0

**Date:** 2026-08-12
**Pedido:** pesquisar o estado da arte (specs, permissões, ativação, times) e trazer a melhor solução de formato público
**Método:** tech-search em 5 frentes (spec Agent Skills · spec Agent Plugins · ativação/bootstrap · distribuição/marketplaces · permissões/segurança), consolidado com a avaliação crítica de `_bench/_research/plugin-vs-skill-vs-squad.md`
**Atualiza:** `_bench/_research/market-compatible-packaging.md` (fatos novos de agosto/2026)
**Cautela:** achados de fontes web via subagentes; os fatos load-bearing estão marcados com fonte

---

## O que a pesquisa mudou (4 fatos novos)

### 1. Agent Plugins 1.0 lançou — e a Anthropic ficou de fora

Lançado **6 de agosto de 2026** (Vercel blog; Google Developers Blog). TSC: AWS, Anysphere/Cursor, GitHub, Microsoft, OpenAI, Vercel; Google entrou como Core Maintainer. Plataformas no lançamento: **ChatGPT, Codex, Cursor, GitHub Copilot, Kiro, VS Code**.

**Nenhuma menção a Anthropic/Claude Code** nos anúncios. O Claude Code continua no ecossistema próprio (`.claude-plugin/plugin.json` + `marketplace.json`).

Consequência: a aposta do memo anterior ("eventualmente Agent Plugins 1.0") deixou de ser risco de maturidade — o risco agora é outro: **a caixa 1.0 não cobre o host Claude**. A embalagem Claude deixa de ser "opcional" e vira obrigatória em paralelo.

### 2. O buraco de contrato é oficial e deliberado — em todas as camadas

- **Agent Plugins 1.0:** manifest tem 10 campos ($schema, name, version, description, author, homepage, repository, license, keywords, extensions). **Permissões/efeitos explicitamente fora do escopo da v1**: "each client decides what a plugin is allowed to do… this restraint is the reason it got six signatures" (agent-plugins.org).
- **Agent Skills:** frontmatter tem `allowed-tools` e `compatibility`, mas no Claude Code `allowed-tools` é **parseado e não aplicado** (issue anthropics/claude-code#37683; análise reversec.com). `permissionMode: bypassPermissions` em skill chega a ser vetor de escalada.
- Skills herdam as permissões plenas do agente por default; ClawHub não exige assinatura nem review (Snyk ToxicSkills).

O enforcement real que existe é **host-side, não manifest-side**: sandbox kernel do Codex (Seatbelt/Landlock, 5 camadas), consent OAuth 2.1 + allowlists do MCP, permission rules do Claude Code. O manifest público nunca será o contrato de segurança.

### 3. O campo de batalha H2/2026 é confiança, não catálogo

Snyk ToxicSkills: prompt injection em **36%** das skills testadas; média de **6,3 issues por skill** (22.511 auditadas); campanha ClawHavoc = 341 skills maliciosas no ClawHub (março/2026). Skills curadas melhoram pass-rate em +16,2 p.p. vs. média pública de qualidade 6,2/12. Enterprise provisioning centralizado (fev/2026) e security scanning viraram "table stakes".

Consequência: postura de segurança auditável do pacote é diferencial de mercado, não burocracia interna.

### 4. Ativação continua dialeto por host; times continuam sem caixa

- Único trigger portátil: **description-matching** (progressive disclosure, 3 tiers). Hooks (SessionStart etc.) são específicos de host e viajam nos diretórios reverse-domain do plugin.
- Nenhum formato de mercado para empacotar time/composição surgiu. O mais perto: plugin Claude Code embarca `agents/` (subagentes) + hooks + skills + MCP — específico de host. Agent Plugins 1.0 não tem componente de agents.

---

## A solução: perfil dual-box, declare-but-verify

```text
{plugin-id}/
├── plugin.json                  # Agent Plugins 1.0 — caixa para Codex/Cursor/Copilot/VS Code/Kiro
├── README.md                    # promessa do produto em prosa (o "rótulo" que humanos e scanners leem)
├── skills/
│   └── {skill-id}/
│       ├── SKILL.md             # porta portátil; description = trigger; allowed-tools declarado (advisory)
│       ├── scripts/             # determinístico, pinado, sem download em runtime
│       └── references/
├── mcp.json                     # TODO efeito colateral com I/O passa por aqui (ver regra 3)
├── .claude-plugin/
│   └── plugin.json              # caixa irmã para o ecossistema Claude (marketplace.json)
├── com.anthropic.claude/        # hooks (SessionStart bootstrap), agents/ (composição Claude)
├── com.openai.codex/            # skill metadata, permission profiles sugeridos
└── com.aiox.enterprise/         # capability.yaml (contrato interno = evidência de auditoria), squad/, dual-run/
```

### Regras (em ordem de importância)

1. **Dual-box é obrigatório, não opcional.** `plugin.json` 1.0 no root cobre o bloco TSC (Codex, Cursor, Copilot, VS Code, Kiro); `.claude-plugin/` cobre Claude. Mesmo miolo (`skills/`), duas tampas de caixa. É o padrão Superpowers/mempalace, agora com metade das embalagens padronizada de verdade. Nenhuma das caixas relocaliza componentes — `skills/` é um só.

2. **Contrato: declarar sem confiar.** Declarar `allowed-tools` + `compatibility` no frontmatter e manter `capability.yaml` (I/O, effects, permissions, owner) em `com.aiox.enterprise/` — sabendo que **nenhum host aplica**. O papel do contrato muda: não é enforcement, é **evidência de auditoria** para o campo de batalha de confiança (scanners, curadoria, enterprise provisioning). Publicar a postura no README: sem `Setup` executável, sem `curl | bash`, scripts pinados e revisáveis, zero fetch de conteúdo externo em runtime (17,7% das skills maliciosas usam isso como vetor).

3. **Efeitos passam por MCP, não por prosa.** O único mecanismo de consentimento que viaja entre hosts é o do MCP (OAuth 2.1, allowlists deny-by-default, EMA). Regra de desenho: skill = procedimento + julgamento; **qualquer ação com efeito externo ou credencial = tool MCP declarada em `mcp.json`**. Isso move a superfície de risco do texto (ininspecionável) para tools (allowlistáveis) — a resposta real ao buraco de contrato.

4. **A porta tem que abrir fria.** O core funciona com description-matching sozinho — sem hook, sem router, sem bootstrap. Hook SessionStart em `com.anthropic.claude/` é *progressive enhancement*, nunca requisito de correção. Teste de aceite: instalar só `skills/{id}` via symlink num host virgem e a skill disparar pela description. (Resolve o pecado nº 3 da avaliação: a porta que só existe no filesystem.)

5. **Composição em camadas, nunca como unidade de distribuição.** Papéis (autor≠avaliador, autoridade exclusiva) descritos como texto no corpo da SKILL.md = camada portátil. Subagentes concretos em `com.anthropic.claude/agents/` = camada Claude. Org persistente com budget/fila (estilo Paperclip) **não cabe em pacote** — é plataforma, fica fora. A pesquisa confirmou: não existe e não está a caminho uma "caixa de time" de mercado; parar de esperar por uma.

6. **Canais na ordem de alcance:** (a) pasta `skills/{id}` avulsa (symlink, `npx skills add`, `.agents/skills/`); (b) Agent Plugin 1.0 via git/tarball/npm; (c) Claude marketplace via `.claude-plugin`; (d) ClawHub se o público OpenClaw importar. Mesmo miolo nos quatro.

### O que continua valendo do memo anterior

- Skill = porta, plugin = caixa, squad-como-caixa = legado. A taxonomia sobreviveu à pesquisa.
- Workspace fora do pacote; `capability.yaml`/dual-run no namespace interno.
- "Everything enters through a skill; not everything is stored as a skill."

### O que a pesquisa corrigiu

| Posição anterior | Correção |
|---|---|
| Agent Plugins 1.0 = aposta sem adoção | Lançado com 6 plataformas + Google; aposta segura **para o bloco TSC** |
| Claude marketplace = "outra embalagem do mesmo miolo", opcional | Obrigatória: Anthropic está fora da spec 1.0 |
| Rótulo público fraco = defeito a consertar no manifest | Deliberado e universal; o conserto não é campo no manifest, é MCP para efeitos + postura auditável + registry trust |
| Ativação portátil = lacuna talvez resolvível | Confirmado dialeto; desenhar para cold-start |
| Falta caixa para times = pendência | Confirmado que não existe nem vem; composição em camadas é a resposta final |

---

## Primeiro artefato (inalterado na essência, ajustado no aceite)

Um plugin mínimo (1 skill, 0 MCP, 0 squad) no layout acima. Aceite ampliado:

1. Codex/Cursor descobrem via `plugin.json` 1.0; Claude descobre via `.claude-plugin/` — **sem código AIOX no PATH**.
2. A skill dispara **fria** (só description) nos dois mundos.
3. `mcp-scan`/scanner equivalente passa limpo (sem Setup exec, sem fetch externo, scripts pinados).
4. `capability.yaml` presente no namespace e ignorado por todos os hosts sem erro.

---

## Fontes

Specs: [agentskills.io/specification](https://agentskills.io/specification) (Dez/2025; name+description obrigatórios; allowed-tools/compatibility opcionais) · [agent-plugins.org/specification](https://agent-plugins.org/specification) (v1.0.0, 6/ago/2026; permissões out of scope) · [MCP Security Best Practices](https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices) (OAuth 2.1, EMA, deny-by-default).

Lançamento/adoção: [Vercel — Introducing Agent Plugins](https://vercel.com/blog/introducing-agent-plugins) · [Google Developers Blog — Agent Plugins](https://developers.googleblog.com/agent-plugins-package-your-skills-tools-and-more/) · [Claude Code plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces).

Segurança: [Snyk ToxicSkills](https://snyk.io/blog/toxicskills-malicious-ai-agent-skills-clawhub/) (36% prompt injection; 76 payloads confirmados) · [reversec — Skill Issues Part 1](https://labs.reversec.com/posts/2026/05/skill-issues-compromising-claude-code-with-malicious-skills-agents-part-1) (allowed-tools não aplicado; bypassPermissions) · [anthropics/claude-code#37683](https://github.com/anthropics/claude-code/issues/37683).

Casa: `_bench/_research/plugin-vs-skill-vs-squad.md` (taxonomia + avaliação crítica) · `_bench/_research/market-compatible-packaging.md` (perfil v1, atualizado por este memo) · `_bench/_research/capability-first-vs-os.md`.
