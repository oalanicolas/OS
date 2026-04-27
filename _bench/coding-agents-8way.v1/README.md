# Benchmark Comparativo: 8 Coding Agents Opensource

**Data:** 19 de Abril, 2026  
**Escopo:** Comparação estrutural de 8 coding agents opensource em atividade  
**Método:** Análise de READMEs, configuração, arquitetura, e modelos de distribuição  

---

## Highlights Por Projeto

| Projeto | Diferencial Principal |
|---------|----------------------|
| **Claude Code** | Motor LLM integrado (512K LOC, TS+Ink). IDE bridge bidirecional. Multi-agent orquestrado. |
| **Codex** | CLI nativo OpenAI (TS+Rust). Sign-in ChatGPT integrado. Desktop + web app híbrida. |
| **Aider** | Pair-programming com git. 100+ linguagens. 5.7M instalações pip. Linting/test automático. |
| **OpenHands** | Autonomous agent (Python). SDK modular. GUI local e cloud. Enterprise self-hosted. |
| **GSD-2** | Estado-máquina + Pi SDK. Auto-mode com recovery. Milestones estruturadas. Worktree isolation. |
| **gstack** | 23 especialistas slash-commands. Design review automático. Playwright browser. Real-time testing. |
| **Superpowers** | TDD obrigatório (red/green). Subagent-driven. 5 metodologias core. Multi-agent plugin. |
| **AI Website Cloner** | Template Next.js + shadcn. Reverse-engineer sites. Parallel builders em worktrees. |

---

## Verdict Por Categoria

### Para Solo Dev
**Melhor:** Aider (menos dependência de setup, pair-prog natural) ou Claude Code (contexto rico, bridge IDE)

### Para Equipe Pequena (2-4)
**Melhor:** GSD-2 (worktrees + git isolado, roadmap compartilhado) ou gstack (especialistas reutilizáveis)

### Para Produção / Enterprise
**Melhor:** OpenHands (SDK modular, self-hosted, RBAC) ou GSD-2 (observable, cost-tracked)

### Para Exploração / Prototipagem
**Melhor:** gstack (/office-hours reframing, design-shotgun visual) ou Claude Code (flexibilidade)

### Para Aprender Arquitetura AI
**Melhor:** Claude Code (512K LOC, orquestração visível) ou OpenHands (SDK desacoplado)

### Para Vibe Coding Controlado
**Melhor:** Superpowers (TDD obrigatório, planos detalhados) ou gstack (/review + /qa automático)

---

## Estrutura Geral

| Aspecto | Distribuição | Prevalência |
|---------|--------------|------------|
| **Linguagem primária** | TS: 5 | Python: 2 | Rust: 1 |
| **CLI vs Plugin** | CLI standalone: 6 | Skill/Plugin: 2 |
| **Dependência IDE** | Nenhuma: 4 | VSCode: 2 | Multi-IDE: 2 |
| **Modelo LLM** | Claude only: 3 | Multi-model: 5 |
| **Autonomia** | Pair-prog: 2 | Assisted: 3 | Autonomous: 3 |

---

## Observações Técnicas

- **Linguagem dominante:** TypeScript (Claude Code, Codex CLI, GSD-2, gstack, Superpowers)
- **Python forte:** Aider, OpenHands
- **Multi-model:** GSD-2, gstack, Superpowers e Codex suportam 20+ provedores; Claude Code e Aider focam em campeões (Anthropic/OpenAI)
- **Git como primitivo:** Aider, GSD-2, gstack, Superpowers usam git como source-of-truth; Claude Code suporta mas não obriga
- **TDD enforcement:** Apenas Superpowers obriga; outros suportam
- **Browser control:** gstack + OpenHands têm browser headless nativo; Aider usa Playwright opcional

---

## Próximos Passos

Veja `comparison-matrix.md` para matriz dimensionada (15 critérios).  
Veja `scorecard.md` para ranking ponderado com visualização ASCII.  
Veja `gap-analysis.md` para síntese de padrões, lacunas, e recomendações.

---

**Gerado:** 2026-04-19 — Leitura de READMEs, package.json/pyproject.toml, docs de arquitetura
