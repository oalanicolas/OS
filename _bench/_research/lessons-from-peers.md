# Erros para não repetir — mecanismo, fix, invariante

**Date:** 2026-09-05 · **Deep**  
**Fontes:** issues+commits em `graph-pitfalls-and-lessons.md` (mina ago); CHANGELOG/README set; protocolos.  
**Não copiar código.** Copiar o **invariante**. O fix deles às vezes é parcial — copiar o invariante, não o patch incompleto.

Cada carta: o que quebrou → por que o silêncio → o que o fix *realmente* mudou → o que copiar → o teste → **em qual job** (não “consertar grafo” no produto errado).

---

## Como usar

Você está a montar E2/M2 (córtex), M1 (arquivo), E1 (nervoso) ou host.  
A família ☠️ aplica a **todo write path**. Over-typing é especialmente M2. Dual-SoT é todo o mundo. Temporal é M1 KG. Isolation é todo o mundo. Métrica mentirosa é todo o mundo.

`job:*` = `taxonomy.md`. Testes T1–T18 = catálogo em `graph-pitfalls-and-lessons.md`.

---

## Família A — Silêncio (parece ok)

### A1. Extract 0/N sem erro

**Quebrou:** gbrain #3038 — `DIR_PATTERN` ~16 dirs do wiki *do autor*. 4 370 páginas importadas → **21 edges**, 99,7% órfãs, **zero erro**. #3737 `extract --stale` aborta **exit 0**. #1184 dream extract **no-op** (0 links) enquanto extract manual funciona. #2849 webhook `noExtract` default → bookmark avança, edges eternamente stale.

**Por que silêncio:** o pipeline mede “rodei”, não “produzi arestas *dados os candidatos*”. Skip e fail usam o mesmo exit.

**Fix real:** fecharam #3038 no *seu* corpus; #3190 (open) — schema-pack `link_types` ainda **decorativo**, extractor preso ao whitelist. O patch não generalizou.

**Copiar:** `candidates > 0 && emitted == 0` → **fail do lote** com os dois números. Skip de extract é flag **ruidosa**, não default. Dream/webhook/CLI = **um** reconciler (#3607: fs-mode 0 edges, db-mode 1 533 no *mesmo* corpus).

**Não copiar:** outra whitelist de pastas “do nosso vocabulário”.

**Teste:** T1, T3. Fixture 100 notas fora da ontologia do autor → alarme, não 21 edges.

**Job:** todo ingest (M1 mine, M2 put, E4 capture).

### A2. Write “ok”, read 0

**Quebrou:** LifeOS #1409 — template sem `BEGIN ENTRIES`; write sucesso, read zero. gbrain #2822 — `put` stdin vazio → página que o embed `--stale` não vê. gsd #4967 — SQL swallow → `create_failed` genérico; auto-mode **continua**.

**Fix real:** round-trip no teste, não assert no write. Auto-mode não segue no zero.

**Copiar:** todo write tem read-back no CI. Empty body = reject. Exception não vira status genérico.

**Teste:** T12. LifeOS #1761: guard que só pega catástrofe deixa **erosão lenta** passar — teste de delta, não só de colapso.

---

## Família B — Semântica fabricada

### B1. Predicado forte sem texto

**Quebrou:** gbrain #3466 — `people/→companies/` ⇒ sempre `works_at` **sem ler o markdown**. **19 497** empregos falsos (artista works_at museu). Fix `dba0ae7b1`.

**Por que escala:** heurística de path é O(páginas), barata, e *parece* KG.

**Fix real:** pararam *essa* regra. Não proibiram predicados fortes em geral.

**Copiar:** ROLE/employment/autoria só com **span no texto** ou registo canónico. Adjacência de pasta ≤ `RELATED_TO` / candidate (não published).

**Teste:** T2. Fixture artista→museu; assert **não** ROLE_AT.

**Job:** M2 extract. M1 que faz KG explícito (`kg_add`) já recusa isto por desenho — não “melhorar” o palácio com auto-`works_at`.

### B2. Identidade = cosseno

**Quebrou:** mem0 #5438 merge 0.95; #5587 pessoa Apple + empresa Apple; #5439/#5597 merge **cruza** `user_id`. mempalace #1605 stopwords viram people; #1557 case-insensitive no init, **case-sensitive no mine** (`Aya` ≠ `aya`).

**Fix real:** denylist; realpath+normcase no cache (#1372). Merge por embedding **não** foi resolvido de forma geral no OSS mem0 — eles **tiraram o grafo externo**.

**Copiar:** identidade = **tipo + workspace + alias registry**. Embedding = fila de candidatos. Matching case-fold **um** em todos os paths.

**Não copiar:** threshold único 0.95; Neo4j+Cypher de LLM (mem0 saiu do OSS: hyphen #4154, cleanup, prefix merge #5630).

**Teste:** T11, T6, T7 (attribution `""` reject — memori #578).

**Job:** M3 entity store, M2 pages, M1 entity registry. Não fundir M5 peer com M2 `people/alice`.

### B3. Slug ≠ texto

**Quebrou:** gbrain #1964 `[[AI 3.0]]` vs slug `ai-3.0` → 0 edges. #2367 `normalizeBasename` come CJK. #1846 resolver dropa target **unambiguous**.

**Copiar:** uma função canónica de slug; candidatos não resolvidos → **lista auditável**, não drop.

**Teste:** nomes com acento/CJK/ponto. T3 paridade.

---

## Família C — Dual-SoT e “existe no README”

### C1. Grafo lê MD; verdade está no SQL

**Quebrou:** gsd #5149 graph só do markdown; SQLite memories = SoT (ADR-013) → `capture_thought` **invisível** no grafo. #5755 cutover: parar dual-write; MD = projeção. #6342 capture sem `structuredFields` → KNOWLEDGE.md **tabelas vazias** com 40+ memórias no DB. #6414 scanner de migração **antes** do DB open → “12/12 não migrados” **falso**.

**Fix real:** cutover explícito. Saúde de migração só com DB aberto + receipt.

**Copiar:** `canonical_write_set ∩ projection_write_set = ∅`. Rebuild do grafo **só** da autoridade. Apagar a projeção **não** apaga prova.

**Job:** E4 (gsd), M2 (links table vs markdown — gbrain já reconcilia no markdown path; `--by-mention` #3674 **só adiciona** — re-scan deixa stale+corretas). Re-extract = **reconcile set** (add+remove por origem), T16.

### C2. Shipado, unwired, sem deps

**Quebrou:** LifeOS #1605 `MemoryGraph.ts` importa graphology; **package.json só `yaml`** → grafo morto no install fresco. #1172 dashboard “0 edges” com corpus cheio. #1255 retriever **só top-level** de KNOWLEDGE. #1573 `getRelevantContext` no Telegram, **não** no CLI. gbrain #2089 takes.embedding **sem writer** — busca vetorial de takes estruturalmente morta. mem0 #6591 AGENTS.md documenta graph **removido**.

**Fix real:** #1573 wired no CLI (MemoryTurnStart). graphology no install ainda é a lição: smoke de **install fresco**.

**Copiar:** `documented_feature F ⇒ smoke(F) on fresh install + main operator path`. Path que o humano usa, ou a feature **não existe**.

**Teste:** T18. CI: clone limpo, um traversal.

### C3. Dois vivos depois da “migração”

**Quebrou:** OpenClaw honcho setup **non-destructive** — files sobem, originais ficam. Builtin + Honcho = dois E3/M5.

**Copiar:** migração declara o SoT *depois*. Sem cutover = dual-SoT. (Mesma família que gsd #5755, outro produto.)

---

## Família D — Isolamento

### D1. Scope que não é porta

**Quebrou:** honcho — named scope é **projeção**; unscoped vê tudo; allowlist ≠ N named scopes (só `explicit`). gbrain `visibility: world` = agentes *deste* brain, não internet. memori #404 headers MCP de attribution **manuais** → mix de projetos.

**Copiar:** default fail-closed em read compartilhado. Attribution **obrigatória e não vazia**. Não vender tenant se o unscoped é o mundo.

**Job:** M5, M2 company brain (I-source), host.

### D2. Cache e singleton

**Quebrou:** mempalace #1372 `/palace` vs `/Palace` vs symlink → **dois caches**. Fix: `realpath` + `normcase`. #1136 `_kg` module-level; `MEMPALACE_PALACE_PATH` rotaciona → **SQLite errado**.

**Copiar:** chave = path canónico (ou case id). Zero singleton global de grafo. Um grafo por connection.

**Teste:** T6. Dois workspaces no mesmo processo.

### D3. Soft-delete pela metade

**Quebrou:** gbrain #1702 / #3754 — search/list filtram `deleted_at`; `get_links` / `backlinks` / `graph-query` **não**. Health fix #1305 **só** no getHealth.

**Copiar:** **toda** leitura (traversal, export, think gather) o mesmo predicado de lifecycle. Patch numa superfície ≠ o grafo.

**Teste:** T4. Delete → ausente de *todas* as APIs de grafo.

### D4. Race no RMW

**Quebrou:** mem0 #6243 `_upsert_entity` sem lock → perde `linked_memory_ids`. gbrain **já tranca** `auto_link:${slug}` no put concurrente. mempalace file lock no mine (#784). LifeOS #1711 `review-state.json` **global** → N sessões corrompem.

**Copiar:** lock/lease por unit. Estado de run por `session_id`/`run_id`, nunca arquivo global da máquina.

**Teste:** T13. Dois writers, zero lost edges.

---

## Família E — Tempo

### E1. Intervalo invertido e dois presentes

**Quebrou:** mempalace #1214 `valid_to < valid_from` **armazenado**, invisível a todo `as_of` — P0. `invalidate`+`add` date-only → as_of `D` devolve **ambos**. Fix: reject no write; `supersede()` atómico; half-open `[from, to)` (`9815f0a`, #1913).

**Copiar:** um primitivo de supersession. Proibir hand-roll invalidate+add. Validator no write.

**Não copiar:** o SQLite deles; copiar o invariante.

**Teste:** T8, T9.

**Job:** M1 KG; qualquer fato mutável (cargo, status). mem0 #4956 v3 extraction **ADD-only** → “works at A” e “works at B” convivem para sempre.

### E2. “March 2026” = vazio silencioso

**Quebrou:** mempalace #1164 / #1167 NL date → empty, **indistinguível** de “sem fato”. Fix: `sanitize_iso_temporal` + raise.

**Copiar:** parse estrito; erro tipado ≠ empty set.

### E3. Cursor de relógio

**Quebrou:** mempalace coordination: `since_created_at` **pula** evento entre réplicas (append order ≠ wall clock). Lei: `since_event_id`.

**Copiar:** cursor de log = id de append. Relógio é janela, não cursor.

**Job:** I-hub, qualquer frota.

---

## Família F — A métrica e o retrieve mentem

### F1. O path default não é o do paper

**Quebrou:** gbrain hybrid caiu a **51,3%** LME (fusion keyword-fallback inédito); vector puro 93%. v0.48 restaurou 93,19% e **confessou** no CHANGELOG. `tokenmax` expansion: **93% → 54,89%** nos mesmos 470q.

**Copiar:** bench no **binário/modo que o usuário liga**. “Máximo” sem o mesmo harness é regressão. Graph signals fail-open **só no rank** (×1.05) — nunca na conclusão.

### F2. Placar de outro artefato

**Quebrou:** mem0 README L54 — 92,5 / 94,4 = **plataforma gerenciada**, `top_200`, opts proprietárias. O clone OSS não é isso. Nosso scorecard 92 **superestima** o local (flag, nota não inventada).

**Copiar:** o número tem que nomear o artefato (OSS vs cloud vs `top_200` vs R@5).

### F3. Hybrid que descarta a lista B

**Quebrou:** mem0 #5742 BM25/entity scoreados; **só** top-k semântico no rank final. gsd #4497 FTS5 ausente → LIKE **silencioso**.

**Copiar:** união explícita antes de fundir. Degradação → `degraded:true` no receipt, não fallback quieto.

**Teste:** T14.

### F4. Health composto

**Quebrou:** gbrain #3591 — 13 908 links no store; `link_coverage: 0` e `link_density_score: 25` (full marks) no **mesmo** payload. #2931 engine `direction both` certo; **tree printer esconde** inbound. gsd #5148 CLI graph existe; slash **não**.

**Copiar:** métrica de grafo = **a query do produto**. Health que mascara zero → fail. Teste no artefato que o operador **vê**.

**Teste:** T5.

### F5. Grafo no gather ≠ páginas na síntese

**Quebrou:** gbrain #2903 `query` rank #1; `think` Pages:0 Graph:1 → “no information”. #2365 think free-form **sem** auto-anchor; query relacional já faz walk. #2556 `think --take` → Takes:0 silencioso. Config `0` virava default (#3552).

**Copiar:** graph hit sem extract reaberto → **não** concluir. Flag de persistência sem side-effect = erro. `0` configurado é 0, não “use default”.

**Teste:** T15.

### F6. Volunteer KPI e quarantine

**Quebrou:** gbrain `--stats` `used` = throttle 5 min (falso ±). OpenClaw context engine throw → **quarantine** + `legacy`; o chat não avisa.

**Copiar:** heurística ≠ probabilidade. Fail-open no *reply* ≠ fail-silent no *ops*. Doctor faz parte do protocolo.

### F7. Writeback ≠ push

**Quebrou:** (nós.) Volunteer default-on no host. `memory.auto_writeback` **off**. Autorizar ponteiro não autoriza gravar.

**Copiar:** T-push e writeback são dois contratos. Opt-in no write.

---

## Família G — Compact, wake, filho

| Quebrou | Invariante |
|---------|------------|
| Compact come verbatim | compact = wake: bank/flush/REFRESH **antes** de sumir o texto |
| `isolatedSession` + `delta` | `session_id` estável, não o id da sessão fresca |
| Sub-agent OpenClaw | só `AGENTS.md`; MEMORY/SOUL **não** herdam |
| Paperclip scoped-wake | **não** reabrir inbox (skill skip 1–4) |
| LifeOS 1.5K × N prompts | hot-layer: first / changed / REFRESH — eles **mediram** o spam |
| Heartbeat OpenClaw vs Paperclip | `NO_REPLY` ≠ janela de adapter. Automations ≠ scratch |

---

## Família H — Nome da tabela ≠ direção

**Quebrou:** (nós, lendo `takes`/`facts`.) Consolidate = `hot facts → cold takes`. Takes de terceiros **nunca** entram em facts.

**Copiar:** ler o `→` no doc primário. Marketing “Dream” são D-cons / D-hygiene / D-promo / D-deriver / D-route — cinco loops.

---

## O que **não** reimplementar (já queimaram o OSS)

| Evitar | Evidência |
|--------|-----------|
| Neo4j/Memgraph + Cypher de LLM | mem0 removeu do OSS |
| `DIR_PATTERN` do wiki pessoal | #3038 |
| `works_at` por pasta | #3466 |
| Dual-write MD+SQL sem cutover | gsd #5755 |
| Merge threshold 0.95 | #5438 |
| KG singleton + path string cache | mempalace #1136/#1372 |
| `invalidate`+`add` date-only | supersede commit |
| Health que mascara zeros | #3591 |
| Extract skipped por default no webhook | #2849 |
| Attribution opcional no header | memori #404 |
| `tokenmax` / fusion sem o bench do default | gbrain 0.48 CHANGELOG |
| Transferir placar Platform → SDK | mem0 README L54 |

---

## Gates (antes de shipar)

Do catálogo T1–T18, os que pagam mais se existirem **amanhã**:

| # | Se falhar, você repetiu |
|---|-------------------------|
| T1 | #3038 |
| T2 | #3466 |
| T3 | #3607 fs vs db |
| T4 | #1702 soft-delete |
| T5 | #3591 health |
| T9 | dois fatos no dia D |
| T10 | gsd dual-SoT |
| T11 | Apple+Apple |
| T15 | think sem páginas |
| T16 | #3674 add-only re-extract |
| T18 | #1605 install sem graphology |

---

## Por job (não aplicar o kit inteiro no produto errado)

| Job | Prioridade |
|-----|------------|
| **M1** | temporal (E1–E3), denylist entity, cursor de log, empty ≠ parse fail |
| **M2** | silêncio extract, over-type, um reconciler, graph≠think, fusion default, facts→takes |
| **M3** | merge/identity, RMW lock, **não** Neo4j, placar ≠ OSS |
| **M4** | attribution obrigatória; não reduzir a “só log” se há conversas |
| **M5** | named ≠ allowlist ≠ auth; unscoped |
| **E1** | heartbeat ≠ dump; scoped-wake; coalesce |
| **E3 / host** | filho não herda; compact+flush; quarantine visível; um memory slot |
| **life-OS** | skill-gated write; retriever no CLI; deps no install |

---

## Ligação

| Artefato | Papel |
|----------|--------|
| `graph-pitfalls-and-lessons.md` | mina (issues, T1–T18) |
| `visa-brain-graph-feature-lessons.md` | consumer VISA, doutrina↔enforcement |
| **este** | mecanismo → invariante → teste → job |
| `taxonomy.md` | para não “consertar o grafo” no SDK |

---

_os-bench lessons v2 | 2026-09-05_
