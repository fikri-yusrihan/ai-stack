# 6. Implement

## Purpose

Build the approved plan one task at a time, in the right place, and keep the plan live.

## Why

- Use one task per dispatch, so each change stays small enough to review and easy to revert.
- Use worktrees per phase, so parallel work does not collide and the main checkout stays clean.
- Never edit tests to make them pass, because a test changed to match the code no longer tests anything.
- Stop work for a design change and update the plan and RFC first, so the docs stay accurate and the next session does not build on a stale design.
- Report each task's structure against the standard, so placement problems are caught per task instead of piling up in the PR.

## When to use

After the plan is approved and the project owner asks to execute it.

## Owner

- The `general` persona owns every PR from start to finish: worktrees, dispatch, review of results, tests.
- The `executor` persona implements one task per dispatch.

## Inputs and outputs

- In: `05-impl-plan.md` with all P0s signed off.
- Out: commits on worktree branches (location set in `execute-impl-plan`); task statuses and Design Pivots updated in the plan.

## Skill and template

- `execute-impl-plan` (PR split, sync, worktree, dispatch, code-quality bar).
- Use the repository’s normal review tooling for dependent PRs and infrastructure changes.
- `standards/architecture.md` for every new class: its checklist S1 to S9 covers where files go, one job per class, dependency direction and an interface at every external boundary.

## Done when

- Each task's definition of done is met and its structure report matches the diff.
- Tests pass, and no assertion was changed to make a test pass. An assertion changes only for a behaviour change the plan records.
- Any design change stopped the work and updated the plan and RFC first.
- Next: [Unslop](./07-unslop.md) before any PR.
