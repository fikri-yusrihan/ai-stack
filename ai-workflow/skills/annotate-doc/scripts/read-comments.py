#!/usr/bin/env python3
"""Read the autosaved browser comments for one Plannotator document."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys


def data_dir():
    if configured := os.environ.get("PLANNOTATOR_DATA_DIR"):
        return Path(configured).expanduser()
    if shutil.which("plannotator"):
        result = subprocess.run(["plannotator", "data-dir"], capture_output=True, text=True)
        reported = Path(result.stdout.strip())
        if result.returncode == 0 and reported.is_absolute():
            return reported
    home_data = Path.home() / ".plannotator"
    xdg_home = Path(os.environ.get("XDG_DATA_HOME", ""))
    if xdg_home.is_absolute() and not (home_data / "drafts").is_dir():
        xdg_data = xdg_home / "plannotator"
        if (xdg_data / "drafts").is_dir():
            return xdg_data
    return home_data


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path, help="exact absolute path passed to annotate")
    parser.add_argument("--data-dir", type=Path, help="override the Plannotator data directory")
    args = parser.parse_args()
    if not args.document.is_absolute():
        parser.error("document must be an absolute path")

    key = hashlib.sha256(f"v1|file|{args.document}".encode()).hexdigest()[:16]
    draft = (args.data_dir or data_dir()) / "drafts" / f"file-{key}.json"
    try:
        data = json.loads(draft.read_text(encoding="utf-8"))
        annotations = data.get("annotations") if isinstance(data, dict) else None
        if not isinstance(annotations, list) or any(not isinstance(item, dict) for item in annotations):
            raise ValueError("the draft has no supported annotations list")
    except FileNotFoundError:
        print("No saved draft found. If the review was submitted, read the job output.", file=sys.stderr)
        return 1
    except (OSError, ValueError) as error:
        print(f"Could not read the saved draft: {error}", file=sys.stderr)
        return 1

    comments = [entry for entry in annotations if "source" not in entry]
    print(f"{len(comments)} browser annotation(s)")
    for entry in comments:
        print(json.dumps({
            "id": entry.get("id"),
            "type": entry.get("type"),
            "originalText": entry.get("originalText"),
            "text": entry.get("text"),
        }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
