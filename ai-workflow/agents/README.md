# Agent personas

Use a model available in your harness. The tiers below express how much reasoning each job usually needs. The role prompt and tool permissions define its scope.

| Persona | Job | Model tier | Scope |
|---|---|---|---|
| [general](./general.md) | Coordinate the work, write project docs and surface owner decisions. | Session default | Orchestration and authorized edits |
| [librarian](./librarian.md) | Answer one research question with evidence. | Fast | Read-only |
| [advisor](./advisor.md) | Review hard designs, challenge assumptions or independently check verification. | Deep reasoning | Read-only |
| [auditor](./auditor.md) | Review a written doc, plan or diff and report concrete findings. | Deep reasoning | Read-only |
| [executor](./executor.md) | Implement and verify one approved plan task. | Implementation | Writes scoped to the task |

The prompts are plain Markdown with Claude Code frontmatter. Install the five persona files in the harness's agent location if it supports this format. For a different format, use the body as the role instructions and configure the model and permissions in the harness. You can also supply the prompt directly in a separate session.

Use read-only permissions for research and review wherever the harness supports them. Give each role the resolved docs root and the relevant artifact paths. Run independent challenge and verification outside the author's session or with a human reviewer as the workflow requires.
