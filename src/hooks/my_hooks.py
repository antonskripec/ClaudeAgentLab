import re

from claude_agent_sdk.types import HookContext, HookInput, HookJSONOutput


# Custom hook for logging
async def log_hook(
    input_data: HookInput, tool_use_id: str | None, context: HookContext
) -> HookJSONOutput:
    print("Tool used:", input_data.get("tool_name"))
    return {}


# Custom hook for auditing tool usage
async def audit_hook(
    input_data: HookInput, tool_use_id: str | None, context: HookContext
) -> HookJSONOutput:
    print("Auditing tool use:", input_data.get("tool_name"))
    return {"async_": True}  # No waiting needed


# Patterns for bash commands considered destructive
DESTRUCTIVE_PATTERNS: list[str] = [
    r"\brm\s+(-\w*\s+)*-\w*[rf]",  # rm -rf, rm -r, rm -f
    r"\bsudo\b",
    r"\bmkfs(\.\w+)?\b",
    r"\bdd\s+.*\bof=",
    r"\bshred\b",
    r":\(\)\s*\{\s*:\|:&\s*\};:",  # fork bomb
    r">\s*/dev/sd\w*",
    r"\bchmod\s+(-\w+\s+)*777\s+/",
    r"\bchown\s+-R\b",
    r"\b(shutdown|reboot|halt|poweroff)\b",
    r"\bgit\s+reset\s+--hard\b",
    r"\bgit\s+clean\s+-\w*f",
    r"\bgit\s+push\s+.*(--force|-f)\b",
    r"\b(curl|wget)\b.*\|\s*(ba|z)?sh\b",
    r"\bRemove-Item\b.*-Recurse",
    r"\b(del|rd|rmdir)\s+/[sq]",
    r"\bformat\s+[a-z]:",
]


# Custom hook that blocks destructive bash commands
async def check_bash(
    input_data: HookInput, tool_use_id: str | None, context: HookContext
) -> HookJSONOutput:

    # Check if the tool being used is Bash
    if input_data.get("tool_name") != "Bash":
        return {}

    # Extract the command being executed in Bash
    # pyrefly: ignore [missing-attribute]
    command: str = input_data.get("tool_input", {}).get("command", "")

    for pattern in DESTRUCTIVE_PATTERNS:
        if re.search(pattern, command, re.IGNORECASE):
            return {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "deny",
                    "permissionDecisionReason": f"Destructive command blocked: {command}",
                }
            }
    return {}
