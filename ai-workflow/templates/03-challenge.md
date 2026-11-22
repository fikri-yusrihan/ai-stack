# Challenge: [Feature Name]

<!-- Status values: Draft | In Review | Approved | In Progress | Done | Superseded | Deferred | Cancelled — GUIDELINES.md § Document Status Lifecycle -->
<!-- Only for big projects: a new data store or service, more than one service, or hard to reverse. Skill: challenge. -->
| Field | Value |
|---|---|
| **PIC(s)** | [Author of the RFC] |
| **Challengers** | [two independent reviewers outside the author's session, e.g. `advisor` persona · second senior reviewer] |
| **Created** | YYYY-MM-DD |
| **Status** | Draft |
| **Scope** | [02-rfc.md](./02-rfc.md) at md5 `[md5]` · [POC](./04-poc-simulation.md) if any |
| **Why it qualifies** | [Which trigger: new data store or service / more than one service / hard to reverse] |

---

## Intent

[Two or three plain sentences stating the goal and success criteria, as given to every challenger.]

## Rubric

Write these questions before the attack. The decision turns on them.

1. Does the design meet each success criterion?
2. What fails first under bad input, load or partial failure?
3. What breaks during a half-finished rollout, and how do we undo it?
4. What is the cheapest alternative that gets most of the value?
5. Should we build it at all?

## Findings

Use one block per verified finding. List dropped findings at the end of this section.

### F1. [Title]

- **Found by**: [challenger 1 / challenger 2 / both]
- **Claim**: [What breaks, in one or two sentences]
- **Evidence**: [Code line at commit, probe command and output, number and its source, or the breaking input]
- **Breaks**: [Which success criterion or rubric question]
- **Author's answer**: Change / Accept the risk / Disagree — [what and why]

### Dropped

| Reviewer | Dropped | Why |
|---|---|---|
| [challenger 1 / challenger 2] | [n] | [No evidence / out of scope / duplicate of F1] |

## Rubric answers

1. [Answer, citing findings]
2. ...

## Recommendation (agents' reading)

[Proceed / change the RFC as listed / stop. Label as the agents' view, not a decision.]

## Decision

| Decision | Decided by | Owner decision | Date |
|---|---|---|---|
| ⏳ [Proceed / Change / Stop] | `AI proposed` | — | — |

<!-- Approved, In Progress and Done require a row with Decided by = Owner confirmed or Owner chose, the owner's decision in their own words, and the date. lint-docs.py checks this. -->

## RFC changes made

| Finding | RFC section changed | Re-checked by |
|---|---|---|
| — | — | — |
