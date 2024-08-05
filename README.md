# Minecraft Bedrock Version Manager Version 9 Test

Manage multiple versions of Minecraft Bedrock Edition with ease.

## ⬆️Features
- Choose from a variety of Minecraft Bedrock versions to play.
- Simple and straightforward installation process.
- Support for all versions (including betas/previews)

## ⚠ Warning!
- All mods, worlds and any content in your current minecraft version, will be deleted when using this launcher!
- To find your worlds, paste the following path in your file explorer's search bar/button:
   `%LocalAppData%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds`
  
## 🕹️Usage
1. Download the latest release from [Releases](https://github.com/crystalvortex/Minecraft-Bedrock-Version-Manager/releases).
2. Open `launcher.exe`.
3. Before proceeding, ensure that you have taken backups of your worlds, mods, and anything else that you think is important.
4. Click Choose Version at the bottom navigation bar
5. Enter the version name you want (This includes any preview), then click install (this will take a while)
6. When the "Installing, this may take a few minutes!" is gone, you can click the "Choose" button on your chosen version, then click "Back".
7. Click play and enjoy on the main launcher screen!
   
## 📃Supported Versions

- All release versions, all betas/previews the moment they come out.

## 🔨Building

To build the project locally, follow these steps:

1. Install the required dependencies by running the following command from the root folder:
   `pip install -r requirements.txt`
2. To turn the project into an executable, install PyInstaller:
   `pip install pyinstaller`
3. Generate the executable by running:
   `pyinstaller --noconfirm --onedir --console --icon "INSERT-ICON-ICO-PATH-HERE" --name "MBVL" --add-data "LauncherData;LauncherData/" --add-data "MinecraftBedrock;MinecraftBedrock/"  "launcher.py"`
4. Navigate to the `dist` directory to find the generated executable.

## 📚Libraries

The following library was used to obtain download links:
- [tinytengu/python-bedrock-appx](https://github.com/tinytengu/python-bedrock-appx)

Feel free to contribute to this project or report any issues you encounter.
