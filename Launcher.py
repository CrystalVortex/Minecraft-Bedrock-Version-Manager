from flask import Flask, render_template, request, jsonify
import os
from LauncherData.python_bedrock_appx.bedrock.versions import Versions
from urllib.request import urlretrieve
import shutil
import webbrowser
import pyuac
import tkinter.messagebox as messagebox

if not pyuac.isUserAdmin():
        print("Not launched as admin")
        messagebox.showerror("Launcher Error", "Start the launcher as admin to continue.") 
        exit()


def get_versions():
    minecraft_directory = "MinecraftBedrock"
    versions = os.listdir(minecraft_directory)
    return versions

app = Flask(__name__, template_folder='LauncherData/Pages')


@app.route('/')
def hello():
    return render_template("launcher.html")

@app.route("/versions")
def versions():
    return render_template("versions.html")

@app.route("/versions/download", methods=["POST"])
def download():
    version = request.json.get("version")
    if os.path.isfile(f"{version}.appx"):
        os.rename(f"{version}.appx", f"{version}.zip")
        pass
    else:
        installver = Versions.get_by_version(version)
        urlretrieve(installver.uri, version+".appx")
        os.rename(f"{version}.appx", f"{version}.zip")

    # Respond with JSON indicating completion
    shutil.unpack_archive(version+".zip","MinecraftBedrock/"+version+"/")
    os.system(f'powershell.exe -Command "Get-AppxPackage -allusers *minecraftUWP* | Remove-AppxPackage -allusers"')
    print("Deleted Minecraft.")
    os.remove(f"MinecraftBedrock/{version}/AppxSignature.p7x")
    os.remove(f"MinecraftBedrock/{version}/[Content_Types].xml")
    os.remove(f"MinecraftBedrock/{version}/AppxBlockMap.xml")
    os.system(f"powershell.exe Add-AppxPackage -Register MinecraftBedrock/{version}/AppXManifest.xml")
    webbrowser.open("minecraft://")
    return jsonify({"message": f"Processing complete for version {version}"})

@app.route("/download_complete/<version>")
def download_complete(version):
    return render_template("versions.html")


@app.route("/save_version", methods=["POST"])
def save_version():
    version = request.json.get("version")
    with open('LauncherData/stored/version.txt', 'w') as f:
        f.write(version)
    return render_template("launcher.html")

@app.route('/get_versions')
def get_versions_route():
    versions = get_versions()
    return jsonify({'versions': versions})

@app.route('/launch')
def launch():
    os.system(f'powershell.exe -Command "Get-AppxPackage -allusers *minecraftUWP* | Remove-AppxPackage -allusers"')
    with open("LauncherData/stored/version.txt", 'r') as file:
        file_contents = file.read()
        os.system(f"powershell.exe Add-AppxPackage -Register MinecraftBedrock/{file_contents}/AppXManifest.xml")
        webbrowser.open("minecraft://")
        webbrowser.open("minecraft-preview://")
        return render_template("launcher.html")
if __name__ == '__main__':
    webbrowser.open("http://localhost:5000")
    app.run(debug=False, port=5000)
