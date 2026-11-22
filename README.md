# public-ai-skills

A portable workflow for engineers and AI coding assistants, from intake through implementation, verification and shipping.

## AI–Engineer Collaboration

Start with the [numbered guide](./ai-workflow/guide/README.md) or the [workspace setup skill](./ai-workflow/SKILL.md). The bundle includes:

- Eleven numbered workflow pages, with optional branches for design challenge and proof of concept.
- Five [persona prompts](./ai-workflow/agents/README.md), with example model tiers.
- Fourteen [workflow skills](./ai-workflow/skills/) for project intake, writing, review, implementation, verification and handoff.
- Eight [project templates](./ai-workflow/templates/), the [guidelines](./ai-workflow/GUIDELINES.md), and an [architecture standard](./ai-workflow/standards/architecture.md).
- Optional [document lint](./ai-workflow/scripts/README.md) for staged docs and CI.

## Optional tools

- [Annotate Doc](./ai-workflow/skills/annotate-doc/SKILL.md) and [Stop Annotate Doc](./ai-workflow/skills/stop-annotate-doc/SKILL.md) support local browser review. [Install Plannotator](./ai-workflow/skills/annotate-doc/install.md) in binary-only mode.
- [Claude Code terminal hooks](./ai-workflow/hooks/README.md) include the runnable iTerm2 status adapter and activation instructions.
- [GitHub Stacked PRs](./ai-workflow/skills/gh-stack/SKILL.md) covers dependent PRs where the repository supports them. [Cleanup Worktrees](./ai-workflow/skills/cleanup-worktrees/SKILL.md) removes confirmed finished checkouts.

## Getting started

1. Use public [`init-project`](./init-project/SKILL.md) to onboard a machine or user and set up or upgrade their docs workspace. It uses the bundled [`ai-workflow` setup instructions](./ai-workflow/SKILL.md).
2. Once the workspace is ready, use [`start-project`](./ai-workflow/skills/start-project/SKILL.md) to create a project or [`resume-project`](./ai-workflow/skills/resume-project/SKILL.md) to continue one. `start-project` defines phases 0–9 and the conditional design challenge. The guide numbers are for navigation.
3. For native skill discovery, install `ai-workflow/` as the setup skill and each desired `ai-workflow/skills/<name>/` directory as its own skill in your harness. Install the top-level `init-project/` entry point if you want to invoke onboarding by that name. If that name already creates projects in your existing setup, keep that installation and use `ai-workflow` to onboard.
4. For Claude Code, follow the [workspace startup instructions](./ai-workflow/SKILL.md#start-the-workflow-in-claude-code). Use the [persona instructions](./ai-workflow/agents/README.md) to configure native agents or run the prompts in separate sessions.

The Markdown workflow works without extra tools. The optional linter uses Python 3 and Git.

## License

[MIT](./LICENSE)
