# Padrões recorrentes — 12 vendors de enterprise AI agents

## 1. Headline templates dominantes

Três fórmulas repetem-se:

**Template A — "Build/Ship/Create [X] for [Y]"** (7/12)
- Dify: "Build Production-Ready AI Agent"
- LangChain: "Ship agents that work wow"
- OpenHands: "Build with coding agents, your way"
- MS Copilot Studio: "Create, customize, and launch AI agents easily"
- CrewAI: "Accelerate AI agent adoption" (variante)
- aider: "AI pair programming in your terminal" (variante)
- Knowledge Plane: "Shared Memory for Engineering Teams" (variante)

**Template B — "[Marca] é [categoria] para [ICP]"** (3/12)
- LangSmith: "AI Agent Observability Platform"
- Salesforce: "The AI Agent Platform"
- Glean: "Work AI that works for all"

**Template C — Contraste poético** (2/12)
- mem0: "AI Agents Forget. Mem0 Remembers."
- Clawith: "OpenClaw empowers individuals. Clawith scales it to frontier organizations."

Observação: Template C é o mais memorável e o menos usado. Sweet spot para AIOX.

## 2. Pain narratives convergentes

Categorias de dor que aparecem repetidas:

- **Context loss / memory** — mem0, Knowledge Plane ("working off last month's context"), Glean (info fragmentada)
- **Debug / observability / opacity** — LangChain ("Agents can be hard to debug"), LangSmith ("what your agents are really doing")
- **Engineering toil** — OpenHands ("Reduce engineering toil"), aider (implícito)
- **Adoption speed / fragmentation** — CrewAI ("adoption across departments"), Dify ("all in one place")
- **Labor scarcity / scale** — Salesforce ("limitless digital labor force"), Glean ("every employee")

**Não verbalizadas bem por ninguém:**
- Custo operacional de agentes em produção (só mem0 toca via tokens)
- Governança / auditoria / compliance (só Glean toca via "permissions enforcement")
- LGPD/data residency (ninguém fala PT-BR ou soberania de dados)
- Failure recovery e retry semantics
- Fadiga de POCs que não viram produção

## 3. CTA patterns

Três famílias:

- **"Start building" / "Try for free" / "Get Started"** — Dify, LangChain, LangSmith, MS CS, Clawith, aider, OpenHands (self-serve)
- **"Get a demo" / "Request a demo"** — CrewAI, Glean, Salesforce (top-down sales)
- **Secundárias criativas:**
  - mem0: "Setup in 60 seconds" (tempo como CTA)
  - Clawith: "Try Now →" (urgência)
  - CrewAI: "Build a crew" (brand-verb)
  - OpenHands: "Try it live" (não "free" — confiança)
  - Knowledge Plane: "Apply for Beta Access" (exclusividade)

"Apply for Beta" e "Build a crew" são os únicos que fogem do padrão genérico.

## 4. Positioning axis — distribuição

| Eixo | Count | Vendors |
|---|---|---|
| Platform | 9 | Clawith, Dify, CrewAI, LangChain, mem0, Salesforce, MS CS, Knowledge Plane, LangSmith |
| Product | 2 | OpenHands, Glean |
| Dev tool | 1 | aider |
| Framework | 0 | — |
| Service | 0 | — |

**"Platform" é o commodity word**. Quem diz "platform" está dizendo nada. Espaço para AIOX se posicionar como "product" (solução completa) ou criar uma categoria nova.

## 5. Social proof tropes

- **Logo wall** em 10/12 (exceções: Clawith, Knowledge Plane — early stage)
- **Case study com métrica hard** em 6/12 (LangChain, OpenHands, Glean, MS CS, mem0, CrewAI)
- **Métricas favoritas:** % redução em tempo/tickets/cost; "X hours saved/week"; "N weeks to deploy"
- **Nomeados com cargo:** Glean (Booking, TIME, Bill), mem0 (OpenNote), Dify (Volvo, Ricoh)
- **Fortune 500 claim:** só MS Copilot Studio usa ("90%")

## 6. Missing patterns — oportunidades

O que quase ninguém faz:

- **Vídeo demo em destaque** — maioria esconde em "Watch video" secundário
- **Pricing totalmente transparente com calculator** — só Dify e mem0 chegam perto
- **Founders visíveis / narrativa de origem** — zero vendors têm founder no hero
- **ROI calculator interativo** — nenhum
- **Comparação side-by-side explícita contra concorrentes** — nenhum (Knowledge Plane chega perto em subtexto RAG)
- **Métrica de custo em moeda** (vs % ou horas) — só mem0 toca
- **Copy em PT-BR nativo (não traduzido)** — zero (CrewAI tem Piracanjuba como logo mas o site é inglês)
- **Transparência de limitações / failure modes** — nenhum vendor admite o que não faz bem
- **SLA / uptime commitments no hero** — zero
- **Time-to-first-agent métrica** — só mem0 ("60 seconds") e Glean ("three weeks") chegam perto
- **Aposta em compliance específica (LGPD, HIPAA, SOC2) no hero** — zero
