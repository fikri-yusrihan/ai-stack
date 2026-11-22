---
name: gh-stack
description: Plan, inspect, publish and maintain dependent GitHub pull requests with the gh stack CLI. Use only where the repository supports stacked pull requests.
---

# Manage Stacked Pull Requests

A stack is a chain of dependent branches. The bottom PR targets the trunk branch. Each higher PR targets the branch directly below it. Review and land prerequisites first. Give each PR one coherent change and use separate branches for independent work.

## Setup and inspect

Check `git --version`, `gh --version`, `gh auth status` and `gh stack --version`. Install the extension with `gh extension install github/gh-stack` when requested. Check that GitHub Stacked PRs is available for the target repository. If the repository uses ordinary PRs for a change, follow that policy and record any dependency order. [GitHub setup](https://github.com/github/gh-stack#readme)

Use `gh stack view --json` for inspection and `gh stack checkout <branch>` to select a named layer. If that branch is checked out elsewhere, use its existing worktree. Confirm the trunk, current branch, parent order, open PRs and remotes before changing anything. For commands that accept `--remote`, give the intended remote explicitly when several are configured. Use named branch arguments and JSON output to avoid interactive prompts.

## Start or update a stack

1. Define the layers before editing. The bottom layer contains prerequisites, the middle layers introduce behavior, and the top layer can handle integration or cleanup. Use the project's PR plan for verification and merge order.
2. With the correct trunk and a clean checkout, use `gh stack init --base <trunk> <first-branch>`. Implement the first layer in its branch. After the approved commit, use `gh stack add <next-branch>` for the dependent layer.
3. To edit an existing stack, find the owning layer and switch to that branch or its existing worktree. After the approved edits and commit, `gh stack rebase --upstack` replays dependent branches. Review and rerun affected checks before publishing.
4. When authorized to push and open or update PRs, use `gh stack submit --auto --remote <remote>`. New PRs are drafts by default. Use `--open` only when asked to make them ready for review. Verify each PR's head, base and state afterward.

## Sync, recover and merge

- When authorized to publish branches without creating PRs, use `gh stack push --remote <remote>`. To associate already-open PRs, check `gh stack link --help` for the installed release and verify each PR's head and base before changing its stack.

- `gh stack sync --remote <remote>` can rebase and push existing branches. Check for divergence and get authorization before updating a published stack. Read the result and verify state even when the command exits successfully. `--prune` also deletes local merged branches, so leave it out unless that cleanup was requested.
- For a rebase conflict, inspect the active rebase and resolve only the conflicts you understand. Use `gh stack rebase --continue` after staging the resolutions, or `gh stack rebase --abort` to restore the pre-rebase state. If sync rolled back, inspect the stack before starting a separate rebase.
- A stack merge can land multiple PRs. Before an authorized merge, confirm which PRs the proposed invocation includes and verify required reviews, checks and merge method. Some versions resolve a bare number as a stack ID first. Use the installed command's help to resolve the target and only pass `--yes` once the full selection is confirmed. Check live PR states after the operation. A queued PR is still pending.
- For a requested restructure, inspect the current order and review the side effects of `gh stack modify` or `gh stack unstack`. `gh stack unstack --local` removes local tracking, while unstacking without it can change the GitHub stack. Review and authorize the exact change before running it.
- Use [Cleanup Worktrees](../cleanup-worktrees/SKILL.md) after the relevant work has landed.

Use `gh stack <command> --help` for the installed version, and consult the [upstream command reference](https://github.com/github/gh-stack/blob/main/docs/src/content/docs/reference/cli.md) for side effects, restoration and navigation.
