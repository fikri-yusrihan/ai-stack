# Optional document lint

Copy `scripts/` to the docs workspace and use Python 3.9 or newer. Run these from its root:

```sh
python3 scripts/lint-docs.py --all
python3 scripts/lint-docs.py --staged
python3 scripts/lint-docs.py --since origin/main
```

`--all` reads the working tree. `--staged` reads the Git index. `--since REF` compares the merge base of `REF` and `HEAD` and reads committed docs at `HEAD`. Substitute your base ref in CI and fetch its history so Git can find the merge base. The default mode is `--staged`. If the docs workspace is a subdirectory of a larger repository, use `--all` from that workspace. Git snapshot modes expect the docs workspace at the repository root.

Lint checks the numbered artifacts in `projects/`, including legacy plan and PR plan filenames. It checks document status, required decision sections, owner sign-off, verification case fields, and project numbering and index links. A reviewer still opens the evidence and checks what it proves.

## Opt in to the Git hook

In a standalone docs Git repo with no existing hooks setup, set the local hook path from the workspace root:

```sh
git config --local core.hooksPath scripts/git-hooks
```

If you already use Git hooks, add `python3 scripts/lint-docs.py --staged` to your current pre-commit hook from the docs repo root. Check that your hook is executable. To undo the local setting introduced by the command above, run `git config --local --unset core.hooksPath`.
