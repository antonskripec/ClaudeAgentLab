from claude_agent_sdk.types import HookContext, HookInput, HookJSONOutput

# Custom tool for logging
async def log_tool(input_data: HookInput,
                   tool_use_id: str | None,
                   context: HookContext) -> HookJSONOutput:
    print("Tool used:", input_data.get("tool_name"))
    return {}

# Custom tool for auditing tool usage
async def audit_tool(input_data: HookInput,
                     tool_use_id: str | None,
                     context: HookContext) -> HookJSONOutput:
    print("Auditing tool use:", input_data.get("tool_name"))
    return {"async_": True} # No waiting needed
