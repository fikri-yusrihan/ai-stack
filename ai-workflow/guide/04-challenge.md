# 4. Challenge (big projects only)

## Purpose

Try once to break a big design before writing the plan. Two independent reviewers argue against the RFC; only findings backed by evidence survive; the project owner decides.

## Why

- Challenge a design that is hard to undo while it is still text, because a flaw found after a data migration or contract change costs a rollback across teams.
- Challenge only big projects, because reviewer time is expensive. Small changes are cheap to fix later, so the challenge would cost more than it saves.
- Use two reviewers working alone, because each has blind spots, and reviewers who read each other's notes converge on the same ones.
- Use reviewers outside the author's session, because the author and sub-agents started from the author's context share the author's assumptions.
- Keep only findings backed by evidence (a code line, a number, a probe, a concrete breaking input), so facts drive the outcome rather than who argues hardest.
- The project owner decides, because accepting a risk or stopping the project is a business call, not a review result.

## When to use

Only when the RFC adds a new data store or service, changes more than one service, or is hard to reverse (data migration, contract change, deletion). A config fix or a fix inside one service does not qualify unless it is hard to reverse; hard to reverse always qualifies.

## Owner

- The `general` persona frames the challenge and answers findings.
- Challengers: two independent reviewers outside the author's session, for example the `advisor` persona plus a second senior reviewer. Each works alone. If a second independent reviewer is not available, ask the project owner; do not substitute a sub-agent from the author's session.
- The project owner decides.

## Inputs and outputs

- In: `02-rfc.md` (In Review) and its revision.
- Out: `03-challenge.md` with intent, rubric, verified findings, the author's answer to each, a recommendation labelled as the agents', and the project owner's decision.

## Skill and template

- `challenge`.
- Template `templates/03-challenge.md`.

## What to ask

- "Challenge the RFC for YYYY-NNN before we plan it."

## What the challengers cover

Failure cases (bad input, timeouts, retries, duplicates, ordering), scale (ten times the researched volume, the largest single item), half-finished rollout and rollback, cost and ownership, and "should we build it at all", with the cheapest alternative.

## Done when

- Every surviving finding has an answer: change, accept the risk, or disagree with evidence.
- The project owner's decision is recorded in the Decision table with `Decided by`, the project owner's decision and the date filled in. `lint-docs.py` checks this when the doc is Approved, In Progress or Done.
- RFC changes from the challenge are made and re-checked.
