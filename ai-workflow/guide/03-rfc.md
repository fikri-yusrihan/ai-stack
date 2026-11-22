# 3. RFC

## Purpose

Write the design for the chosen approach so a reviewer can follow it without opening the code: how it fits what exists, why it reaches the goal, and what was rejected.

## Why

- Write the design before coding, because it is cheaper to change: a problem found in design review is often fixed in minutes; in a PR, it often costs days.
- Map every design step to a numbered problem, so nothing is built without a problem to solve.
- Make success criteria binary (met or not met), because a vague criterion can always be declared met.
- Write the test plan here, before the code exists, so tests check what the design promised rather than what the code happens to do.
- Give every new setting three cases in the test plan (a non-default value, a value at the limit, and a save followed by a read-back), because ordinary tests pass even if a setting is accepted but never stored, or only works at its default.
- Keep a rejection category and revisit condition for each rejected alternative, so a later reader knows when to reopen the choice.

## When to use

After the Approach Selection Log is signed off.

## Owner

- The `general` persona writes the RFC.
- A `librarian` sub-agent fact-checks the Context section.
- The `advisor` persona reviews hard design calls.

## Inputs and outputs

- In: `01-research.md` with the signed-off approach.
- Out: `02-rfc.md` with Business Value, Context, Problem Statement, binary Success Criteria, Scope, Solution Design (including Structure and boundaries), Test Plan, Alternatives Considered.

## Skill and template

- `writing-rfc-doc`.
- Template `templates/02-rfc.md`.

## Test plan note

Write the cases that `verify-feature` will run later: one per success criterion, and for every new setting a non-default case, an at-limit case (the largest value expected in real use when there is no limit) and a save-then-read-back case.

## Done when

- Every design step maps to a numbered problem.
- Every rejected alternative has a rejection category and a revisit condition.
- Structure and boundaries follows the repo's conventions, or names the blocking question that overrides them.
- Next: if the project is big, go to [Challenge](./04-challenge.md); otherwise to [Plan](./05-plan.md). If the mechanism is novel, run the [optional POC](./05-plan.md#optional-poc) before planning.
