# 7. Unslop

## Purpose

Clean the diff before anyone else reads it. The rule above all others: "Prefer the simple solution: clean, well-structured code that is easy to understand, not a mud of everything thrown into one giant function."

## Why

- Clean up generated code even when it works, because narrating comments, defensive branches, forwarding wrappers and long functions make it hard to read. Extra code hides bugs, and reviewers see it as unfinished.
- Clean before the PR, because the author knows the code best now and review time is better spent on design. Cleanup costs less before review.
- Delete comments that repeat the code, because they drift out of date and mislead. Keep comments that explain why, because the code cannot convey that reason.
- Have someone other than the author run the comment pass when possible, because authors defend their own comments.
- Limit cleanup to the diff, because tidying neighbouring code mixes unrelated changes and hides the real one.

## When to use

Before opening any PR or marking it ready, and at the end of each plan task.

## Owner

- The author runs the code part (usually the `executor` persona or whoever wrote it).
- Someone who did not write the code runs the comment pass when possible: the `auditor` or `advisor` persona.

## Inputs and outputs

- In: the branch diff against its base.
- Out: a simpler diff and a short cleanup report (what was split or deleted, which comments stayed and why, who did the comment pass).

## Skill

- `unslop` (it includes the no-comment pass).

## What it removes

Giant functions, classes with two jobs, dead code this change left behind, wrappers that only forward, speculative options, defensive checks no input can reach, duplicate helpers, comments that repeat the code. It keeps comments that explain why.

## Done when

- The cleanup report is in the task or PR summary.
- Tests and build pass again after the cleanup.
- Nothing outside the diff was touched.
