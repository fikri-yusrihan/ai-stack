---
name: writing-rfc-doc
description: Use when writing the Phase 3 RFC / design document (02-rfc.md) after research is done and an approach has been selected
---

# Writing RFC Docs

## Overview

Translates a selected approach (from `01-research.md`'s Approach Selection Log) into `02-rfc.md` — the design document for a project in `projects/YYYY-NNN-<name>/`. Same audience problem as the research doc: a human reviewer who will not go trace through the referenced source to follow the argument. The RFC has to make its own case in plain language.

The rigor doesn't change — every design claim still has to be grounded in code you actually read. What changes is how much of that grounding shows up on the page.

---

## Writing Principles

Same principles as `writing-research-doc`, applied to design instead of discovery:

**Explain how it fits, not just what it does.** For any design decision, answer: how does this integrate with what's already there, and how does it get to the stated goal? "We add a fallback field that the display layer checks before the old one, so existing callers keep working while new callers opt in" beats a diff with no framing.

**Keep it short. Bullets and diagrams over prose walls and code walls.** A Mermaid flowchart for the happy path plus its fallback branches communicates more than a paragraph of "if X then Y, else Z." Use it.

**Code snippets are the exception, not the default.** Include a before/after snippet only when the *comparison itself* is the point and no description could convey it as precisely — e.g., a field renamed across a lookup key where the reviewer needs to see every layer touched. Most Solution Design steps should be describable without one. This RFC is not the implementation plan — the implementation plan (`writing-impl-plan-doc`) is where the real code lives.

**Reference code sparingly.** File/line citations belong in Context (to establish you actually looked) and References (as an appendix), not scattered through every paragraph of Solution Design.

---

## Template Structure

Maps to `templates/02-rfc.md`.

### Header table
Unchanged.

### Business Value
1–2 sentences or a tight list, concrete: what breaks or costs more if this doesn't ship.

### Context
- **Module and service involved** — name it plainly.
- **Current mechanism** — describe today's behavior as a short narrative or diagram, not a file-by-file trace. This section exists so Solution Design is comprehensible; keep it tight enough that a reader carries it forward without rereading.
- **Constraints** — table is fine, one line per constraint.

### Problem Statement
Numbered, plain language, cause → effect. Skip deep code references here — that belongs to the research doc; the RFC can assume the reader has the gist from Business Value + Context.

### Success Criteria
Binary, verifiable bullets, each tied to a numbered problem. No code needed.

### Scope
In-scope / out-of-scope bullets. Plain language deliverables, not file lists.

### Solution Design

**Overview** — one paragraph leading with the non-obvious insight: what did you learn that makes this the right fix? This is the most important paragraph in the doc — if it lands, the steps below should feel obvious.

**Steps** — each step is a short explanation of the mechanism and *why*, before *how*. Use a before/after snippet only per the exception rule above; otherwise describe the change in prose or a bullet list.

**Structure and boundaries** — a Mermaid component diagram of the new units against the existing ones, with arrows in the direction of dependency, plus one line per unit: its responsibility and its package. State that it follows the research doc's `Structure conventions`; if it deliberately does not (a new module with a different layout), say so and link the P0. Mark each boundary that gets an interface (external I/O, stubs, multiple implementations). Rules: `standards/architecture.md`. Class-level detail waits for the impl plan.

**Adding a new [thing] (end-to-end)** — short numbered walkthrough for extensibility. If it's long, say so — that's a signal the design is too complex, not a cue to keep writing.

**Special Cases** — table only for 3+ parallel cases; otherwise prose.

**Flow Diagram** — Mermaid, only where it adds something the prose doesn't already cover.

### Error Handling
Only include if a reader couldn't predict failure behavior from Solution Design already. Table format when included.

### Test Plan
Plain bullets: case, expected behavior. No need to write the actual test code here — that's for the impl plan.

### Alternatives Considered
One paragraph each: what was appealing, why it was rejected, rejection category, revisit condition. No code needed — this is a reasoning record, not a design spec.

### Unresolved Questions, Known Limitations, Future Work, Implementation Learnings
Structure unchanged from the template — plain language throughout.

### References
Where the file/line citations live, kept out of the main narrative above.

---

## File Location

`projects/YYYY-NNN-<name>/02-rfc.md`, copied from `templates/02-rfc.md` in the docs knowledge base.
