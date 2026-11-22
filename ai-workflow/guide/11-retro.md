# 11. Retro

## Purpose

Once a week, review what went well and what went wrong in each project, and turn repeated mistakes into rules or checks to prevent them.

## Why

- Review mistakes in a fixed weekly slot while the details are still known, because mistakes repeat when nobody writes them down.
- Move each agreed improvement into a skill step, template field, lint check or guide page, so it is applied by default next time. Rules left only in chat are forgotten.
- Prefer a mechanical check when possible, because a check runs every time and a reminder does not.
- The project owner approves each improvement, because a new rule changes how everyone works and may cost their time.

## When to use

If the team uses retrospectives, run one weekly or after an incident or an escaped bug.

## Owner

- The `general` persona compiles the retro from the week's project threads and updates the project index with open items.
- The project owner approves any improvement that changes the workflow or their own time.

## Inputs and outputs

- In: the week's project threads, project status records, merged PRs, escaped bugs.
- Out: per project, what went well and what went wrong; numbered improvements; parked items and open decisions.

## Turn rules into structure

After the project owner agrees with an improvement, put it where the work happens:
- a step in the matching skill (for example the setting tests and evidence rules live in `verify-feature`);
- a field in a template;
- a check in `scripts/lint-docs.py` when it can be checked mechanically;
- a page in this guide.

Mention the change in the next retro so the team knows it landed.

## Standing rules from past retros

1. Read the code and the live system before writing a plan, and point to the code line behind every claim. Lives in [Research](./02-research.md).
2. Every test case names the evidence that proves it. If that evidence cannot be opened, the case counts as untested, never as a soft pass. Lives in `verify-feature`.
3. Every new setting gets three tests: a non-default value, a value exactly at the limit, and a save followed by reading it back. Lives in `verify-feature`.
4. Before any prod step there is a readiness check: dependent PRs go in a stated order, and test-data cleanup is agreed with the project owner first. Lives in `verify-feature`.
5. A PR's status is written only after checking the PR in the forge, and the project owner's decisions are recorded in their exact words. Lives in `verify-feature`.
6. An approval relayed by another agent can record a design decision. A merge, deploy, prod step, external post or deletion needs the project owner's own instruction to the acting agent.

## Done when

- The project owner has the retro, and their answers to any decision points are recorded in their words.
- Each agreed improvement has a home in a skill, template, lint check or guide page.
