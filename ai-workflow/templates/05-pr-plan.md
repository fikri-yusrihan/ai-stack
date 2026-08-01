# PR Plan: [Feature Name]

| Field | Value |
|---|---|
| **RFC** | [RFC](./02-rfc.md) |
| **Impl Plan** | [Impl Plan](./03-impl-plan.md) |
| **Created** | YYYY-MM-DD |
| **Status** | ⏳ In Progress \| ✅ All PRs merged |
| **Session PWD** | [Working directory where this opencode session was opened — fill from env on session start] |

---

## Why [N] PRs

> Explain the split rationale. The goal: each PR must be independently reviewable and independently revertable.

| PR | What it contains | What it does NOT touch | Reviewers must evaluate |
|---|---|---|---|
| PR 1 | [What] | [What not] | [The single question a reviewer answers] |
| PR 2 | [What] | [What not] | [The single question] |
| PR 3 | [What] | [What not] | [The single question] |

> **Rule of thumb for PR splitting**:
> - Schema/contract changes come first — safe to ship early and unblock everything else
> - New code without wire-up comes next — purely additive, easy to review in isolation
> - Wire-up + deletion comes last — changes behavior; tests are the gate

---

## PR 1 — [Name]

**Branch**: `[branch-name]`

**Impl plan tasks**: [Phase X, Task Y.Z]

### Summary

[One paragraph: what this PR does and why it has zero/minimal production behavior change.]

### Files Changed

| File | Change |
|---|---|
| `path/to/file` | [What changed] |

### Test Plan

```bash
./gradlew :[module]:test
# Expected: [N]/[N] pass
```

### PR Description Template

```
## Summary

[What this PR does in 2-3 sentences. Link to the RFC.]

This is PR [N] of [total] for [feature name].

**[Production behavior change statement]** — e.g. "No production behavior change in this PR."

## Overall Plan

- **PR 1 (this PR)** — [What]
- **PR 2** — [What]
- **PR 3** — [What]

## Test Plan

1. `./gradlew :[module]:test` → all tests pass
2. [Manual verification step if needed]
```

---

## PR 2 — [Name]

**Branch**: new branch off PR 1's merge commit

**Impl plan tasks**: [Phase X, Tasks Y.Z–Y.W]

### Summary

[What this PR introduces. State explicitly what it does NOT touch — this is the key sentence for reviewers.]

### Files Changed

| File | Change |
|---|---|
| `path/to/NewFile.java` | New — [what it does] |
| `path/to/ModifiedFile.java` | Modified — [what changed] |

### Test Plan

```bash
./gradlew :[module]:test
# → all tests pass ([existing tests] untouched — [old mechanism] still in place)
```

### PR Description Template

```
## Summary

[What this PR does. What it does NOT change.]

This is PR 2 of [total]. PR 3 wires everything together.

## Overall Plan

- **PR 1** — [What] ✅ merged
- **PR 2 (this PR)** — [What], [ExistingClass] untouched
- **PR 3** — Wire-up + deletion
```

---

## PR 3 — Wire-up + Cleanup

**Branch**: new branch off PR 2's merge commit

**Impl plan tasks**: Final phase (wire-up + deletion + integration verification)

### Summary

The payoff PR. Injects [NewComponent] into [ExistingClass], replaces [old mechanism] with [new mechanism], and deletes all dead code. Mostly deletions. The interesting logic was already reviewed in PR 2.

### Files Changed

| File | Change |
|---|---|
| `path/to/ExistingClass.java` | Inject [NewComponent]; replace [old mechanism]; delete [N] methods |
| `path/to/DeadFile.java` | **Deleted** entirely |

### Test Plan

```bash
# Regression gate
./gradlew :[module]:test

# Manual smoke test
./gradlew :[service]:bootRun
```

### PR Description Template

```
## Summary

Wires [NewComponent] into [ExistingClass] and removes all code it replaces.

This is PR 3 of [total]. No new logic added — inject, replace, delete.

**Net deletion**: ~[X] lines removed, ~[Y] lines added.

## How to extend going forward

1. [Step 1]
2. Done — [what does NOT need to change]
```

---

## Summary Timeline

```
PR 1: [What]
  │
PR 2: [What]
  │
PR 3: Wire-up + deletion
      (blocked on PR 2 merge)
```

**Merge sequence**:
1. PR 1 merged
2. PR 2 merged
3. PR 3 merged
