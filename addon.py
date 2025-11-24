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

class BlenderMCPPanel(bpy.types.Panel):
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
        
def register():
    bpy.utils.register_class(BlenderMCPPanel)

def unregister():
    bpy.utils.unregister_class(BlenderMCPPanel)

if __name__ == "__main__":
    register()
            
    
    