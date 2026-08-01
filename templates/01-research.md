# Research: [Topic]

| Field | Value |
|---|---|
| **Context** | [Service/module name and repo] |
| **Date** | YYYY-MM-DD |
| **Status** | Draft \| In Progress \| Final |
| **Session PWD** | [Working directory where this opencode session was opened — fill from env on session start] |

---

## Problem Statement

> One paragraph. What is broken, painful, or missing? Write this as a causal chain: name the specific code path, explain what it does wrong, trace that to the consequence. A reader should be able to verify or refute the problem by reading the referenced code.
>
> Good: "`TripBookingPageLayout.generateLayoutPage()` contains a ~25-case switch on `rawComponent.getType()`. Every new component type requires changes in 3 files — the switch, the converter registry, and the schema. The switch has no exhaustiveness check, so a missing case silently returns null at runtime."
>
> Bad: "The current code is hard to maintain."

---

## Codebase Context

### Key files

| File | Role |
|---|---|
| `FileName.java` | What it does — be specific about the method or class |
| `AnotherFile.java` | What it does |

### Existing patterns found in codebase

> Document what you found by reading the code. Name specific classes, methods, line numbers. No speculation — read first, write second.
>
> For each pattern: describe what it does and how it relates to the problem space. Call out patterns worth reusing AND patterns worth avoiding.

**[Pattern name]** — short description  
`ClassName.methodName()` (L[n]–[n]): what it does and why it matters here.

> List patterns that are relevant to the solution space. Both patterns to reuse AND patterns to avoid.

**Absent patterns (confirmed not present)**:
- No `SomePattern` anywhere in the repo
- No `SomeApproach` — confirmed by [search method]

### Constraints

> What cannot change? External APIs, generated code, shared contracts, team ownership boundaries.

- [Constraint 1] — why it exists
- [Constraint 2] — why it exists

### Special cases

> Edge cases discovered during reading that any solution must handle. These often become P0 blocking questions.

1. `SOME_CASE` — what makes it special and why a naive solution would break it

---

## Approaches Evaluated

> Evaluate at least 3 approaches. Include approaches you rejected — the reasoning belongs in writing.
> Each approach should describe the mechanism and explain why it fits or doesn't fit this codebase specifically. Build toward the verdict; don't just list pros and cons.

### Approach 0: Status Quo

Keep the current code unchanged.

**Verdict**: ❌ [Why the problem is worth solving — be specific about the ongoing cost]

---

### Approach 1: [Name]

**Core idea**: [One sentence.]

```java
// Concrete sketch — illustrating the mechanism, not production code
```

[Paragraph explaining how this would work in this codebase specifically, including relevant constraints it satisfies or violates. The verdict should feel like the conclusion of this paragraph, not a separate label.]

**Verdict**: ✅ / ⚠️ / ❌ — [One sentence justification]

---

### Approach 2: [Name]

[Same structure as Approach 1]

**Verdict**: ✅ / ⚠️ / ❌ — [One sentence justification]

---

### Approach 3: [Name]

[Same structure as Approach 1]

**Verdict**: ✅ / ⚠️ / ❌ — [One sentence justification]

---

### Comparison Table

> Use this table only when approaches have parallel dimensions worth comparing. If the comparison is obvious from the approach descriptions, skip it.

| Approach | [Criterion 1] | [Criterion 2] | [Criterion 3] | Risk | Effort |
|---|---|---|---|---|---|
| 0. Status quo | — | — | — | None | None |
| 1. [Name] | | | | Low/Med/High | Low/Med/High |
| 2. [Name] | | | | | |
| 3. [Name] | | | | | |

---

## Recommendation

### Short-term: Approach N — [Name]

[Why this approach fits the current codebase, constraints, and team. One paragraph.]

### Long-term: Approach N — [Name] *(if applicable)*

[If the short-term is a stepping stone, describe the long-term target and what would need to change to get there.]

---

## Open Questions

> Questions that need answers before implementation can start. These become P0 items in the impl plan.

- [ ] [Question] — why it matters for the design
- [ ] [Question] — options and their implications

---

## Approach Selection Log

> **Fill this section before closing Phase 2.** This is the decision record — not the RFC design, but the *reasoning path* that led there. A future agent reading this should understand why rejected approaches were rejected, and whether they're worth revisiting.
>
> **Phase exit condition**: Do not proceed to RFC until this section is complete.

### [Date] — Approach selection

**Options on the table**: [A], [B], [C]

**Constraints active at this moment**:
- [Constraint] — source: [file, line, or person who established it]

**Eliminated approaches**:

| Approach | Rejection category | Reason | Revisit condition |
|---|---|---|---|
| [Approach A] | `TECHNICAL_INFEASIBLE` \| `BREAKS_EXISTING_CONSTRAINT` \| `COST_TOO_HIGH` \| `DEFERRED` \| `SUPERSEDED` | [Specific reason] | [Condition under which this would be worth re-evaluating, or "Not worth revisiting"] |
| [Approach B] | | | |

**Proceeding with**: [Approach C]

**Decided by**: `AI proposed` \| `[OWNER] confirmed` \| `[OWNER] chose`

**Open questions that could change this**:
- [Question — if answered differently, which approach becomes viable]

---

### Rejection Category Reference

| Category | Meaning | Revisitable? |
|---|---|---|
| `TECHNICAL_INFEASIBLE` | Can't be done given the current stack or constraints | Only if constraints change |
| `BREAKS_EXISTING_CONSTRAINT` | Violates an established contract, interface, or team boundary | Only if constraint is lifted |
| `COST_TOO_HIGH` | Technically feasible, wrong effort/risk ratio *at this time* | Yes — when scope or timeline changes |
| `DEFERRED` | Good idea, wrong time or scope | Yes — explicitly worth revisiting |
| `SUPERSEDED` | Was the plan, replaced mid-implementation | See RFC Implementation Learnings |

---

## References

- `FileName.java` — L[start]–L[end]: [what's there]
- [External reference if relevant]
