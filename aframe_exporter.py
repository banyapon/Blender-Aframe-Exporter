import bpy
import os
from bpy_extras.io_utils import ExportHelper

class ExportAFrame(bpy.types.Operator, ExportHelper):
    bl_idname = "export_scene.aframe"
    bl_label = "Export A-Frame"
    filename_ext = ".html"

    def execute(self, context):
        filepath = self.filepath
        glb_filepath = os.path.splitext(filepath)[0] + ".glb"

        # Export GLB
        bpy.ops.export_scene.gltf(filepath=glb_filepath, export_format='GLB')

        # สร้างไฟล์ HTML (A-Frame)
        with open(filepath, "w") as f:
            f.write(f"""
<!--This file generated from Aframe Exporter, Blender Add-on-->
<!DOCTYPE html>
<html>
<head>
    <link rel="icon" type="image/x-icon" href="https://raw.githubusercontent.com/banyapon/Blender-Aframe-Exporter/main/icons/favicon.ico">
    <title>Aframe Exporter</title>
    <script src="https://aframe.io/releases/1.6.0/aframe.min.js"></script>
</head>

<body>
    <a-scene>
        <a-assets>
            <a-asset-item id="model" src="{os.path.basename(glb_filepath)}"></a-asset-item>
        </a-assets>

        <a-entity id="cameraRig" movement-controls="fly: false; speed: 0.2;">
            <a-entity id="camera" camera position="0 1.6 0" wasd-controls></a-entity>
            <a-entity oculus-touch-controls="hand: left"></a-entity>
            <a-entity oculus-touch-controls="hand: right"></a-entity>
        </a-entity>

        <a-entity gltf-model="#model" static-body></a-entity>
    </a-scene>
</body>

</html>
            """)

        return {'FINISHED'}
