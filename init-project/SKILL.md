---
name: init-project
description: Use when starting a new engineering project in a docs knowledge base — the user states a goal and this scaffolds the numbered project folder, fills the doc header, and drives the AI–Engineer Collaboration workflow from Phase 0. Embeds the repo guidelines so no "read the guidelines first" context is needed.
---

# Init Project

## Overview

Bootstraps a new project in the docs workspace and runs the **AI–Engineer Collaboration workflow** for it. The user supplies only a **goal**; this skill handles numbering, folder creation, header fields, the Phase 0 problem statement, and Phase 1 research kickoff — applying the repo's guidelines automatically.

This skill **is** the guidelines for getting started — do not ask the user to point you at `GUIDELINES.md` or a previous project. The authoritative sources, if you need depth mid-workflow, are `GUIDELINES.md` and `workflows/ai-engineer-collaboration.md` at the workspace root. Look for the most complete project folder under `projects/` as a worked example.

---

## What the user provides vs. what you do

**User provides**: the goal (one or few sentences).

**You ask only if not inferable** (one short batched question):
1. A short kebab-case **project name** (propose one from the goal; confirm).
2. The **target code repo** under study, if the session's working directory is the docs workspace itself (see Session PWD rule).

Everything else — number, folder, header, phase sequencing — you do without prompting.

---

## Step 1 — Scaffold the project

1. **Next number**: read `README.md` Projects table, find the highest `NNN` for the **current year**, add 1. Format `YYYY-NNN-<name>` (e.g. `2026-003-<name>`). Year = current year from the session date.
2. **Create** `projects/YYYY-NNN-<name>/`.
3. **Copy** `templates/01-research.md` → `projects/YYYY-NNN-<name>/01-research.md`. (Other templates are copied later, when their phase begins — not upfront.)
4. **Fill the header table** before writing anything else:
   - `Context` — target service/module + repo.
   - `Date` — today (session date).
   - `Status` — `Draft`.
   - **`Session PWD`** — the working directory where the session was opened, copied **verbatim** from the env `<env>` block (`Working directory`). This must be the **code repo under study**. If the working directory is the docs workspace, that is not a code repo — ask the user for the target repo path and use that. Never leave it blank or a placeholder; use `unknown` only if truly unavailable, and note it.
5. **Repo catalog**: if Phase 1 will target a repo with no entry under `repos/<repo>/`, create the entry during this session from the reading you do (per `GUIDELINES.md` → Repo Catalog). Add `catalog_entry:` + `catalog_verified_commit:` to the research doc frontmatter when catalog info is used.
6. **Add a README row** to the Projects table (number, name, docs so far, today's date). Keep it updated as docs are added.

---

## Step 2 — Run the workflow (phase gates are mandatory)

Drive the phases in order. **Do not advance until the current phase's exit condition is met.** Implementation (Phase 7) does **not** start until every P0 is signed off by the user.

| Phase | You do | Output | Exit gate (blocking) |
|---|---|---|---|
| 0 Problem Framing | Restate the goal as a causal-chain problem statement; confirm with user | header + problem statement in `01-research.md` | Problem statement agreed |
| 1 Research | **Read code first** (fan out parallel explore/librarian agents); document what EXISTS with file+line refs; name absent patterns; capture constraints as **structured fields, not prose** | `01-research.md` | Real code references present; no solutions proposed yet |
| 2 Ideation | Present ≥3 approaches w/ tradeoffs; run adversarial review ("different hat"); ask "what are you NOT recommending and why?" | `## Approach Selection Log` | Log: options, eliminations w/ rejection category, chosen + `Decided by` |
| 3 RFC | Copy `templates/02-rfc.md`; author full design; every decision traces to a problem; binary success criteria | `02-rfc.md` | Every rejected alt has rejection category + revisit condition |
| 4 POC (optional) | Only if approach is novel — prove the one mechanism | `04-poc-simulation.md` | POC answers its one question; divergences noted |
| 5 Pre-conditions | Enumerate every P0 blocking question | P0 table in `03-impl-plan.md` | Every P0 has Decision + `Decided by` = `[OWNER] confirmed`/`[OWNER] chose` |
| 6 Impl Planning | Copy `templates/03-impl-plan.md`; ordered phases + DoD; run pre-planning analysis, review with plan critique | `03-impl-plan.md` | Reviewed; all P0s resolved |
| 7 Implementation | Code phase-by-phase; honest reporting; keep plan live | commits | `## Design Pivots` current; significant pivots → RFC `## Implementation Learnings` |
| 8 Verification | Gap analysis (old vs new), not just "tests pass" | section in impl plan | Gap analysis complete |
| 9 PR Planning | Copy `templates/05-pr-plan.md`; split for reviewability | `05-pr-plan.md` | Merge sequence + external deps written |

### Rejection categories (use verbatim)
`TECHNICAL_INFEASIBLE` · `BREAKS_EXISTING_CONSTRAINT` · `COST_TOO_HIGH` · `DEFERRED` · `SUPERSEDED`

### Decided-by values
`AI proposed` (does NOT unblock implementation) · `[OWNER] confirmed` · `[OWNER] chose`

---

## Non-negotiable rules (from the repo guidelines)

- **Read before writing.** Never describe code you haven't read; every claim cites file + line. Speculation is a defect.
- **Research doc documents what EXISTS** — no solutions in `01-research.md`; the Approach Selection Log comes after the facts. Name absent patterns explicitly.
- **Constraints as structured fields**, not buried prose (prose gets compacted away across sessions).
- **Binary success criteria** — no "improved"/"better".
- **All diagrams are Mermaid** (`flowchart TD` when unsure). Never ASCII art.
- **Don't clean up adjacent code**; scope to the stated task.
- **Report failures honestly**; mark superseded plan items with the reason. Never fixture-game.
- **When a discovery changes the design, stop and update the doc** (RFC + impl plan) before more code.

---

## Red flags

| Thought | Reality |
|---|---|
| "Let me start implementing the goal" | This skill drives docs first; code only after Phase 5 sign-off. |
| "I'll propose the solution in the research doc" | Research = facts only. Solutions go in Approach Log / RFC. |
| "Session PWD is the docs workspace" | That's not a code repo — ask for the target repo path. |
| "I'll copy all 5 templates now" | Copy each template when its phase begins. |
| "The user knows the guidelines, I'll skip the gates" | Phase exit conditions are mandatory regardless. |
| "Skip the README row" | Always register the project in the README table. |
