---
name: "os-bench"
description: "Benchmark comparisons for opensource projects in OS/. Produces canonical artifact set (metadata, inventory, matrix, scorecard, gap-analysis, battle-card, executive-report) per spy skeleton. Supports 2-way and n-way comparisons."
version: "1.0.0"
user-invocable: true
activation_type: "pipeline"
---

# os-bench — Benchmark de Projetos Opensource

Pipeline autocontido para comparar projetos opensource clonados em `/Users/oalanicolas/Code/OS/`.
Produz um set canônico de 7 artefatos (metadata, inventory, matrix, scorecard, gap-analysis, battle-card, executive-report) + artefatos deep de absorção.

## Ativação

Invoque quando o usuário pedir:

- "comparar `{A}` com `{B}`" onde A e B são diretórios em `OS/`
- "benchmark `{A}` vs `{B}` vs `{C}`" (n-way, 2 a 8 projetos)
- "gap analysis entre `{A}` e `{B}`"
- "battle card de `{A}` contra `{B}`"
- "quais features de `{A}` eu deveria absorver no `{B}`"
- "rodar os 6 benchmarks planejados" (`*run-all`)
- qualquer referência a `/os-bench` ou à pasta `_bench/`

NÃO invoque para:

- Análise arquitetural single-repo (use `code-anatomist` ou equivalente)
- Comparação de players de mídia / canais (use `spy` original)
- Pesquisa de mercado / competitive intel de empresas (fora do escopo)

## Princípios

1. **No-invented-claims** — todo score, feature, métrica tem que apontar pra um path real em `OS/{subject}/` ou URL pública citada.
2. **Evidence-based scoring** — cada score 0–100 precisa de 2+ signals documentados no output. Sem signal = score `null` + confidence rebaixada.
3. **Bidirectional-gaps** — gap analysis sempre mapeia A→B E B→A. Nunca unidirecional.
4. **Confidence-disclosure** — cada dimensão carrega `confidence: HIGH|MEDIUM|LOW`. Rollup no topo do artefato.
5. **Local-first** — dado preferencialmente extraído do filesystem clonado (`OS/{subject}/`). Web só como fallback pra métricas de comunidade (stars, downloads).
6. **Deterministic paths** — slug de output sempre `{a}-vs-{b}` (2-way) ou `{topic}-Nway` (n-way). Sem datas no nome da pasta.

## Comandos

| Comando | O que faz | Inputs | Output root |
|---------|-----------|--------|-------------|
| `*help` | Lista comandos e princípios | — | — |
| `*inventory <subject>` | Fact-extraction de 1 repo (Phase 2 do code-anatomist condensada) | subject slug em `OS/` | `OS/_bench/_inventories/{subject}/` |
| `*bench-pair <a> <b> [--pack <pack>]` | Benchmark 2-way completo (7 artefatos) | dois slugs | `OS/_bench/{a}-vs-{b}/` |
| `*bench-nway <topic> <a> <b> [<c> ...]` | Benchmark n-way (matrix + scorecard + executive) | tópico + 2–8 slugs | `OS/_bench/{topic}-Nway/` |
| `*bench-absorb <a> <b>` | Gera roadmap de absorção de features de B em A | dois slugs | `OS/_bench/{a}-vs-{b}/deep/absorption-roadmap.md` |
| `*run-all` | Executa os 6 benchmarks planejados em sequência | — | `OS/_bench/*/` |
| `*list` | Lista benchmarks já produzidos em `OS/_bench/` | — | — |
| `*clean <bench-slug>` | Remove um benchmark com confirmação | bench slug | — |

### Dimension packs disponíveis (`data/dimension-packs.yaml`)

| Pack | Quando usar | Dimensões |
|------|-------------|-----------|
| `coding-agent` | coding agents / CLI assistants | Coding Depth, Autonomy, Context Mgmt, Git Integration, TDD, Multi-agent, Extensibility, Community |
| `memory` | sistemas de memória / RAG / KG | Recall Accuracy, Write Latency, Read Latency, Persistence, Schema Flexibility, Local-first, Vector Support, Graph Support |
| `orchestration` | multi-agent orchestration frameworks | Topology, Delegation Model, State Mgmt, Parallelism, Failure Recovery, Observability, DSL, Deployment |
| `mcp` | MCP servers / protocol impls | Protocol Compliance, Server Count, Transport Support, Auth, Community |
| `observability` | eval / tracing / LLM observability | Trace Granularity, Eval Framework, Cost Tracking, Latency Profiling, Self-hosted, UI Quality |
| `spec-driven` | spec-driven / meta-prompting | Spec Format, Traceability, Executable Specs, TDD Integration, Roundtripping |
| `personal-assistant` | assistentes pessoais multi-channel | Channels, Local-first, Memory, Skills, Cost, Privacy |
| `workflow-infra` | durable workflow / event-sourced | Durability, Retry Semantics, Event Log, Parallelism, Language Support, Cloud Lock-in |

Pesos fechados em 1.00 por pack. Ver `data/dimension-packs.yaml` para signals por dimensão.

## Output Paths

Todos os outputs vão pra `OS/_bench/` — **nunca** fora disso.

```
OS/_bench/
├── INDEX.md                            # lista rolling de benchmarks (mantida manual/*list)
├── _inventories/                       # cache de inventários reutilizáveis
│   └── {subject}/
│       ├── inventory.json
│       ├── inventory.md
│       └── fact-database.yaml
├── {a}-vs-{b}/                         # benchmark 2-way
│   ├── metadata.json
│   ├── inventory-{a}.{json,md}         # copy from _inventories (hardlink ok)
│   ├── inventory-{b}.{json,md}
│   ├── comparison-matrix.{json,md}
│   ├── scorecard.{json,md}
│   ├── gap-analysis.{json,md}
│   ├── battle-card.md
│   ├── executive-report.md
│   └── deep/
│       ├── feature-comparison.md
│       ├── absorption-roadmap.md       # se *bench-absorb rodou
│       └── migration-playbook.md       # opcional
└── {topic}-Nway/                       # benchmark n-way (3+)
    ├── metadata.json
    ├── inventory-{each}.{json,md}
    ├── comparison-matrix.{json,md}     # matriz N colunas
    ├── scorecard.{json,md}             # scorecard N colunas
    └── executive-report.md
```

## Pipeline (bench-pair)

```
1. RESOLVE
   ├── validate(subject_a exists em OS/)
   ├── validate(subject_b exists em OS/)
   ├── detect(comparison_type) → suggest pack
   └── create OS/_bench/{a}-vs-{b}/

2. INVENTORY (reuse cache se existe)
   ├── run tasks/inventory.md em A → _inventories/{a}/
   ├── run tasks/inventory.md em B → _inventories/{b}/
   └── copy para pasta do bench

3. MATRIX
   └── run tasks/bench-matrix.md → comparison-matrix.{json,md}

4. SCORE
   └── run tasks/bench-score.md (usa dimension pack) → scorecard.{json,md}

5. GAP
   └── run tasks/bench-gap.md → gap-analysis.{json,md}

6. BATTLE-CARD
   └── run tasks/bench-battle-card.md → battle-card.md

7. EXECUTIVE
   └── run tasks/bench-executive-report.md → executive-report.md

8. [OPCIONAL] ABSORB
   └── run tasks/bench-absorb.md → deep/absorption-roadmap.md

9. QUALITY GATE (ver seção abaixo)
```

## Quality Gate

Antes de considerar um benchmark completo, **todos** estes checks precisam passar:

- [ ] Todos os 7 artefatos canônicos existem em `OS/_bench/{slug}/`
- [ ] Todos os JSONs parseiam (rodar `node -e "JSON.parse(require('fs').readFileSync('x'))"`)
- [ ] Nenhum score 90+ sem 2+ signals citados
- [ ] Nenhum claim "X tem Y" sem path em `OS/{subject}/...` ou URL
- [ ] Gaps bidirecionais (A-only E B-only documentados — mesmo que um seja 0)
- [ ] Confidence disclosure no topo de scorecard e gap-analysis
- [ ] Dimensão pack e pesos declarados em metadata.json
- [ ] `OS/_bench/INDEX.md` atualizado com entry novo

Script utilitário: `scripts/bench.sh validate {slug}` roda os checks mecânicos.

## Autonomia do Claude

Esta skill é **autocontida**. Não há squad/agentes externos — o próprio Claude executa cada task lendo `tasks/{nome}.md` e produzindo o output.

- Sem dependência de `dr-orchestrator`, `research-head`, `spy-operator`, `bench-analyst` ou qualquer agente sinkra
- Sem dependência de `SINKRA-MAP`, `token-registry`, `composition-rules`
- Sem dependência de `aiox-core`, `sinkra-hub`, `workspace/`

## Benchmarks planejados (`*run-all`)

Lista canônica de 6 benchmarks relevantes pra OS, executáveis em sequência via `*run-all`:

| # | Slug | Pack | Sujeitos |
|---|------|------|----------|
| 1 | `coding-agents-8way` | `coding-agent` | claude-code-main, codex, aider, OpenHands, gsd-2, gstack, superpowers, ai-website-cloner-template |
| 2 | `memory-4way` | `memory` | gbrain, mempalace, mem0, gsd-2 |
| 3 | `orchestration-5way` | `orchestration` | BMAD-METHOD, crewAI, autogen, paperclip, claude-remote-manager |
| 4 | `spec-driven-3way` | `spec-driven` | spec-kit, get-shit-done, superpowers |
| 5 | `personal-assistant-3way` | `personal-assistant` | openclaw, hermes-agent, gbrain |
| 6 | `workflow-infra-2way` | `workflow-infra` | workflow, gh-aw |

Ver `tasks/run-all.md` para detalhes de execução.

## Templates deixados de fora (e porquê)

Do spy original, os seguintes templates **não foram portados** pra esta skill:

| Template | Motivo |
|----------|--------|
| `bench-quadrant-tmpl.md` | Gartner-style quadrant exige eixos "vision vs execution" que não têm signal claro em repos OS. Sem escala comparável cross-pack. |
| `bench-radar-tmpl.md` | ThoughtWorks-style radar (Adopt/Trial/Assess/Hold) é editorial e exige contexto de produção real — escopo fora dessa skill. |
| `bench-synergy-tmpl.md` | Análise de sinergia entre sujeitos já benchmarkados — use `*bench-absorb` que cobre o caso prático (roadmap de absorção). |
| `bench-migration-tmpl.md` | Migration playbook completo exige conhecimento de stack interno — mantido como stub opcional em `deep/migration-playbook.md` quando fizer sentido. |
| `bench-deep-compare-tmpl.md` | Duplicava `executive-report` + `comparison-matrix`. Consolidado. |

De `code-anatomist`, os seguintes templates **não foram portados**:

| Template | Motivo |
|----------|--------|
| `arc42-tmpl.yaml` | Doc arquitetural completo de um sistema — fora do escopo comparativo. |
| `sinkra-composition-proposal-tmpl.yaml` | Composição SINKRA — específico do stack sinkra-hub. |
| `sinkra-token-map-tmpl.yaml` | Token registry SINKRA — idem. |
| `enforcement-gap-report-tmpl.md` | Pressupõe domínio com regras de negócio — OS é infra/tooling. |
| `conformance-report-tmpl.yaml` | Reflexion model requer modelo formal prévio, excessivo pra benchmark. |
| `adoption-proposal-tmpl.yaml` | Focado em adoption cross-BU com signoff humano — overkill pra absorção OS. |

O que foi portado: `fact-database-tmpl.yaml` (inventory deep), `rule-catalog-tmpl.md` (simplificado como extração de invariantes), `decision-model-tmpl.yaml` (opcional quando o subject tiver policies formais).

## Arquivos da skill

```
os-bench/
├── SKILL.md                          # este arquivo
├── README.md                         # quick-start humano
├── data/
│   ├── bench-skeleton.md             # scaffold dos 7 artefatos
│   ├── dimension-packs.yaml          # 8 packs
│   └── output-formats.yaml           # formatos disponíveis
├── templates/
│   ├── battle-card-tmpl.md
│   ├── scorecard-tmpl.md
│   ├── comparison-matrix-tmpl.md
│   ├── gap-analysis-tmpl.md
│   ├── executive-report-tmpl.md
│   ├── inventory-tmpl.md
│   ├── metadata-tmpl.json
│   ├── fact-database-tmpl.yaml
│   ├── rule-catalog-tmpl.md
│   ├── decision-model-tmpl.yaml
│   └── absorption-roadmap-tmpl.md
├── tasks/
│   ├── inventory.md
│   ├── bench-matrix.md
│   ├── bench-score.md
│   ├── bench-gap.md
│   ├── bench-battle-card.md
│   ├── bench-executive-report.md
│   ├── bench-absorb.md
│   └── run-all.md
└── scripts/
    └── bench.sh                      # orquestrador CLI standalone
```

## Fluxo padrão recomendado

```bash
# 1) Inventário dos subjects (cache reusável)
*inventory gbrain
*inventory mempalace

# 2) Benchmark pair
*bench-pair gbrain mempalace --pack memory

# 3) Se quiser absorver features de um no outro
*bench-absorb gbrain mempalace

# 4) Rodar todos os 6 planejados
*run-all
```

## Anti-patterns

- Salvar artefato fora de `OS/_bench/`
- Pontuar dimensão sem listar signal
- Criar nova dimensão sem atualizar `data/dimension-packs.yaml`
- Gap analysis unidirecional (só A→B, sem B→A)
- Usar data no nome da pasta (`{a}-vs-{b}-2026-04-19/`) — slug é estável, metadata.json guarda a data
- Editar inventário dentro de `{a}-vs-{b}/` ao invés de em `_inventories/{subject}/`
- Inventar path `OS/foo/bar` sem checar com `ls` antes

---

*os-bench v1.0.0 — autocontido, sem dependência de squads sinkra*
