# Cross-Bench Synthesis

**Data:** 2026-04-19
**Escopo:** 6 benchmarks executados via skill `os-bench` em `OS/_bench/`
**Método:** triangulação dos 6 executive-reports + scorecards + inventories

---

## 1) Ranking consolidado

| Bench | #1 | #2 | #3 | Last |
|---|---|---|---|---|
| coding-agents-8way | gsd-2 (85.59) | OpenHands (84.42) | claude-code-main (83.82) | ai-website-cloner (61.04) |
| memory-4way | mempalace (83.14) | mem0 (76.36) | gbrain (75.89) | gsd-2 (51.95) |
| orchestration-5way | paperclip (79.62) | autogen (79.14) | crewAI (67.54) | claude-remote-manager (48.58) |
| spec-driven-3way | get-shit-done (73.50) | spec-kit (64.26) | — | superpowers (53.64) |
| personal-assistant-3way | hermes-agent (84.75) | openclaw (80.91) | — | gbrain (68.45) |
| workflow-infra-2way | workflow/Vercel (77.08) | gh-aw (58.20) | — | — |

## 2) Subjects em múltiplos benches (revela generalistas vs especialistas)

| Subject | Benches | Posições | Leitura |
|---|---|---|---|
| **gsd-2** | coding, memory | 1º / last | Coding agent puro; memória é feature lateral. Confundir os dois mata o pitch. |
| **gbrain** | memory, personal-assistant | 3º / 3º | **Generalista forte e consistente** — nenhum último, nenhum primeiro. Complementar, não substituto. |
| **superpowers** | coding, spec-driven | 4º / last | TDD é diferencial isolado (95), mas penaliza em spec-format e roundtripping. |
| **hermes-agent** | personal-assistant | 1º | Única aparição — vence por skill creation autônomo + serverless hibernation. |
| **mempalace** | memory | 1º | Única aparição — política verbatim + local-first são moats claros. |
| **paperclip** | orchestration | 1º | Única aparição — company-sim paradigm é underexplored. |

**Padrão**: quem vence um bench geralmente perde fora dele. gbrain é a exceção — consistência é seu moat silencioso.

## 3) Paradigmas incompatíveis encontrados

Cada categoria tem **3-5 paradigmas distintos que não podem ser reconciliados por um vencedor**:

| Categoria | Paradigmas | Conclusão |
|---|---|---|
| Coding agents | pair-prog (aider) · autonomous (OpenHands) · methodology (superpowers) · product (claude-code) | Não há "o melhor" — perfis diferentes |
| Memory | verbatim local (mempalace) · paraphrase cloud-ecosystem (mem0) · graph postgres (gbrain) · feature lateral (gsd-2) | Escolha é por eixo dominante do requisito |
| Orchestration | agile-pipeline (BMAD) · role-playing (crewAI) · conversacional (autogen) · company-sim (paperclip) · remote-persistence (claude-remote-manager) | 5 modelos mentais distintos |
| Spec-driven | executable-specs (spec-kit) · meta-prompting (GSD) · TDD-enforcement (superpowers) | Zero convergência |
| Workflow infra | durable stateful (Vercel workflow) · agentic sandboxed (gh-aw) | Complementares, não competidores |
| Personal assistant | multi-channel (openclaw) · self-improving (hermes) · knowledge-brain (gbrain) | Camadas diferentes da pilha |

## 4) Lacunas do ecossistema (comum aos 6 benches)

Capabilities que **nenhum projeto cobre bem** atravessam categorias:

1. **Roundtripping code↔spec completo** — spec-kit é one-way, GSD detecta drift mas não reconcilia
2. **Memory stack completo** — ninguém combina verbatim + graph tipado + local-first + vector ecosystem + benchmarks públicos
3. **Multi-paradigm orchestration** — nenhum framework permite escolher topology (pipeline/role/conversation/company) em runtime
4. **Durability + agentic safety unificadas** — Vercel workflow tem replay, gh-aw tem approval gates, ninguém tem os dois
5. **Model switching mid-session** — todos os coding agents travam o modelo por run
6. **Test generation a partir da intent** — TDD é enforced em superpowers mas testes são escritos pelo humano
7. **Eval/observability nativa** — langfuse existe standalone, mas nenhum agent framework expõe trace em OTel-compatível por default

## 5) Anti-patterns consolidados (o que NÃO copiar)

| Anti-pattern | Evidência | Impacto |
|---|---|---|
| OpenAI lock-in pra embeddings | gbrain (core path) | Inviabiliza on-prem/enterprise |
| Telemetria on-by-default em deps core | mem0 (PostHog) | Quebra local-first silenciosamente |
| Schema enum-fixo restritivo | gsd-2 (6 categorias memory) | Otimiza vertical, bloqueia generalização |
| Runtime gRPC distribuído em maintenance | autogen | Lock-in em arquitetura sem suporte |
| Closed-source extensions obrigatórias | codex (RTK binary) | Bloqueia fork/audit |
| Verbatim source leak como "snapshot" | claude-code-main | Zona cinzenta legal |

## 6) Patterns a absorver (o que vale portar)

| Pattern | Fonte | Por quê |
|---|---|---|
| **Política verbatim** ("não paraphraseamos") | mempalace | Diferencia produto; trivial de implementar; alta intenção de usuário |
| **Zero-LLM auto-wiring de edges tipadas** (regex) | gbrain | 100x mais barato que LLM-based extraction |
| **Serverless hibernation + TTL** | hermes-agent | Reduz custo de agents always-on dramaticamente |
| **Red/green TDD como Iron Law** | superpowers | Única forma de enforcer qualidade em agente autônomo |
| **Meta-prompting contra context rot** | get-shit-done | Resolve problema real de janelas longas |
| **Company-sim (org charts + budgets + goals)** | paperclip | Governance escalável pra fleets de agents |
| **Markdown workflows em GitHub Actions** | gh-aw | Trivial de auditar, read-only por default, sandboxed |
| **Event-sourced replay determinístico** | workflow (Vercel) | Debugging e recovery sem estado adicional |
| **Subagents dispatched per task** | superpowers | Paralelismo controlado sem context bloat |
| **Published benchmarks em corpora públicos** | mempalace, mem0 | Única forma honesta de comparar recall |

## 7) Recomendações para seus projetos

### sinkra-hub / aiox / gstack / gbrain

**gbrain** é genuinamente forte (Top 3 em 2 benches). Gaps específicos:
- Adicionar fallback de embeddings (Ollama/FastEmbed) → sobe ~10pts em local-first
- Absorver política verbatim (mempalace) + temporal KG (`valid_from`/`valid_to`)
- Publicar benchmark em LongMemEval/LoCoMo (corpora padrão) pra comparabilidade

**Para o stack de agents geral**:
- Orchestration: paperclip's company-sim > outros. Absorver org-charts + budgets.
- Coding: gsd-2 metodologia (auto-milestone + RTK compression) > outros
- Spec: combinar spec-kit SDD (IDs canônicos FR-###/SC-###) + GSD meta-prompting (ambiguity gate)
- Memory: mempalace verbatim + gbrain graph via MCP (hybrid já sugerido pelo próprio executive report)
- Personal assistant: hermes skill creation + gbrain memory + openclaw multi-channel = stack completa

## 8) Meta-learnings sobre benchmarking

- **Quality gate** (no-invented-claims + evidence paths + confidence disclosure) é o que separa marketing de análise séria. Todos os 6 passaram — forma replicável.
- **N-way vs pair**: N-way revela paradigmas, pair revela tradeoffs finos. Ambos necessários.
- **Inventory cache** (`_bench/_inventories/`) economiza ~30% de tempo em re-runs.
- **Profiles quick vs standard**: quick (README + manifests) é suficiente pra 80% das dimensões. Deep só pra tech-eval de arquitetura.
- **Weighted totals** dependem fortemente do pack escolhido — mudar pesos reordena ranking. Sempre disclosure explícito.

---

## Próximos passos possíveis

1. **Deep-dive em gbrain** — é o melhor candidato pra absorver features dos Top 3 e subir pra winner em múltiplos benches
2. **Paperclip vs autogen pair-wise** — o empate técnico (79.62 vs 79.14) merece 13 artefatos canônicos, não n-way
3. **Coding-agents-8way v2 aprofundado** — com pair-wise entre gsd-2 vs OpenHands (os dois líderes) pra refinar
4. **Benchmark novo: eval-observability** — atualmente só langfuse, mas adicionar promptfoo + braintrust via clone preenche a lacuna
5. **Absorption playbook** — pegar o Top 3 pattern table (§6) e transformar em roadmap de ports pra sinkra/gbrain

---

_Gerada a partir dos 6 executive-reports em `OS/_bench/{slug}/executive-report.md`. Para dados brutos, consulte scorecards e matrizes._
