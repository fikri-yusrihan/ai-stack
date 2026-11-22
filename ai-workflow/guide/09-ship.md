# 9. Ship

## Purpose

Get the verified change reviewed, merged and released in a safe order, with every status checked live.

## Why

- Start shipping only from a Done verification on the current PR head (or a stated exemption), so an untested commit cannot slip in after verification.
- Merge in the stated order, because a PR that depends on another breaks prod if it lands first.
- Read each merge back live, because a queued or auto-merge request is not a merge and status from memory misleads everyone downstream.
- Watch the release, because some failures appear only under real traffic.
- Clean up test data as agreed with the project owner, because deleting the wrong thing is worse than leaving test data for a day.
- Offer `teach` at the end, so the reasons for the design are captured while fresh.

## When to use

After verification is Done on the PR's current head commit. If the head has moved, re-run the affected cases first. A PR that needs no verification (see [Verify](./08-verify.md)) starts here directly; its description says why it is exempt.

## Owner

- The `general` persona opens PRs or marks draft PRs ready, writes the descriptions, and updates the project index only after checking the PR in the forge.
- The project owner reviews the PRs first, then asks for team review; merges and prod steps need their approval.
- Whoever is on call for the service watches the release.

## Inputs and outputs

- In: `06-verification.md` (Done, verified commit equal to the PR head) unless the PR is exempt from verification; `05-impl-plan.md`.
- Out: `07-pr-plan.md` (merge order and external dependencies); open PRs with clean descriptions; after merge, the README row and plan status updated.

## Skills and template

- Use the repository’s PR template and review tools. Request team review when the project owner asks.
- Use the repository’s merge procedure. Remove isolated worktrees only after their work has landed and cleanup is authorized.
- Template `templates/07-pr-plan.md`.

## Landing order

Merge from the bottom of a stack up. Re-check each PR after a rebase. After each merge, confirm the merged state and target branch in the forge. A queued request is still pending.

## Done when

- All PRs are merged in the stated order and read back live.
- The release is watched, with no new error patterns.
- Test data is cleaned up as agreed with the project owner.
- Doc statuses are Done and the README row is updated.
- `teach` is offered to the project owner for the shipped feature ([Teach](./10-teach.md)).
