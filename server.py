from fastmcp import FastMCP

mcp = FastMCP("Blender-MCP")

@mcp.tool()
def add(x: int, y: int) -> int:
    return x + y

