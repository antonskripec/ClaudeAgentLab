import json
from datetime import datetime, timezone
from pathlib import Path

from claude_agent_sdk.types import HookContext, HookInput, HookJSONOutput

# Audit records are appended here as one JSON object per line
AUDIT_LOG_PATH: Path = Path("audit.log")


async def log_tool(input_data: HookInput,
                   tool_use_id: str | None,
                   context: HookContext) -> HookJSONOutput:
    print("Tool used:", input_data.get("tool_name"))
    return {}


async def audit_tool(input_data: HookInput,
                     tool_use_id: str | None,
                     context: HookContext) -> HookJSONOutput:
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "session_id": input_data.get("session_id"),
        "event": input_data.get("hook_event_name"),
        "tool_use_id": tool_use_id,
        "tool_name": input_data.get("tool_name"),
        "tool_input": input_data.get("tool_input"),
    }
    with AUDIT_LOG_PATH.open("a", encoding="utf-8") as audit_file:
        audit_file.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")
    return {}
