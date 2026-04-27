# Gap Analysis: Padrões, Diferenças Paradigmáticas, Lacunas do Ecossistema

---

## Padrão Comum: O Que Todos Compartilham

Todos os 8 projetos implementam um **loop observável agent-driven**:

1. **LLM call** com prompt contextualizado
2. **Tool execution** (file I/O, shell, browser, git)
3. **Output processing** para avanço do workflow
4. **Feedback loop** explícito ou implícito

**Invariantes:**
- CLI ou plugin-based (nenhum requer GUI obrigatória)
- Git-aware (suportam ou usam nativamente)
- Multi-file editing (não apenas line-edits)
- LLM-agnostic option (5 de 8 suportam 20+ modelos)

**Stack dominante:**
- **Linguagem:** TypeScript (5/8) ou Python (2/8)
- **Runtime:** Node.js, Bun, Python 3.10+
- **Distribuição:** npm/pip/binary standalone

---

## Diferenças Paradigmáticas

### Pair-Programming vs. Autonomous

| Paradigma | Exemplos | Filosofia | Trade-off |
|-----------|----------|-----------|-----------|
| **Pair-Prog** | Aider, Claude Code (partial) | Usuário dirige, agent implementa | Mais controle, mais interação |
| **Autonomous** | GSD-2 (/gsd auto), gstack (/ship), OpenHands (agent mode) | Agent dirige, usuário aprova points | Mais velocidade, menos oversight |
| **Hybrid** | Superpowers, gstack (/office-hours + /autoplan) | Estrutura guia, agent detalha | Balanceado, maior custo cognitivo |

### Context Engineering

Três estratégias ortogonais:

| Estratégia | Quem | Como | Custo |
|-----------|------|------|-------|
| **Spec-driven** | Aider, OpenHands, Codex | Agent lê codebase, infere spec | Recuperação sob demanda |
| **Pre-inlined** | GSD-2, gstack | Dispatch injeta tudo relevante | Upfront (mas zero waste no turno) |
| **Compressed** | Claude Code (compaction skill) | Context window otimizado via resumo | Intermediate (query + summarize) |

**Insight:** GSD-2 e gstack trocam custo upfront por zero turno-waste; ideal para autonomous.

### Git Strategy

| Estratégia | Quem | Mecanismo | Auditabilidade |
|-----------|------|-----------|---|
| **Worktree isolation** | GSD-2, gstack (/qa), Superpowers | Branch per slice/feature; squash-merge | Excelente (1 commit = 1 feature) |
| **Auto-commit** | Aider, Codex, gstack (/land-and-deploy) | Commit per change-set; diffs visible | Boa (commits pequenos, rápidos) |
| **User-managed** | Claude Code (default) | Agent propõe, usuário faz git | Rígida (requer vigilância) |

---

## Lacunas do Ecossistema (O Que Ninguém Tem Bem)

### 1. **Collaborative Real-Time Editing**
- **Lacuna:** Nenhum agent suporta sessões paralelas com merge automático
- **Por quê:** Merge conflicts em código são intratáveis sem contexto
- **Solução parcial:** GSD-2 (milestones paralelos, mas mesma pessoa), gstack (/pair-agent para multi-agent, mas single-writer)

### 2. **LLM Model Management (Switching Mid-Session)**
- **Lacuna:** GSD-2 suporta fallbacks, mas nenhum faz on-demand model-switching por complexidade
- **Por quê:** Mudanças de contexto queimam cache, caro
- **Existente:** GSD-2 dynamic routing (complexity scoring) é o mais perto

### 3. **Test Generation from Behavior**
- **Lacuna:** Superpowers enforça red/green, mas nenhum gera testes *a posteriori* de mudanças feitas
- **Por quê:** "Does this test what I intended?" requer domain knowledge
- **Existente:** gstack (/qa auto-generates regression tests) é o mais perto

### 4. **Cross-Language Semantic Understanding**
- **Lacuna:** Todos fazem AST-parsing ou dumb regex; nenhum entende "refactor X to Y" semanticamente
- **Por quê:** Requer multi-language type system (LSP não é suficiente)
- **Existente:** Claude Code + gstack usam LSP, mas read-only

### 5. **Verifiable Delivery Contracts**
- **Lacuna:** Nenhum agent garante "you asked for X, we delivered exactly X"
- **Por quê:** Requer executable specs, que são código
- **Existente:** Superpowers plans come closest (detailed must-haves), GSD-2 verification gates (shell commands)

### 6. **Human-in-the-Loop at Decision Points**
- **Lacuna:** Apenas GSD-2 (remote-questions via Slack/Discord) e gstack (/ask-user-questions) fazem bem
- **Por quê:** Maioria trata humano como reviewer, não stakeholder
- **Existente:** GSD-2 remote-questions, gstack ask-user-questions com structured input

---

## Recomendações: Qual Estudar, Qual Absorver, Qual Usar

### (a) **Para Estudar Mais a Fundo**

**Rank:**

1. **Claude Code** (512K LOC, arquitetura visível)
   - **Por quê:** Bridge system + plugin system + multi-agent coordinator = production-grade orchestration
   - **Tempo:** 3-5 sessões (tool system, coordinator, plugin loading)
   - **Saída esperada:** Entender permissões, hooks, session management

2. **GSD-2** (auto-mode state machine)
   - **Por quê:** Observability + recovery + cost tracking = enterprise-ready autonomy
   - **Tempo:** 2-3 sessões (state machine, dispatch, verification)
   - **Saída esperada:** Entender crash recovery, cost projection, stuck detection

3. **gstack** (23 specialist skills + browser)
   - **Por quê:** Role-based task dispatch + visual feedback = methodical vibe coding
   - **Tempo:** 2-3 sessões (skill architecture, browser commands, design pipeline)
   - **Saída esperada:** Entender skill composition, browser as sensor

### (b) **Ideias para Absorver nos Seus Projetos**

| Ideia | De | Aplicável a |
|-------|----|----|
| Pre-inlined dispatch prompts | GSD-2 | Qualquer autonomous agent |
| Slash-command specialist registry | gstack | Qualquer multi-skill system |
| Worktree-per-milestone | GSD-2 | Qualquer project com múltiplas features |
| Design review before code | gstack (/plan-design-review) | Qualquer UI-heavy project |
| Remote question routing | GSD-2 | Qualquer CI/headless mode |
| Browser-as-eyes | gstack (/qa, /browse) | Qualquer E2E workflow |
| TDD red/green enforcement | Superpowers | Qualquer safety-critical codebase |
| Multi-agent task decomposition | Superpowers (subagent-driven) | Qualquer projeto 5+ pessoas |

### (c) **Para Usar No Dia-a-Dia**

**Use Case Matrix:**

| Seu Use Case | Recomendação | Por quê |
|--------------|--------------|---------|
| Solo dev, nova feature em codebase familiar | **Aider** | Pair-prog + auto-commit, zero overhead |
| Solo dev, grande refactor ou audit | **gstack** (/review + /investigate) | Especialistas reutilizáveis, browser eyes |
| Equipe pequena, shared roadmap | **GSD-2** | Worktrees isoladas, PREFERENCES.md compartilhado |
| Equipe, múltiplos repos | **gstack** (/retro global) + Claude Code | gstack para consolidação, Claude Code para deep work |
| Enterprise, compliance requerido | **OpenHands** (self-hosted) | RBAC, audit logs, isolation |
| Aprendizado acadêmico / pesquisa | **Claude Code** ou **OpenHands SDK** | Código fonte limpo, extensível |

---

## Riscos / Pegadinhas ao Adoptar

### **Claude Code**
- **Risco:** Dependência total de Anthropic (LLM lock, auth)
- **Mitigação:** MCP permite 3rd-party tools, mas core é Claude-only
- **Pegadinha:** Bridge IDE requer macOS/Linux; Windows é experimental

### **Codex**
- **Risco:** OpenAI model churn (GPT-4o → GPT-5 breaking changes)
- **Mitigação:** Suporta fallback models, mas primary é OpenAI-only
- **Pegadinha:** Mono-agent; scaling para teams requer workarounds

### **Aider**
- **Risco:** Repomap parsing pode falhar em linguagens exóticas
- **Mitigação:** 100+ languages suportadas, fallback é full-codebase
- **Pegadinha:** Pair-prog exige interação ativa; não é "set and forget"

### **OpenHands**
- **Risco:** Setup complexity (self-hosted, Kubernetes, DBs)
- **Mitigação:** Cloud tier disponível, mas paga
- **Pegadinha:** SDK é power-tool; agent CLI é mais simples mas menos controle

### **GSD-2**
- **Risco:** Auto-mode stuck detection requer manual intervention
- **Mitigação:** Forensics + recovery steering, mas exige troubleshooting skill
- **Pegadinha:** Worktree isolation pode deixar stale branches se não limpar

### **gstack**
- **Risco:** 23 skills = surface de aprendizado grande
- **Mitigação:** Proactive skill suggestions, mas requires tasting
- **Pegadinha:** Browser /qa pode ser flaky em sites com rate-limiting

### **Superpowers**
- **Risco:** Marketplace plugin-model requer manutenção cross-IDE
- **Mitigação:** Central SKILL.md template, sync scripts
- **Pegadinha:** TDD enforcement significa red tests devem ser reais; não é stub-friendly

### **AI Website Cloner**
- **Risco:** Template lock-in; hard to re-use para non-website projects
- **Mitigação:** Genérico bastante (Next.js + shadcn), mas espera UI-heavy input
- **Pegadinha:** Reverse-engineering pode gerar código feia em sites com inline styles

---

## Síntese Final

### Padrão Arquitetural Emergente

Todos os 8 agentes implementam uma **variação do mesmo loop:**

```
Dispatch (prompt + context) 
  → LLM response (thinking + tool calls) 
  → Tool execution 
  → Output sync (git/file) 
  → Feedback loop
```

**Diferenças são em camadas:**
- **Context layer:** Spec-driven, pre-inlined, ou compressed
- **Dispatch layer:** Pair-prog, assisted, ou autonomous
- **Execution layer:** Mono-agent, sub-agents, ou swarm
- **Sync layer:** Git-native, user-managed, ou file-based

### Recomendação Final

- **If learning:** GSD-2 (state machine + observability) + Claude Code (bridge + plugins)
- **If shipping fast:** Aider (pair-prog simplicity) + gstack (specialists + browser)
- **If building for others:** Superpowers (TDD enforcer) + OpenHands (SDK modularity)
- **If team scalability:** GSD-2 (auto-mode + milestones) + gstack (skill dispatch)

---

**Gerado:** 2026-04-19  
**Fonte:** README analysis + architecture docs + hands-on code inspection
