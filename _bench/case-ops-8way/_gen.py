#!/usr/bin/env python3
"""Generate case-ops-8way JSON artifacts. Run from OS/ root."""
import json
from pathlib import Path

ROOT = Path("_bench/case-ops-8way")
INV = Path("_bench/_inventories")
SUBS = [
    "VISA-BRAIN",
    "gbrain",
    "gsd-pi",
    "superpowers",
    "spec-kit",
    "paperclip",
    "mempalace",
    "LifeOS",
]
DIMS = [
    ("epistemology", "Epistemology", 0.18),
    ("projection_integrity", "Projection Integrity", 0.14),
    ("workspace_isolation", "Workspace Isolation", 0.14),
    ("extract_before_reviewed", "Extract-before-reviewed", 0.14),
    ("graph_honesty", "Graph Honesty", 0.12),
    ("counsel_separation", "Collector ≠ Auditor", 0.12),
    ("human_data_split", "Human/Data Split", 0.08),
    ("process_spine", "Process Spine", 0.08),
]
SCORES = {
    "epistemology": {
        "VISA-BRAIN": 96, "gbrain": 82, "gsd-pi": 50, "superpowers": 48,
        "spec-kit": 62, "paperclip": 55, "mempalace": 70, "LifeOS": 58,
    },
    "projection_integrity": {
        "VISA-BRAIN": 94, "gbrain": 80, "gsd-pi": 86, "superpowers": 72,
        "spec-kit": 84, "paperclip": 78, "mempalace": 68, "LifeOS": 70,
    },
    "workspace_isolation": {
        "VISA-BRAIN": 96, "gbrain": 78, "gsd-pi": 82, "superpowers": 70,
        "spec-kit": 62, "paperclip": 80, "mempalace": 74, "LifeOS": 60,
    },
    "extract_before_reviewed": {
        "VISA-BRAIN": 95, "gbrain": 55, "gsd-pi": 72, "superpowers": 88,
        "spec-kit": 65, "paperclip": 50, "mempalace": 52, "LifeOS": 45,
    },
    "graph_honesty": {
        "VISA-BRAIN": 93, "gbrain": 62, "gsd-pi": 45, "superpowers": 35,
        "spec-kit": 35, "paperclip": 40, "mempalace": 78, "LifeOS": 50,
    },
    "counsel_separation": {
        "VISA-BRAIN": 94, "gbrain": 40, "gsd-pi": 75, "superpowers": 90,
        "spec-kit": 70, "paperclip": 72, "mempalace": 30, "LifeOS": 35,
    },
    "human_data_split": {
        "VISA-BRAIN": 94, "gbrain": 70, "gsd-pi": 48, "superpowers": 50,
        "spec-kit": 55, "paperclip": 72, "mempalace": 60, "LifeOS": 88,
    },
    "process_spine": {
        "VISA-BRAIN": 92, "gbrain": 70, "gsd-pi": 90, "superpowers": 90,
        "spec-kit": 88, "paperclip": 80, "mempalace": 40, "LifeOS": 72,
    },
}

JUST = {
    "epistemology": {
        "VISA-BRAIN": "Layers A/B/C + Fact/Claim/Inference/AgencyFinding; category errors blocked.",
        "gbrain": "Takes vs facts + dream consolidate; no government-finding layer.",
        "gsd-pi": "DECISIONS.md / REQUIREMENTS.md — project memory, not claims.",
        "superpowers": "Process discipline, not an evidence epistemology.",
        "spec-kit": "Spec-as-SoT + constitution; no fact/finding split.",
        "paperclip": "Issues/comments as work objects; no claim vs finding.",
        "mempalace": "Verbatim drawers; no legal layers.",
        "LifeOS": "TELOS/ISA identity, not evidence assessment.",
    },
    "projection_integrity": {
        "VISA-BRAIN": "Dashboard/hot-index/DAG-DIGEST are generated; fingerprint rebuild; portal ≠ vault.",
        "gbrain": "Markdown SoT; Postgres rebuildable cache; compiled truth rewritten.",
        "gsd-pi": ".gsd/ checkboxes are SoT; STATE derived from files.",
        "superpowers": "Ledger + git; no generated operator dashboard.",
        "spec-kit": "spec/plan/tasks files; managed AGENTS block.",
        "paperclip": "Dashboard + continuation_summary; wiki plugin opt-in.",
        "mempalace": "Drawers on disk; little projection layer.",
        "LifeOS": "ISA as living spec; CLAUDE.md is a map.",
    },
    "workspace_isolation": {
        "VISA-BRAIN": "One explicit case root; product kit ≠ workspace; never scan siblings.",
        "gbrain": "Source + OAuth isolation; reads not prefix-private.",
        "gsd-pi": "Worktree leases + fencing; team mode is humans sharing .gsd/.",
        "superpowers": "Plan-scoped worktree; host cwd still implicit.",
        "spec-kit": "Feature dirs; no multi-vault fail-closed.",
        "paperclip": "companyId scope; org chart is not ACL.",
        "mempalace": "Local palace; no product/data kit split.",
        "LifeOS": "User tree; not case-workspace isolation.",
    },
    "extract_before_reviewed": {
        "VISA-BRAIN": "apply-batch rejects reviewed without hash-bound unit extract.",
        "gbrain": "put_page has no reviewed-extract contract.",
        "gsd-pi": "Verify/reviewer gates; not extract-before-reviewed.",
        "superpowers": "Prompt-enforced brief+review; no script reject.",
        "spec-kit": "Checklists; no extract contract.",
        "paperclip": "Comments/docs optional; no extract gate.",
        "mempalace": "Recall skill; no review ledger.",
        "LifeOS": "No extract-before-done machine.",
    },
    "graph_honesty": {
        "VISA-BRAIN": "Graph is index; candidates ≠ proof; SAME_ORIGIN_GROUP; no ranking-as-corroboration.",
        "gbrain": "Zero-LLM edges + graph-signals reorder top-K fail-open; #3466 class risk.",
        "gsd-pi": "memory_relations enum; not an evidence graph.",
        "superpowers": "No evidence graph.",
        "spec-kit": "No evidence graph.",
        "paperclip": "No evidence graph in core.",
        "mempalace": "Temporal KG with supersede/half-open; not a truth oracle.",
        "LifeOS": "Declared MD edges; analytics not counsel gates.",
    },
    "counsel_separation": {
        "VISA-BRAIN": "Collector / $review / $counsel clean session; P6 breaker; coverage ≠ eligibility.",
        "gbrain": "No collector≠auditor; think is the same mind.",
        "gsd-pi": "Three milestone reviewers; not counsel lenses.",
        "superpowers": "Separate implementer and reviewer + breaker.",
        "spec-kit": "type:gate human approve/reject.",
        "paperclip": "QA agent + board; CEO must not IC.",
        "mempalace": "No auditor role.",
        "LifeOS": "No independent counsel skill.",
    },
    "human_data_split": {
        "VISA-BRAIN": "Voice Card/USER never hold evidence; portal is projection + capture.",
        "gbrain": "Two-repo split; USER in agent repo.",
        "gsd-pi": "No Voice/USER contract; KNOWLEDGE.md mixes rules.",
        "superpowers": "Host identity files; no evidence firewall.",
        "spec-kit": "No USER/evidence firewall.",
        "paperclip": "Portal + PARA on $AGENT_HOME; SOUL collapsed in AGENTS.md.",
        "mempalace": "Identity L0 vs drawers; not a legal firewall.",
        "LifeOS": "USER/ISA/constitution split is first-class.",
    },
    "process_spine": {
        "VISA-BRAIN": "P0–P7 + freeze/pack fail-closed + honest close speech.",
        "gbrain": "Day ingest + night dream; not a case phase machine.",
        "gsd-pi": "Milestone/slice/task auto + verify.",
        "superpowers": "brainstorm→plan→SDD→finish.",
        "spec-kit": "specify→gate→plan→tasks→implement.",
        "paperclip": "Goal→issue tree→heartbeat; not P0–P7.",
        "mempalace": "Search-before-answer; no case phases.",
        "LifeOS": "TELOS→ISA→Algorithm; life ops not case ops.",
    },
}

SIG = {
    "epistemology": {
        "VISA-BRAIN": [
            {"signal": "A/B/C layers", "value": "government vs prep vs ingest", "evidence": "VISA-BRAIN/00-Case-Control/Epistemology-Layers.md"},
            {"signal": "category errors blocked", "value": "argument≠evidence; score≠finding", "evidence": "VISA-BRAIN/00-Case-Control/knowledge-model.json"},
        ],
        "gbrain": [
            {"signal": "takes vs facts", "value": "multi-holder vs owner hot memory", "evidence": "OS/gbrain/docs/takes-vs-facts.md"},
            {"signal": "compiled truth", "value": "rewrite vs timeline append", "evidence": "OS/gbrain/docs/guides/compiled-truth.md"},
        ],
        "gsd-pi": [
            {"signal": "DECISIONS.md", "value": "append-only project decisions", "evidence": "OS/gsd-pi/gsd-orchestrator/SKILL.md"},
            {"signal": "REQUIREMENTS.md", "value": "capability contract", "evidence": "OS/gsd-pi/gsd-orchestrator/SKILL.md"},
        ],
        "superpowers": [
            {"signal": "no evidence ontology", "value": "skills are process", "evidence": "OS/superpowers/README.md"},
            {"signal": "spec in plans", "value": "implementation plans not claims", "evidence": "OS/superpowers/skills/writing-plans/SKILL.md"},
        ],
        "spec-kit": [
            {"signal": "spec-driven.md", "value": "spec is SoT", "evidence": "OS/spec-kit/spec-driven.md"},
            {"signal": "constitution", "value": "principles file", "evidence": "OS/spec-kit/templates/constitution-template.md"},
        ],
        "paperclip": [
            {"signal": "issues as work", "value": "no claim/finding types", "evidence": "OS/paperclip/docs/start/core-concepts.md"},
            {"signal": "goal tree", "value": "alignment not epistemology", "evidence": "OS/paperclip/packages/db/src/schema/goals.ts"},
        ],
        "mempalace": [
            {"signal": "verbatim policy", "value": "do not paraphrase user text", "evidence": "OS/mempalace/CLAUDE.md"},
            {"signal": "temporal triples", "value": "valid_from/valid_to", "evidence": "OS/mempalace/mempalace/knowledge_graph.py"},
        ],
        "LifeOS": [
            {"signal": "ISA", "value": "claims/features living spec", "evidence": "OS/LifeOS/LifeOS/install/skills/ISA/SKILL.md"},
            {"signal": "LoadContext", "value": "constitution vs dynamic", "evidence": "OS/LifeOS/LifeOS/install/hooks/LoadContext.hook.ts"},
        ],
    },
    "projection_integrity": {
        "VISA-BRAIN": [
            {"signal": "hot-index fingerprint", "value": "rebuild if stale; never authority", "evidence": "VISA-BRAIN/.codex/skills/investigate-case-evidence/references/evidence-graph.md"},
            {"signal": "dashboard generated", "value": "build_dashboard_projection.py", "evidence": "VISA-BRAIN/AGENTS.md"},
        ],
        "gbrain": [
            {"signal": "system of record", "value": "git markdown; DB cache", "evidence": "OS/gbrain/docs/architecture/system-of-record.md"},
            {"signal": "compiled truth rewrite", "value": "timeline append-only", "evidence": "OS/gbrain/docs/guides/compiled-truth.md"},
        ],
        "gsd-pi": [
            {"signal": "checkbox SoT", "value": ".gsd/ ROADMAP/PLAN", "evidence": "OS/gsd-pi/gsd-orchestrator/SKILL.md"},
            {"signal": "STATE derived", "value": "never hand-edit required", "evidence": "OS/gsd-pi/gsd-orchestrator/SKILL.md"},
        ],
        "superpowers": [
            {"signal": "sdd ledger", "value": "progress.md plan-scoped", "evidence": "OS/superpowers/skills/subagent-driven-development/SKILL.md"},
            {"signal": "git history", "value": "workspace deleted after merge", "evidence": "OS/superpowers/skills/subagent-driven-development/SKILL.md"},
        ],
        "spec-kit": [
            {"signal": "spec persistence", "value": "flow-back/forward/living", "evidence": "OS/spec-kit/docs/concepts/spec-persistence.md"},
            {"signal": "feature dirs", "value": "spec.md plan.md tasks.md", "evidence": "OS/spec-kit/templates/spec-template.md"},
        ],
        "paperclip": [
            {"signal": "continuation_summary", "value": "issue document", "evidence": "OS/paperclip/docs/agents-runtime.md"},
            {"signal": "status cards", "value": "compiled watched queries", "evidence": "OS/paperclip/docs/guides/board-operator/status-cards.md"},
        ],
        "mempalace": [
            {"signal": "layers L0–L3", "value": "identity vs drawers", "evidence": "OS/mempalace/mempalace/layers.py"},
            {"signal": "markdown drawers", "value": "verbatim store", "evidence": "OS/mempalace/CLAUDE.md"},
        ],
        "LifeOS": [
            {"signal": "ISA living", "value": "claims/features SoT", "evidence": "OS/LifeOS/LifeOS/install/skills/ISA/SKILL.md"},
            {"signal": "CLAUDE routing", "value": "map not library", "evidence": "OS/LifeOS/LifeOS/install/hooks/LoadContext.hook.ts"},
        ],
    },
    "workspace_isolation": {
        "VISA-BRAIN": [
            {"signal": "PRODUCT.yml pin", "value": "0..N workspaces outside kit", "evidence": "VISA-BRAIN/AGENTS.md"},
            {"signal": "no sibling scan", "value": "one explicit case root", "evidence": "VISA-BRAIN/.codex/skills/investigate-case-evidence/SKILL.md"},
        ],
        "gbrain": [
            {"signal": "sources + OAuth", "value": "company-brain tutorial", "evidence": "OS/gbrain/docs/tutorials/company-brain.md"},
            {"signal": "prefix not private", "value": "privacy = own source", "evidence": "OS/gbrain/docs/architecture/brains-and-sources.md"},
        ],
        "gsd-pi": [
            {"signal": "worktree ADR", "value": "isolated implementation", "evidence": "OS/gsd-pi/docs/dev/ADR-001-branchless-worktree-architecture.md"},
            {"signal": "child flag", "value": "no recursive spawn", "evidence": "OS/gsd-pi/docs/user-docs/subagents.md"},
        ],
        "superpowers": [
            {"signal": "sdd-workspace", "value": "plan-scoped dir", "evidence": "OS/superpowers/skills/subagent-driven-development/SKILL.md"},
            {"signal": "git worktrees", "value": "using-git-worktrees", "evidence": "OS/superpowers/skills/using-git-worktrees/SKILL.md"},
        ],
        "spec-kit": [
            {"signal": "feature dir", "value": "scripts emit FEATURE_DIR", "evidence": "OS/spec-kit/scripts/python/setup_plan.py"},
            {"signal": "no multi-case lock", "value": "single project assumed", "evidence": "OS/spec-kit/spec-driven.md"},
        ],
        "paperclip": [
            {"signal": "company scoped", "value": "every entity companyId", "evidence": "OS/paperclip/docs/start/core-concepts.md"},
            {"signal": "org not ACL", "value": "visibility company-wide", "evidence": "OS/paperclip/docs/guides/board-operator/org-structure.md"},
        ],
        "mempalace": [
            {"signal": "local palace", "value": "on-device store", "evidence": "OS/mempalace/CLAUDE.md"},
            {"signal": "no kit/data split", "value": "single tree", "evidence": "OS/mempalace/README.md"},
        ],
        "LifeOS": [
            {"signal": "USER tree", "value": "personal knowledge", "evidence": "OS/LifeOS/README.md"},
            {"signal": "not case roots", "value": "one life OS", "evidence": "OS/LifeOS/LifeOS/install/hooks/LoadContext.hook.ts"},
        ],
    },
    "extract_before_reviewed": {
        "VISA-BRAIN": [
            {"signal": "apply-batch reject", "value": "reviewed requires unit extract", "evidence": "VISA-BRAIN/.codex/skills/investigate-case-evidence/SKILL.md"},
            {"signal": "hash + anchors", "value": "source_sha256 + locators", "evidence": "VISA-BRAIN/.codex/skills/investigate-case-evidence/references/evidence-graph.md"},
        ],
        "gbrain": [
            {"signal": "put_page", "value": "no reviewed-extract gate", "evidence": "OS/gbrain/docs/guides/compiled-truth.md"},
            {"signal": "volunteer_context", "value": "push pages not extracts", "evidence": "OS/gbrain/docs/guides/push-context.md"},
        ],
        "gsd-pi": [
            {"signal": "verify gate", "value": "milestone reviewers", "evidence": "OS/gsd-pi/docs/user-docs/subagents.md"},
            {"signal": "T##-SUMMARY", "value": "task completion files", "evidence": "OS/gsd-pi/gsd-orchestrator/SKILL.md"},
        ],
        "superpowers": [
            {"signal": "task-brief file", "value": "prompt-enforced", "evidence": "OS/superpowers/skills/subagent-driven-development/SKILL.md"},
            {"signal": "review-package", "value": "diff as file", "evidence": "OS/superpowers/skills/subagent-driven-development/SKILL.md"},
        ],
        "spec-kit": [
            {"signal": "checklist", "value": "completeness artifact", "evidence": "OS/spec-kit/templates/checklist-template.md"},
            {"signal": "no extract reject", "value": "commands not ledger", "evidence": "OS/spec-kit/templates/commands/implement.md"},
        ],
        "paperclip": [
            {"signal": "comments optional", "value": "no extract contract", "evidence": "OS/paperclip/docs/start/core-concepts.md"},
            {"signal": "heartbeat-context", "value": "pull not extract-gate", "evidence": "OS/paperclip/docs/agents-runtime.md"},
        ],
        "mempalace": [
            {"signal": "recall skill", "value": "search-before-answer", "evidence": "OS/mempalace/skills/mempalace-recall/SKILL.md"},
            {"signal": "no review ledger", "value": "not a case runner", "evidence": "OS/mempalace/README.md"},
        ],
        "LifeOS": [
            {"signal": "no extract machine", "value": "life ops", "evidence": "OS/LifeOS/README.md"},
            {"signal": "ISA completeness", "value": "CheckCompleteness", "evidence": "OS/LifeOS/LifeOS/install/skills/ISA/SKILL.md"},
        ],
    },
    "graph_honesty": {
        "VISA-BRAIN": [
            {"signal": "index not oracle", "value": "edge alone proves nothing", "evidence": "VISA-BRAIN/.codex/skills/investigate-case-evidence/references/evidence-graph.md"},
            {"signal": "SAME_ORIGIN_GROUP", "value": "independence ≠ file count", "evidence": "VISA-BRAIN/.codex/skills/investigate-case-evidence/references/evidence-graph.md"},
        ],
        "gbrain": [
            {"signal": "graph-signals", "value": "reorder top-K fail-open", "evidence": "OS/gbrain/src/core/search/graph-signals.ts"},
            {"signal": "zero-LLM inferLinkType", "value": "regex + role priors", "evidence": "OS/gbrain/src/core/link-extraction.ts"},
        ],
        "gsd-pi": [
            {"signal": "no evidence graph", "value": "milestone DAG only", "evidence": "OS/gsd-pi/gsd-orchestrator/SKILL.md"},
            {"signal": "handoff files", "value": "not typed edges", "evidence": "OS/gsd-pi/src/resources/skills/handoff/SKILL.md"},
        ],
        "superpowers": [
            {"signal": "no graph", "value": "process skills", "evidence": "OS/superpowers/README.md"},
            {"signal": "flowcharts", "value": "skill diagrams not evidence", "evidence": "OS/superpowers/skills/subagent-driven-development/SKILL.md"},
        ],
        "spec-kit": [
            {"signal": "no graph", "value": "workflow YAML", "evidence": "OS/spec-kit/workflows/speckit/workflow.yml"},
            {"signal": "handoffs", "value": "command chain", "evidence": "OS/spec-kit/templates/commands/specify.md"},
        ],
        "paperclip": [
            {"signal": "no evidence graph", "value": "issue tree only", "evidence": "OS/paperclip/docs/start/core-concepts.md"},
            {"signal": "org chart", "value": "reporting not proof", "evidence": "OS/paperclip/docs/guides/board-operator/org-structure.md"},
        ],
        "mempalace": [
            {"signal": "supersede()", "value": "atomic temporal replace #1913", "evidence": "OS/mempalace/CHANGELOG.md"},
            {"signal": "reject inverted interval", "value": "valid_to < valid_from", "evidence": "OS/mempalace/mempalace/knowledge_graph.py"},
        ],
        "LifeOS": [
            {"signal": "MD edges", "value": "wikilink/related", "evidence": "OS/LifeOS/LifeOS/install/skills/ISA/SKILL.md"},
            {"signal": "not counsel gate", "value": "analytics only", "evidence": "OS/LifeOS/README.md"},
        ],
    },
    "counsel_separation": {
        "VISA-BRAIN": [
            {"signal": "P6 independent audit", "value": "$review-immigration-evidence", "evidence": "VISA-BRAIN/.codex/skills/investigate-case-evidence/SKILL.md"},
            {"signal": "$counsel clean session", "value": "coverage-challenge after P7", "evidence": "VISA-BRAIN/AGENTS.md"},
        ],
        "gbrain": [
            {"signal": "think same mind", "value": "no auditor skill", "evidence": "OS/gbrain/README.md"},
            {"signal": "briefing read-only default", "value": "not independent counsel", "evidence": "OS/gbrain/skills/briefing/SKILL.md"},
        ],
        "gsd-pi": [
            {"signal": "3 reviewers", "value": "requirements/integration/acceptance", "evidence": "OS/gsd-pi/docs/user-docs/subagents.md"},
            {"signal": "not counsel", "value": "software verify", "evidence": "OS/gsd-pi/gsd-orchestrator/SKILL.md"},
        ],
        "superpowers": [
            {"signal": "task reviewer", "value": "spec + quality", "evidence": "OS/superpowers/skills/subagent-driven-development/SKILL.md"},
            {"signal": "breaker", "value": "5 rounds then adjudicate", "evidence": "OS/superpowers/skills/subagent-driven-development/SKILL.md"},
        ],
        "spec-kit": [
            {"signal": "type:gate", "value": "approve/reject", "evidence": "OS/spec-kit/workflows/speckit/workflow.yml"},
            {"signal": "human gate", "value": "not multi-lens counsel", "evidence": "OS/spec-kit/workflows/README.md"},
        ],
        "paperclip": [
            {"signal": "QA agent", "value": "qa-acceptance", "evidence": "OS/paperclip/packages/teams-catalog/catalog/bundled/company-defaults/core-exec-team/TEAM.md"},
            {"signal": "board", "value": "strategy/hire approvals", "evidence": "OS/paperclip/docs/start/core-concepts.md"},
        ],
        "mempalace": [
            {"signal": "no auditor", "value": "recall only", "evidence": "OS/mempalace/skills/mempalace-recall/SKILL.md"},
            {"signal": "PreCompact flush", "value": "not review", "evidence": "OS/mempalace/CLAUDE.md"},
        ],
        "LifeOS": [
            {"signal": "no counsel", "value": "life OS", "evidence": "OS/LifeOS/README.md"},
            {"signal": "DA self", "value": "same assistant", "evidence": "OS/LifeOS/LifeOS/install/hooks/LoadContext.hook.ts"},
        ],
    },
    "human_data_split": {
        "VISA-BRAIN": [
            {"signal": "interface contract", "value": "portal vs 00–14", "evidence": "VISA-BRAIN/00-Case-Control/Human-Data-Interface-Contract.md"},
            {"signal": "Voice Card firewall", "value": "no evidence in USER", "evidence": "VISA-BRAIN/AGENTS.md"},
        ],
        "gbrain": [
            {"signal": "two-repo", "value": "agent vs world", "evidence": "OS/gbrain/docs/guides/repo-architecture.md"},
            {"signal": "brain vs memory", "value": "routing table", "evidence": "OS/gbrain/docs/guides/brain-vs-memory.md"},
        ],
        "gsd-pi": [
            {"signal": "KNOWLEDGE.md", "value": "mixes rules and memory", "evidence": "OS/gsd-pi/gsd-orchestrator/SKILL.md"},
            {"signal": "no Voice Card", "value": "coding agent", "evidence": "OS/gsd-pi/README.md"},
        ],
        "superpowers": [
            {"signal": "host CLAUDE.md", "value": "no evidence firewall", "evidence": "OS/superpowers/AGENTS.md"},
            {"signal": "using-superpowers", "value": "process bootstrap", "evidence": "OS/superpowers/skills/using-superpowers/SKILL.md"},
        ],
        "spec-kit": [
            {"signal": "agent-context block", "value": "managed routing", "evidence": "OS/spec-kit/extensions/agent-context/"},
            {"signal": "no USER layer", "value": "spec files only", "evidence": "OS/spec-kit/spec-driven.md"},
        ],
        "paperclip": [
            {"signal": "PARA $AGENT_HOME", "value": "not company DB", "evidence": "OS/paperclip/skills/para-memory-files/SKILL.md"},
            {"signal": "SOUL collapsed", "value": "into AGENTS.md", "evidence": "OS/paperclip/packages/teams-catalog/catalog/bundled/company-defaults/core-exec-team/TEAM.md"},
        ],
        "mempalace": [
            {"signal": "L0 identity", "value": "~100 tokens", "evidence": "OS/mempalace/mempalace/layers.py"},
            {"signal": "verbatim drawers", "value": "user words preserved", "evidence": "OS/mempalace/CLAUDE.md"},
        ],
        "LifeOS": [
            {"signal": "USER tree", "value": "first-class", "evidence": "OS/LifeOS/README.md"},
            {"signal": "ISA vs USER", "value": "work vs person", "evidence": "OS/LifeOS/LifeOS/install/skills/ISA/SKILL.md"},
        ],
    },
    "process_spine": {
        "VISA-BRAIN": [
            {"signal": "P0–P7", "value": "investigate phases + gates", "evidence": "VISA-BRAIN/.codex/skills/investigate-case-evidence/SKILL.md"},
            {"signal": "freeze/pack", "value": "fail-closed --strict", "evidence": "VISA-BRAIN/AGENTS.md"},
        ],
        "gbrain": [
            {"signal": "dream cycle", "value": "night maintenance", "evidence": "OS/gbrain/src/commands/dream.ts"},
            {"signal": "ingest loop", "value": "daytime timeline", "evidence": "OS/gbrain/docs/guides/operational-disciplines.md"},
        ],
        "gsd-pi": [
            {"signal": "headless auto", "value": "spec → milestone", "evidence": "OS/gsd-pi/gsd-orchestrator/SKILL.md"},
            {"signal": "exit 10 blocked", "value": "steer or escalate", "evidence": "OS/gsd-pi/gsd-orchestrator/SKILL.md"},
        ],
        "superpowers": [
            {"signal": "SDD pipeline", "value": "brainstorm→plan→SDD", "evidence": "OS/superpowers/README.md"},
            {"signal": "finishing branch", "value": "merge options", "evidence": "OS/superpowers/skills/finishing-a-development-branch/SKILL.md"},
        ],
        "spec-kit": [
            {"signal": "workflow.yml", "value": "specify + gate + plan", "evidence": "OS/spec-kit/workflows/speckit/workflow.yml"},
            {"signal": "implement command", "value": "tasks → code", "evidence": "OS/spec-kit/templates/commands/implement.md"},
        ],
        "paperclip": [
            {"signal": "heartbeat", "value": "wake + checkout", "evidence": "OS/paperclip/docs/agents-runtime.md"},
            {"signal": "delegation", "value": "CEO breaks goals", "evidence": "OS/paperclip/docs/start/core-concepts.md"},
        ],
        "mempalace": [
            {"signal": "no phases", "value": "search/recall", "evidence": "OS/mempalace/skills/mempalace-recall/SKILL.md"},
            {"signal": "PreCompact", "value": "flush not spine", "evidence": "OS/mempalace/CLAUDE.md"},
        ],
        "LifeOS": [
            {"signal": "Algorithm climb", "value": "life ops", "evidence": "OS/LifeOS/README.md"},
            {"signal": "Pulse", "value": "voice/cron", "evidence": "OS/LifeOS/README.md"},
        ],
    },
}


def write_inv(slug, data):
    d = INV / slug
    d.mkdir(parents=True, exist_ok=True)
    (d / "inventory.json").write_text(json.dumps(data, indent=2) + "\n")
    lines = [
        f"# Inventory: {slug}",
        "",
        f"**Generated:** {data['generatedAt']}  ",
        f"**Path:** `{data['path']}`  ",
        f"**Confidence:** {data['confidence']}  ",
        f"**Extraction:** {data['extraction_method']}",
        "",
        f"> {data['tagline']}",
        "",
        "## Capabilities",
        "",
    ]
    for c in data["capabilities"]:
        ev = ", ".join(f"`{p}`" for p in c["evidence_paths"])
        lines.append(f"- **{c['name']}**: {c['description']} — {ev}")
    lines.append("")
    (d / "inventory.md").write_text("\n".join(lines) + "\n")
    (ROOT / f"inventory-{slug}.json").write_text((d / "inventory.json").read_text())
    (ROOT / f"inventory-{slug}.md").write_text((d / "inventory.md").read_text())


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    (ROOT / "deep").mkdir(exist_ok=True)

    # --- inventories new/refresh ---
    write_inv(
        "VISA-BRAIN",
        {
            "generatedAt": "2026-08-12T22:00:00Z",
            "subject": "VISA-BRAIN",
            "path": "VISA-BRAIN/",
            "location_note": "External product kit (not cloned under OS/). Citations are kit-relative. Evaluated from the author's usa-process checkout.",
            "primary_language": "Markdown",
            "secondary_languages": ["Python", "JSON"],
            "stack": ["stdlib Python validators", "SQLite investigation store", "Obsidian-friendly vault"],
            "license": "proprietary-product-kit",
            "tagline": "Case operating system for high-stakes immigration: vault is memory, agents operate it, graph is not a truth oracle.",
            "metrics": {
                "file_count": None,
                "skill_md_count": None,
                "last_commit_date": "2026-08-12",
                "source_url": None,
            },
            "modules": [
                {"name": "00-Case-Control", "path": "VISA-BRAIN/00-Case-Control/", "type": "library"},
                {"name": "investigate-case-evidence", "path": "VISA-BRAIN/.codex/skills/investigate-case-evidence/", "type": "app"},
            ],
            "external_dependencies_top10": [
                {"package": "Python 3.10+", "version": "stdlib only", "purpose": "validators and investigation_run"}
            ],
            "entry_points": [
                {"kind": "skill", "path": "VISA-BRAIN/AGENTS.md", "command": "$visa-brain / $investigate-case-evidence / $counsel"}
            ],
            "capabilities": [
                {
                    "name": "Epistemology A/B/C",
                    "evidence_paths": ["VISA-BRAIN/00-Case-Control/Epistemology-Layers.md"],
                    "category": "core",
                    "description": "Government record vs private prep vs ingest; category errors blocked.",
                },
                {
                    "name": "Evidence graph ≠ oracle",
                    "evidence_paths": [
                        "VISA-BRAIN/.codex/skills/investigate-case-evidence/references/evidence-graph.md"
                    ],
                    "category": "core",
                    "description": "Projection with fingerprint; Boundary Card; SAME_ORIGIN_GROUP.",
                },
                {
                    "name": "Extract-before-reviewed",
                    "evidence_paths": ["VISA-BRAIN/.codex/skills/investigate-case-evidence/SKILL.md"],
                    "category": "governance",
                    "description": "Script rejects reviewed without hash-bound unit extract.",
                },
                {
                    "name": "Product ≠ workspace",
                    "evidence_paths": ["VISA-BRAIN/AGENTS.md"],
                    "category": "core",
                    "description": "Kit never holds live case data; one explicit case root per op.",
                },
                {
                    "name": "Human/data contract",
                    "evidence_paths": ["VISA-BRAIN/00-Case-Control/Human-Data-Interface-Contract.md"],
                    "category": "ux",
                    "description": "Portal + Voice Card; evidence never in USER/MEMORY.",
                },
                {
                    "name": "Collector ≠ auditor",
                    "evidence_paths": ["VISA-BRAIN/AGENTS.md"],
                    "category": "governance",
                    "description": "$review and $counsel in separate sessions; coverage ≠ eligibility.",
                },
            ],
            "quality_signals": {
                "test_framework": "pytest in parent engineering tree",
                "test_file_count": None,
                "linter": "validate_visa_brain.py",
                "ci_provider": "parent monorepo",
                "ci_workflow_count": None,
            },
            "documentation": {
                "readme_sections": ["Pitch", "Start here"],
                "has_contributing": False,
                "has_architecture_doc": True,
                "docs_page_count": 20,
            },
            "extension_points": {
                "plugins": {"mechanism": "skills + domains JSON", "path": "VISA-BRAIN/.codex/skills/"},
                "hooks": {"mechanism": "phase gates", "events": ["P0-P7"]},
                "mcp": {"client": False, "server": False},
            },
            "unique_selling_points": [
                "Only subject that is a case OS",
                "Graph honesty + legal epistemology together",
                "Mechanical extract-before-reviewed",
            ],
            "limitations": [
                {
                    "description": "Not in OS/; evaluated as external kit",
                    "source": "VISA-BRAIN/AGENTS.md",
                },
                {
                    "description": "Not a company-sim or general knowledge brain",
                    "source": "VISA-BRAIN/PITCH.md",
                },
            ],
            "confidence": "HIGH",
            "extraction_method": "filesystem-scan-external-kit",
            "skill_version": "1.0.0",
        },
    )

    write_inv(
        "mempalace",
        {
            "generatedAt": "2026-08-12T22:00:00Z",
            "subject": "mempalace",
            "path": "OS/mempalace/",
            "primary_language": "Python",
            "secondary_languages": ["Markdown"],
            "stack": ["local memory palace", "temporal KG"],
            "license": "MIT",
            "tagline": "Verbatim local-first memory with temporal knowledge-graph triples.",
            "metrics": {
                "file_count": 553,
                "last_commit_date": "2026-08-11T09:34:45-03:00",
                "source_url": "https://github.com/milla-jovovich/mempalace",
            },
            "modules": [{"name": "mempalace", "path": "mempalace/", "type": "library"}],
            "external_dependencies_top10": [],
            "entry_points": [
                {"kind": "skill", "path": "skills/mempalace-recall/SKILL.md", "command": "recall"}
            ],
            "capabilities": [
                {
                    "name": "Verbatim drawers",
                    "evidence_paths": ["OS/mempalace/CLAUDE.md"],
                    "category": "core",
                    "description": "Do not paraphrase user text.",
                },
                {
                    "name": "Temporal KG",
                    "evidence_paths": ["OS/mempalace/mempalace/knowledge_graph.py"],
                    "category": "core",
                    "description": "valid_from/valid_to + atomic supersede.",
                },
                {
                    "name": "L0–L3 layers",
                    "evidence_paths": ["OS/mempalace/mempalace/layers.py"],
                    "category": "core",
                    "description": "Identity always-on; drawers on search.",
                },
            ],
            "quality_signals": {
                "test_framework": "pytest",
                "test_file_count": None,
                "linter": None,
                "ci_provider": "github-actions",
                "ci_workflow_count": 1,
            },
            "documentation": {
                "readme_sections": ["Memory"],
                "has_contributing": True,
                "has_architecture_doc": False,
                "docs_page_count": 10,
            },
            "extension_points": {
                "plugins": {"mechanism": "MCP + hooks", "path": "integrations/"},
                "hooks": {"mechanism": "PreCompact", "events": ["stop", "precompact"]},
                "mcp": {"client": True, "server": True},
            },
            "unique_selling_points": ["Best verbatim fidelity", "Honest temporal supersede"],
            "limitations": [
                {"description": "Not a case OS or counsel split", "source": "OS/mempalace/README.md"}
            ],
            "confidence": "HIGH",
            "extraction_method": "filesystem-scan",
            "skill_version": "1.0.0",
        },
    )

    write_inv(
        "LifeOS",
        {
            "generatedAt": "2026-08-12T22:00:00Z",
            "subject": "LifeOS",
            "path": "OS/LifeOS/",
            "primary_language": "TypeScript",
            "secondary_languages": ["Markdown"],
            "stack": ["Bun", "Claude Code skills", "ISA"],
            "license": "MIT",
            "tagline": "Personal AI operating system: TELOS, ISA, Pulse — not a case or company OS.",
            "metrics": {
                "file_count": 1890,
                "last_commit_date": "2026-08-07T09:06:43-07:00",
                "source_url": "https://github.com/danielmiessler/LifeOS",
            },
            "modules": [{"name": "LifeOS", "path": "LifeOS/", "type": "app"}],
            "external_dependencies_top10": [],
            "entry_points": [
                {"kind": "skill", "path": "LifeOS/install/skills/ISA/SKILL.md", "command": "ISA"}
            ],
            "capabilities": [
                {
                    "name": "ISA living spec",
                    "evidence_paths": ["OS/LifeOS/LifeOS/install/skills/ISA/SKILL.md"],
                    "category": "core",
                    "description": "Claims/features as personal system of record.",
                },
                {
                    "name": "LoadContext layers",
                    "evidence_paths": ["OS/LifeOS/LifeOS/install/hooks/LoadContext.hook.ts"],
                    "category": "core",
                    "description": "Constitution always-on; USER/ISA on demand.",
                },
                {
                    "name": "USER / identity",
                    "evidence_paths": ["OS/LifeOS/README.md"],
                    "category": "ux",
                    "description": "Life OS identity split.",
                },
            ],
            "quality_signals": {
                "test_framework": "unknown",
                "test_file_count": None,
                "linter": None,
                "ci_provider": None,
                "ci_workflow_count": None,
            },
            "documentation": {
                "readme_sections": ["OS"],
                "has_contributing": True,
                "has_architecture_doc": True,
                "docs_page_count": 20,
            },
            "extension_points": {
                "plugins": {"mechanism": "install skill unpack", "path": "LifeOS/install/"},
                "hooks": {"mechanism": "SessionStart LoadContext", "events": ["session-start"]},
                "mcp": {"client": False, "server": False},
            },
            "unique_selling_points": ["Best human/data split among non-VISA subjects"],
            "limitations": [
                {"description": "Life OS, not case ops", "source": "OS/LifeOS/README.md"}
            ],
            "confidence": "HIGH",
            "extraction_method": "filesystem-scan",
            "skill_version": "1.0.0",
        },
    )

    # copy existing inventories
    for slug in ["gbrain", "gsd-pi", "superpowers", "spec-kit", "paperclip"]:
        src = INV / slug
        if (src / "inventory.json").exists():
            (ROOT / f"inventory-{slug}.json").write_text((src / "inventory.json").read_text())
            md = src / "inventory.md"
            if md.exists():
                (ROOT / f"inventory-{slug}.md").write_text(md.read_text())

    meta = {
        "$schema": "os-bench metadata v1.0",
        "generatedAt": "2026-08-12T22:00:00Z",
        "comparison_type": "nway",
        "slug": "case-ops-8way",
        "subjects": [
            {
                "slug": "VISA-BRAIN",
                "path": "VISA-BRAIN/",
                "source_url": None,
                "detected_stack": ["Markdown", "Python"],
                "external": True,
            },
            {
                "slug": "gbrain",
                "path": "OS/gbrain/",
                "source_url": "https://github.com/garrytan/gbrain",
                "detected_stack": ["TypeScript", "Postgres"],
            },
            {
                "slug": "gsd-pi",
                "path": "OS/gsd-pi/",
                "source_url": "https://github.com/open-gsd/gsd-pi",
                "detected_stack": ["TypeScript"],
            },
            {
                "slug": "superpowers",
                "path": "OS/superpowers/",
                "source_url": "https://github.com/obra/superpowers",
                "detected_stack": ["Markdown"],
            },
            {
                "slug": "spec-kit",
                "path": "OS/spec-kit/",
                "source_url": "https://github.com/github/spec-kit",
                "detected_stack": ["Python"],
            },
            {
                "slug": "paperclip",
                "path": "OS/paperclip/",
                "source_url": "https://github.com/paperclipai/paperclip",
                "detected_stack": ["TypeScript"],
            },
            {
                "slug": "mempalace",
                "path": "OS/mempalace/",
                "source_url": "https://github.com/milla-jovovich/mempalace",
                "detected_stack": ["Python"],
            },
            {
                "slug": "LifeOS",
                "path": "OS/LifeOS/",
                "source_url": "https://github.com/danielmiessler/LifeOS",
                "detected_stack": ["TypeScript"],
            },
        ],
        "dimension_pack": "case-ops",
        "scoring_dimensions": [d[0] for d in DIMS],
        "profile": "full",
        "skill_version": "1.0.0",
        "output_root": "OS/_bench/case-ops-8way/",
        "artifacts_generated": [
            "metadata.json",
            "comparison-matrix.json",
            "comparison-matrix.md",
            "scorecard.json",
            "scorecard.md",
            "gap-analysis.json",
            "gap-analysis.md",
            "battle-card.md",
            "executive-report.md",
            "deep/absorption-roadmap.md",
        ]
        + [f"inventory-{s}.json" for s in SUBS]
        + [f"inventory-{s}.md" for s in SUBS],
        "artifacts_skipped": [],
        "notes": "Pack case-ops is job-specific. VISA-BRAIN is an external kit (not under OS/). A blowout vs OS/ peers is expected: they are adjacent products, not case OS. Do not read this ranking as a general harness ranking.",
        "confidence_overall": "HIGH",
        "quality_gate_passed": False,
        "related": [
            "_bench/_research/company-brain.md",
            "_bench/_research/visa-brain-vs-company-brain.md",
            "_bench/brain-6way/visa-brain-graph-feature-lessons.md",
        ],
    }
    (ROOT / "metadata.json").write_text(json.dumps(meta, indent=2) + "\n")

    # scorecard
    dim_objs = []
    wins = {s: 0 for s in SUBS}
    ties = 0
    for did, name, w in DIMS:
        sc = SCORES[did]
        best = max(sc.values())
        leaders = [s for s, v in sc.items() if v == best]
        if len(leaders) == 1:
            wins[leaders[0]] += 1
        else:
            ties += 1
        dim_objs.append(
            {
                "id": did,
                "name": name,
                "weight": w,
                "scores": sc,
                "signals_observed": SIG[did],
                "confidence": "HIGH",
                "justification": JUST[did],
                "advantage": leaders[0] if len(leaders) == 1 else "TIE",
                "leaders": leaders,
            }
        )
        for s in SUBS:
            assert len(SIG[did][s]) >= 2
            if sc[s] >= 90:
                assert len(SIG[did][s]) >= 2

    totals = {s: round(sum(SCORES[d][s] * w for d, _, w in DIMS), 2) for s in SUBS}
    ranked = sorted(totals.items(), key=lambda kv: -kv[1])
    scorecard = {
        "generatedAt": "2026-08-12T22:00:00Z",
        "comparison_type": "nway",
        "subjects": SUBS,
        "dimension_pack": "case-ops",
        "methods": {
            s: "installed" if s != "VISA-BRAIN" else "installed-external-kit" for s in SUBS
        },
        "dimensions": dim_objs,
        "weighted_totals": totals,
        "overall_winner": ranked[0][0],
        "total_delta": round(ranked[0][1] - ranked[1][1], 2),
        "ranking": [{"slug": s, "total": t} for s, t in ranked],
        "dimension_wins": {**wins, "ties": ties},
        "confidence_overall": "HIGH",
        "limitations": [
            "Pack is case-ops-specific; VISA blowout is expected.",
            "VISA-BRAIN is external (not OS/).",
            "No GitHub stars scored.",
            "Adjacent peers are not failed case OS — they refused the job.",
        ],
    }
    (ROOT / "scorecard.json").write_text(json.dumps(scorecard, indent=2) + "\n")
    print("totals", totals)
    print("winner", ranked[0], "delta", scorecard["total_delta"], "wins", wins)

    # matrix — 16 features
    features = [
        (
            "Epistemology",
            "Fact/claim/finding split",
            {
                "VISA-BRAIN": "yes (A/B/C + AgencyFinding)",
                "gbrain": "partial (takes vs facts)",
                "gsd-pi": "no",
                "superpowers": "no",
                "spec-kit": "partial (spec-as-SoT)",
                "paperclip": "no",
                "mempalace": "partial (verbatim)",
                "LifeOS": "partial (ISA claims)",
            },
        ),
        (
            "Epistemology",
            "Category errors blocked",
            {
                "VISA-BRAIN": "yes",
                "gbrain": "partial (takes/facts doc)",
                "gsd-pi": "no",
                "superpowers": "no",
                "spec-kit": "no",
                "paperclip": "no",
                "mempalace": "no",
                "LifeOS": "no",
            },
        ),
        (
            "Projection",
            "Generated dashboard/digest",
            {
                "VISA-BRAIN": "yes",
                "gbrain": "partial (compiled truth)",
                "gsd-pi": "partial (STATE derived)",
                "superpowers": "no",
                "spec-kit": "partial",
                "paperclip": "yes",
                "mempalace": "no",
                "LifeOS": "partial",
            },
        ),
        (
            "Projection",
            "Fingerprint / rebuild-if-stale",
            {
                "VISA-BRAIN": "yes",
                "gbrain": "partial (sync)",
                "gsd-pi": "no",
                "superpowers": "no",
                "spec-kit": "no",
                "paperclip": "partial",
                "mempalace": "no",
                "LifeOS": "no",
            },
        ),
        (
            "Isolation",
            "Product kit ≠ live data",
            {
                "VISA-BRAIN": "yes",
                "gbrain": "yes (two-repo)",
                "gsd-pi": "partial",
                "superpowers": "partial",
                "spec-kit": "partial",
                "paperclip": "partial (company row)",
                "mempalace": "no",
                "LifeOS": "partial",
            },
        ),
        (
            "Isolation",
            "No sibling scan / one explicit root",
            {
                "VISA-BRAIN": "yes",
                "gbrain": "partial (source scope)",
                "gsd-pi": "partial (worktree)",
                "superpowers": "partial",
                "spec-kit": "no",
                "paperclip": "partial (companyId)",
                "mempalace": "no",
                "LifeOS": "no",
            },
        ),
        (
            "Extract",
            "Mechanical reviewed-without-extract reject",
            {
                "VISA-BRAIN": "yes",
                "gbrain": "no",
                "gsd-pi": "no",
                "superpowers": "partial (prompt)",
                "spec-kit": "no",
                "paperclip": "no",
                "mempalace": "no",
                "LifeOS": "no",
            },
        ),
        (
            "Extract",
            "Disk restart authority / ledger",
            {
                "VISA-BRAIN": "yes",
                "gbrain": "partial (git pages)",
                "gsd-pi": "yes",
                "superpowers": "yes",
                "spec-kit": "partial",
                "paperclip": "yes (issues)",
                "mempalace": "partial",
                "LifeOS": "partial",
            },
        ),
        (
            "Graph",
            "Graph ≠ truth oracle",
            {
                "VISA-BRAIN": "yes (doctrine+P3)",
                "gbrain": "no (signals reorder)",
                "gsd-pi": "n/a",
                "superpowers": "n/a",
                "spec-kit": "n/a",
                "paperclip": "n/a",
                "mempalace": "yes (temporal store)",
                "LifeOS": "partial",
            },
        ),
        (
            "Graph",
            "Independence groups (not file count)",
            {
                "VISA-BRAIN": "yes",
                "gbrain": "no",
                "gsd-pi": "no",
                "superpowers": "no",
                "spec-kit": "no",
                "paperclip": "no",
                "mempalace": "no",
                "LifeOS": "no",
            },
        ),
        (
            "Counsel",
            "Independent review / counsel session",
            {
                "VISA-BRAIN": "yes",
                "gbrain": "no",
                "gsd-pi": "partial",
                "superpowers": "yes",
                "spec-kit": "partial",
                "paperclip": "partial",
                "mempalace": "no",
                "LifeOS": "no",
            },
        ),
        (
            "Counsel",
            "Coverage ≠ eligibility / done",
            {
                "VISA-BRAIN": "yes",
                "gbrain": "no",
                "gsd-pi": "partial",
                "superpowers": "partial",
                "spec-kit": "partial",
                "paperclip": "partial",
                "mempalace": "no",
                "LifeOS": "no",
            },
        ),
        (
            "Human/Data",
            "USER/SOUL forbidden for evidence",
            {
                "VISA-BRAIN": "yes",
                "gbrain": "partial",
                "gsd-pi": "no",
                "superpowers": "no",
                "spec-kit": "no",
                "paperclip": "partial",
                "mempalace": "partial",
                "LifeOS": "partial",
            },
        ),
        (
            "Human/Data",
            "Plain-language portal vs canonical vault",
            {
                "VISA-BRAIN": "yes",
                "gbrain": "no",
                "gsd-pi": "no",
                "superpowers": "no",
                "spec-kit": "no",
                "paperclip": "yes",
                "mempalace": "no",
                "LifeOS": "partial",
            },
        ),
        (
            "Spine",
            "Named phases with fail-closed gates",
            {
                "VISA-BRAIN": "yes (P0–P7 + freeze)",
                "gbrain": "partial (dream)",
                "gsd-pi": "yes",
                "superpowers": "yes",
                "spec-kit": "yes",
                "paperclip": "partial",
                "mempalace": "no",
                "LifeOS": "partial",
            },
        ),
        (
            "Spine",
            "Honest completion language",
            {
                "VISA-BRAIN": "yes (forbidden overclaim)",
                "gbrain": "partial",
                "gsd-pi": "partial",
                "superpowers": "partial",
                "spec-kit": "partial",
                "paperclip": "partial",
                "mempalace": "no",
                "LifeOS": "no",
            },
        ),
    ]

    cats = {}
    for cat, name, values in features:
        cats.setdefault(cat, []).append(
            {
                "name": name,
                "values": values,
                "evidence": {
                    s: [SIG[list(SCORES.keys())[0]][s][0]["evidence"]] for s in SUBS
                },
                "delta": "",
            }
        )
    # don't fake evidence mapping per feature — leave evidence to scorecard signals
    for cat in cats:
        for f in cats[cat]:
            f["evidence"] = {s: ["see scorecard signals"] for s in SUBS}

    matrix = {
        "generatedAt": "2026-08-12T22:00:00Z",
        "comparison_type": "nway",
        "subjects": SUBS,
        "dimension_pack": "case-ops",
        "categories": [{"name": k, "features": v} for k, v in cats.items()],
        "summary": {"total_features": len(features), "notes": "n-way yes|partial|no|n/a"},
        "subject_only_capabilities": {
            "VISA-BRAIN": [
                {
                    "name": "Mechanical extract-before-reviewed",
                    "category": "Extract",
                    "evidence": "VISA-BRAIN/.codex/skills/investigate-case-evidence/SKILL.md",
                },
                {
                    "name": "Boundary Card + SAME_ORIGIN_GROUP",
                    "category": "Graph",
                    "evidence": "VISA-BRAIN/.codex/skills/investigate-case-evidence/references/evidence-graph.md",
                },
            ],
            "gbrain": [
                {
                    "name": "Company-brain sources+OAuth",
                    "category": "Isolation",
                    "evidence": "OS/gbrain/docs/tutorials/company-brain.md",
                }
            ],
            "mempalace": [
                {
                    "name": "Atomic temporal supersede",
                    "category": "Graph",
                    "evidence": "OS/mempalace/mempalace/knowledge_graph.py",
                }
            ],
            "gsd-pi": [],
            "superpowers": [],
            "spec-kit": [],
            "paperclip": [],
            "LifeOS": [],
        },
    }
    (ROOT / "comparison-matrix.json").write_text(json.dumps(matrix, indent=2) + "\n")

    # field gaps — VISA residual vs peers uniques
    gaps = {
        "generatedAt": "2026-08-12T22:00:00Z",
        "comparison_type": "nway-field",
        "subjects": SUBS,
        "dimension_pack": "case-ops",
        "notes": "Field gaps. VISA residuals are hardening. Peer gaps are 'not this job' unless noted as portable.",
        "field_gaps": {
            "VISA-BRAIN": [
                {
                    "id": "GAP-VB-001",
                    "name": "Temporal supersede on mutable CLM",
                    "dimension": "graph_honesty",
                    "type": "Partial",
                    "severity": "MED",
                    "complexity": "MED",
                    "strategic_value": "MED",
                    "priority": "P2",
                    "evidence": "OS/mempalace/mempalace/knowledge_graph.py",
                    "description": "B-028 backlog. Steal mempalace half-open supersede, not a graph DB.",
                },
                {
                    "id": "GAP-VB-002",
                    "name": "Office-level cortex outside the vault",
                    "dimension": "workspace_isolation",
                    "type": "Missing",
                    "severity": "LOW",
                    "complexity": "HIGH",
                    "strategic_value": "LOW",
                    "priority": "P3",
                    "evidence": "OS/gbrain/docs/tutorials/company-brain.md",
                    "description": "Only if product becomes a firm. Never sidecar on case data.",
                },
            ],
            "gbrain": [
                {
                    "id": "GAP-GB-001",
                    "name": "Graph-as-oracle / signals as proof",
                    "dimension": "graph_honesty",
                    "type": "Missing",
                    "severity": "HIGH",
                    "complexity": "MED",
                    "strategic_value": "HIGH",
                    "priority": "P1",
                    "evidence": "VISA-BRAIN/.codex/skills/investigate-case-evidence/references/evidence-graph.md",
                    "description": "Adopt VISA doctrine: edges do not prove; signals must not gate truth.",
                }
            ],
            "gsd-pi": [
                {
                    "id": "GAP-GSD-001",
                    "name": "No evidence epistemology",
                    "dimension": "epistemology",
                    "type": "Missing",
                    "severity": "LOW",
                    "complexity": "HIGH",
                    "strategic_value": "LOW",
                    "priority": "P3",
                    "evidence": "VISA-BRAIN/00-Case-Control/Epistemology-Layers.md",
                    "description": "Out of job. Keep as coding factory.",
                }
            ],
            "superpowers": [
                {
                    "id": "GAP-SP-001",
                    "name": "Script-enforced extract gate",
                    "dimension": "extract_before_reviewed",
                    "type": "Partial",
                    "severity": "MED",
                    "complexity": "MED",
                    "strategic_value": "HIGH",
                    "priority": "P1",
                    "evidence": "VISA-BRAIN/.codex/skills/investigate-case-evidence/SKILL.md",
                    "description": "Portable: reject task-complete without brief/report files.",
                }
            ],
            "spec-kit": [
                {
                    "id": "GAP-SK-001",
                    "name": "Honest completion / coverage≠done",
                    "dimension": "counsel_separation",
                    "type": "Partial",
                    "severity": "MED",
                    "complexity": "LOW",
                    "strategic_value": "MED",
                    "priority": "P2",
                    "evidence": "VISA-BRAIN/.codex/skills/investigate-case-evidence/SKILL.md",
                    "description": "Specify-complete is not implement-correct. Speech rules travel.",
                }
            ],
            "paperclip": [
                {
                    "id": "GAP-PC-001",
                    "name": "USER/evidence firewall",
                    "dimension": "human_data_split",
                    "type": "Partial",
                    "severity": "MED",
                    "complexity": "LOW",
                    "strategic_value": "MED",
                    "priority": "P2",
                    "evidence": "VISA-BRAIN/00-Case-Control/Human-Data-Interface-Contract.md",
                    "description": "Do not collapse SOUL into AGENTS.md; keep PARA off company facts.",
                }
            ],
            "mempalace": [
                {
                    "id": "GAP-MP-001",
                    "name": "Not a case runner",
                    "dimension": "process_spine",
                    "type": "Missing",
                    "severity": "LOW",
                    "complexity": "HIGH",
                    "strategic_value": "LOW",
                    "priority": "P3",
                    "evidence": "VISA-BRAIN/PITCH.md",
                    "description": "Stay the archive. VISA already hashes originals.",
                }
            ],
            "LifeOS": [
                {
                    "id": "GAP-LO-001",
                    "name": "Not case ops",
                    "dimension": "epistemology",
                    "type": "Missing",
                    "severity": "LOW",
                    "complexity": "HIGH",
                    "strategic_value": "LOW",
                    "priority": "P3",
                    "evidence": "VISA-BRAIN/PITCH.md",
                    "description": "Stay the life OS. Voice Card pattern already in VISA.",
                }
            ],
        },
        "counts": {"total_gaps": 8, "p0": 0, "p1": 2, "p2": 3, "p3": 3},
        "action_items": [
            {
                "action_title": "gbrain: document graph≠oracle; stop treating signals as corroboration",
                "target": "gbrain",
                "closes_gap": "GAP-GB-001",
                "priority": "P1",
                "source_to_copy": "VISA-BRAIN/.codex/skills/investigate-case-evidence/references/evidence-graph.md",
            },
            {
                "action_title": "superpowers: script-reject complete without brief/report files",
                "target": "superpowers",
                "closes_gap": "GAP-SP-001",
                "priority": "P1",
                "source_to_copy": "VISA-BRAIN/.codex/skills/investigate-case-evidence/SKILL.md",
            },
            {
                "action_title": "VISA: B-028 temporal supersede from mempalace, stay in backlog order",
                "target": "VISA-BRAIN",
                "closes_gap": "GAP-VB-001",
                "priority": "P2",
                "source_to_copy": "OS/mempalace/mempalace/knowledge_graph.py",
            },
        ],
    }
    (ROOT / "gap-analysis.json").write_text(json.dumps(gaps, indent=2) + "\n")
    print("generated JSON ok")


if __name__ == "__main__":
    main()
