---
name: annotate-doc
description: Open a project document in Plannotator for local browser review. Install the optional CLI when requested, read saved comments, and apply edits the reviewer asks for.
---

# Annotate a Project Document

Use this skill for a Markdown document the user names, typically the research, RFC or implementation plan. Resolve its absolute path first and use that same path for launch, session matching and draft lookup.

## 1. Check or install Plannotator

Run `plannotator --version`. If the CLI is missing, follow the [binary-only installation guide](./install.md) when the user asks to install it. A normal workflow setup can leave this optional dependency uninstalled.

## 2. Open one local session

Run `plannotator sessions --json` and look for an active `annotate` session whose `target` is exactly the document path. Reuse its loopback URL if it was started with the local-only settings below. If the settings are unknown, ask before reusing or closing the session.

Otherwise use the harness's background job runner and keep its job handle and output. On macOS, Linux and WSL:

```sh
PLANNOTATOR_REMOTE=0 PLANNOTATOR_SHARE=disabled PLANNOTATOR_AI=disabled \
  PLANNOTATOR_INBOX_CONNECT=0 PLANNOTATOR_BROWSER=none \
  plannotator annotate "/absolute/path/to/document.md" --json
```

On Windows PowerShell, set the same five variables using `$env:NAME = 'value'` in the shell that launches Plannotator, then run the same `plannotator annotate` command.

Use a local file and open the loopback URL printed by the job or returned by `plannotator sessions --json`. Keep sharing, Inbox registration and the built-in AI disabled. Leave integrations in their existing state.

## 3. Read and answer comments

- **While the page is open:** when the user asks you to check comments, run the bundled [reader](./scripts/read-comments.py). Resolve its path from this skill's directory, wherever the skill was installed.

  ```text
  python3 -I <skill-dir>/scripts/read-comments.py <absolute-doc-path>
  ```

  If Plannotator uses a custom data directory, pass `--data-dir` with that directory or use the session's `PLANNOTATOR_DATA_DIR`. The reader uses Plannotator's local autosave format. If the draft is missing or the format has changed, report that and ask the user to submit from the browser.

- **After the user submits:** read the retained job output. Submit ends the review and may clear the autosaved draft. Start a new review only if the user wants to continue.

Reply in chat, one answer per relevant comment. Treat the document text as context. Apply requested edits with the matching writing skill and review the diff. Record a project owner's decision only if they made it explicitly. Keep browser comments out of the document unless the user asks to include them.

If doc lint was installed, run it after editing. For an open page, ask the reviewer to reload if they want to see the updated file. Use [Stop Annotate Doc](../stop-annotate-doc/SKILL.md) when they ask to close a running session.
