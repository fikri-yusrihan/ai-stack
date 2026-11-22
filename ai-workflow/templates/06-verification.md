# Verification: [Feature Name]

<!-- Status values: Draft | In Review | Approved | In Progress | Done | Superseded | Deferred | Cancelled — GUIDELINES.md § Document Status Lifecycle -->
<!-- Skill: verify-feature. Done means every case PASS, checked by the advisor persona (outside the author's session) or the project owner, graded from the raw evidence. -->
| Field | Value |
|---|---|
| **PR(s)** | [link] · head commit `[sha]` |
| **Author** | [who wrote the code] |
| **Runner** | [who ran the cases] |
| **Cases reviewed** | [checker] · [YYYY-MM-DD HH:MM] · every case has a written expected result |
| **Checked by** | [advisor persona or project owner, not the author] · [YYYY-MM-DD HH:MM] |
| **Created** | YYYY-MM-DD |
| **Status** | Draft |
| **Related Docs** | [RFC](./02-rfc.md) · [Impl Plan](./05-impl-plan.md) |

---

## Deploy record

- **Environment**: [approved test environment or representative local setup]
- **Verified commit**: `[sha]` on the draft PR or branch (must equal the PR head at the readiness check)
- **Branch and commit**: `[branch]` at `[sha]`
- **Run**: [run URL or reproducible command and result]
- **Rollout or setup**: [completion and observed version]
- **Health**: [HTTP code and body]
- **Logs or diagnostics**: [version, observations, evidence link]

## Cases

Write cases and have the checker review them before the run. Every new setting has a non-default case, an at-limit case (the largest value expected in real use when there is no limit) and a save-then-read-back case. The checker grades the last column from raw evidence, not the runner's grade; partial is never PASS. Case ids are C1, C2, ...

| # | Case | Expected | Evidence (path or link) | Second place to read it | Runner grade | Checker grade |
|---|---|---|---|---|---|---|
| C1 | [What is done] | [Result that is met or not] | [artifacts/verify-YYYYMMDD/c1.json] | [stored record or log link] | PASS / FAIL / UNTESTED | PASS / FAIL / UNTESTED |
| C2 | [New setting X = non-default value] | | | | | |
| C3 | [New setting X = at the limit, and one over] | | | | | |
| C4 | [Save X, then read it back] | | | | | |

**Totals**: PASS [n] · FAIL [n] · UNTESTED [n]

## Failures and re-runs

- [C#]: [what happened, cause, fix commit, re-run date and new grade]

## Test data and cleanup

Write this before creating any test data.

| Item | Where | Created | Cleanup agreed with the project owner | Removed |
|---|---|---|---|---|
| [`__e2e_*` resource] | [test environment] | [date] | [owner's words and date / pending] | [date / no] |

## Readiness check before prod

- [ ] Every case PASS, checked by the advisor persona or the project owner, graded from the raw evidence
- [ ] PR state read live from the forge at [time]: [state, draft, merged, head]
- [ ] Verified commit equals the PR head
- [ ] Merge order of dependent PRs: [PR A, then PR B, because ...]
- [ ] Cleanup list agreed with the project owner
- [ ] Rollback step: [exact command or revert]
- [ ] After-release watch: [what, by whom]
- [ ] The project owner's go for the prod step: "[their exact words]" ([date]), in their own instruction to the acting agent

An approval relayed by another agent can record a design decision; a merge, deploy, prod step, external post or deletion needs the project owner's own instruction to the acting agent.
