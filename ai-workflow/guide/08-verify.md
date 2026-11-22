# 8. Verify

## Purpose

Prove the change works in a real environment, case by case, with evidence an independent checker can open, before calling the PR verified or taking any prod step.

## Why

- Run the feature on the approved test target, because green unit tests and CI do not exercise it the way a user or caller does.
- Name each case's evidence and a second place to read it (a separate source that shows the same result, not a copy of the first), so untested cases are not reported as PASS. Evidence that does not open is UNTESTED, never a soft pass.
- Give every new setting three cases (a non-default value, a value exactly at the limit or, with no limit, the largest value expected in real use, and a save followed by a read-back), because they catch values accepted but never persisted and settings that only work at their default.
- Have an independent checker grade every case, so the author does not grade their own work. The checker reads the cases before the run, so weak expected results are fixed before anyone is tempted to fit them to the output.
- Grade from raw evidence, because the runner's summary already contains their interpretation. Partial is never PASS.
- Run verification on a draft PR or branch commit and require the verified commit to equal the PR head at the readiness check, so the code that ships is the code tested.
- Check readiness before prod (PR order, cleanup list, rollback step, the project owner's approval), because release incidents often come from order, leftover test data or no way back, not the feature itself.
- Write PR status only after a live check, because status from memory is often already wrong.

## When to use

Every PR that changes behaviour. Not needed for PRs that change no behaviour: docs-only, formatting-only or behaviour-free dependency bumps. Use the repository’s infrastructure plan and apply evidence for infrastructure changes.

A PR with no project folder (a small fix) puts its cases, expected results and evidence in the PR description instead of `06-verification.md`. The checker rule is the same, and an approved test deployment is still required when the change is deployable. The description must also have a "Cases reviewed" line (the cases the checker reviewed) and a "Checked by" line (the checker, named as in `06-verification.md`). Lint cannot see the PR description, so the checker confirms those lines by hand.

## Owner

- The `general` persona (or the `executor` it dispatches) sets up the test target at the candidate commit, runs the cases and saves the evidence.
- The checker is the `advisor` persona (an independent reviewer outside the author's session) or the project owner. They read the cases before the run, then grade every case from the raw evidence. An `auditor` sub-agent started from the author's own session is not independent.
- The project owner approves the prod step in their own instruction to the acting agent.

## Inputs and outputs

- In: the draft PR (or branch) and its head commit, the RFC's test plan. Verify runs before the PR is marked ready; if the head moves, the affected cases are re-run.
- Out: `06-verification.md`: deploy record, case table with PASS, FAIL or UNTESTED and evidence for each, failures and re-runs, test data and cleanup list, readiness check.

## Skill and template

- [`verify-feature`](../skills/verify-feature/SKILL.md), using the project’s approved test procedures.
- Template `templates/06-verification.md`.

## Done when

- Every case is PASS in the checker's column, partial counts as FAIL, the verified commit equals the PR head, and the doc's Status is Done. `lint-docs.py` rejects a Done verification doc with missing or open cases, an unreviewed case list, or a checker other than the `advisor` persona or the project owner.
