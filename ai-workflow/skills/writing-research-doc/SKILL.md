---
name: writing-research-doc
description: Use when writing the Phase 1 research / codebase-assessment document (01-research.md) after exploring a codebase, before proposing any solution
---

# Writing Research Docs

## Overview

Translates codebase exploration into `01-research.md` — the fact-finding artifact for a project in `projects/YYYY-NNN-<name>/`. The reader is a human engineer (possibly not the one who wrote it, possibly not deep in this specific file) who needs to understand **what the system actually does today** well enough to evaluate the approaches later in the doc. They are not going to open the referenced source files to follow along — the doc has to carry the explanation on its own.

This doc still requires the same investigation rigor as before: every claim must come from code you actually read, never speculation. What changes is the *artifact* — translate what you found into plain language, not a citation trail.

---

## Investigation: fan out to the librarian agent

Don't read the whole codebase yourself in the orchestrating context. Fan out exploration across the `librarian` persona — one per file, module, or service worth exploring in parallel — rather than reading everything in the orchestrating context.

- Brief each subagent with a specific question ("how does X get looked up today", "does pattern Y exist anywhere in this repo"), not "go explore this codebase."
- Each subagent reports back what it found, with enough specificity that you don't need to re-read the file yourself to trust it.
- You (the orchestrator) synthesize those reports into the doc. Personally verify anything that ends up load-bearing for the Problem Statement or a Verdict before you write it down — a subagent's report is a lead, not a citation you can forward unchecked.

This is the same dispatch pattern as `execute-impl-plan`'s implementation step, applied to research instead of coding.

---

## Writing Principles

**Explain how the code works.** For example, the renderer reads a block from its cache and fetches the block from storage on a miss. Cite the source where it helps a reviewer verify the explanation.

**Keep it short.** A reader should have the full picture in a few minutes. If a section restates something already clear from the section above, cut it.

**Bullets and diagrams over prose walls.** A sequence of steps is a bulleted list. Anything with a branch, a fallback path, or more than ~4 steps is a Mermaid diagram (flowchart for request paths, sequence diagram for calls between services). Prose is for the connective reasoning between steps, not for the steps themselves.

**Name things by role, not by class.** "The pricing calculator" or "the currency cache" reads better than a class name, unless that class name is genuinely how the team refers to the thing in conversation.

**Reference code sparingly, and only when it's load-bearing.** A file/line citation earns its place when the exact detail matters and prose can't convey it precisely — an exact threshold, an actual error string, a genuinely surprising one-liner. Don't cite a file just to prove you read it. One citation per claim, max, and never a full method signature or class hierarchy dump.

**Verify silently, explain plainly.** The bar is not "cite it," it's "get it right." Read the file, confirm the behavior, then write the explanation as if you were describing it to a colleague over a coffee, not annotating a pull request.

---

## Template Structure

Maps to `templates/01-research.md`. Fill every section that phase 1 has reached.

### Header table
Unchanged — Context, Date, Status.

### Problem Statement
One short paragraph, plain language. What's broken or missing, and what it costs someone (a user, an operator, a future engineer)? Cause → effect, no code.

> Good: “Adding a document block requires changes in the renderer, registry and schema. If the renderer lacks a case, the document silently drops the block.”
> Put the exact method and source reference after the explanation so the reader can verify it.

### Codebase Context
Replace a file-by-file walkthrough with **how the system behaves today**, told as a short bulleted flow or a Mermaid diagram. Call out the 1–2 existing patterns worth reusing and the 1–2 worth avoiding, described by what they do — not by their line numbers.

- **Existing patterns** — one line each: what it does, why it matters here (reuse or avoid).
- **Absent patterns** — name anything you specifically confirmed does NOT exist, so the next reader doesn't go looking.
- **Structure conventions** — the template's table, filled with the fields in `standards/architecture.md` § 5 as structured fields, not prose, so they survive compaction. Take them from a Structure survey (see `standards/architecture.md` § 5), by a `librarian` or yourself, from code you read. Without these, the RFC and plan cannot follow the repo's convention.
- Keep a **Key Files** table only as an optional appendix at the bottom of this section, for the next AI session to jump in quickly — not as the primary explanation.

### Constraints / Special Cases
Bullets, plain language: what can't change and why, and which edge cases any solution must survive.

### Approaches Evaluated
For each approach (including Approach 0 — status quo):

- **One paragraph**: what the approach is, **how it integrates with what exists today** (what stays as-is, what it replaces), and **whether/how it achieves the stated goal**. This paragraph is the explanation — the verdict should read as its natural conclusion.
- A small diagram if the approach changes the shape of a flow.
- Skip the "concrete sketch" code block by default. Only include a few illustrative lines if there's genuinely no other way to convey a subtle mechanism — this is the exception, not the template default.
- **Verdict**: ✅ / ⚠️ / ❌ — one sentence.

Comparison table, Recommendation, Open Questions, Approach Selection Log — structure unchanged from the template, written in the same plain-language style.

### References
Keep this section as the place heavier file/line citations live, for the next AI session's benefit — not inline in the prose above.

---

## File Location

`projects/YYYY-NNN-<name>/01-research.md`, copied from `templates/01-research.md` in the docs knowledge base.
