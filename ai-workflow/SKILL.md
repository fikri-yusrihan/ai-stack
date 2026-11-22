---
name: ai-workflow
description: Set up, upgrade or onboard into a docs workspace for the AI–Engineer Collaboration workflow. Installs the numbered guide, project templates, guidelines, persona prompts and phase skills.
---

# Set Up the AI–Engineer Collaboration Workflow

Resolve the docs workspace first. Use the path the user provides, or look for `GUIDELINES.md`, `templates/01-research.md` and `projects/` in the workspace. Ask for a destination only if it is unclear. The docs workspace may be separate from the code repository.

## Provision a new workspace

From this skill's directory, copy `AGENTS.md`, `GUIDELINES.md`, and the `agents/`, `guide/`, `skills/`, `standards/`, `templates/` and `workflows/` directories to the chosen docs root. Create `projects/`. Copy `templates/workspace-readme.md` to `README.md` at the docs root to start the project index.

Copy `scripts/` only when the user wants doc lint. See the [lint instructions](./scripts/README.md). Installing a Git hook requires a separate opt-in. If the user wants Claude Code terminal status in iTerm2, follow the [optional hook setup](./hooks/README.md). Keep that setup separate from provisioning the workspace.

Keep every path relative to the chosen docs root. To install skills or personas in the user's harness, follow its normal setup. A harness that reads Markdown can use the copied files directly. See the [persona instructions](./agents/README.md) for role prompts and model tiers. If the user asks to install the optional annotation CLI, follow the [Plannotator installation guide](./skills/annotate-doc/install.md). The [gh-stack skill](./skills/gh-stack/SKILL.md) covers its optional GitHub CLI extension.

## Start the workflow in Claude Code

Copy [`CLAUDE.md`](./CLAUDE.md) into the docs root, or merge the `@AGENTS.md` import and workflow instructions into the workspace's existing file. For project-only discovery, copy the five agent files into `.claude/agents/` and each desired skill directory into `.claude/skills/` at that root. Copy or link each complete skill directory, including its scripts and references. Resolve workspace documents from the docs root. Install the public top-level `init-project` skill separately if you want the optional onboarding command. For access from separate code repos, install the same assets in your Claude Code user skills and agents directories and give the session the docs workspace path.

From the docs workspace, run `claude --agent general`. Use `/start-project` or `/resume-project` as appropriate. The optional iTerm2 hook reports status while the session runs.

## Upgrade an existing workspace

Compare the bundled files with the workspace before copying. Merge its `AGENTS.md` and `GUIDELINES.md` with any local instructions and keep its README index and project docs. Adopt the new templates for new projects. [Resume Project](./skills/resume-project/SKILL.md) recognises the legacy `03-impl-plan.md` and `05-pr-plan.md` artifact names.

## Onboard an agent or start work

Read the workspace's `AGENTS.md` and `GUIDELINES.md`. Use the [numbered guide](./guide/README.md) to find the relevant step. Invoke [Start Project](./skills/start-project/SKILL.md) for a new project or [Resume Project](./skills/resume-project/SKILL.md) with the folder for an existing one.
