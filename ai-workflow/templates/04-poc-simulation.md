# POC Simulation: [Feature Name]

| Field | Value |
|---|---|
| **RFC** | [RFC](./02-rfc.md) |
| **Impl Plan** | [Impl Plan](./03-impl-plan.md) |
| **Created** | YYYY-MM-DD |
| **Purpose** | [One sentence: what single question this POC answers] |
| **Status** | ⏳ In Progress \| ✅ All [N] tests passing |
| **Session PWD** | [Working directory where this opencode session was opened — fill from env on session start] |

> **When to write a POC**: When the implementation approach is novel enough that you're not sure it will work mechanically. The POC answers one question: "Does this technical approach actually work?" It is NOT production code — skip error handling, edge cases, and production quality. It CAN skip Spring context, actual RPC clients, and any external dependencies.

> **Production design divergence** (fill in after implementation): [If the production implementation differs from this simulation, document what changed and why here.]

---

## What We Are Simulating

> One paragraph: the core claim of the RFC that this POC validates. Quote the "three lines of code" or "one mechanism" that the whole approach hinges on.

The core claim of the RFC is:

```java
// The claim — paste the key mechanism here
```

This simulation proves [specific claim] by verifying [specific thing] against [real classes / stub classes / actual data shapes].

---

## The Mechanisms Explained

> For each non-obvious mechanism involved, explain it in plain language before showing the test. Future engineers reading this should understand WHY before they see HOW.

### Mechanism 1: [Name]

**The problem**: [What naive code would do wrong]

**The solution**: [How the mechanism fixes it]

```java
// Concrete before/after showing the mechanism
```

**How it works internally**: [What Jackson / Spring / the framework actually does]

---

### Mechanism 2: [Name]

[Same structure]

---

### Mechanism 3: [Name]

[Same structure]

---

## Edge Cases Covered

> Before writing the test, audit for edge cases. Document them here and add a test for each one.

| Edge Case | Test name | Rationale |
|---|---|---|
| [Edge case description] | `testSomething_scenario_expectedBehavior` | [Why this edge case matters] |
| Null field | `testResolver_nullField_skipped_noNpe` | Avoid NPE when optional fields are absent |
| Missing key in bundle | `testResolver_missingKey_passthroughRawKey` | Graceful degradation — raw key preserved |

---

## The Simulation Test

> This test should be self-contained — it must not require Spring context, real RPC clients, or AWS credentials. Use stubs for external dependencies.

```java
package [test package];

// [imports]

/**
 * POC simulation proving [mechanisms] work together.
 */
public class Test[FeatureName]Poc {

    static class Stub[ExternalDependency] {
        // [fields and constructor]
    }

    @BeforeMethod
    public void setUp() {
        // stub data
    }

    // =========================================================================
    // Test 1: The happy path
    // Proves: [core claim of the RFC]
    // =========================================================================
    @Test
    public void test[Mechanism]_[scenario]_[expectedOutcome]() {
        // GIVEN
        // WHEN
        // ASSERT
    }

    // =========================================================================
    // Test 2: [Mechanism isolation]
    // Proves: [specific mechanism works in isolation]
    // =========================================================================
    @Test
    public void test[Mechanism]_[scenario]_[expectedOutcome]() {
        // ...
    }

    // =========================================================================
    // Test 3: Edge case — [description]
    // Proves: [what graceful behavior looks like]
    // =========================================================================
    @Test
    public void test[Mechanism]_[edgeCase]_[expectedBehavior]() {
        // ...
    }
}
```

---

## Test Execution Notes

### Current state

| Test | Status | Notes |
|---|---|---|
| Test 1 — happy path | ⏳ / ✅ | |
| Test 2 — [scenario] | ⏳ / ✅ | |
| Test 3 — [edge case] | ⏳ / ✅ | |

### Phase acceptance gate

1. [Step 1 — e.g. run codegen]
2. [Step 2 — verify generated artifact]
3. [Step 3 — run tests]

---

## What This Simulation Does NOT Cover

| Excluded | Why |
|---|---|
| [Special case] | [Different mechanism — handled in impl plan Phase N] |
| [External client calls] | Simulated via stub |
| [Nested objects] | [Specific gap — describe workaround or follow-up task] |

---

## Summary: Mechanism Interaction Diagram

```
[Input data shape]
  {
    "field1": "RAW_KEY",
    "field2": "ANOTHER_KEY"
  }
         │
         │  [Step 1: mechanism name]
         ▼
[Intermediate state]
         │
         │  [Step 2: mechanism name]
         ▼
[Final state]
  {
    "field1": "Resolved Value"   ← resolved ✓
    "field2": "Another Value"    ← resolved ✓
  }
```
