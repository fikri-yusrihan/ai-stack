# Architecture Standard

The single source of truth for code structure when an agent designs, plans, writes or reviews code. `general`, `executor`, `auditor`, `advisor` and `librarian` read this file by path (`<docs-root>/standards/architecture.md`); pass its resolved path when briefing sub-agents. Other docs link here without restating it.

**Why it exists.** Working code passes tests and looks plausible, so structural defects (a class that does five jobs, files scattered across unrelated packages, a boundary with no interface) survive AI generation. Human review catches them late, if at all. They arise when agents write code straight from a task description, without a design step. This standard requires agents to **design with well-known architecture first, then write**, so the result can be checked before human review.

---

## The rule above all others

> "Prefer the simple solution: clean, well-structured code that is easy to understand, not a mud of everything thrown into one giant function."

Everything in this standard serves that sentence. When two rules conflict, choose the one that makes the code simpler to follow. The precedence rules (P1 to P5) and checklist (S1 to S9) below are how the sentence is checked; they keep their numbers. P1 still decides layout: a simpler design never means departing from the repo's existing package layout. The `unslop` skill applies this rule to every diff before a PR opens.

---

## 1. Precedence: principles decide the design, the repo's idiom decides the layout

The standard is repo-neutral. It rests on well-known architecture (section 2) and is expressed in whatever idiom the target repo already uses.

| # | Rule |
|---|---|
| P1 | **Layout, naming and wiring follow the repo's idiom.** Package layout, layering, naming suffixes and wiring style come from the target repo, proven by reading the code (the Structure survey, section 5), never assumed. |
| P2 | **Responsibility, dependency direction and boundaries follow the principles in section 2,** even where neighbouring code does not. A repo's idiom does not excuse a class that does five jobs or a rule that imports an SDK. |
| P3 | **A different structure is a decision, not a default.** Replacing the repo's layout (for example a full ports-and-adapters module in a layered repo) is allowed only as a P0 with `Owner chose`. The agent never switches the structure on its own because it prefers another one. |
| P4 | **Do not imitate outliers.** Copy the nearest analogue that is small, cohesive and tested. A class past the S4 triggers is a legacy outlier, not a template, even when it is the closest analogue by name. Name outliers in the survey so nobody copies them. |
| P5 | **Do not restructure existing code as a side effect.** Moving or splitting existing classes needs its own plan task. Splitting your own new code into proper units is part of the task and needs no approval. |

---

## 2. Architecture basis, and the design note that comes before code

### The well-known ideas this standard applies

| Idea (source) | In one line | Where it shows up |
|---|---|---|
| Layered architecture | Presentation, service and data layers; calls go one way | S1, S5 |
| Clean Architecture, the Dependency Rule (Martin) | Source dependencies point toward the business rules; rules know nothing of frameworks or I/O | S5, S8 |
| Hexagonal, Ports and Adapters (Cockburn) | The core talks to the outside through ports; adapters implement them, so I/O can be replaced or faked | S6, S7 |
| SOLID (Martin) | SRP: one reason to change. OCP: extend without editing callers. LSP and ISP: honest, small interfaces. DIP: depend on abstractions | S3, S4, S6, S9, section 4 |
| Cohesion and coupling; GRASP (Larman) | Put behavior with the data and knowledge it needs; keep unrelated things apart | S1, S3 |
| Package by feature, modular monolith | One cohesive package per feature, with a small public surface and hidden internals | S1 |
| Domain-Driven Design, lightly (Evans) | Names come from the domain; model and persistence shapes are not the same thing | S2, S8 |
| Design patterns (Gamma et al.) | Named solutions to recurring problems; used when the problem is present | section 4 |
| Externalised configuration (Twelve-Factor) | Limits and switches live in configuration, not in code | S9 |

### The design note

**Before writing code that adds a class, or changes a class's dependencies or public methods**, state a design note. It is a few lines, not a document, and it is the answer to "which known architecture am I applying here?":

1. **Style.** The architectural style the target area follows (layered, ports and adapters, package by feature, or mixed), from the Structure survey.
2. **Units.** Each new unit with one sentence of responsibility (S3), CRC-card style.
3. **Dependencies.** Who calls whom, with the arrows pointing the way S5 requires.
4. **Boundaries.** Each external system the change touches, with the port (interface) it is behind, or the reason there is none (S6).
5. **Patterns.** Any pattern from section 4 and the present problem it solves, or "none".

Where it lives: in the plan's `Structure and Responsibilities` table and the RFC's `Structure and boundaries` when the work goes through the workflow; otherwise as the first thing the writer produces before editing, and it goes into that writer's report: the orchestrator (`general`) when it writes code itself, or the `executor` (whose note is the plan rows it confirmed). A change that adds no class and leaves every class's dependencies and public methods as they were needs no note. Code that needed a note and has none is reviewed as a structural finding.

### What "done" means structurally

A reader who has never seen the feature can answer these without opening more than the obvious files:

1. Where do I find it? (S1, S2)
2. What does each class do, in one sentence? (S3, S4)
3. What does it depend on, and in which direction? (S5, S6)
4. What breaks if I replace the database, queue or HTTP client? (S6, S7)

---

## 3. The checklist (cite these IDs in reviews and reports)

### Placement

| ID | Rule | A violation looks like |
|---|---|---|
| S1 | **Placement follows the nearest analogue.** A new file lives where its closest analogue lives: in a feature-organised repo, with the rest of its feature and in the matching layer sub-package; in a layer-organised repo, in the layer package the analogue uses. No new top-level package unless the plan names it. | A file placed away from where its analogue sits (in a feature-organised repo, one feature scattered over unrelated packages); a `controller` in `util`; a new `common` or `helper` package. |
| S2 | **Names follow the repo's suffix conventions and state the responsibility.** | `Manager`, `Helper`, `Processor`, `Handler` with no domain noun; a `Service` that is a controller; `Impl` where the repo has none. |

### Responsibility

| ID | Rule | A violation looks like |
|---|---|---|
| S3 | **One reason to change.** State each class's responsibility in one sentence without "and". Keep apart: orchestration (the order of steps), rules (decisions), I/O adapters (queue, store, HTTP, DB) and mapping. | One class that parses the request, applies the business rules, calls an external API, writes the database and sends the notification. |
| S4 | **Size and shape triggers.** Any of these needs a stated reason in the plan's responsibility table, or a split: a new class over about 300 lines; a constructor with more than 5 collaborators; a method over about 40 lines or nested more than 3 levels; a unit that needs more than 3 mocks to test; a `Util` class holding unrelated methods. The numbers trigger a decision; they are not a style quota. | A 700-line `*ServiceImpl`; `*Util` with a dozen static methods from different features. |

### Dependencies and boundaries

| ID | Rule | A violation looks like |
|---|---|---|
| S5 | **Dependency direction.** Entry points (controller, queue consumer, listener, scheduler, RPC endpoint) depend on services; services depend on rules and on repository or client interfaces; never the reverse. Entry points parse, authorize, delegate and map the response, and hold no business rules. Business rules import no web, messaging or SDK types. | A controller or consumer that loops over rows and applies rules; a rule class that imports an AWS or Mongo type; a service that reads `HttpServletRequest`. |
| S6 | **Interfaces where the design needs them.** (a) Follow the repo's convention for services (for example `Service` plus `ServiceImpl`; where the repo splits contract and implementation modules, the interface goes in the contract module and the implementation in the implementation module). (b) Always put an interface at external I/O: queue, object store, HTTP or Feign client, search, and any data access beyond the repo's existing repository abstraction. (c) Always add one where the plan names two or more implementations, or a stub or fake. (d) Do not add one for a pure internal helper or a private single-use collaborator. (e) Where the repo's style is mixed, or the nearest analogue calls an external system through a concrete class, (b) and (c) still apply: the analogue guides placement and naming (S1, S2), not a missing seam (P2). | A listener that calls the S3 SDK directly; a stub that exists with no interface to swap it; an `IFoo`/`FooImpl` pair for a private helper. |
| S7 | **Explicit failure contracts at boundaries.** A boundary method says in its type whether a miss, a transient failure and a final failure differ (result type, `Optional`, or the repo's exception-with-code style). It does not return `null` for "not found" or swallow an exception to look successful. | A client that returns `null` on timeout and on "no match". |
| S8 | **Models stay in their layer.** Follow the repo: where it separates API models from persistence entities, do not leak entities through the API or request models into rules. | A Mongo document returned straight from a controller. |
| S9 | **Wiring is visible.** Collaborators arrive by the repo's wiring style (constructor injection by default); whichever style the repo uses (injection or plain `new`), a service or rule does not build its own I/O collaborators (clients, stores, queues) inside itself: they are passed in and built in the composition root (a configuration class or its equivalent); no hidden static state; switches and limits come from the repo's configuration mechanism, not constants buried in a method. | `new SqsClient()` inside a service rather than passed in from the composition root; a magic number for a retry limit. |

A deviation is allowed when it is **named in the plan's Structure and Responsibilities table with its reason**. An unnamed deviation is a finding.

---

## 4. Patterns on demand

A pattern needs a present problem in this change, never a future one. If the "Use when" column does not hold today, do not add the pattern.

| Pattern | Use when | Do not |
|---|---|---|
| Polymorphism or Strategy instead of a type switch | The same `switch` or `if` chain on a type appears in 2 or more places, or the plan adds a third variant | Replace a single two-branch `if` |
| Registry or Factory | Choosing the variant by key is itself a responsibility that callers should not repeat | Wrap a plain constructor |
| Port and adapter | A call crosses to an external system, or a stub is needed (S6b, S6c) | Wrap in-process collaborators |
| Decorator | A cross-cutting behavior (retry, limiter, metrics, logging) wraps an existing interface without changing its callers | Subclass to add behavior |
| Explicit state machine (one class owns the transitions) | A lifecycle with 3 or more states and guarded transitions | Scatter status checks across classes |
| Builder | An immutable object with several optional fields | A three-argument constructor |
| Composition over inheritance | Always the default | An abstract base class that exists only to share code |

Avoid: hand-rolled singletons, `Manager` or `Helper` catch-alls, generic frameworks for one use, and any pattern added for its name.

---

## 5. Structure survey (do this before designing or writing)

A `librarian` produces it, or the executor does it for its own task. Without it, nobody can apply P1 or P4. It has these fields, each from code actually read, and an absent item is stated as absent:

| Field | Content |
|---|---|
| Organizing principle | By feature, by layer, or mixed, with the evidence (the package tree to two levels) |
| Layer sub-packages | The names the repo uses (for example `controller`, `service`, `repository`, `listener`, `model`) |
| Naming suffixes | How services, repositories, clients, listeners and models are named |
| Boundary style | How the repo declares interfaces and implementations, and where each lives |
| Wiring style | Constructor injection, field injection, plain `new`, configuration classes |
| Nearest analogue | The closest existing feature that is small, cohesive, tested and recently maintained, with paths. Prefer one the owner names in the repo catalog's reference features |
| Outliers not to copy | Classes past the S4 triggers, with their line counts |
| Test layout | Where tests sit and which framework |

Record it in the research doc under `Structure conventions` and, when the repo's catalog entry has a `Key Conventions` section, check the two agree.

---

## 6. Where it is enforced

| Phase | Who | What |
|---|---|---|
| 1 Research | `librarian` | Structure survey into `01-research.md` `Structure conventions` |
| 2 to 3 Ideation, RFC | orchestrator, `advisor` (hard calls) | RFC `Structure and boundaries`; approaches that disagree with P1 are labelled as such and need a P0 |
| 6 Impl planning | orchestrator, `auditor` | `Structure and Responsibilities` table in the plan; the auditor checks it against S1 to S9 and the survey |
| 7 Implementation | `executor`, orchestrator | Survey and design note before writing; Structure report with every change; orchestrator verifies it against the diff |
| 8 Verification | `auditor` | Architecture pass on the diff, citing S-IDs |

### Executor Structure report

Every executor report includes this table for each new or changed class, then a pass or a named deviation for each of S1 to S9:

| Class | Package (path) | Responsibility (one sentence, no "and") | Depends on | Interface and why |
|---|---|---|---|---|

---

## 7. Java and Spring notes

General practice for the stack the repos use, applied within P1:

- Controllers and consumers are thin (S5). Transaction boundaries sit on the service layer, not on the controller or the repository.
- Configuration lives in the repo's configuration package and properties mechanism, and feature switches are properties with a default (S9).
- In a multi-module build, contract types (request and response models, client and service interfaces) live in the API or common module and implementations in the implementation module. Do not put implementations in a contract module, and do not let a contract module depend on an implementation one.
- Where the repo has module-verification tooling (an ArchUnit suite or Spring Modulith's `verify()`), a violation it reports is a finding, and new rules belong in that suite rather than in prose.
- Repo-specific conventions, reference features and known outliers belong in that repo's catalog entry (`repos/<repo>/index.md`, `Key Conventions`), not in this file, so this standard stays valid for every repo.
