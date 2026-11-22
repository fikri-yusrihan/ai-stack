---
name: resume-project
description: Use when picking up an existing project in a new session or with a different agent — given a project folder path (for example projects/YYYY-NNN-name/), reads the docs, reports where the project stands, then waits for what the user wants to do next
---

# Resume Project

## Overview

Rebuilds working context for a project that already has docs, so the user can switch session or agent and immediately say what they want done. **This skill is read-only**: it gathers, reports, and stops. It never edits docs, advances a phase, runs project code, or starts the work — the user's next message decides that.

The project workflow itself (phases, exit gates, sub-agents) is owned by the `start-project` skill. Use it to interpret what you read; do not restate it.

---

## Input

The user gives a **project folder path**: absolute, or relative to the docs workspace. A bare project number or slug is fine. Search the project index and check the matching directory. If nothing or several folders match, ask once. If no path was given at all, ask for one.

---

## Step 1 — Inventory

`ls -la` the folder, including subfolders (`wave-N/`, `e2e/`, `poc/`). Note each doc's size and modified date. Find the project's row in `README.md` in the Projects table for its recorded docs and last-updated date.

---

## Step 2 — Read the docs

Read in this order, and stop reading a doc once you have what its row below asks for:

| Doc | Extract |
|---|---|
| `HANDOVER.md` (if present) | Read fully. It is the previous session's own summary — treat it as claims to check against the docs below, not as fact. |
| `brief.md` | Ask, goals, known conditions, effort estimate |
| `01-research.md` | Header table (`Status`, `Date`, `Context`), Problem Statement, `## Approach Selection Log`, Open Questions |
| `02-rfc.md` | Header, success criteria, the first paragraph of Solution Design, rejected alternatives (titles only), Unresolved Questions, `## Implementation Learnings` |
| `05-impl-plan.md` (older projects: `03-impl-plan.md`) | Header, the P0 table (count ✅ vs ⏳, and every `Decided by`), task status markers per phase, `## Design Pivots`, Risk Register |
| `03-challenge.md`, `04-*`, `06-verification.md`, `07-pr-plan.md` (older: `05-pr-plan.md`), `08-teach.md`, other docs | Title, `Status`, and the opening paragraph |

**Large docs.** Some docs run to 100KB+. Never read those top to bottom: get the heading outline first (`grep -n '^#'`), then read only the sections in the table. When there are several large docs, dispatch one `librarian` per doc with the extraction list above, and verify anything load-bearing yourself before reporting it.

Every fact in the briefing must trace to a doc and section. If a section you expected is missing, say so — that absence is itself a finding (for example, no `Approach Selection Log` means the Phase 2 gate was never closed).

---

## Step 3 — Work out where the project stands

From which docs exist, their `Status` values (see `GUIDELINES.md` § Document Status Lifecycle) and the exit gates in `start-project`, decide the current phase and whether its gate is met. Flag contradictions rather than resolving them silently, for example:

- the README row and the doc headers disagree
- `HANDOVER.md` says a task is done but the plan still shows it pending
- a P0 is `AI proposed`, or is ✅ with no `Decided by`
- code work appears to have started while a P0 is still open

---

## Step 4 — Check the code side

Only if the research doc's `Context` names a code repo that exists locally (not this docs repo), and only with read-only commands:

- `git -C <repo> branch --show-current`, `git status --short`, `git log --oneline -5`
- `git -C <repo> worktree list` to locate any task worktree
- Check related PRs in the forge when you have read access.

If the repo or a worktree is missing, say so. If the current working directory is not that repo, mention it — the user may want to start the session there.

---

## Step 5 — Briefing

Reply in this shape, under about 25 lines, then stop:

```
Project   <number-name> · <path>
Phase     <N — name> · doc Status: <values> · gate: <met / open: why>
Goal      <1–2 sentences, from the problem statement>
Decided   <chosen approach, decided by whom, source doc>
Blocked   <unresolved P0s, open questions — each with its doc reference>
Progress  <tasks done / total, last completed task, pivots so far>
Code      <repo, branch, worktree, dirty or clean, PRs — or "not started">
Check     <contradictions or stale items found in Step 3>
Open next <the 2–4 files most relevant to continuing>

What would you like to do?
```

Omit a line only if it truly does not apply. Do not propose a plan, offer to start work, or pick a next step for the user.

---

## After the briefing

Follow the user's instruction. If it means entering a doc phase, load the matching skill first (`writing-research-doc`, `writing-rfc-doc`, `writing-impl-plan-doc`, `execute-impl-plan`), as `start-project` requires.
