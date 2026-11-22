# Research: [Topic]

<!-- Status values: Draft | In Review | Approved | In Progress | Done | Superseded | Deferred | Cancelled — GUIDELINES.md § Document Status Lifecycle -->
| Field | Value |
|---|---|
| **Context** | [Service/module name and repo] |
| **Date** | YYYY-MM-DD |
| **Status** | Draft |

---

## Problem Statement

> One paragraph. What is broken, painful, or missing? Write this as a causal chain: name the specific code path, explain what it does, trace that to the bad outcome.
>
> Good: "`DocumentRenderer.renderBlock()` contains a ~25-case switch on `block.type()`. Every new component type requires changes in 3 files — the switch, the converter registry, and the schema. The switch has no exhaustiveness check, so a missing case silently returns null at runtime."
>
> Bad: "The current code is hard to maintain."

---

## Codebase Context

### Key files

| File | Role |
|---|---|
| `FileName.[ext]` | What it does — be specific about the method or class |
| `AnotherFile.[ext]` | What it does |

### Existing patterns found in codebase

> Document what you found by reading the code. Name specific classes, methods, line numbers. No speculation — read first, write second.
>
> For each pattern: describe what it does and how it relates to the problem space. Call out patterns worth reusing AND patterns worth avoiding.

**[Pattern name]** — short description  
`ClassName.methodName()` (L[n]–[n]): what it does and why it matters here.

**Absent patterns (confirmed not present)**:
- No `SomePattern` anywhere in the repo — confirmed by [search method]
- No `SomeApproach` — confirmed by [search method]

### Structure conventions

> How the target repo organizes code today, from code you read (rules and survey method: `standards/architecture.md` § 5). Structured fields so they survive compaction. Write "absent" where something does not exist. Do not propose a structure here.

| Field | Finding (with paths) |
|---|---|
| Organizing principle | [by feature / by layer / mixed — package tree to two levels] |
| Layer sub-packages | [e.g. controller, service, repository, listener, model] |
| Naming suffixes | [services, repositories, clients, listeners, models] |
| Boundary style | [how interfaces and implementations are declared, and where each lives] |
| Wiring style | [constructor injection / field injection / plain `new` / config classes] |
| Nearest analogue | [closest small, cohesive existing feature, with paths] |
| Outliers not to copy | [classes past the size triggers, with line counts] |
| Test layout | [where tests sit, framework] |

### Constraints

> What cannot change? External APIs, generated code, shared contracts, team ownership boundaries.

- [Constraint 1] — why it exists
- [Constraint 2] — why it exists

### Special cases

> Edge cases discovered during reading that any solution must handle. These often become P0 blocking questions.

1. `SOME_CASE` — what makes it special and why a naive solution would break it

---

## Approaches Evaluated

> Evaluate the status quo plus at least 3 other approaches. Include approaches you rejected — the reasoning belongs in writing.
> Each approach should describe the mechanism and explain why it fits or doesn't fit this codebase specifically. Build toward the verdict; don't just list pros and cons.

---

### Approach 0: Status Quo

Keep the current code unchanged.

**Verdict**: ❌ [Why the problem is worth solving — be specific about the ongoing cost]

---

### Approach 1: [Name]

**Core idea**: [One sentence.]

```text
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

> Questions that must be answered before implementation can start. These become P0 items in the impl plan.

- [ ] [Question] — why it matters, what the options are
- [ ] [Question] — options and their implications

---

## Approach Selection Log

> **Fill this section before closing Phase 2.** This is the decision record — not the design, but the reasoning path that led there. A future agent reading only this section should understand why rejected approaches were rejected and whether they're worth revisiting.
>
> **Phase exit condition**: Do not proceed to RFC until this section is complete.

### [Date] — Approach selection

**Options on the table**: [A], [B], [C]

**Constraints active at this moment**:
- [Constraint] — source: [file, line, or person]

**Eliminated approaches**:

| Approach | Rejection category | Reason | Revisit condition |
|---|---|---|---|
| [Approach A] | `TECHNICAL_INFEASIBLE` \| `BREAKS_EXISTING_CONSTRAINT` \| `COST_TOO_HIGH` \| `DEFERRED` \| `SUPERSEDED` | [Specific reason] | [Condition, or "Not worth revisiting"] |
| [Approach B] | | | |

**Proceeding with**: [Approach C]

**Decided by**: `AI proposed` \| `Owner confirmed` \| `Owner chose`

**Open questions that could change this**:
- [Question — if answered differently, which approach becomes viable]

---

## References

- `FileName.[ext]` — L[start]–L[end]: [what's there]
- [External reference if relevant]
