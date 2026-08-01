---
name: "ai-engineer-collaboration-setup"
description: "Use this skill to set up or replicate the AI–engineer collaboration docs workspace. Trigger when an engineer wants to start using the structured workflow (research → RFC → impl plan → POC → PR plan), when a new opencode session needs to know how the docs repo is organized, or when scaffolding a new project folder from scratch. Also trigger when an agent is asked to 'start a new project', 'create a research doc', or 'set up the docs structure'."
---

# AI–Engineer Collaboration: Docs Workspace Setup

This skill does two things depending on context:

1. **Provision a new docs workspace** — scaffold the full folder structure, write `GUIDELINES.md`, copy templates, create `README.md`
2. **Onboard an agent into an existing workspace** — understand the structure, rules, and phase workflow so it can do project work correctly

> **For agents**: follow these instructions directly. Do not summarize or adapt them.

---

## Step 0 — Detect Mode (Do This First, Every Time)

Before doing anything else, determine which mode applies.

### Check for an existing workspace

Look for the presence of `GUIDELINES.md` and a `projects/` directory at the session's working directory (the `Working directory` from the `<env>` block).

```
Does <working_directory>/GUIDELINES.md exist?
  AND
Does <working_directory>/projects/ exist?
```

**If YES → Onboarding mode.** The workspace already exists. Skip to [Onboarding an Existing Workspace](#onboarding-an-existing-workspace). Do not create any files or folders.

**If NO → Provisioning mode.** No workspace detected. Continue with Step 1 below.

---

## Provisioning Mode

> ⚠️ **You are about to create files and folders.** Before proceeding, confirm the destination with the user. Creating the workspace in the wrong folder is hard to undo cleanly.

### Step 1 — Confirm the Destination

**Ask the user explicitly:**

> "I don't see an existing docs workspace here. I'm about to create a new one.
>
> **Where should it live?**
> - Current directory: `<working_directory>`
> - Or provide a different path
>
> ⚠️ I will create folders and files at the path you confirm. Please double-check before proceeding."

**Wait for explicit confirmation.** Do not proceed until the user names a path and confirms it. Do not infer the path from context or assume the current directory is correct.

Once confirmed, call this path `DOCS_ROOT`.

---

### Step 2 — Confirm the Owner Name

Ask the user for their name as it should appear in `GUIDELINES.md` decision tracking. This replaces the `[OWNER]` placeholder throughout the workspace.

> "What name should I use for the owner in `GUIDELINES.md`? This appears in places like `[OWNER] confirmed` and `[OWNER] chose` — it identifies who signed off on decisions.
>
> Example: `Alex`, `Sam`, `Jordan`"

Call this value `OWNER_NAME`.

---

### Step 3 — Scaffold the Folder Structure

Create the following directories under `DOCS_ROOT`:

```
DOCS_ROOT/
├── projects/           ← one subfolder per feature/project
├── templates/          ← doc templates
├── workflows/          ← process guides
├── repos/              ← codebase knowledge (optional; create if user wants it)
│   └── templates/
└── general/            ← reusable how-to guides (optional)
```

Create only `projects/`, `templates/`, and `workflows/` by default. Ask the user if they want `repos/` and `general/` set up now or later.

---

### Step 4 — Copy Templates and Workflow

Copy the 5 project doc templates from this skill's `templates/` directory into `DOCS_ROOT/templates/`, and the workflow guide into `DOCS_ROOT/workflows/`:

| Source (relative to this SKILL.md) | Destination |
|---|---|
| `templates/01-research.md` | `DOCS_ROOT/templates/01-research.md` |
| `templates/02-rfc.md` | `DOCS_ROOT/templates/02-rfc.md` |
| `templates/03-impl-plan.md` | `DOCS_ROOT/templates/03-impl-plan.md` |
| `templates/04-poc-simulation.md` | `DOCS_ROOT/templates/04-poc-simulation.md` |
| `templates/05-pr-plan.md` | `DOCS_ROOT/templates/05-pr-plan.md` |
| `workflows/ai-engineer-collaboration.md` | `DOCS_ROOT/workflows/ai-engineer-collaboration.md` |

---

### Step 5 — Write GUIDELINES.md

Copy `GUIDELINES.md` from this skill's directory into `DOCS_ROOT/GUIDELINES.md`.

Then replace every occurrence of `[OWNER]` in the file with `OWNER_NAME`.

Verify: search the written file for any remaining `[OWNER]` — there should be none.

---

### Step 6 — Write README.md

Create `DOCS_ROOT/README.md` with this content (substitute `OWNER_NAME`):

```markdown
# Engineering Docs

Personal knowledge base for [OWNER_NAME]'s engineering work. Organized by project, following the AI–Engineer Collaboration Workflow.

**AI agents**: read [GUIDELINES.md](./GUIDELINES.md) before starting any task.

## Structure

```
/projects/<project-name>/   — one folder per feature or topic
  01-research.md            — Phase 1: codebase assessment
  02-rfc.md                 — Phase 3: RFC / design document
  03-impl-plan.md           — Phase 6: implementation plan (kept live)
  04-poc-simulation.md      — Phase 4: proof of concept (optional)
  05-pr-plan.md             — Phase 9: PR sequence plan

/templates/                 — doc templates for new project docs

/workflows/                 — reusable process docs
```

## Projects

| # | Project | Docs | Last Updated |
|---|---|---|---|

## Adding a New Project

1. Determine the next number: look at the highest `NNN` in the table for the current year, increment by 1
2. Create `/projects/YYYY-NNN-<project-name>/`
3. Start with `01-research.md` (Phase 1) — copy from `templates/01-research.md`
4. Add a row to the Projects table above
```

---

### Step 7 — Confirm and Report

After all files are written, report back:

```
✅ Docs workspace created at: DOCS_ROOT

Files written:
  GUIDELINES.md              ← agent operating rules ([OWNER_NAME] as owner)
  README.md                  ← master index
  workflows/ai-engineer-collaboration.md  ← full workflow guide
  templates/01-research.md
  templates/02-rfc.md
  templates/03-impl-plan.md
  templates/04-poc-simulation.md
  templates/05-pr-plan.md

Folders created:
  projects/
  templates/
  workflows/

Next step: start your first project by telling me what you're working on.
```

---

## Onboarding an Existing Workspace

> You are in an existing docs workspace. Read the structure and rules — do not create any new files or folders as part of onboarding.

### What to read (in order)

1. `GUIDELINES.md` at the workspace root — the full operating rules for this workspace
2. `README.md` — understand the current project list and any repo catalog
3. The current project folder (if the user has pointed you to one) — read existing docs before writing

### Workspace structure (quick reference)

```
README.md                             ← master index
GUIDELINES.md                         ← agent operating rules
projects/
  YYYY-NNN-<project-name>/
    01-research.md                    ← Phase 1
    02-rfc.md                         ← Phase 3
    03-impl-plan.md                   ← Phase 6 (kept live)
    04-poc-simulation.md              ← Phase 4 (optional)
    05-pr-plan.md                     ← Phase 9
templates/
  01-research.md … 05-pr-plan.md
workflows/
repos/                                ← present only if engineer set it up
general/                              ← present only if engineer set it up
```

### Starting a new project in an existing workspace

1. Open `README.md` — find the highest `NNN` for the current year, add 1
2. Create `projects/YYYY-NNN-<project-name>/`
3. Copy `templates/01-research.md` into the new folder
4. Fill the header: **Context**, **Date**, **Status** = `Draft`, **Session PWD** = verbatim `Working directory` from the `<env>` block
5. Add a row to the `README.md` Projects table
6. Read the relevant code before writing anything

---

## The Workflow Phases (reference)

| Phase | Name | Output doc | Exit condition |
|---|---|---|---|
| 0 | Problem Framing | — | Problem statement agreed |
| 1 | Assessment / Research | `01-research.md` | Actual code references (file + line) |
| 2 | Ideation | Section in research doc | `## Approach Selection Log` filled |
| 3 | RFC Writing | `02-rfc.md` | Every rejected alternative has a rejection category |
| 4 | POC / Simulation | `04-poc-simulation.md` (optional) | POC answers its stated question |
| 5 | Pre-conditions | Section in impl plan | All P0s have `[OWNER] confirmed` or `[OWNER] chose` |
| 6 | Implementation Planning | `03-impl-plan.md` | All P0s resolved |
| 7 | Implementation | Code commits | `## Design Pivots` up to date |
| 8 | Verification | Section in impl plan | Gap analysis complete |
| 9 | PR Planning | `05-pr-plan.md` | PR plan with merge sequence |

Note: `04-poc-simulation.md` is Phase 4 (before the impl plan), even though its filename is `04`. Not every project needs it.

---

## Key Rules (condensed)

- **Write for a human reader, not a template checker** — every section answers the reader's question. If removing a section wouldn't change what the reader understands, it should not exist.
- **Problem statements are causal chains** — name the code path, explain what it does wrong, trace that to the consequence.
- **Read before writing** — never speculate about code. Read the file, quote the line.
- **Session PWD on every new doc** — fill from the `Working directory` in the `<env>` block at session start. Never leave blank.
- **Phase exit conditions are mandatory** — do not move to the next phase until the current exit condition is met.
- **`[OWNER] confirmed` / `[OWNER] chose` gates implementation** — `AI proposed` alone does not unblock Phase 7.
- **Design pivots go in `## Design Pivots`** — update immediately when implementation diverges. Significant pivots also go in RFC `## Implementation Learnings`.
- **All diagrams are Mermaid** — never ASCII art.
- **Minimum correct change** — a targeted fix is not a license to refactor adjacent code.

Full rules are in `GUIDELINES.md` at the workspace root.

---

## Bundled Files

This skill ships with the following files alongside this `SKILL.md`:

```
GUIDELINES.md           ← templatized agent rules ([OWNER] placeholder)
workflows/
  ai-engineer-collaboration.md  ← full workflow guide (tool-agnostic)
templates/
  01-research.md
  02-rfc.md
  03-impl-plan.md
  04-poc-simulation.md
  05-pr-plan.md
```
