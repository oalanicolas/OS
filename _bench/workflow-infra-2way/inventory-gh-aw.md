# Inventário: gh-aw (GitHub Agentic Workflows)

**Path:** `OS/gh-aw/`
**Date:** 2026-04-19
**Extraction Method:** filesystem-scan + doc-scan
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | gh-aw |
| Source URL | https://github.com/github/gh-aw |
| Primary language | Go |
| Secondary languages | JavaScript (compiled helpers), Markdown (workflow DSL), YAML (compiled lock files) |
| Stack | Go 1.25, cobra, GitHub Actions, MCP Go SDK, Charmbracelet TUI, actionlint, gosec |
| License | MIT (`LICENSE`) |
| Tagline | Write agentic workflows in natural language markdown, and run them in GitHub Actions. "Actions + Agent + Safety." |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| LOC (ballpark, Go+JS) | ~526,558 | `find + wc -l` over `.go`/`.js` |
| Files | 4,044 | filesystem scan |
| Workflow `.md` sources | 272 | `.github/workflows/*.md` |
| Compiled `.lock.yml` | 196 | `.github/workflows/*.lock.yml` |
| Test files | 1,050 | `**/*_test.go` |
| README length | 953 lines | `README.md` (large community contrib list) |
| Last commit | 2026-04-19 | `git log -1` (`4fb0d86`) |
| Docs site | github.github.com/gh-aw | `docs/` (Astro + Starlight) |
| Version | v0.40.1 (pre-1.0) | `CHANGELOG.md` |
| Skills | 22 | `skills/` dir |

## Modules / Top-level Structure

| Module | Path | Type | Description |
|--------|------|------|-------------|
| CLI | `cmd/gh-aw/` | app | Main `gh aw` CLI (cobra-based) |
| WASM CLI | `cmd/gh-aw-wasm/` | app | WASM build for browser/editor embedding |
| Compiler core | `pkg/workflow/` | library | Markdown→GitHub Actions YAML compiler; safe-output, sandbox, pinning logic |
| Parser | `pkg/parser/` | library | Markdown frontmatter parser |
| CLI commands | `pkg/cli/` | library | add/compile/run/logs/status/fix/update/install |
| Action pins | `pkg/actionpins/` | library | SHA pinning + supply-chain validation |
| Agent drain | `pkg/agentdrain/` | library | Output draining/validation |
| Utilities | `pkg/{logger,stats,styles,tty,gitutil,repoutil,envutil,fileutil,stringutil,timeutil,sliceutil,semverutil,typeutil,testutil,console,constants,types}` | library | Shared helpers |
| Schemas | `schemas/agent-output.json` | library | JSON schema for engine output |
| Actions | `actions/` | library | Shared Action steps used by compiled workflows |
| Specs | `specs/` | library | Security-architecture specs (threat model, validation) |
| Docs | `docs/` | app | Astro + Starlight site |
| Internal tools | `internal/tools/` | library | Private tool wiring |
| Sample workflows | `.github/workflows/` | library | 272 .md source workflows, 196 compiled .lock.yml |

## External Dependencies (top 10)

| Package | Version | Purpose |
|---------|---------|---------|
| github.com/spf13/cobra | v1.10.2 | CLI framework |
| github.com/cli/go-gh/v2 | v2.13.0 | `gh` API + auth |
| github.com/modelcontextprotocol/go-sdk | v1.5.0 | MCP client/server |
| github.com/rhysd/actionlint | v1.7.12 | Lint generated Actions YAML |
| github.com/securego/gosec/v2 | v2.25.0 | Security scanner |
| github.com/google/jsonschema-go | v0.4.2 | JSON schema handling |
| github.com/santhosh-tekuri/jsonschema/v6 | v6.0.2 | JSON schema validation |
| github.com/goccy/go-yaml | v1.19.2 | YAML parse/emit |
| charm.land/bubbletea/v2 | v2.0.6 | TUI framework |
| charm.land/lipgloss/v2 | v2.0.3 | TUI styling |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| CLI | `cmd/gh-aw/` | `gh aw` (installs as gh extension) |
| WASM | `cmd/gh-aw-wasm/` | WASM compiler (editor embedding) |
| MCP server | documented as `gh aw mcp-server` | `gh-aw` itself exposes MCP |

## Capabilities (observed)

### Core Capabilities

| Capability | Evidence | Notes |
|------------|----------|-------|
| Markdown-as-DSL agentic workflows | `OS/gh-aw/docs/src/content/docs/introduction/how-they-work.mdx`, `OS/gh-aw/.github/workflows/*.md` | YAML frontmatter + NL body; 272 sample workflows shipped. |
| Compile to GitHub Actions lock file | `OS/gh-aw/docs/src/content/docs/reference/compilation-process.md`, `OS/gh-aw/.github/workflows/*.lock.yml` | `gh aw compile` deterministically emits hardened YAML. |
| Multi-engine support | `OS/gh-aw/docs/src/content/docs/reference/engines.md` | Copilot (default), Claude, Codex, Gemini, Crush (experimental). Per-engine feature matrix. |
| Dual concurrency control | `OS/gh-aw/docs/src/content/docs/reference/concurrency.md` | Per-workflow groups (issue/PR/branch-keyed) + per-engine `gh-aw-{engine-id}` cap. |
| Multi-trigger events | `OS/gh-aw/docs/src/content/docs/reference/frontmatter.md`, `OS/gh-aw/docs/src/content/docs/reference/triggers.md` | Standard Actions triggers + reaction, stop-after, manual-approval, forks, skip-roles, skip-bots, skip-if-match. |

### Governance / Safety Capabilities

| Capability | Evidence | Notes |
|------------|----------|-------|
| Safe outputs (validated writes) | `OS/gh-aw/pkg/workflow/safe_outputs_validation*.go`, `OS/gh-aw/docs/src/content/docs/reference/safe-outputs*.md` | Read-only by default; writes go through vetted handler (add_comment, create_pull_request, assign_to_agent, assign_milestone, autofix, …). |
| AWF agent sandbox (firewall) | `OS/gh-aw/docs/src/content/docs/reference/sandbox.md`, `OS/gh-aw/README.md` | Default `sandbox.agent: awf` — domain-based egress + activity logging via `gh-aw-firewall`. |
| MCP Gateway (experimental) | `OS/gh-aw/docs/src/content/docs/reference/mcp-gateway.md` | Routes MCP calls through single HTTP gateway (`gh-aw-mcpg`). |
| Human approval gates | `OS/gh-aw/docs/src/content/docs/reference/frontmatter.md` | `on.manual-approval` uses GitHub Environments. |
| Tool allow-lists | `OS/gh-aw/docs/src/content/docs/reference/tools.md` | `tools:` + `tools.github.allowed:` per workflow. |
| SHA-pinned dependencies | `OS/gh-aw/pkg/actionpins/`, `OS/gh-aw/pkg/workflow/action_pins.go`, `OS/gh-aw/pkg/workflow/action_sha_checker.go` | Auto-sync from `.github/aw/actions-lock.json`. |
| Secret redaction | `OS/gh-aw/CHANGELOG.md` | Built-in regex redaction for GitHub/Azure/Google/AWS/OpenAI/Anthropic tokens. |
| Threat detection | `OS/gh-aw/docs/src/content/docs/reference/threat-detection.md` | Prompt-injection detection layer. |
| Lockdown mode | `OS/gh-aw/docs/src/content/docs/reference/lockdown-mode.md` | Extra-restrictive runtime profile. |

### UX / Extensibility Capabilities

| Capability | Evidence | Notes |
|------------|----------|-------|
| `gh extension install` | `OS/gh-aw/install.md`, `OS/gh-aw/install-gh-aw.sh` | GitHub-native distribution. |
| Interactive TUI run | `OS/gh-aw/pkg/tty/`, `OS/gh-aw/docs/interactive-run-mode.md` | Charmbracelet-based dry-run/demo UI. |
| `gh aw add` marketplace | `OS/gh-aw/docs/src/content/docs/reference/frontmatter.md` | `owner/repo/path@ref` install + `resources:` companions + `redirect:` chains. |
| Claude skill packs | `OS/gh-aw/skills/` | 22 skill packs for authoring/debugging. |
| Cost/rate-limit controls | `OS/gh-aw/docs/src/content/docs/reference/cost-management.md`, `OS/gh-aw/docs/src/content/docs/reference/rate-limiting-controls.md` | stop-after, skip-roles/bots, engine.concurrency, cost in `gh aw logs`. |
| WASM compiler | `OS/gh-aw/cmd/gh-aw-wasm/`, `OS/gh-aw/docs/src/content/docs/reference/wasm-compilation.md` | Browser/editor embedding. |

## Tests / Quality Signals

| Signal | Value | Evidence |
|--------|-------|----------|
| Test framework | Go testing + testify | `go.mod` |
| Test files | 1,050 | `**/*_test.go` |
| Integration tests | `*_integration_test.go` pattern | e.g., `action_pins_integration_test.go`, `add_comment_discussions_integration_test.go` |
| Linter | golangci-lint + gosec | `Makefile`, `go.mod` |
| CI | GitHub Actions | `.github/workflows/*` (smoke-copilot/claude/codex/opencode + agentics-maintenance) |
| actionlint | embedded | `pkg/workflow` uses `rhysd/actionlint` to lint emitted YAML |

## Documentation

| Type | Path | Status |
|------|------|--------|
| README | `README.md` | 953 lines (auto-updated contrib list) |
| CHANGELOG | `CHANGELOG.md` | active |
| AGENTS.md | `AGENTS.md` | exists |
| CONTRIBUTING | `CONTRIBUTING.md` | exists |
| DEVGUIDE | `DEVGUIDE.md` | make-target guide |
| SECURITY.md | `SECURITY.md` | exists |
| Docs site | `docs/` (Astro/Starlight) | Extensive reference/intro/patterns/examples/guides |
| Specs | `specs/` | security-architecture-spec + summary + validation |

## Configuration Surface

| File | Format | Purpose |
|------|--------|---------|
| workflow `.md` files | Markdown + YAML frontmatter | The DSL |
| `.github/aw/` | JSON | Compiled-workflow assets (action_pins.json, agent config) |
| `Makefile` | Make | Build/test/release (`make build`, `make test`, ~75 targets) |
| `go.mod` / `go.sum` | Go | Deps |
| `Dockerfile` | Docker | Reproducible build image |
| `install-gh-aw.sh` | Shell | Extension installer |

## Extension Points

| Extension Type | Where | How to extend |
|----------------|-------|---------------|
| AI engines | `pkg/workflow/agentic_engine.go`, `engine:` frontmatter | 5 supported (Copilot/Claude/Codex/Gemini/Crush) |
| MCP servers | `pkg/workflow/tools_parser.go`, `tools: {mcp: ...}` | Custom MCP tools inline in frontmatter |
| Safe outputs | `pkg/workflow/safe_outputs_*`, `safe-outputs:` | add_comment, create_pull_request, assign_*, autofix, push_to_pull_request_branch, update/remove label, etc. |
| Custom agents | `.github/agents/*.md`, `engine.agent` | Copilot-specific agent personas |
| Skills | `skills/` | Markdown packs consumed by agents |
| Resources / redirects | `resources:`, `redirect:` frontmatter | `gh aw add` companion fetching + move-aware |

## Notable Design Decisions

- **Compile, don't interpret** — workflows compile to standard `.lock.yml` so the runtime is GitHub Actions itself — evidence: `OS/gh-aw/docs/src/content/docs/reference/compilation-process.md`.
- **Safety first** — read-only default, safe-outputs for writes, AWF firewall for egress — evidence: `OS/gh-aw/README.md` Guardrails section + `OS/gh-aw/pkg/workflow/safe_outputs_validation.go`.
- **Dual concurrency** — workflow-level groups keyed by issue/PR + engine-level caps — evidence: `OS/gh-aw/docs/src/content/docs/reference/concurrency.md`.
- **Companion projects (not monolith)** — gh-aw-firewall, gh-aw-mcpg, gh-aw-actions — evidence: `OS/gh-aw/README.md` Related Projects.

## Limitations / Known Issues

- Tightly coupled to GitHub Actions runtime — not portable to GitLab/Jenkins/self-hosted without a different runner.
- No durable event-log replay at the LLM-step level — retries live at the Actions job/step granularity.
- Pre-1.0 (v0.40.1); some features still experimental (MCP Gateway, Crush engine).
- Project currently on "Spring Break" notice in README — expect maintenance delays.

## Unique Selling Points

- Zero custom runtime — stands on GitHub's native CI/CD and permission model.
- Security-by-default multi-layer: compile-time validation, AWF runtime isolation, tool allow-lists, safe-outputs, SHA pinning, secret redaction, approval gates.
- Markdown-native DSL readable/diff-able by humans and agents.
- Rich ecosystem: companion firewall + MCP gateway + shared actions + installable from the workflow marketplace.

---

## Extraction Notes

- Scanned directories: cmd/, pkg/, internal/, docs/, schemas/, skills/, specs/, actions/, .github/
- Skipped directories: .git/, vendor/, tmp/, scratchpad/
- Data sources: filesystem (100%) + README + CHANGELOG + docs/ content + DEVGUIDE
- Tools used: filesystem scan + Grep + targeted Read of go.mod + docs

---

_Generated by os-bench inventory task | Template v1.0_
