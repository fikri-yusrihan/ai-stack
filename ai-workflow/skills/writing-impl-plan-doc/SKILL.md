---
name: writing-impl-plan-doc
description: Use when writing the Phase 6 implementation plan (05-impl-plan.md) after the RFC is approved and all P0 pre-conditions are ready to be resolved
---

# Writing Implementation Plan Docs

## Overview

Translates an approved RFC into `05-impl-plan.md` — the execution document for a project in `projects/YYYY-NNN-<name>/`. This is the opposite audience problem from the research doc and RFC: the primary reader is an **AI agent that will execute this plan later**, with a human engineer reviewing the plan (and the resulting diffs) for correctness. Nobody needs the design motivation re-explained here — that's what the RFC is for. This document earns its keep by being precise enough that execution requires no guessing.

**Write code, not prose.** Every task should be dominated by a concrete snippet, a before/after diff, or an exact command — with just enough surrounding text to say what file, what's changing, and how to verify it's done. If a task reads more like an essay than a diff, it's wrong for this doc.

**Sketch units, not one big class.** Each snippet shows one unit with its one responsibility. An agent copies the shape it is shown, so a sketch that puts parsing, rules and I/O in one class produces that class. Show the interface and the implementation separately where S6 requires one.

---

## Writing Principles

**Show, don't explain.** State the file, show the code, list the definition-of-done checkboxes. Skip the paragraph justifying *why* — that's in the RFC, linked at the top. A task description longer than 2 sentences of prose is a sign something belongs in the RFC instead.

**Every task is independently executable.** An AI agent picking up Task 2.3 in isolation should be able to do it correctly from the task's own content: exact file path, exact snippet, exact definition of done. Don't make execution depend on remembering something said three tasks ago — repeat the relevant detail instead.

**P0s block code, not vibes.** Phase 0 pre-conditions must all be `✅` with `Decided by: Owner confirmed` or `Owner chose` before any task below it is written as ready to execute. `AI proposed` alone means the task is not actually unblocked yet — mark it clearly if you write it anyway.

**Definition of done is a checklist, not a sentence.** Prefer 2–4 concrete, verifiable checkboxes ("compiles", "existing test X passes unmodified", "method Y deleted") over one vague line.

**Sequence for cheap failure.** Order phases so additive, non-production-touching changes land first; wire-up and deletion land last, since that's where behavior actually changes and mistakes are expensive.

---

## Template Structure

Maps to `templates/05-impl-plan.md` — the structure itself doesn't change, this skill exists to keep the *content* code-first:

- **Header + Overview** — one paragraph max, link the RFC for rationale, state the net file diff (added/modified/deleted) up front.
- **Phase 0 — Pre-conditions** — the P0 table, verbatim from the RFC/research docs' unresolved items, each resolved with a decision and a one-sentence reasoning (not a paragraph).
- **Structure and Responsibilities** — directly after Phase 0: one row per new or changed unit (class), so the plan reviewer sees the structure before any code exists. Columns: unit, package path, responsibility in one sentence without "and", depends on, interface and why (S6), nearest analogue it follows. A size trigger (S4) or any other deviation from S1 to S9 is named in this table with its reason; an unnamed deviation is a finding. Rules: `standards/architecture.md`. A task creates one responsibility, or lists the units it creates.
- **Phase N — Tasks** — each task: what, exact file(s), a real code sketch (close to production-ready, not pseudocode), definition-of-done checklist. Use **Before/After** blocks whenever a task modifies existing code — this is the one place before/after diffs are the default, not the exception.
- **Wire-up + Cleanup phase** — last phase, always: connect new pieces, delete dead code, list every deleted file/method explicitly.
- **File Structure (final)** — a tree showing new/modified/deleted files at a glance.
- **Design Pivots** — filled live during execution, not written in advance; leave the table empty with the "—" placeholder row.
- **Risk Register** — short table, only real risks (something that could silently break in production), not generic execution risk.
- **References** — link RFC and research doc; file/line citations here if needed for the agent executing the plan.

---

## File Location

`projects/YYYY-NNN-<name>/05-impl-plan.md`, copied from `templates/05-impl-plan.md` in the docs knowledge base. Keep it live — update task statuses and the Design Pivots table as execution proceeds, per `GUIDELINES.md`.
