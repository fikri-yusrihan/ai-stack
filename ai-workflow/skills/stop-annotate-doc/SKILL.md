---
name: stop-annotate-doc
description: Close the Plannotator browser annotation sessions the user identifies. Match the document or session PID and retain saved drafts.
---

# Stop Annotate Sessions

## 1. Identify the sessions

Run `plannotator sessions --json` in the same environment used to launch the review. Keep only entries whose `mode` is `annotate`. Match the exact document path, the exact set of documents in a requested project, or the named PID. If the request leaves the target unclear, show the matching sessions and resolve the scope before stopping them.

Submitting feedback in the browser closes the active review and sends the feedback to the launch job. Stopping a session can lose comments that have not autosaved. Prefer Submit if the user wants to retain feedback that has just been entered.

## 2. Close the selected session

- If the current session launched the annotation and holds its background job handle, use the harness's stop action for that job.
- On macOS, Linux and WSL, use the bundled [stop helper](./scripts/stop-session.py) for a session launched elsewhere. Pass the confirmed PID and the exact absolute document path from the session list.

  ```text
  python3 -I <skill-dir>/scripts/stop-session.py <pid> <absolute-doc-path>
  ```

  It rechecks the active registry and process command before sending SIGTERM. It only accepts single-file sessions launched in the form used by [Annotate Doc](../annotate-doc/SKILL.md). If it cannot verify the match, use the terminal or job manager that launched the session to close that specific job. On native Windows, use its launch job handle or submit from the browser.

Re-run `plannotator sessions --json` to verify the selected sessions are gone. Leave other sessions, saved drafts and history in place.
