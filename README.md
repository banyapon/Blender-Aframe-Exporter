# Blender A-Frame Exporter

[![Blender Version](https://img.shields.io/badge/Blender-3.0+-orange.svg)](https://www.blender.org/) [![Blender Version](https://img.shields.io/badge/Blender-4.0+-orange.svg)](https://www.blender.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This Blender add-on simplifies the process of exporting your 3D scenes into interactive web experiences using A-Frame, a popular web framework for building virtual reality (VR) and augmented reality (AR) experiences.

## Features

![Showcase](https://github.com/banyapon/Blender-Aframe-Exporter/blob/main/dist/8.png?raw=true)

* **Seamless Export:** Quickly export your entire Blender scene, including models, materials, and animations, to A-Frame HTML and GLB (binary glTF) files.
* **Collision Detection:** Automatically add collision detection to your exported models using A-Frame's physics system, enabling interactive experiences.
* **Camera Controls:** Easily set up basic WASD controls for navigating your A-Frame scene with the camera.
* **Customization:** Customize the generated A-Frame code to add additional features, components, or interactions.

## Installation

1. Download the latest release of the add-on (`.zip` file) from the [Releases](https://github.com/banyapon/Blender-Aframe-Exporter/releases/tag/release) page.
2. In Blender, go to `Edit` > `Preferences` > `Add-ons` > `Install...`
![Go to `Edit` > `Preferences` > `Add-ons` > `Install](https://raw.githubusercontent.com/banyapon/Blender-Aframe-Exporter/main/dist/1.png)
3. Select the downloaded `.zip` file and click `Install Add-on`.
![Zip File](https://github.com/banyapon/Blender-Aframe-Exporter/blob/main/dist/2.png?raw=true)
4. Enable the "A-Frame Exporter" add-on in the list.
![Enable add-on](https://github.com/banyapon/Blender-Aframe-Exporter/blob/main/dist/3.png?raw=true)

## Usage

1. Create your 3D scene in Blender.
![Create Scene](https://github.com/banyapon/Blender-Aframe-Exporter/blob/main/dist/5.png?raw=true)
2. Go to `File` > `Export` > `A-Frame (.html)`.

    ![Export Aframe](https://github.com/banyapon/Blender-Aframe-Exporter/blob/main/dist/6.png?raw=true)

3. Choose a location to save the files and click `Export A-Frame`.
![VS Code](https://github.com/banyapon/Blender-Aframe-Exporter/blob/main/dist/7.png?raw=true)
4. The add-on will generate an HTML file (`your_scene_name.html`) and a GLB file (`your_scene_name.glb`).
5. Open the HTML file in a web browser to view your interactive A-Frame scene.
![WebXR](https://github.com/banyapon/Blender-Aframe-Exporter/blob/main/dist/9.png?raw=true)

## Additional Notes

* Make sure you have a web server running to view the exported HTML file correctly.
* For more advanced A-Frame features and customization, refer to the [A-Frame documentation](https://aframe.io/docs/).

## Contributing

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.

## License

This add-on is released under the MIT License.
