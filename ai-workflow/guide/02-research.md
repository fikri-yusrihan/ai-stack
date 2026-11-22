# 2. Research

## Purpose

Read the code and live state to learn what the system does today, then compare the status quo and at least three other approaches, and record the choice and who made it.

## Why

- Read the code and live state first, so the design starts from facts rather than memory. Claims that point to a code line can be checked; claims from memory cannot.
- Compare at least three approaches plus the status quo, because a single option hides its trade-offs and a choice between two is often a false choice.
- Complete the structure survey (layout, naming, nearest small example, outliers) here, so the design follows the repo rather than the author's habits.
- Record every rejected option and its reason in the Approach Selection Log, so the same idea is not proposed again months later without new facts.
- Get the project owner's sign-off on the choice, because the approach is the most expensive decision to reverse.
- For teardown or logging work, start from a table built from the code (every module and what it creates; every logging call and what it writes), because a list from memory misses the item that causes the incident.

## When to use

After intake, for every project.

## Owner

- The `general` persona writes the doc.
- `librarian` sub-agents run parallel lookups, one question each, including the structure survey and read-only live questions. Prod reads need the project owner's approval.
- The `advisor` persona stress-tests the chosen approach on hard calls.
- The project owner chooses or confirms the approach.

## Inputs and outputs

- In: the agreed problem statement.
- Out: `01-research.md` with Codebase Context, Structure conventions, Constraints, Approaches Evaluated (status quo plus at least three), Recommendation, and the Approach Selection Log.

## Skill and template

- `writing-research-doc`, every time you enter this phase.
- `standards/architecture.md` § 5 for the structure survey fields.

## Done when

- Every claim traces to code or data read this session.
- No solution is proposed before the facts section.
- The Approach Selection Log names the options, why each was rejected (with category), and the choice with `Decided by` = `Owner confirmed` or `Owner chose`.
