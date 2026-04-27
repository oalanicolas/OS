# Scorecard — enterprise-platforms-5way

Calculo: `sum(cell_score * weight) * 20` — `cell_score` em 0-5 vindo de `comparison-matrix.md`, pesos do pack `enterprise-agents-10d` em `metadata.json`. Resultado em 0-100.

## Overall ranking

| # | Subject | Score (0-100) | Barra |
|---:|---|---:|---|
| 1 | **Clawith** | **84.20** | `██████████████████████████████████████████` |
| 2 | **agent-governance-toolkit** | **83.00** | `█████████████████████████████████████████` |
| 3 | **dify** | **74.00** | `█████████████████████████████████████` |
| 4 | **paperclip** | **68.20** | `██████████████████████████████████` |
| 5 | **memori-labs** | **58.00** | `█████████████████████████` |

## Per-dimension contribution (weighted, cada celula = score_celula × peso × 20)

| Dimensao | Peso | Clawith | AGT | Memori | Dify | Paperclip |
|---|---:|---:|---:|---:|---:|---:|
| Multi-tenancy | 0.12 | 12.0 | 7.2 | 9.6 | 9.6 | 12.0 |
| Governance & Audit | 0.13 | 10.4 | 13.0 | 2.6 | 7.8 | 10.4 |
| Paradigm flexibility | 0.11 | 8.8 | 11.0 | 8.8 | 4.4 | 6.6 |
| Memory architecture | 0.11 | 8.8 | 4.4 | 11.0 | 6.6 | 2.2 |
| Skill marketplace | 0.10 | 10.0 | 6.0 | 2.0 | 8.0 | 6.0 |
| Durability | 0.09 | 7.2 | 9.0 | 5.4 | 7.2 | 7.2 |
| Safety & sandboxing | 0.09 | 7.2 | 9.0 | 3.6 | 5.4 | 5.4 |
| Observability | 0.09 | 5.4 | 9.0 | 5.4 | 9.0 | 7.2 |
| Deployment flex | 0.08 | 8.0 | 8.0 | 4.8 | 8.0 | 6.4 |
| Community | 0.08 | 6.4 | 6.4 | 4.8 | 8.0 | 4.8 |
| **TOTAL** | **1.00** | **84.2** | **83.0** | **58.0** | **74.0** | **68.2** |

---

## Breakdown por foco

Reescalado para 0-100 dividindo pelo somatorio dos pesos das dimensoes incluidas.

### Focus: engineering team (paradigm_flex + skill_marketplace + deployment_flex + observability + community)

Peso somado: 0.46

| # | Subject | Score | Barra |
|---:|---|---:|---|
| 1 | **agent-governance-toolkit** | 87.83 | `███████████████████████████████████████████` |
| 2 | Clawith | 83.91 | `█████████████████████████████████████████` |
| 3 | dify | 81.30 | `████████████████████████████████████████` |
| 4 | paperclip | 67.39 | `█████████████████████████████████` |
| 5 | memori-labs | 56.09 | `████████████████████████████` |

**Leitura:** time de engenharia quer se plugar facil em qualquer stack, ter muitos tools, deploy ja resolvido e observability. AGT vence por ser framework-agnostic + SRE completo + SDKs em 5 linguagens.

### Focus: product team (multi_tenancy + skill_marketplace + memory_architecture + observability + community)

Peso somado: 0.50

| # | Subject | Score | Barra |
|---:|---|---:|---|
| 1 | **Clawith** | 85.20 | `██████████████████████████████████████████` |
| 2 | dify | 82.40 | `█████████████████████████████████████████` |
| 3 | agent-governance-toolkit | 66.00 | `█████████████████████████████████` |
| 4 | memori-labs | 65.60 | `████████████████████████████████` |
| 5 | paperclip | 64.40 | `████████████████████████████████` |

**Leitura:** time de produto quer compartilhar skills org-wide, isolar teams e nao perder contexto. Clawith vence com digital employees + Plaza + memoria por agente + multi-tenant nativo + marketplace de skills.

### Focus: enterprise governance (governance_audit + multi_tenancy + safety_sandboxing + durability + observability)

Peso somado: 0.52

| # | Subject | Score | Barra |
|---:|---|---:|---|
| 1 | **agent-governance-toolkit** | 90.77 | `█████████████████████████████████████████████` |
| 2 | Clawith | 81.15 | `████████████████████████████████████████` |
| 2 | paperclip | 81.15 | `████████████████████████████████████████` |
| 4 | dify | 75.00 | `█████████████████████████████████████` |
| 5 | memori-labs | 51.15 | `█████████████████████████` |

**Leitura:** governance/risk/compliance quer OWASP mapping, policy enforcement deterministico, audit trail, sandbox. AGT e a unica ferramenta com OWASP 10/10 explicitamente mapeado — ganha isolado. Clawith e Paperclip empatam com boa multi-tenancy + approval gates.

---

## Sinal por subject (headline)

- **Clawith** — campeao overall e campeao no foco "product team". Melhor combinacao de multi-tenancy + memoria por agente + skill marketplace + digital employees.
- **agent-governance-toolkit** — campeao no foco "engineering team" e "enterprise governance". Unico com OWASP Agentic 10/10 mapeado + deterministic policy + SRE completo. Mas e library, nao plataforma.
- **dify** — top 1 em community e observability; paradigm flexibility e o gargalo (trava em pipeline/low-code).
- **paperclip** — forte em multi-company isolation e governance-com-rollback. Perde duro em memory architecture (roadmap).
- **memori-labs** — campeao absoluto em memory architecture, mas nao e plataforma: nao tem skill marketplace, nao tem orchestration, governance minima.
