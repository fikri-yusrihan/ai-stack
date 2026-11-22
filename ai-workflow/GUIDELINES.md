# Engineering Docs Guidelines

Use this workspace to record engineering research, designs, implementation plans and verification. [Start Project](./skills/start-project/SKILL.md) defines the phase gates. The [numbered guide](./guide/README.md) provides the walkthrough.

## Workspace layout

| Path | Purpose |
|---|---|
| `README.md` | Project index. Keep it current as docs are added and their status changes. |
| `projects/YYYY-NNN-<name>/` | One folder per project. Use a unique number within the year. |
| [`templates/`](./templates/) | Starting points for project docs. Copy a template when its phase begins. |
| [`guide/`](./guide/README.md) | Numbered workflow pages. |
| [`agents/`](./agents/README.md) and [`skills/`](./skills/) | Role prompts and task instructions. |
| [`standards/`](./standards/architecture.md) | Code structure rules and survey. |

New projects use the following names. Keep the filenames already used by existing projects, including legacy `03-impl-plan.md` and `05-pr-plan.md`.

| Artifact | When to use |
|---|---|
| `01-research.md` | Record evidence, constraints and the approach decision. |
| `02-rfc.md` | Explain the selected design, trade-offs and success criteria. |
| `03-challenge.md` | Record independent challenge and the owner decision for a large or hard-to-reverse change. |
| `04-poc-simulation.md` | Prove a specific novel mechanism when needed. |
| `05-impl-plan.md` | Record blocking questions, ordered tasks, structure and pivots. |
| `06-verification.md` | Record cases, evidence and independent grades for behavior changes. |
| `07-pr-plan.md` | Record PR order, dependencies and checks between merges. |
| `08-teach.md` | Explain the shipped feature and offer a short quiz. |

## Writing and reviewing docs

- Read code before describing it. Cite the file and line behind load-bearing claims. Record the target repository and module in `Context`. Use repo-relative paths and stable revisions where they help someone find the evidence.
- Establish how the system works today and record constraints in structured fields. Capture the nearest comparable module and how it is wired in the research doc's `Structure conventions`.
- Compare the status quo and alternatives. State the costs, evidence, rejection reasons and conditions that would change the decision. In the RFC, connect each design decision to a specific problem or constraint and use success criteria someone can verify.
- In the implementation plan, put blockers first. Give each task exact files or entry points, dependencies and an observable definition of done. Use the [architecture standard](./standards/architecture.md) to explain each new unit's responsibility and boundary.
- Use Mermaid for flows that help readers follow actors, requests or decisions. Use tables when they make comparisons or lookups easier.
- Keep the plan live. When a discovery changes an approved decision, record the pivot in the plan and update the RFC before continuing. Keep the project owner's decision and the reasoning together.
- Use synthetic examples in shareable docs. Remove secrets, personal details and non-public identifiers from examples and evidence before sharing.

The original [collaboration rationale](./workflows/ai-engineer-collaboration.md) explains the research, feedback and handoff practices behind these rules.

## Document status lifecycle

Use the exact values below in the header `Status` row for artifacts 01–07. `08-teach.md` has no status requirement.

| Status | Meaning |
|---|---|
| Draft | The author is still preparing the document. |
| In Review | The draft has met the prerequisites for review. It can return to Draft for changes. |
| Approved | The project owner has signed off. |
| In Progress | Approved work is underway. |
| Done | The work described by the document is complete and verified where applicable. |
| Superseded | Another artifact replaces this one. Link to it. |
| Deferred | The owner has paused the work. Return to Draft when work resumes. |
| Cancelled | The owner has closed the work. Record the reason. |

Status is a record of progress. The gate and its supporting evidence determine whether work can advance. When an older project resumes, apply these rules as its docs are updated.
