# ClaudeAgentLab

A small sandbox for experimenting with the [Claude Agent SDK](https://pypi.org/project/claude-agent-sdk/) in Python.

`src/main.py` sends a single prompt to Claude through the SDK's `query()` function and prints every streamed message as pretty-printed JSON, so you can see exactly what the agent returns.

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)
- An Anthropic API key

## Setup

1. Install dependencies:

   ```sh
   uv sync
   ```

2. Create a `.env` file in the project root with your API key:

   ```env
   ANTHROPIC_API_KEY=sk-ant-...
   ```

   `.env` is ignored by git, so the key won't be committed.

## Usage

```sh
uv run src/main.py
```

To try a different prompt, system prompt, model or effort level, edit the `ClaudeAgentOptions` and the `query(prompt=...)` call in [src/main.py](src/main.py).

## Project layout

```
src/main.py         Entry point: configures the agent and streams its output
tools/my_tools.py   Placeholder for custom agent tools
scripts/notify.sh   Placeholder helper script
pyproject.toml      Project metadata and dependencies
```

## Development

Type checking uses [Pyrefly](https://pyrefly.org/), installed with the `dev` dependency group:

```sh
uv run pyrefly check
```
