import logging

from claude_agent_sdk.types import HookContext, HookInput, HookJSONOutput

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
)

logger = logging.getLogger(__name__)


# Logs the start of a tool call with its name, input, and ID.
async def log_tool_call(
    input_data: HookInput, tool_use_id: str | None, context: HookContext
) -> HookJSONOutput:
    logger.info(
        "TOOL START name=%s input=%s id=%s",
        input_data.get("tool_name"),
        input_data.get("tool_input"),
        tool_use_id,
    )

    return {}


# Logs the end of a tool call with its name, result, and ID.
async def log_tool_result(
    input_data: HookInput, tool_use_id: str | None, context: HookContext
) -> HookJSONOutput:
    logger.info(
        "TOOL END name=%s result=%s id=%s",
        input_data.get("tool_name"),
        input_data.get("tool_response"),
        tool_use_id,
    )

    return {}


# Logs a failed tool call with its name, input, ID, and error.
async def log_tool_failure(
    input_data: HookInput, tool_use_id: str | None, context: HookContext
) -> HookJSONOutput:
    logger.error(
        "TOOL FAILED name=%s input=%s id=%s error=%s interrupted=%s",
        input_data.get("tool_name"),
        input_data.get("tool_input"),
        tool_use_id,
        input_data.get("error"),
        input_data.get("is_interrupt", False),
    )

    return {}
