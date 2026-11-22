# Claude Code terminal status hooks

On macOS, iTerm2 can show when a Claude Code session is working, waiting for input, or idle. This is optional and applies to Claude Code running in iTerm2. Workflow setup does not enable these hooks.

## Recommended setup

1. Make sure `claude --version` works in iTerm2.
2. In iTerm2, choose **iTerm2 → Install Claude Code Integration**. Follow the steps to enable the Python API, install the hook, and show the **Session Status** tool. The Workgroup and profile trigger steps are optional.
3. Open a new Claude Code session in iTerm2. Send a prompt and check **View → Toolbelt → Session Status** for the working state and the return to idle.

The iTerm2 installer registers the command for its installed version in your Claude Code user settings. If it already installed the integration, use its existing hooks. To remove or repair that setup, use iTerm2's uninstall or reinstall menu item. [iTerm2 integration guide](https://iterm2.com/claude-code-integration.html)

## Run the bundled hook

The [hook script](./claude-code-status.sh) forwards the unmodified Claude Code event on standard input to iTerm2’s standalone `cc-status` helper. It uses `$HOME/.config/iterm2/cc-status` by default. If it is elsewhere, export `AI_WORKFLOW_CC_STATUS` with the absolute executable path before starting Claude Code. Use the installer setup above if your iTerm2 version supplies a different command.

From the `ai-workflow/hooks/` directory, install a local copy of the script:

```sh
mkdir -p "$HOME/.local/bin"
install -m 755 claude-code-status.sh "$HOME/.local/bin/ai-workflow-claude-status"
```

Open the [settings example](./claude-code.settings.example.json) to see the ten events forwarded by the script. Use one status integration per event.

- Back up your Claude Code user settings. The default file is `~/.claude/settings.json`.
- Merge the example's entries into the corresponding arrays in the existing `hooks` object. Keep existing settings and unrelated hooks. If an event already has the same status hook, keep one copy.
- Verify the installed events with `/hooks` and check the iTerm2 toolbelt in a new session. To undo the manual setup, remove only the entries you added.

The example passes the hook payload through standard input to the status helper. Its output and exit failure are ignored so a status update cannot make a workflow decision. The helper only reports session activity. Claude Code reads the engineering workflow through [`CLAUDE.md`](../CLAUDE.md) and the installed personas and skills. [Claude Code hook settings](https://code.claude.com/docs/en/hooks)
