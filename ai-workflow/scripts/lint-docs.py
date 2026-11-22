#!/usr/bin/env python3
"""Check the structure of project documents. No third-party dependencies."""

import argparse
from collections import Counter
from pathlib import Path, PurePosixPath
import re
import subprocess


STATUS_VALUES = {
    "Draft", "In Review", "Approved", "In Progress", "Done",
    "Superseded", "Deferred", "Cancelled",
}
REVIEW_STATUSES = {"In Review", "Approved", "In Progress", "Done"}
APPROVED_STATUSES = {"Approved", "In Progress", "Done"}
OWNER_SIGNOFF = {"Owner confirmed", "Owner chose"}
CHECKER_ROLES = {"advisor", "advisor persona", "the advisor persona", "owner", "project owner", "the project owner"}
DOC_NAMES = {
    "01-research.md", "02-rfc.md", "03-challenge.md", "04-poc-simulation.md",
    "05-impl-plan.md", "06-verification.md", "07-pr-plan.md",
    "03-impl-plan.md", "05-pr-plan.md",
}
PROJECT_NUMBER = re.compile(r"^(\d{4}-\d{3})-.+$")


def git(root, *args):
    return subprocess.run(
        ["git", "-C", str(root), *args],
        check=True, capture_output=True, encoding="utf-8",
    ).stdout


def snapshot(root, since, all_docs):
    """Select paths and a reader from the same workspace snapshot."""
    if all_docs:
        paths = sorted(path.relative_to(root).as_posix()
                       for path in (root / "projects").rglob("*.md") if path.is_file())
        return paths, paths, lambda path: (root / path).read_text(encoding="utf-8")

    if since:
        changed = git(root, "diff", "--name-only", "--diff-filter=ACMR", "-z", f"{since}...HEAD")
        paths = git(root, "ls-tree", "-r", "--name-only", "-z", "HEAD")
        return changed.split("\0"), paths.split("\0"), lambda path: git(root, "show", f"HEAD:{path}")

    changed = git(root, "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z")
    paths = git(root, "ls-files", "-z")
    return changed.split("\0"), paths.split("\0"), lambda path: git(root, "show", f":{path}")


def plain(value):
    return value.strip().strip("*_`").strip()


def cells(line):
    return [value.strip() for value in re.split(r"(?<!\\)\|", line.strip()[1:-1])]


def section(text, heading):
    match = re.search(rf"^## {re.escape(heading)}(?:[ \t]+[^\n]*)?\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return match.group(1) if match else None


def table_rows(text):
    headers = None
    for line in (text or "").splitlines():
        line = line.strip()
        if not (line.startswith("|") and line.endswith("|")):
            headers = None
            continue
        values = cells(line)
        if headers is None:
            headers = [plain(value).lower() for value in values]
        elif not all(re.fullmatch(r":?-+:?", value) for value in values):
            yield dict(zip(headers, map(plain, values))) if len(headers) == len(values) else {}


def header_value(text, field):
    match = re.search(rf"^\|\s*\*\*{re.escape(field)}\*\*\s*\|\s*(.*?)\s*\|", text, re.M)
    return plain(match.group(1)) if match else ""


def filled(value):
    return bool(value) and value.lower() not in {"-", "—", "–", "tbd", "pending", "unresolved"} and not value.startswith("[")


def plan_errors(text):
    preconditions = section(text, "Phase 0")
    if preconditions is None:
        yield "Approved plan needs a Phase 0 pre-conditions section."
    for row in table_rows(preconditions):
        if not row:
            yield "A pre-conditions row does not match its table header."
            continue
        blocker = row.get("#", "")
        if blocker.upper().startswith("P0"):
            decision = row.get("decision", "").removeprefix("✅").strip()
            if row.get("decided by") not in OWNER_SIGNOFF or not filled(decision) or "⏳" in decision:
                yield f"{blocker} needs a decision and owner sign-off in Decided by."
    if section(text, "Design Pivots") is None:
        yield "Approved plan needs a Design Pivots section."


def verification_errors(text):
    rows = list(table_rows(section(text, "Cases")))
    if not rows:
        yield "Done verification needs at least one case."
    for row in rows:
        case_id = row.get("#", "")
        if not re.fullmatch(r"C[1-9]\d*", case_id):
            yield "Each case needs an ID such as C1 and a row matching the table header."
        if row.get("checker grade") != "PASS":
            yield f"{case_id or 'Case'} needs PASS in Checker grade."
        if not filled(row.get("expected", "")):
            yield f"{case_id or 'Case'} needs a written expected result."
        evidence = row.get("evidence (path or link)", "") or row.get("evidence (path or link, md5)", "")
        for label, value in (("primary evidence", evidence), ("a second evidence source", row.get("second place to read it", ""))):
            if not filled(value) and not re.fullmatch(r"\[[^\]]+\]\([^\s)]+\)", value):
                yield f"{case_id or 'Case'} needs {label}."

    checker = plain(header_value(text, "Checked by").split("·")[0]).lower()
    reviewer = plain(header_value(text, "Cases reviewed").split("·")[0]).lower()
    author = plain(header_value(text, "Author").split("·")[0]).lower()
    if checker not in CHECKER_ROLES or checker == author:
        yield "Checked by must record an independent advisor or project owner."
    if reviewer not in CHECKER_ROLES:
        yield "Cases reviewed must record an independent advisor or project owner."


def lint_doc(path, text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    status = header_value(text.split("\n## ", 1)[0], "Status")
    name = PurePosixPath(path).name
    if status not in STATUS_VALUES:
        yield "Use a valid Status in the document header."
    if status in REVIEW_STATUSES:
        required = {"01-research.md": "Approach Selection Log", "02-rfc.md": "Alternatives Considered"}.get(name)
        if required and section(text, required) is None:
            yield f"{status} requires a {required} section."
    if name.endswith("impl-plan.md") and status in APPROVED_STATUSES:
        yield from plan_errors(text)
    if name == "03-challenge.md" and status in APPROVED_STATUSES:
        decisions = table_rows(section(text, "Decision"))
        if not any(row.get("decided by") in OWNER_SIGNOFF
                   and filled(row.get("owner decision", "")) and filled(row.get("date", ""))
                   for row in decisions):
            yield "Approved challenge needs an owner sign-off, decision and date."
    if name == "06-verification.md" and status == "Done":
        yield from verification_errors(text)


def project_index_errors(paths, read):
    folders = {parts[1] for path in paths
               if len(parts := PurePosixPath(path).parts) >= 3 and parts[0] == "projects"}
    numbered = {folder: match[1] for folder in folders if (match := PROJECT_NUMBER.fullmatch(folder))}
    if not numbered:
        return
    readme = read("README.md")
    for number, count in sorted(Counter(numbered.values()).items()):
        if count > 1:
            yield f"{count} project folders share {number}."
    for folder in sorted(numbered):
        if f"projects/{folder}/" not in readme and f"projects/{folder})" not in readme:
            yield f"{folder} needs a link in the project index in README.md."


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--staged", action="store_true", help="check the Git index (default)")
    modes.add_argument("--since", metavar="REF", help="check changes from the merge base with REF to HEAD")
    modes.add_argument("--all", action="store_true", help="check all project docs in the working tree")
    parser.add_argument("--workspace", type=Path, default=Path(__file__).resolve().parents[1],
                        help="docs root (defaults to the parent of scripts/)")
    args = parser.parse_args()
    root = args.workspace.resolve()

    try:
        changed, paths, read = snapshot(root, args.since, args.all)
        docs = []
        for path in changed:
            parts = PurePosixPath(path).parts
            if len(parts) >= 3 and parts[0] == "projects" and parts[-1] in DOC_NAMES:
                docs.append(path)
        failures = [(path, error) for path in sorted(docs) for error in lint_doc(path, read(path))]
        if docs or args.all or "README.md" in changed:
            failures.extend(("README.md", error) for error in project_index_errors(paths, read))
    except (OSError, subprocess.CalledProcessError, UnicodeError) as error:
        detail = getattr(error, "stderr", None) or str(error)
        parser.exit(2, f"doc lint could not read the workspace: {detail.strip()}\n")

    for path, error in failures:
        print(f"{path}: {error}")
    print(f"Checked {len(docs)} document(s). {len(failures)} error(s).")
    return int(bool(failures))


if __name__ == "__main__":
    raise SystemExit(main())
