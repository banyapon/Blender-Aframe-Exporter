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
<!DOCTYPE html>
<html>
<head>
    <script src="https://aframe.io/releases/1.ุ.0/aframe.min.js"></script>
    <script src="https://cdn.jsdelivr.net/gh/n5ro/aframe-physics-system@v4.0.1/dist/aframe-physics-system.min.js"></script> 

    <script>
        AFRAME.registerComponent('camera-control', 
 {{
            init: function() {{
                this.el.setAttribute('wasd-controls', '');
                this.el.setAttribute('look-controls', '');
            }}
        }});
    </script>
</head>
<body>
    <a-scene physics>
        <a-assets>
            <a-asset-item id="model" src="{os.path.basename(glb_filepath)}"></a-asset-item>
        </a-assets>
        <a-entity
            id="camera-rig"
            position="0 1.6 0"
            movement-controls="speed: 0.2"
            camera-control
        >
            <a-entity
                camera
                position="0 0 0"
                look-controls="pointerLockEnabled: true"
            ></a-entity>
        </a-entity>
        <a-entity
            gltf-model="#model"
            static-body
            geometry="primitive: box"
            collision-filter="group: all; collidesWith: all"
        ></a-entity>
    </a-scene>
</body>
</html>
            """)

        return {'FINISHED'}
