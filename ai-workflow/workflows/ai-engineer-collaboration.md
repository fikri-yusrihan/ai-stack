# AI–Engineer Collaboration

Start with the [numbered workflow guide](../guide/README.md). Read [Start Project](../skills/start-project/SKILL.md) for the phase gates and [Guidelines](../GUIDELINES.md) for document standards.

## The Collaboration Model

The engineer owns decisions and approves the gates. The assistant gathers evidence, compares options, drafts decisions for review and carries out approved work. Read unfamiliar code together and review the diff in small checkpoints.

## Confidence and evidence

Fluent output can contain a wrong assumption, a missed case or an unsupported constraint. Ask what the assistant read, what it ruled out, and which checks could change the conclusion. Write the problem in your own words before asking the assistant to restate it. Record critical constraints as fields and re-check them when work crosses a session boundary.

## Session Handoff

When ending a session, the AI produces a handoff summary:

Fields:
1. **Goal** — what the feature is trying to accomplish
2. **Progress** — done / in-progress / blocked
3. **Critical context** — decisions made, rejected approaches, open questions
4. **Next steps** — exactly what to do next, in order
5. **Key files** — files that matter for resuming

Without this, the next session starts from scratch.

---

## Collaboration Anti-Patterns

| Anti-Pattern | What it Looks Like | Correct Behavior |
|---|---|---|
| Speculating before reading | AI proposes a solution without reading the relevant code | Insist: "read the file first" |
| Fixture gaming | AI modifies test assertions to make failing tests pass | Revert. Fix the production code |
| Scope creep | AI refactors adjacent code while fixing a bug | Scope to the minimum correct change |
| Confident hallucination | AI states a library behavior it hasn't verified | Ask: "show me where you verified this" |
| Premature implementation | AI starts writing code before the design is settled | Hold implementation until RFC is reviewed |
| Context drift | AI forgets a constraint stated 10 turns ago | Re-state critical constraints; put them in docs |
| Silent assumption | AI assumes a behavior rather than surfacing it as a question | Block any P0 ambiguity before coding |
| Constraint buried in prose | Critical constraint stated in a paragraph, not a structured field | Extract to structured schema — prose gets compacted, fields don't |
| Reviewing for comfort | Reading a plan and asking "does this look right?" | Review against explicit criteria you defined before reading the plan |

---
