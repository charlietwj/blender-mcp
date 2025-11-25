import bpy

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
    bl_idname = "BLENDERMCP_OT_STARTSERVER"
    bl_label = "Start the connection to Claude Desktop"

    def execute(self, context):
        if not hasattr(bpy.types, "blendermcp_server"):
            bpy.types.blendermcp_server = BlenderMCPServer()
        elif not bpy.types.blendermcp_server:
            bpy.types.blendermcp_server = BlenderMCPServer()
        
        bpy.types.blendermcp_server.start()
        context.scene.blendermcp_server_running = True

        return {'FINISHED'}

def register():
    bpy.utils.register_class(BLENDERMCP_PT_Panel)

def unregister():
    bpy.utils.unregister_class(BLENDERMCP_PT_Panel)

if __name__ == "__main__":
    register()
            
    
    