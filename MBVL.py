from python_bedrock_appx.bedrock.versions import Versions 

import requests

import os

import webbrowser

file = open("generated_versions.html",mode="w")

file.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MCBE Version Manager</title>
</head>
<body style="background-color: black;">
   <style>
        button {
            background-color: #1e1e1e;
            border: none;
            color: white;
            padding: 10px 20px;
            border-radius: 15px;
            display: inline-block;
            margin: 10px;
            transition: opacity 0.3s;
        }
        
        button:hover {
            opacity: 0.7;
            cursor: pointer;
        }
        
        button:active {
            opacity: 0.3;
        }
    </style>
           <h1 style="color:white;font-weight:900;font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;text-align:center;">Versions</h1>
           </hr>
""")
        

print("Loading...")

url = "https://raw.githubusercontent.com/CrystalVortex/Minecraft-Bedrock-Version-Manager/main/versions.txt"
response = requests.get(url, headers={'Cache-Control': 'no-cache'})

html_content = response.text

# Split the HTML content by lines and iterate over them
lines = html_content.split('\n')
for i, line in enumerate(lines, start=1):
    line = line.strip()  # Remove leading and trailing whitespace
    if line:  # Check if the line is not empty after stripping
        version = Versions.get_by_version(line)
        print(line+" <- Searching")
        file.write(f"""
<a href={version.uri} target="_blank">                   
<button>{line}</button>
</a>
""")
    file.write("</body>\n</html>")

webbrowser.open("generated_versions.html")
