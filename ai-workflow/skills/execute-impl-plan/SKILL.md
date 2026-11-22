---
name: execute-impl-plan
description: Execute one approved implementation-plan task at a time using the target repository's branch and worktree conventions. Verify the result and keep the plan current.
---

# Execute an Implementation Plan

## 1. Confirm the inputs

Read the approved plan and RFC. Check the P0 table for owner sign-off and review earlier task results. For existing projects, the plan may be `03-impl-plan.md` instead of `05-impl-plan.md`.

Use each repository's documented review and integration procedure. Record the PR sequence, dependency order and verification between changes. Confirm the target branch and remote from the repository and check the local working tree before creating a branch.

## 2. Prepare an isolated checkout

Use the project's agreed worktree location and branch naming. If a worktree belongs to the task, check its branch and state before reusing it. Otherwise, use standard Git from the target code repository:

```text
git fetch <remote>
git worktree add -b <task-branch> <worktree-path> <remote>/<base-branch>
```

Replace the placeholders with the agreed values. Leave unrelated working changes and branches alone. Obtain authorization for remote changes and shared environments.

## 3. Brief the executor

Send one approved task with its target checkout, exact files, code sketch, reuse entry points, dependencies and definition of done. Include the research doc's Structure conventions, the task's Structure and Responsibilities rows, and the resolved path of the architecture standard. Pass the test commands and any known limits.

If the approval or plan depends on an assumption the checkout contradicts, pause that task. Update the Design Pivots record and the RFC where the decision affects contracts or boundaries. Get the owner's decision before implementing the changed design.

## 4. Verify and record the task

Review the real diff against the task and the executor's Structure report. Run the agreed checks and record their results. Apply `unslop` to task changes. Confirm the definition of done item by item, keeping any failed or unrun check visible. Update the plan and move to the next approved task when its dependencies are ready.
