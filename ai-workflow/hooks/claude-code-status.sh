#!/bin/sh
# Forward Claude Code's event to iTerm2 without returning a hook decision.
status_helper=${AI_WORKFLOW_CC_STATUS:-"$HOME/.config/iterm2/cc-status"}

if [ -x "$status_helper" ]; then
    "$status_helper" >/dev/null 2>&1 || true
fi
