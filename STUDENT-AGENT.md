# STUDENT-AGENT — Sparring crítico do `sinkra-hub`

Agente autônomo que **estuda continuamente** os repos opensource em `OS/`, **compara** com o estado atual do `sinkra-hub`, e **propõe melhorias acionáveis**. Eterno aprendiz de boas práticas, com missão clara: tornar o `sinkra-hub` melhor.

**Não é estudo neutro.** Cada investigação termina com a pergunta: *"o que disso o `sinkra-hub` deveria adotar, evitar, ou repensar?"*

## Tese

`sinkra-hub` é monorepo de produção (SINKRA v3.2, 8 camadas, governança constitucional, 4 negócios). `OS/` é coleção de 30 repos OS de AI agents — referências de mercado, paradigmas validados, padrões emergentes.

O agente faz a ponte: **traz o melhor da pesquisa OS pra prática do sinkra-hub**, sem que você precise ler 30 repos manualmente.

## Stack (tudo já em OS/)

| Camada | Repo | Papel |
|--------|------|-------|
| Executor + skill creation | `hermes-agent` | Loop autônomo, multi-model, auto-cria skills, roda em VPS $5 |
| Memória persistente | `gbrain` | Knowledge graph com self-wiring entity links, 95% recall@5 |
| Auto-melhoria do prompt | `gepa` | Reflective prompt evolution multi-objetivo (Pareto) |
| Spec da missão | `get-shit-done` (GOAL.md) | Fitness function explícita |
| Exploração paralela (opcional) | `superpowers` | Subagents pra investigação multi-ângulo |

Nada novo é clonado. Toda peça já está em `OS/`.

## Objetivo concreto

**Output primário:** **issues no GitHub do `sinkra-hub`**, cada uma com:

1. **Origem** — qual repo OS observado, qual padrão extraído
2. **Estado atual no sinkra-hub** — o que já existe, com refs (`packages/`, `squads/`, `.aiox-core/`)
3. **Gap identificado** — o que está faltando ou poderia ser melhor
4. **Proposta acionável** — mudança específica, não conceito abstrato
5. **Impacto estimado** — quais camadas (L1-L8) afetadas, qual constitution principle reforçado
6. **Risco / esforço** — pequeno / médio / grande

**Você decide tudo.** Agente nunca:
- escreve código no sinkra-hub
- abre PR
- faz commit
- cria branch
- altera arquivos do working tree

Agente **só** abre issues via `gh issue create`. Você triagia (close / accept / discuss) no fluxo normal do GitHub.

**Output secundário:** knowledge graph cumulativo de padrões observados em OS/ — substrato pra futuras decisões arquiteturais.

## Por que essa ponte vale

Olhando o `sinkra-hub` (CLAUDE.md):

- **Constitution + 7 princípios** ↔ `agent-governance-toolkit` (Microsoft, OWASP Agentic Top 10) tem padrões de policy enforcement sub-ms
- **Squads SINKRA-governed** ↔ `BMAD-METHOD` (12+ agentes), `paperclip` (org charts, budgets), `Clawith` (digital employees) — todos abordam governance de squads
- **Story-Driven, Task-First** ↔ `spec-kit` (GitHub), `get-shit-done` (Amazon/Google/Shopify), `superpowers` (TDD red/green) — toda metodologia spec-driven
- **`.aiox-core/` framework** ↔ `crewAI`, `autogen`, `dify` — frameworks multi-agente comparáveis
- **L8 Evolution Matrix (self-learning)** ↔ `gepa`, `ADAS`, `AI-Scientist-v2` — auto-melhoria sistemática
- **Memory / minds/** ↔ `mem0`, `mempalace`, `gbrain`, `memori-labs` — memory infrastructure
- **MCP** ↔ `mcp-servers` (referência oficial)
- **Observability** ↔ `langfuse`

Cada par dessa lista é uma **investigação cruzada** que o agente vai fazer.

## Arquitetura

```
┌─────────────────────────────────────────────────────────┐
│  CRON / SERVERLESS WAKEUP                               │
└────────────────────────┬────────────────────────────────┘
                         ▼
┌─────────────────────────────────────────────────────────┐
│  STUDENT-AGENT (Hermes especializado)                   │
│  1. Snapshot do sinkra-hub (último commit, AGENTS.md,   │
│     constitution, squads, packages)                     │
│  2. Consulta gbrain: "qual cruzamento estudar agora?"   │
│  3. Lê repo OS escolhido (com lente sinkra-hub)         │
│  4. Produz: relatório + N propostas de melhoria         │
│  5. Salva em gbrain + posta em sinkra-hub/.proposals/   │
│  6. Se múltiplo de N: dispara GEPA                      │
│  7. Hiberna                                             │
└────────────┬────────────────────────────┬───────────────┘
             ▼                            ▼
   ┌──────────────────┐         ┌────────────────────┐
   │  GBRAIN          │         │  GEPA              │
   │  - patterns      │         │  - lê issues       │
   │  - sinkra_state  │         │    fechadas/abertas│
   │  - issues        │         │  - LLM-as-judge    │
   │  - decisions     │         │  - muta system     │
   └──────────────────┘         │    prompt          │
                                └────────────────────┘
                                        │
                                        ▼
                          ┌──────────────────────────┐
                          │  GitHub Issues           │
                          │  alanicolas/sinkra-hub   │
                          │  label: student-agent    │
                          │  (gh issue create)       │
                          └──────────────────────────┘
```

## Loop de execução

### Wake cycle

```
1. Student acorda
2. Carrega snapshot do sinkra-hub:
   - HEAD commit, AGENTS.md, .aiox-core/constitution.md
   - Lista de squads, packages, services
   - Últimas decisões arquiteturais (ADRs)
3. Carrega state do gbrain:
   - patterns_observed: {repo: [pattern1, pattern2, ...]}
   - sinkra_coverage: {sinkra_layer: studied_against_repos[]}
   - proposals: {id, status, related_pattern}
4. Decide próxima investigação (ver "Política de seleção")
5. Executa investigação cruzada (ver "Tipos de investigação")
6. Gera 1-N propostas de melhoria (formato canônico)
7. Validação pré-submit:
   - dedup contra issues abertas/fechadas com mesmo pattern
   - check de violação de constitution (rejeita antes de abrir)
   - check de rejeição prévia (mesmo pattern já closed:not_planned)
8. Persiste:
   - relatório em gbrain.reports
   - patterns no graph
   - **issues abertas via `gh issue create -R alanicolas/sinkra-hub`**
     com labels: `student-agent`, `os-source:<repo>`, `layer:Lx`, `principle:#N`
9. Se len(reports) % 50 == 0 → GEPA cycle
10. Hiberna
```

### GEPA cycle (a cada 50 investigações)

GEPA otimiza pela **taxa de aceitação de issues**:

```
1. Carrega últimas 50 issues + status via gh:
   - fechada como completed → +1 (você endossou)
   - fechada como not_planned → -1 (você rejeitou)
   - aberta com label "approved" → +1
   - aberta com label "wontfix" → -1
   - aberta sem decisão → 0
   - virou PR mergeado → +2 (sinal mais forte)
2. LLM-as-judge analisa correlação estilo ↔ aceitação
3. Score por eixo (ver "Fitness")
4. GEPA propõe N mutações do system prompt
5. Próximas investigações usam mutações em A/B
6. Mantém mutações cuja taxa de aceitação sobe
```

**Sinal real, não sintético**: o feedback do GEPA é seu comportamento de triagem real no GitHub. Você fecha issue como `not_planned` → GEPA aprende o que você não quer ver de novo.

## Política de seleção

Prioridade decrescente:

1. **Backlog explícito** — issues no sinkra-hub com label `student-agent:backlog` (perguntas suas que viram tasks pro agente)
2. **Mudança recente no sinkra-hub** — squad nova, package novo, ADR novo → buscar precedentes em OS/
3. **Cruzamentos canônicos não-feitos** — pares (sinkra_layer, repo_OS) ainda não estudados
4. **Aprofundamento de pattern** — pattern observado em N repos → vale virar proposta sistêmica?
5. **Drift** — repo OS teve commits relevantes desde último estudo

## Tipos de investigação

| Tipo | Pergunta-mãe | Output |
|------|--------------|--------|
| **Cruzamento direto** | "Como `X` (OS) resolve Y, e como `sinkra-hub` resolve hoje?" | Battle-card + 1-3 propostas |
| **Padrão emergente** | "Pattern P aparece em 4+ repos OS — sinkra deveria adotar?" | Proposta sistêmica (afeta múltiplas camadas) |
| **Validação de decisão** | "ADR Z do sinkra-hub diverge da prática OS — está certo divergir?" | Análise de trade-off + recomendação |
| **Detecção de risco** | "OWASP Agentic Top 10 (agent-governance-toolkit) cobre o que sinkra não cobre?" | Lista priorizada de gaps de segurança |
| **Antipattern** | "Pattern A é usado por sinkra mas N repos OS abandonaram — por quê?" | Alerta + alternativas |

## Formato canônico da issue

**Title:** `[student-agent] <título curto e acionável>`

**Labels (auto-aplicadas):**
- `student-agent` (sempre)
- `os-source:<repo>` (ex: `os-source:agent-governance-toolkit`)
- `layer:L<N>` (uma ou mais)
- `principle:#<N>` (constitution principle reforçado)
- `effort:S` | `effort:M` | `effort:L`
- `risk:low` | `risk:medium` | `risk:high`

**Body:**

```markdown
> Issue gerada automaticamente pelo Student-Agent.
> Origem: OS/<repo>/<arquivo|módulo>
> System prompt version: v<N>
> Investigação ID: <gbrain_report_id>

## Pattern observado em OS/
<descrição concreta com refs a arquivos do OS>

## Estado atual no sinkra-hub
<descrição do que existe hoje, com refs a arquivos:linhas usando permalinks>

## Gap
<diferença específica, não genérica>

## Proposta
<mudança acionável: "trocar Y por Z em arquivo W"; não "considerar X">

## Impacto
- [ ] Reduz acoplamento entre A e B
- [ ] Habilita caso de uso C
- [ ] Reforça principle #<N> da constitution

## Riscos / contraindicações
<o que pode dar errado; quando NÃO adotar>

## Como triagar
- ✅ **Aceitar**: feche como `completed` ou aplique label `approved`
- ❌ **Rejeitar**: feche como `not_planned` (com comment do motivo — alimenta GEPA)
- 💬 **Discutir**: deixe aberta com label `discussion`
```

**Comando real:**

```bash
gh issue create -R alanicolas/sinkra-hub \
  --title "[student-agent] <título>" \
  --body-file <generated.md> \
  --label student-agent,os-source:<repo>,layer:L<N>,effort:M,risk:low
```

## Fitness function (4 eixos, GEPA otimiza Pareto)

LLM-as-judge avalia cada proposta em:

1. **Especificidade** — proposta é acionável (`mudar X em Y`) ou abstrata (`considerar Z`)?
2. **Ancoragem** — cita refs concretas tanto no OS quanto no sinkra-hub?
3. **Adequação** — respeita os 7 principles da constitution? Não viola CLI-First, KISS, etc.?
4. **Originalidade** — agrega algo que não está em propostas anteriores nem em ADRs existentes?

**Sinal real (peso maior):** estado da issue no GitHub.
- closed:completed → +1
- closed:not_planned → -1
- label `approved` → +1
- label `wontfix` → -1
- virou PR mergeado → +2
- aberta sem decisão → 0 (não conta após N dias para evitar enviesar pra ruído)

GEPA otimiza pra subir a razão (positivos / total).

**Anti-padrões penalizados:**
- Issues tipo "considerar adotar X" sem mudança concreta
- Sugestões que violam KISS (adicionar camada por camada)
- Repetir proposta já fechada como `not_planned` com mesmo pattern
- Recomendar repo OS que sinkra-hub explicitamente decidiu não usar (ver ADRs de rejeição)
- Issues sem permalinks (devem citar arquivos:linhas reais)

## Estrutura no gbrain

```
entities:
  - Repo {name, path, stack, category, last_studied}
  - Pattern {name, description, repos_observed[]}
  - SinkraLayer {id (L0-L8), description, current_implementation}
  - Issue {gh_number, gh_url, title, status, labels[], fitness_scores, system_prompt_version}
  - ConstitutionPrinciple {id (1-7), text}
  - ADR {id, title, decision, sinkra_state}

relations:
  - Pattern -OBSERVED_IN-> Repo
  - Issue -DERIVED_FROM-> Pattern
  - Issue -AFFECTS-> SinkraLayer
  - Issue -REINFORCES-> ConstitutionPrinciple
  - Issue -CONTRADICTS-> ADR
  - Issue -DUPLICATES-> Issue (pra dedup)
  - ADR -REJECTS-> Pattern
```

## Operação

### Modo VPS ($5/mês, sempre ligado)
- Cron a cada 4h
- ~6 investigações/dia → ~40/semana → GEPA cycle ~1x/semana
- Modelos: Haiku 4.5 varredura, Sonnet 4.6 síntese, Opus 4.7 GEPA judge
- Output: 1-3 issues/dia abertas no GitHub do sinkra-hub
- **Rate limit auto-aplicado**: máximo 5 issues abertas por dia pra não floodar

### Modo manual (boost)
- CLI `student propose --layer=L2 --against=BMAD-METHOD,paperclip`
- Útil quando você quer estudo focado em decisão pendente

### Modo "review meeting"
- Você triagia as issues no fluxo normal do GitHub (web ou `gh issue list -l student-agent`)
- Cada close/label alimenta GEPA na próxima sync

### Permissões (segurança)
- Token do GitHub usado pelo agente tem **escopo mínimo**: `issues:write` apenas
- **Sem** permissão pra: push, branch, PR, contents:write, workflows
- Issues abertas sempre com label `student-agent` pra filtragem fácil
- Auditoria: `gh issue list -l student-agent --state all` mostra tudo que o agente já fez

## Roadmap de implementação

### Fase 0 — fundação (1 semana)
- [ ] Subir gbrain local com schema acima
- [ ] Criar GitHub PAT com escopo `issues:write` apenas
- [ ] Criar labels no sinkra-hub: `student-agent`, `os-source:*`, `layer:L0..L8`, `principle:#1..#7`, `effort:S/M/L`, `risk:low/medium/high`, `approved`, `discussion`
- [ ] Adaptar `hermes-agent` com:
  - leitura de snapshot do sinkra-hub (HEAD, AGENTS.md, constitution) — read-only via `gh api`
  - geração de issue no formato canônico
  - submit via `gh issue create`
- [ ] `student.system.md` v0
- [ ] Rodar manual em 3 cruzamentos (ex: `agent-governance-toolkit` ↔ sinkra L7) — modo dry-run primeiro (gera markdown sem abrir issue)

### Fase 1 — autonomia (1 semana)
- [ ] Cron na VPS, hibernação, state em gbrain
- [ ] Sync periódica: agente lê estado das issues abertas pra dedup e fitness
- [ ] Rate limit: max 5 issues novas/dia
- [ ] Backlog: `gh issue list -l student-agent:backlog` (você cria issues pedindo investigações específicas)

### Fase 2 — auto-melhoria (1 semana)
- [ ] GEPA integrado, otimizando por taxa de aceitação real
- [ ] 4 eixos de fitness em LLM-as-judge
- [ ] Versionamento de system prompts + rollback
- [ ] Cada issue inclui `system_prompt_version: vN` no body pra rastrear qual versão produziu

### Fase 3 — escala (contínuo)
- [ ] Subagents `superpowers` pra cruzamentos pesados (>3 repos OS de uma vez)
- [ ] Webhook: commit no sinkra-hub dispara investigação relevante (read-only)
- [ ] Síntese mensal: issue resumo `[student-agent] Monthly digest` com top patterns
- [ ] Dashboard: heatmap (sinkra_layer × repo_OS) com cobertura — pode ser issue fixada ou GitHub Project

## Métricas de sucesso (90 dias)

Tudo mensurável via `gh issue list -l student-agent`:

- **≥ 100 issues abertas**
- **Taxa de aceitação ≥ 30%** (closed:completed + approved + merged) / total decidido
- **≥ 20 issues viraram PR mergeado** no sinkra-hub
- **Cobertura: cada uma das 8 camadas SINKRA estudada contra ≥ 3 repos OS**
- **GEPA: system prompt em v3+ com taxa de aceitação crescente entre versões**
- **Knowledge graph: ≥ 50 patterns documentados, ≥ 30 com origem em múltiplos repos**
- **Zero ações destrutivas**: nenhuma escrita fora de `issues` na API do GitHub (auditável via audit log)

## Princípios

1. **Único canal de saída: GitHub issues.** Agente não escreve código, não abre PR, não faz commit, não cria branch, não toca em arquivos do working tree do sinkra-hub. Só `gh issue create`.
2. **Token com escopo mínimo** (`issues:write`). Sem permissão técnica de fazer mais do que abrir issues, mesmo que tente.
3. **Toda issue é acionável** — refs a arquivos com permalinks, mudança concreta, não conceito.
4. **Constitution é lei** — proposta que viola principle é rejeitada antes de virar issue.
5. **Memória > computação** — gbrain acumula valor; relatórios individuais são descartáveis.
6. **Rejeição é sinal** — issue fechada como `not_planned` vira input pro GEPA, não lixo.
7. **Rate limit duro** — max 5 issues/dia. Se agente "quer" abrir mais, vai pra fila e abre amanhã.
8. **KISS no próprio agente** — Student-Agent não pode ser mais complexo que aquilo que ele propõe simplificar.

## Conexão com outros casos de uso

Mesma arquitetura (Hermes + gbrain + GEPA) serve outros agentes auto-melhoráveis:

| Variante | Fitness | Output |
|----------|---------|--------|
| **Student-Agent** (este) | taxa de aceitação humana | propostas pro sinkra-hub |
| **Clone-Agent** | fidelidade ao corpus do clonado | textos no estilo Alan |
| **Bench-Agent** | qualidade de scorecard | comparativos n-way no `OS/_bench/` |

Construir Student-Agent primeiro **valida o stack** pra depois aplicar nos outros casos. Se Hermes + gbrain + GEPA funcionar pra propor melhorias com taxa de aceitação > 30%, a arquitetura está provada.
