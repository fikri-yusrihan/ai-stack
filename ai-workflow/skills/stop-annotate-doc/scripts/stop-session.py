#!/usr/bin/env python3
"""Stop one verified single-document Plannotator annotate session on POSIX."""

import argparse
import json
import os
from pathlib import Path
import shlex
import shutil
import signal
import subprocess
import sys


def active_session(binary, pid, document):
    result = subprocess.run([binary, "sessions", "--json"], capture_output=True, text=True, check=True)
    sessions = json.loads(result.stdout)
    if not isinstance(sessions, list):
        return False
    return any(isinstance(row, dict) and row.get("pid") == pid
               and row.get("mode") == "annotate" and row.get("target") == document for row in sessions)


def matches_process(binary, pid, document):
    possible_names = {Path(binary).name, binary, str(Path(binary).resolve())}
    expected_args = ["annotate", document, "--json"]
    if sys.platform.startswith("linux"):
        process = Path(f"/proc/{pid}")
        args = os.fsdecode((process / "cmdline").read_bytes()).split("\0")[:-1]
        return args[1:] == expected_args and os.path.samefile(process / "exe", binary)

    result = subprocess.run(
        ["ps", "-ww", "-p", str(pid), "-o", "command="],
        capture_output=True, text=True, check=True,
    )
    command = result.stdout.strip()
    if any(command == f"{name} {' '.join(expected_args)}" for name in possible_names):
        return True
    try:
        executable, *args = shlex.split(command)
    except ValueError:
        return False
    return executable in possible_names and args == expected_args


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pid", type=int)
    parser.add_argument("document", type=Path)
    args = parser.parse_args()
    if args.pid <= 1 or not args.document.is_absolute():
        parser.error("provide a session PID greater than 1 and an absolute document path")
    if sys.platform != "darwin" and not sys.platform.startswith("linux"):
        parser.error("use the original job handle on this platform")
    binary = shutil.which("plannotator")
    if not binary:
        parser.error("plannotator is not on PATH")

    document = str(args.document)
    try:
        if not active_session(binary, args.pid, document) or not matches_process(binary, args.pid, document):
            print("Refused: the active session and process do not match this PID and document.", file=sys.stderr)
            return 1
        os.kill(args.pid, signal.SIGTERM)
    except (OSError, ValueError, subprocess.CalledProcessError) as error:
        print(f"Could not verify or signal the selected session: {error}", file=sys.stderr)
        return 1
    print(f"Sent SIGTERM to Plannotator session {args.pid}. Recheck the session list.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
