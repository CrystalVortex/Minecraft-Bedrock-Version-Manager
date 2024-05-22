# Minecraft Bedrock Version Manager

Manage multiple versions of Minecraft Bedrock Edition with ease.

## ⬆️Features
- Choose from a variety of Minecraft Bedrock versions to play.
- Simple and straightforward installation process.
- Support for upcoming versions.

## 🕹️Usage

1. Download the latest release from [Releases](https://github.com/crystalvortex/Minecraft-Bedrock-Version-Manager/releases).
2. Open `launcher.exe`.
3. Before proceeding, ensure that you have taken backups of your worlds.
4. Delete your current Minecraft Bedrock version.
5. Open the downloaded `.appx` file. If the downloaded file doesn't have a `.appx` extension, simply add it at the end of the file name (e.g., `app.appx`).
6. To find your worlds, paste the following path in your file explorer's search bar/button:
   `%LocalAppData%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds`
   For more information on finding the Minecraft Windows 10/11 Edition save location, refer to [this guide](https://windowsloop.com/find-minecraft-windows-10-edition-save-location/).
7. If you encounter any issues or problems, please report them in the issues section of this repository.

## 📃Supported Versions

- All versions of Bedrock are available from 0.13.0.0 to the latest.

## 🔨Building

To build the project locally, follow these steps:

1. Install the required dependencies by running the following command from the root folder:
   `pip install -r requirements.txt`
2. To turn the project into an executable, install PyInstaller:
   `pip install pyinstaller`
3. Generate the executable by running:
   `pyinstaller --onefile MBVL.py`
4. Navigate to the `dist` directory to find the generated executable.

## 📚Libraries

The following library was used to obtain download links:
- [tinytengu/python-bedrock-appx](https://github.com/tinytengu/python-bedrock-appx)

Feel free to contribute to this project or report any issues you encounter.
