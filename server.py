from fastmcp import FastMCP

mcp = FastMCP("BlenderMCP")

class BlenderConnection:

    def __init__(self):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass

    def send_code(self, code: str):
        pass

    def get_response(self):
        pass

@mcp.tool()
def add(x: int, y: int) -> int:
    return x + y

