---
name: cleanup-worktrees
description: Inspect Git worktrees for the active project and remove confirmed clean checkouts whose exact changes have landed. Keep unpublished or uncertain work.
---

# Clean Up Finished Worktrees

## 1. Scope the inventory

Resolve the project and the repositories or exact worktree paths from the request and the project's plan. If those are unclear, confirm scope first. Run `git -C <repo> worktree list --porcelain` in the relevant repositories and match entries against those paths or their recorded branches. The first entry is the main worktree. Exclude it, unrelated checkouts and the shell's current checkout.

## 2. Classify the candidates

For each scoped linked worktree, record its path, branch and commit. Use `git -C <worktree> status --porcelain=v1 --untracked-files=all` and check whether ignored files contain anything the user needs to keep. Keep dirty, locked, detached or uncertain checkouts for review.

Check the repository's forge or integration branch for evidence that the exact work landed:

- For a merged PR, match the target repository, the head repository and branch (including forks), and the full PR head SHA at merge to the worktree's current `HEAD`. This works for squash merges too. For GitHub, use `gh pr view <number> --repo <owner>/<repo> --json state,mergedAt,headRefOid,headRefName,headRepository,headRepositoryOwner` after resolving the PR from the plan or forge.
- When there was no PR, confirm the local head is reachable from the intended, current integration branch. If a squash or other rewrite prevents that check, keep the worktree unless there is independent evidence identifying the exact changes that landed.
- Keep an open or closed-unmerged PR, a local head that differs from the merged head, or a branch with commits you cannot account for. If the forge or integration ref cannot be verified, report the uncertainty and preserve the worktree.

## 3. Confirm and remove

Show the exact worktrees eligible for removal and why, plus what will be kept. Obtain confirmation for the removal list. Immediately before each removal, recheck the recorded branch, head and cleanliness.

From another worktree in that repository, run:

```text
git -C <repo> worktree remove <confirmed-worktree>
git -C <repo> worktree list --porcelain
```

Use the normal removal command and report any refusal. Do not use `--force`, prune unrelated worktree metadata, or sweep directories.

Removing a worktree leaves its branch. Handle local or remote branch deletion only on a separate explicit request. Check that the branch still points at the verified commit and is unused by other worktrees or open PRs. Use the repository's normal branch deletion procedure. A squash-merged branch may be rejected by `git branch -d`. Preserve it unless the owner specifically approves deleting that verified local ref.

Report removed and preserved worktrees with their reasons.
