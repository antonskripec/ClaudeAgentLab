from mcp.server.mcpserver import MCPServer
from pydantic import Field

mcp = MCPServer("DocumentMCP", log_level="ERROR")


@mcp.tool(
    name="read_doc_contents",
    description="Read the contents of a document and return it as a string",
)
async def read_doc_contents(
    doc_id: str = Field(description="Document ID to read"),
) -> str:
    # Validate the doc_id
    if not doc_id.strip():
        raise ValueError("Document ID cannot be empty")

    # Implement the logic to read the document contents based on the doc_id
    # For now, we'll return a placeholder string
    return f"Contents of document with ID: {doc_id}"


# Run the server over stdio when launched as a subprocess by the Claude agent
if __name__ == "__main__":
    mcp.run()
