import asyncio
import os

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
)


# Main async function to run the Claude SDK client and query the auth module
async def main():
    async with ClaudeSDKClient(options=options) as client:
        await client.query(prompt="Summarize the auth module")
        async for message in client.receive_response():
            print(message)


# Entry point for the script
if __name__ == "__main__":
    asyncio.run(main())
