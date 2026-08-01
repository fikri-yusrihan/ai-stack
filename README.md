# public-ai-skills

A collection of AI workflow skills for structured engineering collaboration between engineers and AI coding assistants.

---

## `ai-workflow` — AI–Engineer Collaboration Skill

This skill provides a structured, phase-based workflow for working with AI coding assistants on non-trivial engineering tasks. It covers the full lifecycle from problem framing through PR planning, and can either **provision a new docs workspace** from scratch or **onboard an AI agent** into an existing one.

### What's Included

| File | Purpose |
|---|---|
| `SKILL.md` | Skill entry point — detects mode (provision vs. onboard) and drives setup |
| `GUIDELINES.md` | Operating rules for AI agents working in the docs workspace |
| `workflows/ai-engineer-collaboration.md` | Full phase-by-phase workflow guide (tool-agnostic) |
| `templates/01-research.md` | Phase 1: codebase assessment & research |
| `templates/02-rfc.md` | Phase 3: RFC / design document |
| `templates/03-impl-plan.md` | Phase 6: implementation plan (kept live during implementation) |
| `templates/04-poc-simulation.md` | Phase 4: proof of concept simulation (optional) |
| `templates/05-pr-plan.md` | Phase 9: PR sequence plan |

### The 9-Phase Workflow

| Phase | Name | Who Leads | Output |
|---|---|---|---|
| 0 | Problem Framing | Engineer | Agreed problem statement |
| 1 | Assessment / Research | AI | `01-research.md` with real code references |
| 2 | Ideation & Approach Selection | Engineer | Approach Selection Log in research doc |
| 3 | RFC Writing | AI | `02-rfc.md` |
| 4 | POC / Simulation *(optional)* | AI | `04-poc-simulation.md` |
| 5 | Blocking Questions | Engineer | P0 table with owner sign-off |
| 6 | Implementation Planning | AI | `03-impl-plan.md` |
| 7 | Implementation | AI | Code commits + Design Pivots log |
| 8 | Verification | Both | Gap analysis |
| 9 | PR Planning | AI | `05-pr-plan.md` |

Phase exit conditions are mandatory — the AI must not advance until the current phase's exit condition is met.

---

## Installation

### OpenCode + OhMyOpenCode

Copy the skill into your OpenCode skills directory:

```bash
# User-level (recommended)
cp -r . ~/.config/opencode/skills/ai-workflow

# Or project-level
cp -r . .opencode/skills/ai-workflow
```

Then in any session, load the skill by name:

```
Use the ai-workflow skill to set up a new docs workspace.
```

### Claude Code

Copy into your Claude skills directory:

```bash
cp -r . ~/.claude/skills/ai-workflow
```

### Any AI Assistant

Point your AI to `SKILL.md` and ask it to follow the instructions.

---

## Usage

### Provision a new workspace

When no workspace exists yet, the skill will:

1. Confirm the destination directory with you
2. Ask for your name (used in `[OWNER]` decision tracking throughout)
3. Create `projects/`, `templates/`, and `workflows/` directories
4. Copy all templates and the workflow guide
5. Write `GUIDELINES.md` with your name substituted for `[OWNER]`
6. Create a `README.md` master index

### Onboard into an existing workspace

If `GUIDELINES.md` and `projects/` already exist at the working directory, the skill switches to onboarding mode — it reads the structure and rules without creating any files.

---

## Key Design Principles

- **Read before writing** — AI agents must read actual code before making any claims about it
- **Phase exit conditions** — no phase is skipped; each has a documented, verifiable exit condition
- **Decision preservation** — every approach selection, P0 resolution, and design pivot is documented with reasoning and rejection categories
- **Owner sign-off gates implementation** — `AI proposed` alone does not unblock coding; `[OWNER] confirmed` or `[OWNER] chose` is required
- **Problem statements are causal chains** — name the code path, explain what it does wrong, trace to the consequence
- **All diagrams use Mermaid** — no ASCII art

---

## License

See [LICENSE](./LICENSE).
