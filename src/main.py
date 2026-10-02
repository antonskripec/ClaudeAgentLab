import dataclasses
import json
import os
from typing import Any

import anyio
from claude_agent_sdk import AgentDefinition, ClaudeAgentOptions, HookMatcher, query
from dotenv import load_dotenv

from hooks.my_hooks import audit_hook, check_bash, log_hook
from tools.constants import Tool

# Load environment variables from a .env file
load_dotenv()

# Retrieve the API key from environment variables and configure the Claude agent options
api_key: str | None = os.getenv("ANTHROPIC_API_KEY")

# Check if the API key is set in the environment variables
if api_key is None:
    raise RuntimeError("ANTHROPIC_API_KEY is not set")

# Define the security reviewer sub agent
reviewer = AgentDefinition(
    description="""
                                        Reviews code for security flaws.
                                        Use after any change to auth code.
                                        """,
    prompt="""
                                    You are a security reviewer.
                                    Report each finding with its file, line and fix.
                                  """,
    tools=[Tool.Read, Tool.Grep, Tool.Glob],
)


# Configure the Claude agent options with the retrieved API key
options: ClaudeAgentOptions = ClaudeAgentOptions(
    system_prompt="""
        You are an expert Python developer.
        Explain everything clearly and concisely.
        """,
    model="claude-opus-5-5",
    effort="medium",
    env={"ANTHROPIC_API_KEY": api_key},
    hooks={
        "PreToolUse": [
            HookMatcher(hooks=[log_hook]),
            HookMatcher(matcher="Bash", hooks=[check_bash]),
        ],
        "PostToolUse": [HookMatcher(hooks=[audit_hook])],
    },
    agents={"reviewer": reviewer},
    allowed_tools=[Tool.Read, Tool.Grep, Tool.Glob, Tool.Task],
)


# Run the main async function
async def main() -> None:
    async for response in query(
        prompt="Explain async/await in Python", options=options
    ):
        # Messages are dataclasses; convert to a dict and pretty-print as indented JSON
        data: dict[str, str | Any] = {
            "type": type(response).__name__,
            **dataclasses.asdict(response),
        }
        print(json.dumps(data, indent=2, ensure_ascii=False, default=str))


# Execute the main async function using anyio
anyio.run(main)
