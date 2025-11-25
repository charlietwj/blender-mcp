import bpy
import socket
import threading

bl_info = {
    "name": "BlenderMCP",
    "author": "Charlie",
    "version": (1, 0),
    "blender": (3, 0, 0),
    "location": "View3D > Sidebar > BlenderMCP",
    "description": "Use MCP to connect Blender to Claude Desktop",
    "category": "Interface",
}

class BlenderMCPServer:
    
    def __init__(self):
        self.is_running = False
        self.socket = None
        self.server_thread = None

    def start(self):
        if self.is_running:
            print("Server is already running")
            return 
        
        self.is_running = True
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        localhost = "127.0.0.1"
        port = "5678"
        self.socket.bind((localhost, port))
        self.socket.settimeout(1.0)
        self.socket.listen()

        self.server_thread = threading.Thread(
            target=self.server_loop,
            daemon=True
        )
        self.server_thread.start()

    def stop(self):
        self.is_running = False
        if self.socket:
            self.socket.close()
            self.socket = None

        if self.server_thread:
            if self.server_thread.is_alive():
                self.server_thread.join(timeout=1.0)

            self.server_thread = None

    def server_loop(self):
        while self.is_running:
            try:
                conn, _ = self.socket.accept()
                conn.setblocking(True)
                
                thread = threading.Thread(
                    target=self.handle_client,
                    args=(conn,),
                    daemon=True
                )
                thread.start()
            except socket.timeout:
                continue

    def handle_client(self, conn: socket.socket):        
        with conn:
            while self.is_running:
                data = conn.recv(65536)
                if not data:
                    break

                code = data.decode()
                self.execute_code(code)

    def execute_code(self, code):
        pass

class BLENDERMCP_PT_Panel(bpy.types.Panel):
    bl_label = "Blender MCP"
    bl_idname = "BLENDERMCP_PT_Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "BlenderMCP"
    
    def draw(self, context):
        layout = self.layout
        obj = context.object
        
        row = layout.row()
        row.label(
            text="Hi world!",
            icon="WORLD_DATA"
        )
        
        row = layout.row()
        row.label(
            text='Active object is: ' + obj.name
        )
        
        row = layout.row()
        row.prop(obj, "name")
        
        row = layout.row()
        row.operator("mesh.primitive_cube_add")

class BLENDERMCP_OT_StartServer(bpy.types.Operator):
    bl_idname = "blendermcp.start_server"
    bl_label = "Start the connection to Claude Desktop"

    def execute(self, context):
        if not hasattr(bpy.types, "blendermcp_server"):
            bpy.types.blendermcp_server = BlenderMCPServer()
        elif not bpy.types.blendermcp_server:
            bpy.types.blendermcp_server = BlenderMCPServer()
        
        bpy.types.blendermcp_server.start()
        context.scene.blendermcp_server_running = True

        return {'FINISHED'}
    
class BLENDERMCP_OT_StopServer(bpy.types.Operator):
    bl_idname = "blendermcp.stop_server"
    bl_label = "Stop the connection to Claude Desktop"

    def execute(self, context):
        if hasattr(bpy.types, "blendermcp_server") and bpy.types.blendermcp_server:
            bpy.types.blendermcp_server.stop()
            del bpy.types.blendermcp_server

        context.scene.blendermcp_server_running = True

        return {'FINISHED'}

def register():
    bpy.types.Scene.blendermcp_server_running = bpy.props.BoolProperty(
        name = "Server Running",
        default = False
    )

    bpy.utils.register_class(BLENDERMCP_PT_Panel)
    bpy.utils.register_class(BLENDERMCP_OT_StartServer)
    bpy.utils.register_class(BLENDERMCP_OT_StopServer)

    print("Register Blender addon")

def unregister():
    bpy.utils.unregister_class(BLENDERMCP_PT_Panel)

if __name__ == "__main__":
    register()
            
    
    