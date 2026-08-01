# Implementation Plan: [Feature Name]

| Field | Value |
|---|---|
| **RFC** | [RFC](./02-rfc.md) |
| **Module** | [module name] |
| **Created** | YYYY-MM-DD |
| **Status** | In Progress \| ✅ Complete |
| **Session PWD** | [Working directory where this opencode session was opened — fill from env on session start] |

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
| P0-1 | [Question] | [What it determines] | [A] / [B] | ⏳ Unresolved / ✅ [Decision] | `AI proposed` \| `[OWNER] confirmed` \| `[OWNER] chose` | [One sentence — why this option over the others] |
| P0-2 | [Question] | [What it determines] | [A] / [B] | ⏳ Unresolved / ✅ [Decision] | | |

> **Rule**: Do not start Phase 1 until all P0 items are ✅. "Decided by" = `[OWNER] confirmed` or `[OWNER] chose` is required before proceeding — AI proposals alone do not unblock.

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
- `path/to/File.java` — [what changes]

```java
// Concrete implementation sketch
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
```java
// old code
```

**After**:
```java
// new code
```

**Definition of done**:
- [ ] [ExistingClass] compiles
- [ ] All existing tests pass without modification
- [ ] Dead code deleted: [list files/methods]

---

### Task N.2 — Delete dead code

**Files to delete**:
- `path/to/DeadFile.java`
- `path/to/AnotherDeadFile.java`

**Methods to delete from [ClassName]**:
- `deadMethod1()`
- `deadMethod2()`

**Definition of done**: No compile errors; existing tests still pass.

---

### Task N.3 — Integration verification

> Manual verification after all tests pass. Tests prove correctness; this proves nothing broke end-to-end.

```bash
# Start the service
./gradlew :[module]:bootRun

# Hit the relevant endpoint with a real payload
curl -X POST [endpoint] -d @test-payload.json
```

---

## File Structure (final)

```
[module]/src/main/java/[package]/
├── [new-package]/
│   ├── NewFile.java           ✅ new
│   └── ModifiedFile.java      ✅ modified
└── [existing-package]/
    └── ExistingFile.java      ✅ switch collapsed; dead methods deleted
```

**Deleted**:
- `path/to/DeletedFile.java`

---

## Design Pivots

> Fill this section whenever the implementation diverges from the RFC. Silence = the plan was followed exactly.

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
- `FileName.java` — L[start]–L[end]: [relevant section]
