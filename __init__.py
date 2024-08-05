import bpy
from . import aframe_exporter  # นำเข้าโมดูลที่มีคลาส ExportAFrame

bl_info = {
    "name": "A-Frame Exporter",
    "author": "Banyapon Poolsawas",
    "version": (1, 0, 0),
    "blender": (3, 0, 0),
    "location": "File > Export",
    "description": "Export Blender scene to A-Frame HTML and GLB",
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