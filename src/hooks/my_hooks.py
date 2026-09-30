from claude_agent_sdk.types import HookContext, HookInput, HookJSONOutput


async def log_tool(input_data: HookInput,
                   tool_use_id: str | None,
                   context: HookContext) -> HookJSONOutput:
    print("Tool used:", input_data.get("tool_name"))
    return {}
