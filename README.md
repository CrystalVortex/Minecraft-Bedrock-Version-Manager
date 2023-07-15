
# Minecraft-Bedrock-Version-Manager
You can choose multiple versions of Minecraft bedrock to play
New versions to use coming soon!
<strong>
# ❗How to use:
Open  launcher.exe in [Releases](https://github.com/crystalvortex/Minecraft-Bedrock-Version-Manager/releases). </br>

Delete your current version on mcbe (Take backups of your worlds). </br>

and open the appx file that you downloaded! (if the downloaded file doesnt end with a .appx at the end just add it eg: app.appx) </br>

To find your worlds, paste this in your search bar/button: </br>
%LocalAppData%\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftWorlds

More info can be found here: https://windowsloop.com/find-minecraft-windows-10-edition-save-location/ </br>

Report any issues/problems in issues

# ❓Supported Versions:
+ 1.19 Versions
+ 1.20 Versions


</strong>


# 🛠️ Building
Install the requirements. Cd into the root folder first. </br>
```
pip install -r requirements.txt
```
Turning it into an exe </br>
```
pip install pyinstaller
```

```
pyinstaller --onefile MBVL.py
```

Navigate to dist 

# 📕Libraries
Used to get download links: </br>
[tinytengu/python-bedrock-appx](https://github.com/tinytengu/python-bedrock-appx) </br>
