# OS update — convergência das melhorias (2026-08-23)

**Data:** 2026-08-23  
**Escopo:** os 34 repositórios de `repos.tsv`  
**Janela:** SHA local anterior → `origin/{branch}` após `./update.sh`  
**Método:** `git log`, `git diff`, release notes e paths locais. Commit count mede atividade, não qualidade.  
**Resultado da sincronização:** 23 fast-forwards, 9 já atualizados, 1 clone novo (`hermes-agent`) e 1 remoto indisponível (`next-level-outreach`).

---

## Veredito

**Os projetos não estão convergindo em “mais autonomia”. Estão convergindo em tornar a autonomia comprovável, limitada e recuperável.**

O padrão comum desta janela é um **control plane honesto**:

1. estado real vence narrativa do modelo;
2. toda execução longa ganha identidade, dono, lease e estado terminal;
3. retry deixa de ser a resposta universal — recovery passa a depender da fase e da evidência;
4. permissões, tempo, contexto, bytes e fan-out ficam limitados;
5. claims, traces e reviews passam a carregar provenance/content binding;
6. testes e evals deixam de ser relatórios e viram enforcement;
7. a mesma capability precisa funcionar em vários hosts sem fingir que todos têm o mesmo runtime.

Essa direção confirma parte da síntese de abril, mas muda a prioridade. O próximo moat para AIOX/gstack/gbrain não é adicionar outra persona, outro squad ou outro dashboard. É **fechar o ciclo claim → evidence → state transition → recovery**.

---

## Números da atualização

- 34 entradas no manifesto.
- 33 checkouts sincronizados com sucesso: 23 avançaram, 9 já estavam no topo e `hermes-agent` foi clonado.
- 5.749 commits recebidos nos 23 fast-forwards.
- O diff bruto soma ~2,37 M inserções e ~1,29 M deleções, mas é dominado por repos grandes, arquivos gerados, lockfiles e renames; não é métrica comparável de valor.
- `openclaw` sozinho responde por 3.073 commits; `gh-aw`, `codex`, `dify`, `paperclip` e `langfuse` também tiveram janelas grandes. Por isso, as conclusões abaixo exigem recorrência entre repos e evidência concreta — não volume.
- `next-level-outreach`: `git pull --ff-only` falhou com `Repository not found` para `https://github.com/henriquecaner/next-level-outreach`. O clone local foi preservado em `b9349db`; não houve tentativa de adivinhar novo owner/URL.

---

## 1. Estado real vence narrativa

Este foi o padrão mais forte da janela. Sistemas maduros estão removendo falsos verdes: “done” sem teste, “healthy” sem probe, “ok” quando houve erro, “current” sobre conteúdo já alterado.

Evidência cruzada:

- **gbrain** não checkpointa mais import com status `error` como concluído (`4e4677b1b`, `src/commands/sync.ts`) e o doctor não afirma que o supervisor está parado quando `--fast` nem executou a checagem (`eb247ad8f`, `src/commands/doctor.ts`).
- **LifeOS 7.40.4** deriva a faixa de fase do estado real, classifica claims por tipo de verificador e transforma cada achado de auditoria em gate determinístico (`Releases/v7.40.4/README.md`).
- **gstack 1.66.1** liga resultado de teste/review ao fingerprint do working tree; se o conteúdo muda, a evidência deixa de ser fresca (`bin/gstack-wtree`, `bin/gstack-evidence`, `1cab5e11`).
- **mem0** parou de apresentar erro de busca como resultado vazio (`a10c0cd0`, `integrations/mem0-plugin/scripts/_search.py`).
- **OpenClaw** mantém canais unhealthy como unhealthy após clock rollback, em vez de derivar readiness falsa (`a7d30b9bd28`, `src/gateway/channel-health-policy.ts`).
- **Mempalace** tornou re-mining e locks honestos e impede ingest de arquivo não regular de bloquear indefinidamente (`1654cd2`, `db29959`, `mempalace/miner.py`).

### O que isso ensina

No AIOX, `unknown`, `skipped`, `stale`, `partial`, `failed` e `settled` precisam ser estados distintos. Um check não executado nunca pode produzir verde; erro não pode virar lista vazia; output escrito não prova transição concluída.

**Regra proposta:** nenhum estado positivo sem `evidence_ref` verificável e compatível com o conteúdo/versão atual.

---

## 2. Recovery virou parte do modelo de domínio

Os bugs mais caros não são mais “a função falhou”. São execuções que ficam vivas sem poder terminar: lease morto, worker congelado, descendente órfão, timer consumido cedo, takeover automático sem autoridade.

Evidência cruzada:

- **gsd-pi** corrigiu attempts settled bloqueados por `orphaned-active-unit`, closeout interrompido por limite do provider e milestone reservations órfãs (`87607f6e`, `9004dc84`, `123dc58f`; `src/resources/extensions/gsd/auto-recovery.ts`, `task-settle.ts`, `orphan-milestone-discard.ts`).
- **Codex** encerra descendentes retomados quando a árvore é arquivada e introduziu suspensão explícita de root turn inacabado (`a1d4aea265`, `4f39251a01`; `thread_archive.rs`, `turn_suspension.rs`).
- **Paperclip** parou de tomar automaticamente tarefas stranded; recovery agora expõe ações e observabilidade em vez de assumir ownership (`f572e0867`, `server/src/services/recovery/`).
- **Workflow** re-arma continuação entregue cedo com nova chave de idempotência, cria step + evento atomicamente e prende IDs à ordem do event log (`bf9de1cd8`, `71bc027a6`, `9b1b8c711`).
- **OpenClaw** recupera follow-ups de runs settled, respeita cancelamento durante compaction e retoma runs após reconnect (`a77fbdef330`, `b26ee4fb350`, `9b9afc3fda6`).
- **gbrain 0.46.26** reparou private queues abandonadas com owner token, lease e lanes explícitas de recuperação (`CHANGELOG.md`, `69aea15e8`).

### O que isso ensina

Retry não é recovery. O contrato precisa modelar:

`queued → claimed → running → settling → settled | failed | cancelled | suspended`

Com invariantes:

- owner/lease para qualquer estado ativo;
- estado terminal monotônico;
- parent cancel/archive propaga para descendentes;
- idempotency key é renovada quando o evento anterior já foi consumido;
- takeover só com prova de lease expirado e ação registrada;
- toda recuperação informa de qual estado saiu, quem autorizou e qual evidência fechou a transição.

---

## 3. “Bounded” virou primitiva de segurança

Tempo, contexto, bytes, escopo e fan-out sem limite aparecem repetidamente como a mesma classe de defeito.

Evidência cruzada:

- **Paperclip** adicionou ledger de bytes agregado, limite de frame, chunking e transporte fail-closed para a ponte duplex (`05b35d466`, `c5050396c`, `141b81529`; `packages/adapter-utils/src/duplex-*`).
- **OpenHands** mantém o socket vivo, mas limita handshakes presos (`c59a28a24`, `src/utils/websocket-handshake.ts`).
- **Langfuse** limitou a claim query do scheduler de monitors (`93eb91d78`, `packages/shared/src/features/monitors/scheduler/scheduler.ts`).
- **GEPA** reduziu contexto reflexivo redundante e separou cache de valset de rollouts de treino (`b265bf9c`, `ef525a44`).
- **gstack** tornou evals pagos diff-billed e o suite gratuito sharded com deadlines e contrato de saída (`410b4928`, `CHANGELOG.md` 1.66.0.0).
- **Superpowers 6.3** agrupa microtarefas de mesmo formato, impede que implementadores/revisores gerem netos e usa waits event-driven no Codex (`RELEASE-NOTES.md`).
- **Codex** honra aprovações granulares de sandbox no unified exec (`9445ef227e`, `codex-rs/core/src/tools/handlers/unified_exec/exec_command.rs`).

### O que isso ensina

Todo capability AIOX deveria declarar budgets no contrato: `timeout`, `max_tokens/context`, `max_parallel`, `max_output_bytes`, `max_retries`, `allowed_scope` e política de override. Budget excedido deve produzir estado tipado — não timeout genérico nem retry infinito.

---

## 4. Provenance deixou de ser metadata decorativa

Vários projetos passaram a usar provenance para decidir comportamento, não apenas para mostrar auditoria depois.

Evidência cruzada:

- **Codex** tipa fragmentos de input/context, preserva kinds após merge e distingue thread de Guardian de subagent (`4582c0a498`, `c9b19deb09`; `context-fragments/`, `turn_metadata.rs`).
- **OpenHands** envia provenance de template versionado e correlaciona telemetria de conversa com identidade do Canvas (`b1f0accae`, `35331e795`; `src/manifests/manifest-validation.ts`).
- **gstack** adicionou evidence ledger, trust envelope para conteúdo de tracker e receipts hash-chained de egress (`1cab5e11`, `1d41ee3a`; `bin/gstack-evidence`, `bin/gstack-issue-guard`, `bin/gstack-egress`).
- **Workflow** usa ordem do event log como fonte determinística para correlation IDs (`9b1b8c711`).
- **Langfuse** preserva model prompts nos traces e liga evaluators aos scores (`b8e8c832d`, `c23526cbe`).
- **BMAD** passou review content/diff por path em vez de inline, preservando identidade do artefato revisado (`ea668933`, `1911f8a0`; `src/bmm-skills/ship/bmad-code-review/`).

### O que isso ensina

O envelope mínimo de execução deve viajar inteiro por handoff, merge, compaction e trace:

`artifact_id`, `content_hash`, `kind`, `origin`, `producer`, `thread_role`, `workspace`, `version`, `permissions`, `evidence_refs`, `created_at`.

Sem isso, reviewer pode validar outro diff, memory pode consolidar instrução como fato, trace pode perder o prompt que explica o resultado e claim antigo pode parecer atual após rebase.

---

## 5. Review está ficando adversarial e independente

O movimento não é simplesmente “mais reviewers”. É separar coleta, julgamento e adjudicação para evitar contaminação e consenso precoce.

Evidência cruzada:

- **BMAD** lança todas as camadas antes de consumir resultados, julga findings antes de agrupá-los e adiciona falsificação explícita de claims (`3fd6929e`, `0f5d5101`, `268dc28e`).
- **Codex** separa Guardian reviews de subagents no modelo de thread e preserva outcomes estritos de auto-review (`c9b19deb09`, `970b7f2ff4`).
- **gh-aw** adicionou adjudicação determinística de experimentos e PureLock para transformar funções puras em propriedades cobertas (`7b2adec18c`, `84c5956481`; `pkg/cli/experiments_decision.go`, `docs/adr/55077-*`).
- **LifeOS** fecha releases com duas auditorias read-only independentes e converte todo achado em gate permanente (`Releases/v7.40.4/README.md`).
- **gstack** usa duas lentes independentes por finding nas ondas de segurança e fixa cada propriedade com teste de regressão (`CHANGELOG.md` 1.67.1.0).

### O que isso ensina

O review AIOX deveria ter quatro etapas persistidas:

1. **collect** — todos os reviewers recebem o mesmo artefato/hash;
2. **independent review** — sem ver achados dos pares;
3. **adjudicate** — cada finding é confirmado, refutado ou marcado inconclusivo;
4. **regressionize** — finding confirmado vira teste/gate quando mecanizável.

Agrupar achados antes de julgá-los reduz diversidade; deixar o mesmo agente autorar e validar mantém o self-review disfarçado.

---

## 6. Observabilidade entrou no loop operacional

Tracing e dashboards estão deixando de ser camada lateral. Agora influenciam readiness, recovery, avaliação e controle humano.

Evidência cruzada:

- **Codex** expõe status runtime de conexão MCP e traces de criação de turn context (`343074d420`, `be6ebb1f6d`; `codex-rs/app-server-protocol/src/protocol/v2/mcp.rs`).
- **Dify** adicionou tracing unificado e neutro de provider (`3a8fbcbd02`, `api/core/ops/unified_trace/`).
- **Langfuse** lançou UX nova de evals, métricas de lifecycle de MicroVM e scheduler limitado/instrumentado (`a7fa476e7`, `43da57e29`, `93eb91d78`).
- **Paperclip** tornou recovery e transporte duplex observáveis com dispositions explícitas (`10d2781a2`, `f572e0867`).
- **LifeOS** passou a derivar dashboard/phase strip da mesma fonte de estado e finalmente incluiu o export estático no payload (`Releases/v7.40.4/README.md`).

### O que isso ensina

Health não é “processo está vivo”. Para cada capability, expor separadamente:

- liveness;
- readiness;
- current owner/lease;
- last successful transition;
- last failed transition + typed cause;
- queue depth/oldest age;
- budget consumido;
- evidence freshness.

Dashboard só deve render esses fatos; nunca inferir sucesso por ausência de erro.

---

## 7. Multi-host virou requisito de produto — e continua não sendo um prompt universal

A superfície compatível cresceu em paralelo em projetos diferentes.

Evidência cruzada:

- **Superpowers 6.3** adicionou Devin, Hermes e documentação Grok, além das embalagens Claude/Codex/Cursor/Kimi/Gemini (`b36e082`, `.devin-plugin/`, `.hermes-plugin/`, `.codex-plugin/`).
- **gbrain 0.46.18** adicionou skillpacks curados por persona, variantes de plugin e manifests Claude/Codex (`489e27757`, `plugin-variants/`).
- **BMAD** adicionou Grok como target do installer e continuou materializando skills por host (`c96b7d1d`, `tools/installer/`).
- **mem0** corrigiu plugins para Cursor/Codex/Antigravity e virou `MemoryStore` nativo do Strands (`530d802b`, `8d5b7865`).
- **OpenHands** passou a permitir seleção dos providers suportados (`4bf8dd3aa`).
- **ai-website-cloner-template** propagou fallback Atlas por todas as superfícies (`92872bc`, `.codex/skills/`, `.gemini/commands/`, `.cursor/commands/`, etc.).

### O que isso ensina

A tese anterior continua válida: **Agent Plugin é a caixa pública; Agent Skill é a porta; contrato AIOX fica interno**. A novidade é que compatibilidade agora precisa de matriz de testes por host, não apenas arquivos presentes.

Não copiar o gerador universal como SOT sem equivalence tests. Cada target deve provar discovery, trigger, tool mapping, consent e lifecycle no runtime real.

---

## 8. Cerimônia e autonomia estão sendo calibradas por risco

Outro sinal de maturidade: remover passos não implica remover gates. Projetos estão reduzindo cerimônia para trabalho pequeno e aumentando prova para trabalho perigoso.

Evidência cruzada:

- **Superpowers 6.3** roteia brainstorming em `spike`, `bounded` ou `architectural`; pequenas mudanças pulam o ritual de dois documentos, mantendo aprovação antes de implementar (`RELEASE-NOTES.md`).
- **LifeOS** dimensiona o brief do delegate pelo blast radius (`Releases/v7.40.4/README.md`).
- **BMAD** expõe escolhas reais no spec checkpoint e remove menus/notation que confundiam controle humano (`9b4df487`, `f7622389`, `67d876f1`).
- **Paperclip** removeu o passo “mission” do wizard, mas apertou auth, tenant binding, sandbox transport e permissões (`3ff636bc4`, `5bc6031f7`, `fbd20b28d`).
- **gstack** torna re-pairing para escopo menor revogação imediata do grant antigo (`85fd9db5`, `browse/src/token-registry.ts`).

### O que isso ensina

O número de documentos/personas não mede rigor. AIOX deve escolher o profile por risco:

- **spike:** timebox + sandbox + descarte;
- **bounded:** spec curta + teste focado + review único independente;
- **architectural/high-blast-radius:** ADR/spec, múltiplas lentes, dual-run/cutover e owner explícito.

O gate fica; a quantidade de papel muda.

---

## O que mudou desde a síntese de abril

| Lacuna de abril | Estado nesta janela | Evidência |
|---|---|---|
| Eval/observability nativa | **Fechando rapidamente** | Codex MCP/context trace; Dify unified trace; Langfuse eval UX; Paperclip recovery telemetry; LifeOS receipts |
| Durability + agentic safety unificadas | **Parcial; convergência forte nas bordas** | Workflow atomicidade/idempotência; gsd-pi leases/settle; Codex thread lifecycle; Paperclip recovery/tenant binding |
| Model switching/provider neutrality | **Parcial** | OpenHands provider selector; Dify provider-neutral trace; gbrain key-aware routing |
| Roundtrip code ↔ spec | **Ainda aberto** | BMAD melhora review por path/falsificação; spec-kit endurece workflow/manifest, mas reconciliação bidirecional continua ausente |
| Memory stack completo | **Ainda aberto; honestidade operacional melhorou** | gbrain sync/visibility/recovery; mempalace ingest/re-mine; mem0 integrações e erro ≠ vazio |
| Test generation a partir da intent | **Ainda aberto** | Houve grande avanço em gates/regressões, não em gerar teste correto da intenção |
| Multi-paradigm orchestration | **Ainda aberto** | Lifecycle ficou melhor, mas topologia continua fixa por produto |

Leitura: três gaps viraram foco explícito do mercado — observabilidade, durability/safety e provider neutrality. Os outros quatro continuam diferenciação disponível.

---

## Roadmap de absorção para AIOX

### P0 — control plane honesto

1. **Execution Envelope canônico**
   - IDs: run/turn/thread/parent/artifact/workspace.
   - `content_hash`, `kind`, producer, permissions, budgets e evidence refs.
   - Preservado em handoff, compaction, merge e trace.

2. **Lifecycle único para trabalho assíncrono**
   - Estados monotônicos e terminalidade explícita.
   - Owner + lease + renewal + expiry.
   - Cancel/archive em cascata.
   - Recovery actions tipadas; sem takeover silencioso.

3. **Honesty invariants**
   - `not_checked != passed`.
   - `error != empty`.
   - `artifact_written != settled`.
   - `process_alive != ready`.
   - `claim_valid` exige evidence atual para o content hash atual.

### P1 — prova e limites

4. **Evidence ledger content-bound**
   - Registrar comando, exit, content hash, timestamp e artifact refs.
   - Invalidar automaticamente quando o conteúdo muda.

5. **Review adjudication pipeline**
   - Fan-out simultâneo; findings cegos entre pares.
   - Falsification pass.
   - Confirm/refute/inconclusive antes de dedupe.
   - Achado confirmado vira regression guard.

6. **Budgets no capability contract**
   - Tempo, tokens/contexto, bytes/output, concorrência, retries e scope.
   - Override explícito e auditável.

### P2 — interoperabilidade e operação

7. **Matriz de compatibilidade executável**
   - Claude, Codex, Hermes, Grok/Devin onde houver target.
   - Testar discovery, trigger, tools, consent, teardown e upgrade.
   - Targets nativos; igualdade só quando provada.

8. **Health operacional por capability**
   - Liveness, readiness, lease, fila, budget, último sucesso/falha e evidence freshness.
   - Provider-neutral trace IDs no envelope.

9. **Evals por impacto**
   - Suite mínima sempre honesta.
   - Evals caros selecionados pelo diff + dependências afetadas.
   - Nenhum arquivo de teste fora do runner/CI.

### Critérios de aceite mínimos

- matar o processo em cada transição e provar retomada/terminalidade;
- repetir o mesmo evento e provar idempotência;
- alterar o working tree depois do teste e provar que a evidência fica stale;
- expirar lease e provar recovery autorizado, sem takeover prematuro;
- cancelar parent durante compaction/review e provar teardown dos descendentes;
- simular check pulado, erro de busca e probe indisponível e provar que nenhum vira verde;
- exceder cada budget e provar falha tipada;
- rodar o mesmo replay concorrente e obter os mesmos IDs/ordem.

---

## O que não copiar

- **Megawaves como método.** Release com 111 fixes ou milhares de commits pode conter trabalho excelente, mas volume não é arquitetura nem prova de absorção segura.
- **Auto-heal que reescreve autoridade.** Corrigir config ou tomar tarefa automaticamente sem lease/evidence cria falso verde e disputa de ownership.
- **Dashboard que infere.** UI bonita sobre estado derivado de logs incompletos repete exatamente os bugs que LifeOS/OpenClaw/gbrain corrigiram.
- **Compatibilidade por tradução cega.** N hosts listados no README sem testes reais só multiplica drift.
- **Mais personas para cobrir lifecycle ruim.** Nenhum papel compensa falta de estado terminal, idempotência e recovery.
- **Observabilidade sem ação.** Trace que não ajuda readiness, adjudication ou recovery é custo, não control plane.

---

## Delta por projeto atualizado

| Projeto | Commits | Melhoria dominante observada |
|---|---:|---|
| BMAD-METHOD | 24 | Review por path, falsificação de claims, fan-out antes de adjudicação, checkpoints mais claros, target Grok |
| OpenHands | 69 | Socket resiliente, provenance de templates/conversas, seleção de provider, instrumentação de onboarding |
| agent-governance-toolkit | 46 | Replay protection no Django trust middleware + atualização de supply chain/deps |
| ai-website-cloner-template | 3 | Fallback Atlas propagado pelas superfícies multi-host |
| codex | 537 | Thread/Guardian lifecycle, content kinds, suspensão/cancelamento, approvals granulares, status MCP e tracing |
| dify | 279 | RBAC em endpoints, tracing provider-neutral, agent runtime/home snapshot, simplificação de contratos/UI |
| gbrain | 136 | Honesty de sync/doctor, visibility uniforme, queue leases/recovery, skillpacks multi-host, key-aware routing |
| gepa | 5 | Menos contexto reflexivo, cache train/val isolado, batch eval correto |
| gh-aw | 676 | Adjudicação determinística de experimentos, PureLock, credential checks, erros padronizados e gates gerados |
| gsd-pi | 187 | State/lease/settle/recovery de auto-mode, verificação cross-platform e descarte limitado de órfãos |
| gstack | 14 | Evidence binding, egress receipts, evals por diff, security sweep, grants revogados imediatamente |
| hermes-agent | clone | Clone que faltava materializado; baseline local agora disponível em `f293e7206` |
| huashu-design | 2 | Reescrita de preparação cognitiva e ampliação das rotas visuais |
| langfuse | 232 | Eval UX, lifecycle metrics, monitor scheduler limitado, prompts preservados em traces |
| mcp-servers | 3 | Compatibilidade explicitamente limitada a MCP Python 1.x (`>=1.29,<2`) |
| mem0 | 30 | Strands MemoryStore nativo, correções multi-host, segurança de dependências, erro de busca honesto |
| memori-labs | 1 | Preview enterprise no README; mudança de posicionamento, não de runtime |
| mempalace | 23 | Re-mine/locks/ingest hardening e consistência de chunks multi-batch |
| openclaw | 3.073 | Gateway/worker/session recovery, health verdadeiro, cancelamento em compaction, performance e multi-platform |
| paperclip | 239 | Duplex sandbox com budgets, auth/tenant binding, recovery sem takeover automático, onboarding simplificado |
| spec-kit | 87 | Manifest/workflow validation fail-closed, adoção em projetos existentes, release 1.0.1 |
| superpowers | 1 | Devin/Hermes/Grok, cerimônia por risco, batching SDD, waits Codex event-driven, worktree safety |
| workflow | 78 | Idempotência, atomicidade, sealed event log, WebSockets, deterministic IDs e long-poll terminal |
| LifeOS | 4 | Receipts release: claim verifiers, gates de payload, auditoria dupla, dashboard real, zero-token heartbeat |

---

## Ledger da sincronização

| Projeto | Estado | Novos commits | SHA anterior → atual |
|---|---|---:|---|
| ADAS | já atualizado | 0 | `2702bee8f → 2702bee8f` |
| AI-Scientist-v2 | já atualizado | 0 | `96bd51617 → 96bd51617` |
| BMAD-METHOD | atualizado | 24 | `401814f2d → 67d876f1c` |
| Clawith | já atualizado | 0 | `251aeba8c → 251aeba8c` |
| OpenHands | atualizado | 69 | `2e7136cb6 → 1e995e89a` |
| agent-governance-toolkit | atualizado | 46 | `81955d480 → b57055888` |
| ai-website-cloner-template | atualizado | 3 | `3040f9c75 → 92872bc40` |
| aider | já atualizado | 0 | `5dc9490bb → 5dc9490bb` |
| autogen | já atualizado | 0 | `027ecf0a3 → 027ecf0a3` |
| claude-remote-manager | já atualizado | 0 | `5e8cb0389 → 5e8cb0389` |
| codex | atualizado | 537 | `91d6f4899 → c9b19deb0` |
| crewAI | já atualizado | 0 | `22e5d3988 → 22e5d3988` |
| dify | atualizado | 279 | `12e683840 → 8bdf702f7` |
| gbrain | atualizado | 136 | `99dd1a083 → 4e4677b1b` |
| gepa | atualizado | 5 | `81dbae904 → b265bf9ca` |
| get-shit-done | já atualizado | 0 | `bdcaab2c7 → bdcaab2c7` |
| gh-aw | atualizado | 676 | `f791e7b0b → 7b2adec18` |
| gsd-2 | já atualizado | 0 | `33c00aaff → 33c00aaff` |
| gsd-pi | atualizado | 187 | `95f8c3fbb → 87607f6e3` |
| gstack | atualizado | 14 | `94993f740 → 85fd9db55` |
| hermes-agent | clonado | — | `— → f293e7206` |
| huashu-design | atualizado | 2 | `1572d431f → d3a4685c6` |
| langfuse | atualizado | 232 | `803cd0f4a → 3c3ca18ee` |
| mcp-servers | atualizado | 3 | `76d64c822 → 599dafc10` |
| mem0 | atualizado | 30 | `14c431735 → 8d5b7865b` |
| memori-labs | atualizado | 1 | `538b61f24 → a7bf568cd` |
| mempalace | atualizado | 23 | `7db7e0bd4 → 359c579d2` |
| next-level-outreach | **pull falhou: remoto 404** | 0 | `b9349dbb0` preservado |
| openclaw | atualizado | 3.073 | `b9f5548b2 → 8578b8f55` |
| paperclip | atualizado | 239 | `1a377424d → 05b35d466` |
| spec-kit | atualizado | 87 | `f2583e675 → 27f50f7e6` |
| superpowers | atualizado | 1 | `44c9b2d6e → b36e0829c` |
| workflow | atualizado | 78 | `efbc408c4 → 3c0d60be9` |
| LifeOS | atualizado | 4 | `58381b3df → ce046f264` |

---

## Fontes locais principais

- `repos.tsv`, `update.sh`.
- `BMAD-METHOD/src/bmm-skills/ship/bmad-code-review/`.
- `codex/codex-rs/{context-fragments,core,app-server,app-server-protocol}/`.
- `gbrain/CHANGELOG.md`; `gstack/CHANGELOG.md`; `gsd-pi/CHANGELOG.md`.
- `LifeOS/Releases/v7.40.4/README.md`; `superpowers/RELEASE-NOTES.md`.
- `workflow/.changeset/{wait-continuation-rearm,atomic-step-created-event,log-order-draws,run-status-long-poll}.md`.
- `paperclip/packages/adapter-utils/src/duplex-*`; `paperclip/server/src/services/recovery/`.
- `openclaw/src/{gateway,agents}/`; `langfuse/packages/shared/src/features/`; `dify/api/core/ops/unified_trace/`.
- Commits e SHAs citados ao longo do memo.

_Research memo — atualização local e síntese cross-project; sem re-score dos benchmarks históricos._
