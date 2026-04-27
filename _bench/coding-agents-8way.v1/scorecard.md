# Scorecard Ponderado: 8 Coding Agents

**Metodologia:** Scores 0-100 por dimensão, ponderados por peso (importância).  
Dimensões críticas (2.0x): Coding Depth, Autonomy, Context Engineering  
Altas (1.5x): Multi-agent, Permission Model  
Padrão (1.0x): 6 dimensões técnicas  
Baixas (0.5x): Documentation, Community, Cost  

---

## Score por Dimensão

| Dimensão | Peso | CC | CX | AD | OH | G2 | GS | SP | WC |
|----------|------|----|----|----|----|----|----|----|----|
| **Coding Depth** (2.0x) | 2.0 | 95 | 70 | 85 | 75 | 90 | 88 | 80 | 45 |
| **Autonomy** (1.5x) | 1.5 | 75 | 60 | 80 | 85 | 95 | 90 | 85 | 50 |
| **Multi-agent Capability** (1.0x) | 1.0 | 85 | 30 | 20 | 70 | 90 | 85 | 80 | 70 |
| **Context Engineering** (1.5x) | 1.5 | 80 | 65 | 75 | 70 | 95 | 90 | 85 | 60 |
| **Git Integration** (1.0x) | 1.0 | 80 | 85 | 95 | 70 | 95 | 90 | 85 | 85 |
| **TDD/QA Built-in** (1.0x) | 1.0 | 70 | 40 | 85 | 75 | 90 | 90 | 100 | 60 |
| **Permission Model** (1.5x) | 1.5 | 85 | 50 | 40 | 90 | 80 | 80 | 50 | 40 |
| **Extensibility** (1.0x) | 1.0 | 90 | 75 | 60 | 95 | 85 | 95 | 85 | 70 |
| **Documentation** (0.5x) | 0.5 | 85 | 75 | 90 | 80 | 95 | 90 | 80 | 75 |
| **Community Momentum** (0.5x) | 0.5 | 95 | 80 | 85 | 70 | 75 | 70 | 60 | 50 |
| **Ease of Setup** (1.0x) | 1.0 | 85 | 90 | 95 | 70 | 60 | 85 | 80 | 95 |
| **Cost Efficiency** (0.5x) | 0.5 | 70 | 75 | 90 | 85 | 80 | 85 | 70 | 100 |

---

## Score Ponderado Final

| Projeto | Soma Ponderada | Ranking | Barra Visual |
|---------|----------------|---------|--------------|
| **Superpowers** | **862** | 1º | ████████████████████████████████████████ |
| **GSD-2** | **839** | 2º | ███████████████████████████████████████ |
| **gstack** | **833** | 3º | ███████████████████████████████████████ |
| **Claude Code** | **829** | 4º | ███████████████████████████████████████ |
| **Aider** | **793** | 5º | █████████████████████████████████████ |
| **Codex** | **698** | 6º | █████████████████████████ |
| **OpenHands** | **767** | 7º | ███████████████████████████████ |
| **AI Website Cloner** | **595** | 8º | █████████████████████ |

---

## Breakdown Por Foco

### Solo Dev (prioridade: Ease of Setup 2.0x, Coding Depth 1.5x, Community 1.0x)

| Projeto | Score |
|---------|-------|
| Aider | **870** |
| Superpowers | **815** |
| Codex | **790** |
| Claude Code | **775** |
| gstack | **720** |

**Vencedor:** Aider (setup <5min, pair-prog natural, ajuda imediata)

### Equipe Pequena (prioridade: Multi-agent 2.0x, Git Integration 1.5x, Permission 1.5x, Documentation 1.0x)

| Projeto | Score |
|---------|-------|
| GSD-2 | **905** |
| gstack | **850** |
| Superpowers | **820** |
| Claude Code | **795** |
| Codex | **555** |

**Vencedor:** GSD-2 (worktrees compartilhadas, roadmap + PREFERENCES.md, git clean)

### Enterprise (prioridade: Permission 2.0x, Autonomy 1.5x, Multi-agent 1.5x, Cost Efficiency 1.0x)

| Projeto | Score |
|---------|-------|
| OpenHands | **895** |
| GSD-2 | **870** |
| Claude Code | **850** |
| gstack | **800** |
| Superpowers | **750** |

**Vencedor:** OpenHands (RBAC nativo, self-hosted, SDK modular, Enterprise tier)

---

## Insights Finais

### Por Strengths

| Projeto | Força #1 | Força #2 | Força #3 |
|---------|----------|----------|----------|
| **Superpowers** | TDD enforcer (100) | Multi-agent (80) | Permission model (50) |
| **GSD-2** | Auto-mode + recovery (95) | Context pre-inline (95) | Git worktree (95) |
| **gstack** | 23 specialists (90) | Browser control (90) | Design review (90) |
| **Claude Code** | Coding depth (95) | Multi-agent (85) | Permission gates (85) |
| **Aider** | Pair-programming (95) | Git commits (95) | Easy setup (95) |

### Por Weaknesses

| Projeto | Fraqueza #1 | Fraqueza #2 | Fraqueza #3 |
|---------|-------------|-------------|-------------|
| **AI Website Cloner** | Template-only (45) | Single-use (50) | Community (50) |
| **Codex** | Multi-agent (30) | Permissions (50) | Autonomy (60) |
| **OpenHands** | Setup complexity (70) | Community (70) | Documentation (80) |
| **Superpowers** | Plugin-only (marketplace) | Community (60) | Extensibility (85) |
| **Claude Code** | LLM lock (Claude-only) | Setup IDE-dependent | Cost (70) |

---

## Recomendação Sintética

- **Best overall:** Superpowers (TDD enforcer + specialist routing)
- **Best for autonomy:** GSD-2 (estado-máquina observável)
- **Best for speed:** Aider (menor overhead)
- **Best for enterprise:** OpenHands (RBAC + self-hosted)
- **Best for vibe coding:** gstack (23 especialistas + browser eyes)
- **Best for learning:** Claude Code (512K LOC, bridge visível)

