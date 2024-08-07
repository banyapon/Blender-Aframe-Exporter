import bpy
import os
import shutil
import http.server
import socketserver
import threading
import webbrowser
from bpy.props import BoolProperty, IntProperty
from bpy_extras.io_utils import ExportHelper

class ServerThread(threading.Thread):
    def __init__(self, directory, port):
        super().__init__()
        self.directory = directory
        self.port = port
        self.httpd = None
        self.error = None

    def run(self):
        os.chdir(self.directory)

        # Error handling for the server
        try:
            handler = http.server.SimpleHTTPRequestHandler
            with socketserver.TCPServer(("", self.port), handler) as httpd:
                self.httpd = httpd
                print(f"Serving at port {self.port}")
                httpd.serve_forever()
        except OSError as e:
            self.error = e

    def stop(self):
        if self.httpd:
            self.httpd.shutdown()
            
class ExportAFrame(bpy.types.Operator, ExportHelper):
    bl_idname = "export_scene.aframe"
    bl_label = "Export A-Frame"
    filename_ext = ".html"

    start_server: BoolProperty(
        name="Start Local Server",
        description="Automatically start a local server after export",
        default=False
    )

    port: IntProperty(
        name="Port",
        description="Port number for the local server",
        default=8200,
        min=1,
        max=65535
    )


    def execute(self, context):
        filepath = self.filepath
        glb_filepath = os.path.splitext(filepath)[0] + ".glb"

        # Export GLB
        bpy.ops.export_scene.gltf(filepath=glb_filepath, export_format='GLB')

        # Copy favicon
        favicon_path = os.path.join(os.path.dirname(__file__), "icons", "favicon.ico")
        if os.path.exists(favicon_path):
            shutil.copy(favicon_path, os.path.dirname(filepath))

        # Create HTML (A-Frame)
        with open(filepath, "w") as f:
            f.write(f"""
<!DOCTYPE html>
<html>
<head>
    <link rel="icon" href="favicon.ico">
    <title>Aframe Exporter</title>
    <script src="https://aframe.io/releases/1.6.0/aframe.min.js"></script>
</head>

<body>
    <a-scene>
        <a-assets>
            <a-asset-item id="model" src="{os.path.basename(glb_filepath)}"></a-asset-item>
        </a-assets>

        <a-entity id="cameraRig" movement-controls="fly: false; speed: 0.2;">
            <a-entity id="camera" camera look-controls position="0 1.6 0" wasd-controls></a-entity>
            <a-entity oculus-touch-controls="hand: left"></a-entity>
            <a-entity oculus-touch-controls="hand: right"></a-entity>
        </a-entity>

        <a-entity gltf-model="#model" static-body></a-entity>
    </a-scene>
</body>
</html>
            """)

        if self.start_server:
            self.server_thread = ServerThread(os.path.dirname(filepath), self.port)
            self.server_thread.start()

            if self.server_thread.error:  # Check for errors
                self.report({'ERROR'}, f"Failed to start server: {self.server_thread.error}")
                return {'CANCELLED'}

            url = f"http://localhost:{self.port}/{os.path.basename(filepath)}"
        else:
            url = "file://" + filepath 

        webbrowser.open_new_tab(url)
        return {'FINISHED'}

    def start_local_server(self, directory, port):
        os.chdir(directory)
        handler = http.server.SimpleHTTPRequestHandler
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"Serving at port {port}")
            threading.Thread(target=httpd.serve_forever).start()

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

class ExportAFramePanel(bpy.types.Panel):
    bl_label = "A-Frame Export Settings"  # Label for the panel
    bl_idname = "OBJECT_PT_aframe_export" # Unique identifier for the panel
    bl_space_type = 'PROPERTIES'  # Panel location (Properties Editor)
    bl_region_type = 'WINDOW'  # Panel type (window)
    bl_context = "scene"  # Context for the panel (Scene)
    bl_options = {'DEFAULT_CLOSED'}  # Panel is closed by default

    def draw(self, context):
        layout = self.layout

        # Export Button
        layout.operator("export_scene.aframe", text="Export A-Frame")  # Add the export operator button

        # Local Server Options
        row = layout.row()  # Create a new row for the checkbox and button
        row.prop(context.scene, "aframe_local_server", text="Start Local Server")  # Checkbox to toggle local server
        if context.scene.aframe_local_server:  # Show port input if the checkbox is checked
            row = layout.row()  # Create a new row for the port input
            row.prop(context.scene, "aframe_server_port", text="Port")  # Input field for the port number