import asyncio
import dataclasses
import json
import os
import sys
from pathlib import Path
from typing import Any

from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the API key from environment variables and configure the Claude agent options
api_key: str | None = os.getenv("ANTHROPIC_API_KEY")

# Check if the API key is set in the environment variables
if api_key is None:
    raise RuntimeError("ANTHROPIC_API_KEY is not set")

# Set the API key as an environment variable for the current process
os.environ["ANTHROPIC_API_KEY"] = api_key

# Configure the Claude agent options
options = ClaudeAgentOptions(
    model="claude-opus-5-5",
    allowed_tools=["Read", "Grep", "Glob"],
    effort="medium",
    env={"ANTHROPIC_API_KEY": api_key},
    mcp_servers={
        "DocumentMCP": {
            "type": "stdio",
            "command": sys.executable,
            "args": [str(Path(__file__).parent / "tools" / "my_mcps.py")],
        }
    },
)


# Format an SDK message (a dataclass) as indented JSON, tagged with its type name
def format_message(message) -> str:
    data: dict[str, Any] | Any = (
        dataclasses.asdict(message) if dataclasses.is_dataclass(message) else message
    )
    return json.dumps(
        {"type": type(message).__name__, "data": data},
        indent=2,
        ensure_ascii=False,
        default=str,
    )


# Main async function to run the Claude SDK client and query the auth module
async def main():
    async with ClaudeSDKClient(options=options) as client:
        # Question 1 : Send a query to the Claude SDK client to summarize the auth module
        await client.query(prompt="Summarize the auth module")
        async for message in client.receive_response():
            print(format_message(message))

        # Question 2 : Send a query to the Claude SDK client to identify functions lacking tests
        await client.query(prompt="Which of those functions lacks tests?")
        async for message in client.receive_response():
            print(format_message(message))


# Entry point for the script
asyncio.run(main())
