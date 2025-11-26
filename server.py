from fastmcp import FastMCP
import socket

mcp = FastMCP("BlenderMCP")

class BlenderConnection:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, "_initialized"):
            self.host = "127.0.0.1"
            self.port = 5678
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sock.connect((self.host, self.port))
            self._initialized = True

    def execute_code(self, code: str) -> str:
        pass

@mcp.tool()
def execute_blender_code(code: str):
    """
    Execute python code in Blender.
    """

    try:
        blender = BlenderConnection()
        result = blender.execute_code(code)
        return f"Code executed successfully: {result}"
    except Exception as e:
        return f"Error occurred: {str(e)}"


