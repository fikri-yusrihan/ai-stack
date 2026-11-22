# 5. Plan

## Purpose

Settle every question that would change the code, then write a plan the executing agent can follow without guessing.

## Why

- Answer blocking questions (P0s) before any code, because answering halfway through a build means rework, or worse, an unnoticed guess.
- Unblock a P0 only with the project owner's answer, never `AI proposed`, because agents filling their own gaps let unapproved designs reach production.
- Name files, code sketches and a definition of done per task, so the executor builds the design and the reviewer can compare the diff to the plan.
- Write the Structure and Responsibilities table before the code, because placement and boundaries are cheap to fix on paper and expensive after review.
- Include the verification task in the last phase, so testing is planned work rather than an afterthought.

## When to use

After the RFC is approved (and the challenge decided, for big projects).

## Owner

- The `general` persona writes the plan and lists the blocking questions (P0s, which must be answered before any code).
- The project owner answers every P0.
- The `auditor` persona reviews the finished plan.

## Inputs and outputs

- In: `02-rfc.md`, `03-challenge.md` if any.
- Out: `05-impl-plan.md`: P0 table, Structure and Responsibilities table, phases of tasks with code sketches and checklists, a final wire-up and cleanup phase, Design Pivots (empty), Risk Register. The test cases from the RFC carry into the verification task.

## Skill and template

- `writing-impl-plan-doc`.
- Template `templates/05-impl-plan.md`.

## Done when

- Every P0 is ✅ with `Decided by` = `Owner confirmed` or `Owner chose`. `AI proposed` never unblocks code.
- The auditor's findings are resolved or dismissed with a reason.
- Every deviation from the structure checklist (S1 to S9 in `standards/architecture.md`) is named with its reason.
- For changes in behavior, the last phase includes a verification task that uses `verify-feature`.
- The project owner approves the plan before implementation starts.

## Optional POC

When a novel mechanism needs proof, pick one question and run a small, reproducible experiment before settling blockers or writing tasks. Record the result and any design changes in [`04-poc-simulation.md`](../templates/04-poc-simulation.md).
