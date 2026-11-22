# Implementation Plan: [Feature Name]

<!-- Status values: Draft | In Review | Approved | In Progress | Done | Superseded | Deferred | Cancelled — GUIDELINES.md § Document Status Lifecycle -->
| Field | Value |
|---|---|
| **RFC** | [RFC](./02-rfc.md) |
| **Module** | [module name] |
| **Created** | YYYY-MM-DD |
| **Status** | Draft |

---

## Overview

> One paragraph: what this plan accomplishes and the core approach. Reference the RFC for design rationale — this document is about execution, not design.

**Net result**:
- Files deleted: [list]
- Files added: [list]
- Files modified: [list]

---

## Phase 0 — Pre-conditions

> Resolve ALL of these before writing any code. P0 questions are ambiguities that would cause the implementation to fork depending on the answer. If you start without resolving them, you will need to rewrite.

| # | Question | Why it blocks | Options | Decision | Decided by | Reasoning |
|---|---|---|---|---|---|---|
| P0-1 | [Question] | [What it determines] | [A] / [B] | ⏳ Unresolved / ✅ [Decision] | `AI proposed` \| `Owner confirmed` \| `Owner chose` | [One sentence — why this option over the others] |
| P0-2 | [Question] | [What it determines] | [A] / [B] | ⏳ Unresolved / ✅ [Decision] | | |

> **Rule**: Do not start Phase 1 until all P0 items are ✅. "Decided by" = `Owner confirmed` or `Owner chose` is required before proceeding — AI proposals alone do not unblock.

---

## Structure and Responsibilities

> One row per new or changed unit, so structure is reviewed before code exists. Rules and checklist IDs: `standards/architecture.md`. This table is the design note from section 2 of the standard: name the architectural style you are applying (layered, ports and adapters, package by feature) and any pattern with the present problem it solves. Follow the research doc's `Structure conventions`; a unit that deviates from S1 to S9 (including any size trigger in S4) is named here with the reason. An unnamed deviation is a review finding. A task creates one responsibility, or lists the units it creates.

**Style**: [the architectural style this area follows: layered / ports and adapters / package by feature / mixed] **Patterns**: [pattern and the present problem it solves, or "none"]

| Unit | Package path | Responsibility (one sentence, no "and") | Depends on | Interface and why (S6) | Follows (nearest analogue) |
|---|---|---|---|---|---|
| `[ClassName]` | `[path/to/package]` | [what it does] | [collaborators] | [none / interface name: external I/O, stub, repo convention] | `[ExistingClass]` |

---

## Phase 1 — [Name]

> **Status**: ⏳ In Progress | ✅ Complete
>
> Group tasks that can be done without touching existing production code first. Safe to implement early — if something is wrong here, you find out cheaply.

---

### Task 1.1 — [Task name]

> **Status**: ⏳ | ✅

**What**: [Exactly what to do]

**File(s) to create/modify**:
- `path/to/File.[ext]` — [what changes]

```text
// Concrete implementation sketch (not required to be production-ready, but should be close)
```

**Definition of done**:
- [ ] [Verifiable condition — e.g. "compiles", "test passes", "method deleted"]
- [ ] [Verifiable condition]

---

### Task 1.2 — [Task name]

[Same structure]

---

## Phase 2 — [Name]

> **Status**: ⏳ | ✅
>
> [What this phase accomplishes and why it's sequenced after Phase 1]

---

### Task 2.1 — [Task name]

[Same structure as 1.1]

---

## Phase 3 — [Name]

> **Status**: ⏳ | ✅

---

### Task 3.1 — [Task name]

[Same structure]

---

## Phase N — Wire-up + Cleanup

> The final phase. Connect new pieces to the existing system. Delete dead code. This is usually the highest-risk phase — it changes behavior.

### Task N.1 — [Wire-up task]

**What**: Inject [NewComponent] into [ExistingClass]. Replace [old mechanism] with [new mechanism].

**Before**:
```text
// old code
```

**After**:
```text
// new code
```

**Definition of done**:
- [ ] [ExistingClass] compiles
- [ ] All existing tests pass without modification
- [ ] Dead code deleted: [list files/methods]

---

### Task N.2 — Delete dead code

**Files to delete**:
- `path/to/DeadFile.[ext]`
- `path/to/AnotherDeadFile.[ext]`

**Methods to delete from [ClassName]**:
- `deadMethod1()`
- `deadMethod2()`

**Definition of done**: No compile errors; existing tests still pass.

---

### Task N.3 — Integration verification

Run the relevant integration check on the approved test target. Record the setup command, test input, expected result and evidence in `06-verification.md`. Compare against the baseline where behavior must be preserved.


---

## File Structure (final)

```
[module]/[source-directory]/
├── [new-package]/
│   ├── NewFile.[ext]           ✅ new
│   ├── AnotherNewFile.[ext]    ✅ new
│   └── ModifiedFile.[ext]      ✅ modified
└── [existing-package]/
    └── ExistingFile.[ext]      ✅ switch collapsed; dead methods deleted
```

**Deleted**:
- `path/to/DeletedFile.[ext]`

---

## Design Pivots

> Fill this section whenever the implementation diverges from the RFC. A pivot is required here when the change affects:
> - A public API contract or method signature
> - A data structure shape used by more than one task
> - The behavior of a component that other phases depend on
>
> Everything else: log briefly and keep going. Silence = the plan was followed exactly.

| # | What changed | Why | Impact on remaining tasks | RFC updated? |
|---|---|---|---|---|
| — | — | — | — | — |

> When a pivot is significant, update `## Implementation Learnings` in `02-rfc.md` too.

---

## Risk Register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| [Risk description] | Low/Med/High | Low/Med/High | [How to catch it early] |

---

## References

- [RFC](./02-rfc.md)
- [Research doc](./01-research.md)
- `FileName.[ext]` — L[start]–L[end]: [relevant section]
