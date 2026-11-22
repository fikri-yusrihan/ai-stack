---
name: start-project
description: Use when starting a new engineering project in the docs knowledge base — the user states a goal and this scaffolds the numbered project folder, fills the doc header, and drives the AI–Engineer Collaboration workflow from Phase 0. This skill is the single source of truth (SSOT) for the project workflow — phases, gates, sub-agents, decision rules, and behavior rules.
---

# Start Project

## Overview

Bootstraps a new project in the docs workspace and runs the **AI–Engineer Collaboration workflow** for it. The user supplies only a **goal**; this skill handles numbering, folder creation, header fields, the Phase 0 problem statement, and Phase 1 research kickoff.

**This skill is the single source of truth for the project workflow.** Phases, exit gates, sub-agent assignments, decision-preservation rules and AI behavior rules live here and nowhere else. Other docs link to this file instead of restating it — if you find a conflicting copy elsewhere, this file wins and the copy is stale.

Related docs (not duplicates — different jobs):

| Doc | Owns |
|---|---|
| `GUIDELINES.md` | Workspace layout, writing principles and document statuses |
| `README.md` | Project index |
| `workflows/ai-engineer-collaboration.md` | Collaboration rationale and handoff format. |
| `writing-research-doc` / `writing-rfc-doc` / `writing-impl-plan-doc` skills | Per-doc template mapping and writing style |

---

## What the user provides vs. what you do

**User provides** the goal. Resolve the docs workspace by locating its `templates/01-research.md` and `GUIDELINES.md`. Use the `ai-workflow` setup skill if it has not been provisioned.

**You ask only if not inferable** (one short batched question):
1. A short kebab-case **project name** (propose one from the goal; confirm).
2. The **target code repo** under study, if the goal does not name one. `Context` must name the target service/module and repo.

Everything else — number, folder, header, phase sequencing — you do without prompting.

---

## Step 1 — Scaffold the project

1. **Next number**: read `README.md` Projects table, find the highest `NNN` for the **current year**, add 1. Format `YYYY-NNN-<name>` (e.g. `2026-028-<name>`). Year = current year from the session date. Check no existing folder already uses the number.
2. **Create** `<project-folder>` = `projects/YYYY-NNN-<name>/`.
3. **Copy** `templates/01-research.md` → `<project-folder>/01-research.md`. (Other templates are copied later, when their phase begins — not upfront.)
4. **Fill the header table** before writing anything else:
   - `Context` — target service/module + repo.
   - `Date` — today (session date).
   - `Status` — `Draft` (see `GUIDELINES.md` § Document Status Lifecycle).
5. **Repo catalog**: if the workspace maintains a repo catalog, use and update it according to the workspace guidelines. Add `catalog_entry:` + `catalog_verified_commit:` to the research doc frontmatter when an existing catalog is used.
6. **Add a README row**: Projects table (link to the project folder, docs so far, today's date) for the new project. Keep it updated as docs are added.

---

## Step 2 — Run the workflow (phase gates are mandatory)

Drive the phases in order. **Do not advance until the current phase's exit gate is met.** Implementation (Phase 7) does **not** start until every P0 is signed off by the user.

**Read the matching writing skill every time you enter a doc phase** (1–2: `writing-research-doc`, 3: `writing-rfc-doc`, 5–6: `writing-impl-plan-doc`, 7: `execute-impl-plan`) — including when re-entering a phase in a later session. Skill content does not carry over between sessions.

| Phase | You do | Output | Sub-agents | Exit gate (blocking) |
|---|---|---|---|---|
| 0 Problem Framing | Restate the goal as a causal-chain problem statement; confirm with user | header + problem statement in `01-research.md` | — | Problem statement agreed |
| 1 Research | **Read code first**; document what EXISTS; name absent patterns; capture constraints as **structured fields, not prose**; record the target repo's `Structure conventions` (see the architecture standard) | `01-research.md` | `librarian` × N, one per module/question/external doc, one of them the Structure survey | Real code references present; `Structure conventions` filled; no solutions proposed yet |
| 2 Ideation | Present the status quo plus ≥3 other approaches w/ tradeoffs; evaluate reuse and modularity (below); run adversarial review; ask "what are you NOT recommending and why?" | `## Approach Selection Log` | `advisor` to stress-test the chosen approach (hard calls only) | Log: options, eliminations w/ rejection category, choice and owner sign-off in `Decided by` |
| 3 RFC | Copy `templates/02-rfc.md`; author full design; every decision traces to a problem; binary success criteria; fill `Structure and boundaries` | `02-rfc.md` | `librarian` for Context-section fact checks | Every rejected alt has rejection category + revisit condition; `Structure and boundaries` follows the repo's convention or names the P0 that overrides it |
| 3b Challenge (big projects only) | Only if the RFC adds a data store or service, changes more than one service, or is hard to reverse: follow the `challenge` skill; independent reviewers try to break the design, only evidence-backed findings survive | `03-challenge.md` | Two independent reviewers outside the author's session (for example the `advisor` persona plus a second senior reviewer), each alone with the challenge brief (`advisor` role prompt) | Every surviving finding answered; decision `Decided by` = `Owner confirmed`/`Owner chose` |
| 4 POC (optional) | Only if approach is novel — prove the one mechanism | `04-poc-simulation.md` | — | POC answers its one question; divergences noted |
| 5 Pre-conditions | After RFC approval, start the draft from `templates/05-impl-plan.md` and enumerate every P0 blocking question | P0 table in `05-impl-plan.md` | — | Every P0 has Decision + `Decided by` = `Owner confirmed`/`Owner chose` |
| 6 Impl Planning | Expand the draft from Phase 5 into ordered phases and definitions of done; fill `Structure and Responsibilities` for every new unit; brief the plan reviewer on reuse and modularity and on the architecture standard (below) | `05-impl-plan.md` | `advisor` on RFC/POC *before* drafting (non-trivial designs only); `auditor` on the finished plan | `auditor` reviewed, findings resolved or dismissed with reason; all P0s resolved; every deviation from S1 to S9 is named with a reason; owner approves the plan |
| 7 Implementation | Follow `execute-impl-plan`; keep plan live | commits | `executor` per task | `## Design Pivots` current; significant pivots → RFC `## Implementation Learnings`; each task's Structure report checked against the diff |
| 8 Verification | Run `unslop` on the diff; gap analysis (old vs new), not just "tests pass"; for every PR that changes behaviour follow `verify-feature`: verification on the approved test target at the candidate commit, every case PASS/FAIL/UNTESTED with evidence that opens, checked by the `advisor` persona or the project owner, graded from the raw evidence | section in impl plan; `06-verification.md` | two `librarian`s (old behavior / new behavior) then `auditor` on the diff, including its structure review; the `advisor` persona or the project owner as the checker for `06-verification.md`, graded from the raw evidence | Gap analysis complete; structure findings resolved or accepted by the project owner; PRs that change behaviour: `06-verification.md` Done (all PASS, checked by the `advisor` persona or the project owner, graded from the raw evidence) |
| 9 PR Planning | Copy `templates/07-pr-plan.md`; split for reviewability; readiness check before any prod step (`verify-feature` step 6) | `07-pr-plan.md` | — | Merge sequence + external deps written |

After every shipped feature (PRs merged, verification Done), offer the `teach` skill: a one-page explainer with a short quiz for the project owner, saved as `08-teach.md`. A plain-words walk through all steps is in [`guide/`](../../guide/README.md).

As work progresses, update the document status and project index. Use `In Review` for a draft ready for review and `Approved` after the project owner signs off.

### Reuse and modularity in Phases 2 and 6

Before proposing a new mechanism, look for code that already owns the behavior: existing helpers, modules and established patterns first, then standard-library features, native platform capabilities and installed dependencies. Search by behavior as well as symbol name; read relevant implementations and callers to verify contracts and edge cases. Carry forward verified Phase 1 findings, extending the search where the proposed design introduces a mechanism not yet investigated.

- **Phase 2 — compare reuse before building.** Include an approach that reuses or extends an existing mechanism when one fits. Name the candidates inspected and explain any concrete mismatch in the existing Approaches Evaluated / Approach Selection Log; a claim that reuse is unavailable needs the relevant search scope and evidence. Assess behavioral compatibility, ownership and dependency direction, not just similar-looking code.
- **Modularity — give each boundary a current purpose.** Justify a new module or abstraction through a present responsibility, caller need or required contract. Prefer cohesive components with explicit interfaces; preserve useful boundaries even with one implementation. Avoid speculative flexibility, duplicated policies and shared utilities that couple unrelated responsibilities. Choose readable code that fits the repository over fewer lines or files. The concrete rules (placement, one responsibility per class, dependency direction, where interfaces are required, which patterns earn their place) are in the architecture standard below.
- **Phase 6 — review the concrete plan against those choices.** Brief the `auditor` to inspect proposed helpers, modules, abstractions and dependencies against the verified reuse candidates and approved design. Reuse tasks must name the existing entry points and show the intended call or extension; new mechanisms must have a concrete reason existing options fall short. Report evidence-backed duplication or coupling problems with their consequence and a compatible alternative, within the auditor's existing finding limit. If a simpler alternative changes an approved design decision, surface it for decision and update the design before revising implementation tasks.

These checks feed the existing decision records and reviews. Required behavior, security, error handling, tests and phase gates remain constraints on every simplification.

### Architecture standard

Structure is checked at every phase from research to verification, because a structural defect that tests do not catch is found late, at human review. The rules live in [`standards/architecture.md`](../../standards/architecture.md) (checklist IDs S1 to S9) and nowhere else; do not restate them in a project doc.

- **Principles for the design, the repo's idiom for the layout.** Responsibility, dependency direction and boundaries follow well-known architecture (layered, ports and adapters, SOLID, package by feature; the standard's section 2). Package layout, naming and wiring follow the target repo (P1, P2). A different structure for a new module is a P0 that needs `Owner chose` (P3). Design before code: state the design note (standard section 2) before writing classes.
- **Survey before design.** Phase 1 records `Structure conventions` in the research doc, using the fields in § 5 of the standard. Every later phase reuses it instead of re-deriving it.
- **Plan the units, not just the files.** The impl plan's `Structure and Responsibilities` table lists each new class with its package, one-sentence responsibility, dependencies and interface decision. A task that would put two responsibilities in one class is split in the plan, not at review.
- **Check at the end of each task.** The `executor` returns a Structure report; the orchestrator verifies it against the diff (see `execute-impl-plan`); the Phase 8 `auditor` reviews the whole diff for S1 to S9.
- **Structure findings block.** A confirmed violation is fixed, or the project owner accepts it as a named deviation. It is not dismissed as taste.

### Sub-agents

Definitions and example model tiers live in [`agents/`](../../agents/README.md). The orchestrating session synthesizes reports and writes the docs itself — sub-agents gather, review, or implement; they never own a decision.

| Agent | Model tier | Use for | Outside its scope |
|---|---|---|---|
| `librarian` | Fast | Read-only search: internal codebase questions, external docs, usage examples. Fire several in parallel, each with one specific question. | Writing, deciding, "go explore this codebase" |
| `advisor` | Deep reasoning | Reviewing an RFC/design for backward compatibility, bottlenecks, scalability. Expensive. | Routine review, small changes |
| `auditor` | Deep reasoning | Critiquing written docs, plans, code or a PR. Defaults to approving; max 3 concrete findings per pass. | Style preferences, fixing issues itself |
| `executor` | Implementation | Implementing one approved impl-plan task, self-explanatory code, scoped to the task. | Unapproved plans, adjacent cleanup |

Use the matching role prompt when a harness lacks a native persona. Keep independent review in a separate session or with a human reviewer.

Delegate when there are 2+ independent research angles, a plan/RFC that needs review, or plan tasks to implement. Work directly for a single file at an obvious location.

### P0 format

| # | Question | Why it blocks | Options | Decision | Decided by | Reasoning |
|---|---|---|---|---|---|---|
| P0-1 | The question | What forks depending on the answer | A / B / C | ✅ Decision or ⏳ Unresolved | `AI proposed` \| `Owner confirmed` \| `Owner chose` | One sentence — why this option |

`Decided by` must be `Owner confirmed` or `Owner chose` before Phase 7. `AI proposed` alone never unblocks implementation. Before starting Phase 7, scan the impl plan: any `AI proposed` or `⏳` row means stop and ask.

### Decision preservation

Document every revisitable decision at the point it is made, not retrospectively.

| Decision point | Where | When |
|---|---|---|
| Approach selection | `## Approach Selection Log` in `01-research.md` | Before closing Phase 2 |
| Rejected alternatives | `## Alternatives Considered` in `02-rfc.md` | Before the RFC is done |
| P0 resolution | P0 table in `05-impl-plan.md` | Before Phase 7 |
| Design pivots | `## Design Pivots` in `05-impl-plan.md` | Immediately |
| Significant pivots | `## Implementation Learnings` in `02-rfc.md` | Same session |

A decision is not documented until it states: what was decided, the constraints at the time, why each alternative was rejected (with category), and when a rejected alternative would be worth revisiting.

**Rejection categories (use verbatim):**

| Category | Meaning | Revisitable? |
|---|---|---|
| `TECHNICAL_INFEASIBLE` | Can't be done given current stack or constraints | Only if constraints change |
| `BREAKS_EXISTING_CONSTRAINT` | Violates an established contract, interface, or team boundary | Only if constraint is lifted |
| `COST_TOO_HIGH` | Feasible, wrong effort/risk ratio now | Yes — when scope or timeline changes |
| `DEFERRED` | Good idea, wrong time or scope | Yes — explicitly worth revisiting |
| `SUPERSEDED` | Was the plan, replaced mid-implementation | See RFC Implementation Learnings |

**Decided-by values:** `AI proposed` (does NOT unblock implementation) · `Owner confirmed` · `Owner chose`

---

## Non-negotiable rules

- **Read before writing.** Never describe code you haven't read; every claim must trace to a file and line you read. Whether the *doc* shows that citation depends on doc type (impl plan: code-first; research/RFC: plain language, cite only load-bearing details). Speculation is a defect. If you haven't read a file, say so and read it.
- **Research doc documents what EXISTS** — no solutions in `01-research.md`; the Approach Selection Log comes after the facts. Name absent patterns explicitly.
- **Constraints as structured fields**, not buried prose (prose gets compacted away across sessions).
- **Binary success criteria** — no "improved"/"better".
- **All diagrams are Mermaid** (`flowchart TD` when unsure). Never ASCII art.
- **Alternatives Considered is never empty.**
- **Don't clean up adjacent code**; scope to the stated task.
- **Structured code.** Place files where the repo's convention puts them; one responsibility per class; interfaces at external boundaries; see the architecture standard. A working change with the wrong structure is not done.
- **Self-explanatory code.** No comments that restate code; comment only a non-obvious "why". Delete what your own change made dead (imports, fields, flag branches) as you go.
- **Report failures honestly.** Show failing output; mark superseded plan items with the reason. Never fixture-game — fix production code, not the assertion.
- **When a discovery changes the design, stop and update the doc** (RFC + impl plan) before writing more code.

---

## Red flags

| Thought | Reality |
|---|---|
| "Let me start implementing the goal" | Docs first; code only after Phase 5 sign-off. |
| "I'll propose the solution in the research doc" | Research = facts only. Solutions go in Approach Log / RFC. |
| "The class probably does X" | Read the file. |
| "I'll copy all 5 templates now" | Copy each template when its phase begins. |
| "The user knows the guidelines, I'll skip the gates" | Exit gates are mandatory regardless. |
| "The AI's P0 answer looks right, proceed" | `AI proposed` does not unblock Phase 7. |
| "Tests fail, I'll adjust the assertion" | Revert. Fix production code. |
| "Code diverged slightly, I'll fix the RFC later" | Stop. Update RFC + impl plan now. |
| "Skip the README row" | Always register the project and keep the row current. |
| "I'll put it all in one class for now" | Split in the plan, not at review. One responsibility per class (S3). |
| "The nearby class is big, I'll match it" | A class past the S4 triggers is an outlier, not a template (P4). |
| "This package layout is cleaner than the repo's" | The repo's idiom decides layout (P1). A different structure is a P0. |
| "I'll just write it, the task is clear" | Design note first (standard section 2): style, units, dependencies, boundaries, patterns. |
| "CI is green, so the PR is verified" | Every PR that changes behaviour needs `verify-feature`: an approved test target, evidence per case, checked by the `advisor` persona or the project owner, graded from the raw evidence. |
| "I'll open the PR and clean up after review" | Run `unslop` before the PR opens. |
| "This design is big but the RFC looks fine" | A new data store or service, several services, or a hard-to-reverse change goes through `challenge` first. |
