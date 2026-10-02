from claude_agent_sdk import ToolAnnotations, tool


# Tool for logging messages
@tool(
    "log_message",
    "Log a message",
    {"message": str},
    annotations=ToolAnnotations(read_only_hint=True),
)
async def log_message(args) -> dict[str, list[dict[str, str]]]:
    print(args["message"])
    return {"content": [{"type": "text", "text": "logged"}]}
