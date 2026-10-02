from claude_agent_sdk import tool


@tool("log_message", "Log a message", {"message": str})
async def log_message(args) -> dict[str, list[dict[str, str]]]:
    print(args["message"])
    return {"content": [{"type": "text", "text": "logged"}]}
