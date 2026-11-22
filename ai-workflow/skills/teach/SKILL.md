---
name: teach
description: Offer after every shipped feature (merged and verified), or when the project owner asks "teach me" about something built. Writes a one-page explainer for the project owner - the problem, the options weighed and why this one, how the code flows through the main files, the traps - and ends with 3 to 5 quiz questions. Saves it as 08-teach.md in the project folder.
---

# Teach

## Overview

The project owner should understand how a shipped feature was built and remember why. People make better decisions about a system when they know its foundations, and the reasons are easiest to capture right after shipping.

Write the explainer for the project owner, not a reviewer. Keep it to about one page and base it on the project's records, stating only what the docs and code show.

## When to use it

- After every shipped feature. Once its PRs are merged and `verify-feature` is Done, offer it to the project owner; write it when they say yes.
- On request, for any merged feature or subsystem ("teach me how X works"). If it has no project folder or verification record, work from the merged code and mark the missing parts "not recorded".
- Not before the code is merged: an explainer of a design that may still change teaches the wrong thing.

## Inputs

Read, in this order, and stop when you have what you need:
1. `01-research.md`: Problem Statement, Approach Selection Log.
2. `02-rfc.md`: Solution Design overview, Alternatives Considered, Implementation Learnings.
3. `03-challenge.md` if present: the findings that changed the design.
4. `05-impl-plan.md`: Design Pivots.
5. `06-verification.md`: cases that failed first and why.
6. The merged code: the entry point, the main service, the main boundary. Read the files at the merge commit.

Every statement in the explainer traces to one of these sources. If something is missing, say "not recorded" rather than guessing.

## Write it

Copy `templates/08-teach.md` to `<project>/08-teach.md`. Keep it near one page. Sections:

1. **The problem in one paragraph.** What was broken or missing, and who it hurt. No code.
2. **What we chose and why.** The two or three options considered, one line each, and why the chosen one won. Who decided, quoted if the project owner decided.
3. **How it works.** Build the picture step by step. Start with one sentence naming the thing in general terms. Then walk one real request or job through the main files in order, one line per file: what it does at that step. When there are three or more moving parts, use a short series of small Mermaid diagrams, each adding one piece, rather than one big diagram.
4. **Traps.** Three to five pitfalls for someone changing this code: a hidden constraint, a limit, an ordering rule, the bug found in verification. Name the file for each.
5. **Quiz.** Three to five questions that check understanding of the reasons, not trivia. At least one "what would break if...", one "why not the other option", one "where would you change X". Put answers in a collapsed section at the end so the reader can try first. Answering helps the reasons stick better than reading alone.

## Style

- Plain English, as you would speak to a colleague. Short sentences.
- Lead with the mechanism, not a framing line ("the key insight is..." is cut).
- One name per thing.
- Code only when a line is itself the point (an exact limit, a surprising condition), at most three short snippets.
- Apply `unslop` Part 3 to the text before sending.

## Deliver

Tell the project owner where the file is and paste the first two sections in chat. Offer to explain any part in more detail. If they answer the quiz, check against the records and correct gently, citing the source.
