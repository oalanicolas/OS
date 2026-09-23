# O que estávamos deixando passar — revisão 2026-09-05

Auditoria do cluster de second-brain / taxonomia / benches.  
**P0 = fato errado no fio. P1 = ainda mede a palavra. P2 = buraco conhecido.**

---

## P0 — fato (já corrigido nesta passagem, onde dava)

| Buraco | Onde estava | Correção |
|--------|-------------|----------|
| **D-cons invertido** | taxonomia + `second-brain-protocols`: “takes → facts” | Primário: `hot facts → cold takes`. Takes de terceiros **nunca** entram em facts. `OS/gbrain/docs/takes-vs-facts.md` |
| **mem0 R@k no clone** | scorecard 92 com LoCoMo 92.5 / LME 94.4 | README L54: scores da **plataforma gerenciada**, opts proprietárias, `top_200`. OSS ≠ o número. Flag no scorecard; **não** baixei a nota à mão (seria inventar outro número) |
| **writeback = push** | protocolos implicavam captura ambiente junto do volunteer | Push = leitura, default-on no host. `memory.auto_writeback` **off** por default, opt-in. `ambient-writeback.md` |
| **hub fingerprint = auth** | “recusa search se o hub driftou” | CLI recusa *encaminhar ao hub*; o path direto continua. Não é ACL. (apontado na revisão VISA/MKT de `second-brain-convergence.md`) |
| **IDs colidem** | job `M1` vs citação Markdown `[M1]` no convergence VISA/MKT | `taxonomy.md` §13: neste cluster `job:M1`, nunca âncora `[M1]` |

O arquivo `_research/second-brain-convergence.md` **não é mais o memo de produto de setembro** que este agente escreveu. Foi substituído por uma revisão VISA-BRAIN / MKT-LENDARIO que *corrige* vários dos P0 acima. Dois documentos no mesmo path = o tipo de colisão que a taxonomia existe para impedir. Não mesclei os dois neste passo.

---

## P1 — ainda mede / ainda mistura

| Buraco | Por que passa |
|--------|----------------|
| **confidence HIGH** no 5-way com mem0 92 plataforma | Deveria ser MEDIUM em `recall_accuracy` do M3. Não rebaixei o overall neste passo. |
| **M3 no mesmo ranking que M1/M2** | Jobs diferentes. Ranking admitido M1–M4 ainda *ordena* SDK contra arquivo fiel. O pack premia local-first; M3 perde por kind, não por ser pior SDK. Comprar pelo rank ainda erra se ignorar o ID — o executive agora diz isso, o **número** ainda está na mesma tabela. |
| **M4 “só log de ação”** | Memori README também persiste conversas. Reduzimos o job demais. |
| **Matrizes** | `memory-5way/comparison-matrix.json` ainda lista gsd-2 sem `job_id`. MD 6-way agora tem ID; JSON não. |
| **`personal-assistant-3way` (abril)** | Pontua gbrain como assistente (canais 20%). Stale; contradiz “gbrain = M2, OpenClaw = host”. |
| **`quality_gate_passed: true`** | n-way sem gap-analysis; matrizes sem IDs até agora. O PASS é mecânico, não taxonômico. |
| **Protocolos sem IDs E/M** | `wake-protocols` / `host-protocols` ainda falam “gbrain” não `job:M2`. |
| **`CROSS-BENCH-SYNTHESIS.md`** | Não sabe M1–M4 nem exclusões. |
| **Pack yaml** | `dimension-packs.yaml` memory ainda cita `gsd-2` no description. A regra §12 não entrou no yaml. |
| **Inventários abril** | `_inventories/gbrain` foi refresh; copies em outros benches podem divergir. |
| **graph-pitfalls** | Tips de agosto; LME não reabre extract silencioso, mas SHA/versão estão velhos. |

---

## P2 — buracos que a taxonomia já nomeou e ninguém fechou

- Domínio **vida** sem jobs (TELOS, Pulse).  
- **M3** talvez seja kind integração, não job de saber.  
- Clawith E1+E3: sem teste “produto vs Frankenstein”.  
- Packs `wake` / `host` / `agent-brain` não existem — e **não devem** nascer só para caber a palavra.  
- Nenhum LME **OSS** re-rodado (gbrain-evals é sibling; mem0 platform não é o clone).  
- Compose legal Paperclip + OpenClaw + um `slots.memory` + gbrain volunteer: **não executado**.  
- Trabalho local **não commitado**.

---

## O que a revisão de ranking *não* resolveu sozinha

Tirar LifeOS do total ponderado impede o “5º cérebro”. Continua possível ler a tabela de dimensões (LifeOS 70.58 na mesma grade) como ranking. A linha † ajuda; um leitor apressado ainda soma.

Ordenar M1>M2>M3>M4 no mesmo pack continua sendo **uma** ordenação de store-features, útil para M1 vs M2 (verbatim vs síntese no yaml). Inútil para “qual second brain comprar”. O executive tem a frase; o cérebro humano lê a coluna Total primeiro.

---

## Próximo, se for para não deixar passar de novo

1. Rebaixar confidence do M3 recall **ou** `null` até haver número OSS.  
2. Separar visualmente a tabela admitida da diagnóstica (LifeOS/gsd-2 noutra secção, não coluna †).  
3. Renomear ou prefixar citações do convergence VISA/MKT (`[MKT-1]`) para não comer `job:M1`.  
4. Stamp `job_id` no `dimension-packs.yaml` description e no `personal-assistant-3way` (stale).  
5. Commit deste cluster para o path parar de ser reescrito por baixo.

---

_os-bench audit | 2026-09-05_
