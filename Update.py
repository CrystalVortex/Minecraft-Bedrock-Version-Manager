import requests

import time

import shutil

time.sleep(1)

print("Are you sure you want to continue? (All files relating to Minecraft Bedrock Version Manager will be reset and updated)")

time.sleep(1)

print("Press the enter key to continue")

input()

url = 'https://github.com/nobody1256/Minecraft-Bedrock-Version-Manager/archive/refs/heads/main.zip'
r = requests.get(url, allow_redirects=True)
open('Minecraft-Bedrock-Version-Manager-main.zip', 'wb').write(r.content)

shutil.unpack_archive('Minecraft-Bedrock-Version-Manager-main.zip', 'Minecraft Bedrock Version Manager (Updated Version)')

print("Update complete...")
print("Press the enter key to finish")
input()
