# OS update — convergência das melhorias (2026-09-05)

**Data:** 2026-09-05  
**Escopo:** os 34 repositórios de `repos.tsv` (estado no momento do `./update.sh`)  
**Janela:** SHA local de 2026-08-23 → `origin/{branch}` após o sync de hoje  
**Método:** `git log`/`git diff` nos clones, changelogs e paths locais. Commit count mede atividade, não qualidade.  
**Antecessor:** [`os-update-convergence-2026-08-23.md`](./os-update-convergence-2026-08-23.md)  
**Resultado da sincronização:** 23 fast-forwards, 10 já no topo, 1 remoto ainda 404 (`next-level-outreach`).

---

## Veredito

**A tese de 23/08 se confirmou e apertou.** Os projetos não estão adicionando autonomia. Estão impedindo que o *harness* — background default, recovery já consumida, spawn inferido, write race — transforme um contrato honesto em run stranded.

O padrão comum desta janela é um **dispatch/session contract que sobrevive à falha do host**:

1. filho backgroundado não pode prender o pai sem deadline + ramo de recovery;
2. a alavanca de recovery ela mesma envelhece — `recoveryActionId` consumido não é saída;
3. “done” continua sendo claim; o completion gate trata a resposta do modelo como pretensão;
4. modo degradado precisa de nome (`no_key`, `timeout`, `UNAVAILABLE`) — nunca `ready`/`no-cli` por inferência;
5. trigger de sessão spawned só vale se for eco machine-verifiable, não prosa no prompt;
6. mutação de grafo/memória sem fila serializada é perda silenciosa;
7. provenance ilegível falha fechada; volume de commits continua não sendo arquitetura.

O moat para AIOX não mudou de família. O que mudou é a borda: **fechar o ciclo claim → evidence → state transition → recovery não basta se o dispatch e a alavanca de recovery puderem mentir.**

---

## Números da atualização

- 34 entradas no manifesto.
- 33 checkouts sincronizados: 23 avançaram, 10 já estavam no topo.
- 17.112 commits recebidos nos 23 fast-forwards.
- `hermes-agent` (7.310) e `openclaw` (6.664) dominam o volume; juntos são ~82% dos commits. Conclusões abaixo exigem recorrência *entre* repos e path citado — não contagem.
- `next-level-outreach`: segundo sync consecutivo com `Repository not found` em `https://github.com/henriquecaner/next-level-outreach`. Clone local preservado em `b9349dbb0`. O manifesto passa a comentar a entrada para o `update.sh` deixar de falhar.

---

## 1. Dispatch deixou de ser “chamar o subagente”

O defeito mais caro desta janela é o pai que espera um JSON que nunca volta porque o host backgroundou o filho.

Evidência cruzada:

- **gstack 1.79.0.0** pinou `run_in_background: false` em todo dispatch síncrono e deu deadline + recovery aos quatro passos de `/ship` que parseiam a última linha como JSON. Terceira recorrência da classe #497/#2440. O pin mora em `test/run-in-background-guidance.test.ts`; o SoT da frase é `{{FOREGROUND_DISPATCH_NOTE}}` (`CHANGELOG.md` 1.79.0.0, `0d1bd5616`).
- **gstack 1.78.0.0** fechou o falso spawned: o trigger só vale o eco `SESSION_KIND: spawned` no preamble. Texto de prompt/arquivo não pode auto-decidir AskUserQuestion (`CHANGELOG.md` 1.78.0.0).
- **gsd-pi** aborta o turn do host em pause permanente do provider e admite blocker report no completion gate (`CHANGELOG.md` 1.16.2, `#1977`).
- **OpenClaw** unificou snapshots de admissão na recovery de restart e preserva outcomes de scheduled-run recuperados (`d56cfcbe8a3`, `76fb700f132`).
- **Paperclip** recupera sessões nativas no restart e sessões Codex ACPX já settled, sem retomar issue hidden (`7b094724e`, `96421b066`, `b98badb24`; `packages/paperclip-runner/docs/durable-recovery.md`).

### O que isso ensina

Todo fan-out AIOX precisa de um contrato de dispatch, não de uma esperança:

- foreground explícito **ou** poll com deadline e ramo de falha tipado;
- filho nunca muta VERSION/changelog/review do pai;
- trigger spawned é eco/env, nunca inferência de prosa;
- “zero comments” / “docs ok” sem retorno do filho é `UNAVAILABLE`, não sucesso.

**Regra proposta:** nenhum `await child` sem `deadline`, `on_timeout` e `failure_json`. Silêncio não é done.

---

## 2. A alavanca de recovery também fica stale

23/08 pediu owner/lease/estado terminal. Esta janela mostrou o próximo bug: a *saída* de recovery já foi gasta, ou aponta para um abort que o sucessor invalidou.

Evidência cruzada:

- **gsd-pi** — `finalize/retry` race + `gsd_task_recovery_resume` sem handler `remediate` deixa tarefa completed stranded (`5cb9410a`, `#2113`). Prompt de recovery autorizado fica stale depois que o auto claims o Attempt sucessor (`8ebd37ff`, `#1989`). Abort route stale é voided no reopen para as alavancas voltarem a viver (`CHANGELOG.md` 1.16.2, `#1948`). Tentativa settled morta pelo guard `orphaned-active-unit` sem resume (`#1942`). Mensagem em `src/resources/extensions/gsd/auto-recovery.ts` cita `recoveryActionId` já abortado e recusa re-dispatch.
- **Hermes 0.21.0** — lease de turn cross-process, escopo na conversation root; delegate child não compartilha lease do pai (`tests/state/test_session_turn_lease.py`, `#84234`). `agent/turn_recovery.py` repara in-place *antes* do retry genérico; `hermes_cli/update_receipt.py` preserva receipt ativo across module purge (`fada877519`).
- **Paperclip** — recovery durable autentica o transporte (ticket de 5s, HMAC do transcript, lease de conexão, counters anti-replay) antes de mandar `welcome` (`packages/paperclip-runner/docs/durable-recovery.md`).
- **Workflow** — settle do awaiter do hook *in-process* em vez de re-invocar; HMR de dev falha se o step registration ficou stranded (`7cc5c88a8`, `584155897`; `packages/core/src/runtime/suspension-handler.ts`).
- **Clawith v1.11.4/1.11.5** — runs longas recuperáveis across compression/deadlines; tool calls aceitas estáveis na recovery do Runtime; loops de repair irrecuperáveis terminam visíveis (`55e0ad8f`, `1dbad6d9`, `c9774e54`).

### O que isso ensina

Recovery precisa de **geração**. Não basta ter um `recoveryActionId`. O contrato é:

`lever_issued → lever_consumed | lever_voided | lever_superseded`

Invariantes:

- reopen/void invalida a rota de abort antiga;
- sucessor que claims o Attempt queima a alavanca do predecessor;
- lease de turn é por conversation root, não por processo;
- takeover só com prova de expiry **e** de que a alavanca ainda é a vigente.

---

## 3. Completion gate: a resposta do modelo é claim

23/08 já pedia evidence_ref. Agora o gate de “tarefa completa” virou um juiz separado.

Evidência cruzada:

- **Clawith** — completion gate independente: “The candidate answer is a claim, not evidence. Tool success is evidence only for what that Tool Result objectively proves.” Pass só com requisito explícito satisfeito; senão `repair` (`f79c210c`, `backend/app/services/agent_runtime/verification.py`). Consent de tool fica bound ao receipt (`e830e249`).
- **gstack 1.78** — Codex CLI que não executa reporta `broken_install`, nunca `ready`. Fallback same-family deixou de ser vendido como “cross-model coverage” (`CHANGELOG.md` 1.78.0.0, `#2745`, `#2735`).
- **gbrain 0.48.2.0** — reranker Voyage fail-open sem chave: `degraded: reranker_skipped (no_key)` em `search --explain` e `reranker_health` no doctor. Probe lenta de `--version` classifica `timeout`, nunca `no-cli` (`CHANGELOG.md` 0.48.2.0 / 1.78 cite `#2716`; `src/core/ai/gateway.ts`, `src/commands/doctor.ts`).
- **OpenHands** — policy de evidence em code review reforçada (`4524a9199`, `#17089`).
- **spec-kit** — preset fail-closed se provenance/registry for ilegível; entrada corrompida ≠ ausente (`8e0f0f74`, `src/specify_cli/presets/__init__.py`).

### O que isso ensina

O envelope de 23/08 ganha um campo operacional:

`completion_verdict ∈ {pass, repair}` + `evidence[]` + `missing_requirements[]`

Nenhum orquestrador AIOX deve aceitar a última mensagem do agente como terminalidade. Tool ok ≠ goal ok. `ready` é um status ganho, não o default da ausência de erro.

---

## 4. Modo degradado virou produto — e precisa ser medido

Evidência cruzada:

- **gbrain** publicou receipt LongMemEval no flip do reranker (2026-09-02, `172df271`, 470 scored): hybrid 93.19% recall_all@5; hybrid + `voyage:rerank-2.5` **95.32%**; hybrid + LLM multi-query expansion **54.89%** (harmful at small k). O modo `tokenmax` que liga expansion perde 183 questões que o hybrid acertava (`CHANGELOG.md` 0.48.2.0).
- **Mempalace 3.8/3.9** — fingerprint do backend e do embedding ativo; write guard de library stale no reconnect MCP; purge de closets stale (`e016aff`, `733a0c6`, `b55d032`, `f92095e`; `mempalace/config.py` `search_config_fingerprint`).
- **mcp-servers** — mutações do knowledge graph serializadas numa fila; falha de uma op não trava as seguintes (`d73f99ef`, `#4555`; `src/memory/index.ts` `withLock`).
- **GEPA** — release só passa se a CI do wheel verde (`0632cdb5`, `.github/workflows/build_and_release.yml`).
- **LifeOS** — só higiene nesta janela (issue templates + crédito de 29 contributors). O produto relevante continua sendo 7.40.4 Receipts, já absorvido em 23/08.

### O que isso ensina

Capability sem braço degradado nomeado é mentira de disponibilidade. AIOX deve expor:

- path default medido;
- path degradado medido (e *pior* quando o “upgrade” dilui evidência, como expansion@k=5);
- fingerprint do backend/embedding no health;
- write recusado se o library/index estiver stale.

---

## 5. Observabilidade e release viraram enforcement

Evidência cruzada:

- **Langfuse 4.21 → 4.30** em duas semanas; handbook de agents manda parar de inventar staleness (`51e2bfe99`, `#17075`).
- **gh-aw** — métricas MCP privacy-preserving nos usage artifacts; docs/skills stale corrigidos em série; Defender scan e block de release advisory-affected (`c5ef3e88b`, `da776ae173`).
- **Codex** — Guardian review evidence sobrevive a compaction; provenance MCP exposta ao lifecycle de tools; ambientes deferred recuperados após provision failure (`9f97cb79eb`, `21ff2e802c`, `e6249b5296`; `codex-rs/ext/guardian-v2/`).
- **BMAD 6.13.0-next** — stamper de release falha se skill directory não tem manifest; cada plugin do marketplace Claude é stampado (`26695850`, `edb144f3`).
- **OpenHands 1.16.0** — `base_url` de subscription LLM preservado (`2ead26e77`).

### O que isso ensina

Trace que não impede release podre é custo. O gate de corte AIOX deveria recusar: skill sem manifest, evidence de review perdida na compaction, métrica inventada, advisory conhecida no artefato publicado.

---

## O que mudou desde 23/08

| Lacuna em 23/08 | Estado em 05/09 | Evidência |
|---|---|---|
| Lifecycle + recovery | **Apertou na alavanca** | gsd-pi lever stale/consumed; Hermes turn lease; Paperclip durable transport |
| Honesty invariants | **Apertou no degradado nomeado** | gbrain `no_key`/`timeout≠no-cli`; gstack `broken_install≠ready` |
| Budgets / bounds | **Apertou no dispatch** | gstack foreground pin + 10 min recovery; OpenClaw byte cap de compaction |
| Provenance | **Fail-closed em preset** | spec-kit registry ilegível; Mempalace fingerprints; Codex Guardian across compaction |
| Review adversarial | **Virou completion gate** | Clawith claim≠evidence; OpenHands review evidence policy |
| Multi-host | **Incremental** | BMAD marketplace stamp; mem0 Strands/DeepSeek/Kimi changelogs; gsd-pi Hermes integration version bump |
| Roundtrip spec ↔ code | **Ainda aberto** | spec-kit 1.0.2–1.0.4 é release/provenance, não reconciliação bidirecional |
| Test from intent | **Ainda aberto** | Mais pins/regressions (gstack 8 660 testes), não geração da intenção |

Leitura: o mercado gastou estas duas semanas *operacionalizando* o control plane de 23/08. Os gaps de spec-roundtrip e test-from-intent continuam diferenciação.

---

## Roadmap de absorção — delta sobre 23/08

P0–P2 de 23/08 continuam válidos. Acrescentar:

### P0′ — dispatch e alavanca

10. **Dispatch contract** em todo fan-out síncrono: flag de foreground, deadline, `failure_json`, filho sem autoridade de VERSION/review.
11. **Recovery generation**: void/supersede da alavanca no reopen e no successor claim; recusar re-dispatch com `recoveryActionId` abortado.
12. **Completion gate independente**: a última mensagem do agente entra como `claim`; `pass` exige evidence atual.

### Critérios de aceite novos

- backgroundar o filho no host e provar que o pai termina com falha tipada, não hang;
- consumir a alavanca de recovery e provar que a segunda chamada é `lever_consumed`, não retry;
- desligar a API do reranker/modelo e provar `degraded` nomeado, nunca `ready`;
- compactar o thread e provar que Guardian/review evidence ainda está no envelope;
- duas mutações de grafo no mesmo turn e provar que as duas sobrevivem.

---

## O que não copiar (desta janela)

- **Megawave como método.** 7k commits de Hermes ou OpenClaw não são um design review. Absorver padrão recorrente, não o dump.
- **Expansion como default em k pequeno.** O receipt do gbrain mostra o “upgrade” derrubando recall de 93% para 55%.
- **Inferir spawned/ready/no-cli** a partir de prosa, timeout ou ausência de erro.
- **Re-dispatch com alavanca morta.** É o jeito mais rápido de cravar um wedge `orphaned-active-unit`.
- **Vender same-family como independência.** gstack já teve que desfazer esse copy.

---

## Delta por projeto atualizado

| Projeto | Commits | Melhoria dominante observada |
|---|---:|---|
| hermes-agent | 7.310 | Turn lease cross-process, turn_recovery antes do retry, receipt de update sobrevive a purge; volume alto — absorver o contrato, não o dump |
| openclaw | 6.664 | Session/restart recovery, scheduled-run outcomes, compaction heartbeat, memory path recovery; mesmo caveat de volume |
| codex | 607 | Guardian evidence across compaction, MCP provenance no tool lifecycle, recover deferred envs |
| gh-aw | 581 | MCP metrics privacy-preserving, harden de release/advisory, docs stale em série |
| paperclip | 406 | Durable runner recovery (native + Codex ACPX), transporte autenticado, stranded recovery ignora hidden |
| langfuse | 374 | Releases 4.21→4.30; handbook contra staleness inventada |
| dify | 339 | Gates de CI/e2e e readiness do console; pouco sinal estrutural novo vs 23/08 |
| mempalace | 149 | 3.8/3.9: fingerprints de backend/embedding, stale-library write guard, closet purge |
| BMAD-METHOD | 145 | 6.13.0-next: stamper fail-closed sem manifest, marketplace Claude stampado |
| Clawith | 128 | v1.11.4/1.11.5: completion gate claim≠evidence, runs recuperáveis, consent bound a receipt |
| gsd-pi | 121 | 1.16.2→1.17.0: lever stale/consumed, orphaned-active-unit, provider pause honesta, recover de SUMMARY legado |
| spec-kit | 73 | 1.0.2–1.0.4: provenance/registry fail-closed |
| OpenHands | 59 | 1.16.0; review evidence policy; preserve `base_url` |
| workflow | 54 | Hook awaiter settled in-process; fail em step registration stranded |
| gbrain | 33 | 0.48.2.0: Voyage rerank default, `no_key` fail-open, LongMemEval 95.32% vs expansion 54.89% |
| mcp-servers | 27 | Fila serializada em mutações do memory graph |
| mem0 | 15 | Bumps de SDK/CLI/plugin; changelogs Strands/DeepSeek/Kimi |
| gstack | 10 | 1.70→1.79: ship não strand, spawned echo-only, `broken_install≠ready`, upgrade restore |
| agent-governance-toolkit | 7 | Refresh de dependência AES do benchmark |
| gepa | 4 | Release gated na CI / testes do wheel |
| LifeOS | 4 | Higiene (issue template + créditos); produto segue em 7.40.4 |
| huashu-design | 1 | Self-check de versão a cada 30 dias |
| memori-labs | 1 | Use case enterprise no README |

---

## Ledger da sincronização

| Projeto | Estado | Novos commits | SHA anterior → atual |
|---|---|---:|---|
| ADAS | já atualizado | 0 | `2702bee8f → 2702bee8f` |
| AI-Scientist-v2 | já atualizado | 0 | `96bd51617 → 96bd51617` |
| BMAD-METHOD | atualizado | 145 | `67d876f1c → beb368e5f` |
| Clawith | atualizado | 128 | `251aeba8c → 45fc701c3` |
| OpenHands | atualizado | 59 | `1e995e89a → 2ead26e77` |
| agent-governance-toolkit | atualizado | 7 | `b57055888 → 359a2332f` |
| ai-website-cloner-template | já atualizado | 0 | `92872bc40 → 92872bc40` |
| aider | já atualizado | 0 | `5dc9490bb → 5dc9490bb` |
| autogen | já atualizado | 0 | `027ecf0a3 → 027ecf0a3` |
| claude-remote-manager | já atualizado | 0 | `5e8cb0389 → 5e8cb0389` |
| codex | atualizado | 607 | `c9b19deb0 → 51c97f3a6` |
| crewAI | já atualizado | 0 | `22e5d3988 → 22e5d3988` |
| dify | atualizado | 339 | `8bdf702f7 → dde1d500b` |
| gbrain | atualizado | 33 | `4e4677b1b → 8c70f6255` |
| gepa | atualizado | 4 | `b265bf9ca → 0632cdb5d` |
| get-shit-done | já atualizado | 0 | `bdcaab2c7 → bdcaab2c7` |
| gh-aw | atualizado | 581 | `7b2adec18 → c5ef3e88b` |
| gsd-2 | já atualizado | 0 | `33c00aaff → 33c00aaff` |
| gsd-pi | atualizado | 121 | `87607f6e3 → e34e7d7d0` |
| gstack | atualizado | 10 | `85fd9db55 → 0d1bd5616` |
| hermes-agent | atualizado | 7.310 | `f293e7206 → 9dd6634c5` |
| huashu-design | atualizado | 1 | `d3a4685c6 → a790f704d` |
| langfuse | atualizado | 374 | `3c3ca18ee → 7637df1e1` |
| mcp-servers | atualizado | 27 | `599dafc10 → d73f99efb` |
| mem0 | atualizado | 15 | `8d5b7865b → dae67f74f` |
| memori-labs | atualizado | 1 | `a7bf568cd → 10d650150` |
| mempalace | atualizado | 149 | `359c579d2 → d5250c788` |
| next-level-outreach | **pull falhou: remoto 404 (2ª vez)** | 0 | `b9349dbb0` preservado; entrada comentada no manifesto |
| openclaw | atualizado | 6.664 | `8578b8f55 → d4d766d39` |
| paperclip | atualizado | 406 | `05b35d466 → 1dceee9a4` |
| spec-kit | atualizado | 73 | `27f50f7e6 → 4a7341a93` |
| superpowers | já atualizado | 0 | `b36e0829c → b36e0829c` |
| workflow | atualizado | 54 | `3c0d60be9 → c12933292` |
| LifeOS | atualizado | 4 | `ce046f264 → 5e2f2e8c0` |

---

## Fontes locais principais

- `repos.tsv`, `update.sh`.
- `gstack/CHANGELOG.md` 1.78–1.79; `gstack/test/run-in-background-guidance.test.ts`.
- `gbrain/CHANGELOG.md` 0.48.2.0; `gbrain/src/core/ai/gateway.ts`; `gbrain/src/commands/doctor.ts`.
- `gsd-pi/CHANGELOG.md` 1.16.2; `gsd-pi/src/resources/extensions/gsd/auto-recovery.ts`.
- `Clawith/backend/app/services/agent_runtime/verification.py`.
- `paperclip/packages/paperclip-runner/docs/durable-recovery.md`.
- `hermes-agent/agent/turn_recovery.py`; `hermes-agent/tests/state/test_session_turn_lease.py`.
- `spec-kit/src/specify_cli/presets/__init__.py`.
- `mcp-servers/src/memory/index.ts`.
- `workflow/packages/core/src/runtime/suspension-handler.ts`.
- `codex/codex-rs/ext/guardian-v2/`.
- `mempalace/config.py` (`search_config_fingerprint`).
- Memo anterior: `_bench/_research/os-update-convergence-2026-08-23.md`.

_Research memo — atualização local e síntese cross-project; sem re-score dos benchmarks históricos._
