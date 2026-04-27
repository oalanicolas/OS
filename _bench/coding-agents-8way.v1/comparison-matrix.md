# Matriz Comparativa: 8 Coding Agents

**Colunas abreviadas:** CC (Claude Code) | CX (Codex) | AD (Aider) | OH (OpenHands) | G2 (GSD-2) | GS (gstack) | SP (Superpowers) | WC (Website Cloner)

| Dimensão | CC | CX | AD | OH | G2 | GS | SP | WC |
|----------|----|----|----|----|----|----|----|----|
| **Linguagem primária** | TS | TS+Rust | Python | Python | TS | TS | TS | TS |
| **Modelo distribuição** | CLI (npm) | CLI (npm/brew/binary) | CLI (pip) | CLI (npm)+SDK | CLI (npm)+Web | Skills (Bun) | Plugin (marketplace) | Template (npm) |
| **Dependência IDE** | Nenhuma | Nenhuma | Nenhuma | Nenhuma | Nenhuma | Nenhuma | Marketplace multi-IDE | Nenhuma |
| **LLM suportado** | Claude só | OpenAI (+ChatGPT OAuth) | 50+ modelos | 20+ modelos | 20+ modelos | 20+ modelos | Plugin-agnostic | Claude/OpenAI |
| **Autonomia** | Pair-prog + assisted | Assisted | Pair-prog | Autonomous | Autonomous (auto-mode) | Autonomous (23 skills) | Autonomous (subagent) | Assisted (template) |
| **Modo multi-agent** | Swarm (subagents) | Mono | Mono | Mono (SDK) | Swarm (milestones paralelos) | Swarm (skill dispatch) | Subagent-driven | Worktrees paralelos |
| **Context management** | Compressed (compaction) | Spec-based | Spec + repomap | Spec-based | Pre-inlined (fase-específico) | Pre-inlined (dispatch) | Plan-based (detalhado) | Template-scoped |
| **Memória persistente** | Long-term (memdir) | None (stateless) | None (session) | Session (DB) | Long-term (graph) | None (session) | None (plan-based) | None (worktree) |
| **Integração git** | Suporta (+bridge) | Nativa (commits) | Nativa (auto-commit) | Suporta | Nativa (worktree/branch) | Nativa (commits) | Suporta (worktree) | Worktree automático |
| **TDD/QA built-in** | Opcional | Não | Linting+teste | Suporta (SDK) | Verificação obrigatória | /qa automático | **Obrigatório** (red/green) | Template-scoped |
| **Governance/permissions** | Approval gates (hooks) | Ad-hoc | Ad-hoc | RBAC (enterprise) | Approval gates + sandboxed | Approval gates (/guard) | Ad-hoc (skill config) | Ad-hoc |
| **Comunidade (stars aprox)** | ~512K LOC | Rustlings | 50K+ stars | 20K+ stars | 30K+ stars | Garry+team | 10K+ stars | 5K+ stars |
| **Atividade** | Daily (Anthropic) | Regular (OpenAI) | Very active | Active | Very active | Daily (Garry) | Regular | Moderate |
| **Público-alvo** | Devs (CLI+IDE) | ChatGPT users | Independentes | Equipes/Enterprise | Teams+solo | Solo/small teams | Focused builders | Learners |
| **Diferencial principal** | Motor orquestrado; bridge IDE | ChatGPT OAuth integrado | Simplicidade pair-prog | SDK modular + self-hosted | Auto-mode observável | 23 especialistas + browser | TDD enforcer | Reverse-engineer template |

---

## Legenda Compacta

- **Linguagem primária:** Dominante. TS = TypeScript, Rust = compilado
- **Modelo distribuição:** CLI npm (npm install -g), CLI pip (pip install), Skill (Bun-based), Plugin (marketplace/registry)
- **Dependência IDE:** Nenhuma = standalone, VSCode = VSCode bridge, Multi = múltiplas IDEs
- **LLM suportado:** Cantidad e breadth de modelos suportados
- **Autonomia:** Pair (usuário conduz) | Assisted (agent propõe) | Autonomous (agent executa)
- **Multi-agent:** Mono (single agent) | Sub-agents (children com isolation) | Swarm (parallel workers)
- **Context management:** Basic (arquivo-a-arquivo) | Spec (spec-driven) | Compressed (context windows otimizadas) | Pre-inlined (injected)
- **Memória persistente:** None (session-only) | Session (JSONL/cache) | Long-term (graph/knowledge)
- **Git integration:** None (user-managed) | Suporta (tools disponíveis) | Nativa (auto-commits, branch management)
- **TDD/QA:** Não (skipped) | Opcional (available) | Obrigatório (enforced)
- **Governance:** Ad-hoc (user decision) | Approval gates (workflow stages) | Sandboxed (restricted execution) | RBAC (role-based)
- **Atividade:** Daily/continuous | Very active (weekly) | Active (regular) | Regular (bi-weekly) | Moderate (ad-hoc)

---

## Observações de Célula

| Célula | Notas |
|--------|-------|
| **CC LLM** | Anthropic só; MCP permite 3rd-party mas core é Claude |
| **CX Autonomia** | Sign-in + OAuth, mas agent fica em assisted-only |
| **AD Git** | Commits automáticos + diffs. Pair-programming core. |
| **OH Multi-agent** | SDK permite N agents, mas interface é única |
| **G2 Context** | Dispatch-prompt pré-inlined por fase, zero waste |
| **GS Multi-agent** | 23 skills = 23 especialistas, dispatch via chat |
| **SP TDD** | red-green-refactor obrigatório em todo task |
| **WC Multi-agent** | Builders paralelos em worktrees, merge smart |

