# public-ai-skills

A collection of AI workflow skills for structured engineering collaboration between engineers and AI coding assistants.

---

## Skills

### [`ai-workflow/`](./ai-workflow/) — AI–Engineer Collaboration

A structured, phase-based workflow for working with AI coding assistants on non-trivial engineering tasks. Covers the full engineering lifecycle from problem framing through PR planning.

The skill can either **provision a new docs workspace** from scratch or **onboard an AI agent** into an existing one.

**Includes**: `SKILL.md`, `GUIDELINES.md`, `workflows/ai-engineer-collaboration.md`, and 5 document templates (research, RFC, impl plan, POC simulation, PR plan).

**9-phase workflow**: Problem Framing → Assessment/Research → Ideation → RFC Writing → POC (optional) → Blocking Questions → Implementation Planning → Implementation → Verification → PR Planning

---

### [`init-project/`](./init-project/) — Init Project

Bootstraps a new project folder in an existing docs workspace and drives the AI–Engineer Collaboration workflow from Phase 0. The user provides only a goal; the skill handles numbering, folder scaffolding, header fields, and phase sequencing.

Requires an existing docs workspace (provisioned by `ai-workflow`).

---

## Installation

### OpenCode + OhMyOpenCode

```bash
# Copy individual skills into your skills directory
cp -r ai-workflow ~/.config/opencode/skills/ai-workflow
cp -r init-project ~/.config/opencode/skills/init-project
```

Then load by name in any session:

```
Use the ai-workflow skill to set up a new docs workspace.
Use the init-project skill to start a new project.
```

### Claude Code

```bash
cp -r ai-workflow ~/.claude/skills/ai-workflow
cp -r init-project ~/.claude/skills/init-project
```

### Any AI Assistant

Point your AI to the `SKILL.md` inside the relevant skill folder.

---

## How the skills work together

1. **First time setup** — run `ai-workflow` to provision your docs workspace (creates `projects/`, `templates/`, `workflows/`, `GUIDELINES.md`)
2. **Each new project** — run `init-project` to scaffold a numbered project folder and kick off the 9-phase workflow

---

## License

See [LICENSE](./LICENSE).
