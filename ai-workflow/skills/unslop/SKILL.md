---
name: unslop
description: Use before opening any PR, and before marking a plan task done. A required cleanup pass over the diff - simplify structure, delete dead code, needless wrappers and comments that repeat the code, keep comments that explain why - then clean the PR text. Includes the no-comment pass. Applies the top rule first, then the architecture standard (S1 to S9).
---

# Unslop

## The rule above all others

> "Prefer the simple solution: clean, well-structured code that is easy to understand, not a mud of everything thrown into one giant function."

Every step below serves this sentence. If a step conflicts with it, the sentence wins. The rules that make it checkable live in `standards/architecture.md`: checklist S1 to S9 covers file placement, naming, one responsibility per class, size triggers, dependency direction, interfaces at external boundaries, failure contracts, models per layer and visible wiring. This skill checks the diff against those rules.

## Overview

AI-written code tends to work yet be hard to read: comments that narrate, needless defensive branches, wrappers that only forward a call, and one long function that does everything. A reviewer sees unfinished work, and the extra code hides the next bug. This pass removes it before anyone else has to read it.

Scope is the diff of this change only: files and lines this work added or made obsolete. Adjacent code stays as it is (`start-project` rule "Don't clean up adjacent code"; architecture standard P5, which forbids restructuring existing code as a side effect). Restructuring existing code needs its own plan task.

The pass has three parts, in order: code, comments, PR text.

## When to run it

- Before opening a PR or marking a draft PR ready. Required.
- At the end of each plan task, as part of the code-quality bar in `execute-impl-plan` step 4.
- After a large fix-up commit, before asking for re-review.

## Part 1: Code

Read the full diff (`git diff <base>...HEAD`), not a summary. For each item, fix it or explain why it stays.

1. **Giant functions.** A method over about 40 lines, nested more than 3 levels, or doing more than one job (parse, decide, call out, map) is split into named steps. Each new function's name says what it does. See S3 (one reason to change per class) and S4 (size triggers: a class over about 300 lines, a method over about 40, more than 5 collaborators).
2. **Mixed responsibilities.** Split a class whose job needs "and" to describe it (S3). Keep orchestration, rules, I/O and mapping separate.
3. **Dead code.** Delete what this change made unused: imports, fields, methods, parameters, feature-flag branches that no longer fork, mid-migration scaffolding, commented-out code.
4. **Needless wrappers.** A function or class that only forwards to another with the same arguments goes, unless it is the interface at an external boundary (S6, the rule that external I/O sits behind an interface).
5. **Speculative code.** Options, hooks, generic types or config switches with no caller today go. A pattern needs a present problem (standard section 4).
6. **Defensive noise.** Null checks for values that cannot be null, catch blocks that log and rethrow unchanged, retries around calls that are not retried elsewhere. Keep a guard only when a real input can reach it, and say which.
7. **Duplicated logic.** Replace a second copy of an existing helper with a call to it (`start-project` reuse rules).
8. **Names.** Names come from the domain and state the responsibility. No `Manager`, `Helper`, `Util`, `Processor` without a domain noun (S2).
9. **Simpler shape.** When the same result needs fewer moving parts (a table instead of a switch chain repeated twice, a plain value instead of a builder for three fields), use the simpler one. Simple means easy to follow, not fewest lines.

Then run the repo's tests and build again. Revert a cleanup that breaks a test; do not "fix" the test.

## Part 2: Comments (the no-comment pass)

The code should say what it does. Keep comments only when they explain why, plus the fixed exceptions listed under "Keep" below.

Delete:
- comments that restate the next line ("increment the counter", "call the service");
- banners, section dividers and change-history notes ("added by", "fixed on");
- commented-out code;
- TODOs with no assignee or ticket;
- long justifications that a better name or a smaller function would make unnecessary. Fix the code, then delete the comment.

Keep, and make short:
- why the code does something surprising: a hidden constraint, a workaround for a library or platform bug, an invariant that is not visible locally, a deliberate trade-off. Link the issue, RFC or decision when one exists;
- doc comments on a public API or contract, an intended exception, because callers read them without opening the code;
- license headers and lint suppressions that have a stated reason.

A comment explaining why our code works this way is a hint. First ask whether a clearer name, a type or a small extracted function would make the reason obvious. If yes, do that and delete the comment. If no, keep it.

**Fresh eyes.** Authors defend their own comments. When a sub-agent is available, have someone other than the author run Part 2: the `auditor` or `advisor` persona, or a second reviewer. They mark each comment as delete, keep or reshape, and the author applies the result. If no second reviewer is available, say so in the PR report.

## Part 3: PR text and commit messages

Use the repository's PR template and the project's PR plan, then clean it:
- Plain words. Say what changed and why, and what the PR does not touch (`GUIDELINES.md` PR rule).
- One name per thing; use it every time.
- No filler ("in order to" becomes "to"), no praise, no "not just X but Y", no stock closers.
- Numbers instead of adjectives: "cuts the query from 3 calls to 1", not "greatly improves".
- Claims about tests or deploys only with their evidence (see `verify-feature`).

## Output

Report in the task or PR summary:
- what was simplified or split (function or class names);
- deleted: count of dead items and comments, with the main ones named;
- comments kept, each with its one-line reason;
- who ran the comment pass, and whether it was the author;
- anything left for a separate task because it is outside this diff.

## Red flags

| Thought | Reality |
|---|---|
| "It works, so it is done" | A working change with the wrong structure is not done. |
| "The comment helps the reader" | If it repeats the code, it does not. If it explains why, keep it. |
| "I'll split this function in a follow-up" | Split your own new code now. Only existing code waits for its own task. |
| "This wrapper might be useful later" | Later gets its own change. Delete it. |
| "While I'm here, I'll tidy the neighbour" | Out of scope. Note it, don't touch it. |
| "Fewer lines is simpler" | Simpler is easier to follow. Sometimes that is more, smaller functions. |
