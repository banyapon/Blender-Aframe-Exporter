import bpy
from . import aframe_exporter

bl_info = {
    "name": "A-Frame Exporter",
    "author": "Banyapon Poolsawas",
    "version": (1, 0, 5), 
    "blender": (4, 0, 0),
    "location": "File > Export, Scene Properties > A-Frame Export Settings",
    "description": "Export Blender scene to A-Frame HTML and GLB with local server",
    "warning": "",
    "category": "Export",
}

def menu_func_export(self, context):
    self.layout.operator(aframe_exporter.ExportAFrame.bl_idname, text="A-Frame (.html)")

def register():
    bpy.utils.register_class(aframe_exporter.ExportAFrame)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    bpy.utils.unregister_class(aframe_exporter.ExportAFrame)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()