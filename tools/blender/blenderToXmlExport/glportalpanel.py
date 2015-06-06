import bpy

class GlPortalPanel(bpy.types.Panel):
    """GlPortal panel in the toolbar"""
    bl_label = "Set Type"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'TOOLS'
    bl_category = "GlPortal"
    
    def draw(self, context):
        layout = self.layout

        layout.label("Wall:")
        row = layout.row()
        split = layout.split()
        col = split.column(align=True)
        col.operator("wm.set_portable", text="Set Portable", icon='MESH_PLANE')
        col.operator("wm.set_wall", text="Set Tiles", icon='MESH_PLANE')

        layout.label("Volume:")
        row = layout.row()
        split = layout.split()
        col = split.column(align=True)
        col.operator("wm.set_acid", text="Set Acid", icon='MESH_CUBE')
        
        layout.label("Trigger:")
        row = layout.row()
        split = layout.split()
        col = split.column(align=True)
        col.operator("wm.add_death", text="Death", icon='MESH_CUBE')
        col.operator("wm.add_radiation", text="Radiation", icon='MESH_CUBE')
        col.operator("wm.add_win", text="Win", icon='MESH_CUBE')
        
        layout.label("Map:")
        row = layout.row()
        split = layout.split()
        col = split.column(align=True)
        col.operator("wm.fix_map", text="Fix Map", icon='MESH_CUBE')
