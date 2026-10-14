
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Community Chat Server")

messages = [
    {"user": "Amit", "text": "Hello, Python developers!"},
    {"user": "Priya", "text": "I need help with FastAPI."},
]


@mcp.tool()
def get_messages() -> list[dict]:
    """Get recent community chat messages."""
    return messages[-10:]


@mcp.tool()
def send_message(user: str, message: str) -> str:
    """Send a message to the community chat."""
    messages.append({"user": user, "text": message})
    return f"Message sent by {user}: {message}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
