import tkinter

import customtkinter

import subprocess

import webbrowser

import datetime

import time

import logging

import requests 


from termcolor import colored



new = 1
url1 = "https://download1442.mediafire.com/hps9uekiiojg/p5yxrsv39uvgdo0/Microsoft.MinecraftUWP_1.18.3004.0_x86__8wekyb3d8bbwe.Appx"

new = 2
url2 = "https://download2388.mediafire.com/hy5mdh6wemig/j3gn0szp5zriw6z/Microsoft.MinecraftUWP_1.18.1004.0_x86__8wekyb3d8bbwe.Appx"

new = 3
url3 = "https://download2391.mediafire.com/xgqv0ppevcjg/zq0pcoqbsfbhvfw/Minecraft-1.18.12.1.Appx"

new = 4 
url4 = "https://download2340.mediafire.com/3dey0di3wbdg/5o9wz0ltbb6xv5x/Minecraft-1.18.2.3.Appx"

new = 5
url5 = "https://download2273.mediafire.com/mq7cfyzxoqjg/kmelqlxa658388m/Minecraft-1.18.1.2.Appx"

new = 6 
url6 = "https://download2390.mediafire.com/wz6eg2nsscyg/wjekuyje36e51ql/Minecraft-1.18.0.2.Appx"
new = 7 
url7 = "https://download1935.mediafire.com/909odepkbncg/tjsgntidc54rru4/Minecraft-1.18.31.4.Appx"

new =8
url8 = "https://download1514.mediafire.com/vrb2a3jo8teg/t1x8yqadoxe3yqa/MC.1.19.Appx"




def openweb():
    webbrowser.open(url1,new=new)
    print("[LOG]:You clicked download 1.18.30 at:")
    print(datetime.datetime.now())
    logger.warning('[LOG]:You clicked download 1.18.30')

def openweb2():
    webbrowser.open(url2,new=new)
    print("[LOG]:You clicked download 1.18.10 at:")
    print(datetime.datetime.now())
    logger.warning('[LOG]:You clicked download 1.18.10')

def openweb3():
    webbrowser.open(url3,new=new)
    print("[LOG]:You clicked download 1.18.12.1 at:")
    print(datetime.datetime.now())
    logger.warning('[LOG]:You clicked download 1.18.12.1')

def openweb4():
    webbrowser.open(url4,new=new)
    print("[LOG]:You clicked download 1.18.2.3 at:")
    print(datetime.datetime.now())
    logger.warning('[LOG]:You clicked download 1.18.2.3')

def openweb5():
    webbrowser.open(url5,new=new)
    print("[LOG]:You clicked download 1.18.1.2 at:")
    print(datetime.datetime.now())
    logger.warning('[LOG]:You clicked download 1.18.1.2')

def openweb6():
    webbrowser.open(url6,new=new)
    print("[LOG]:You clicked download 1.18 at:")
    print(datetime.datetime.now())
    logger.warning('[LOG]:You clicked download 1.18')

def openweb7():
    webbrowser.open(url7,new=new)
    print("[LOG]:You clicked download 1.18.31 at:")
    print(datetime.datetime.now())
    logger.warning('[LOG]:You clicked download 1.18.31')

def openweb8():
    webbrowser.open(url8,new=new)
    print("[LOG]:You clicked download 1.19 at:")
    print(datetime.datetime.now())
    logger.warning('[LOG]:You clicked download 1.19')


logger = logging.getLogger('Vlauncher')

handler = logging.FileHandler('VLauncher.json')

logger.addHandler(handler)

logger.warning('Versions loaded')
logger.warning('starting window (G=1024x1024,WT=Ctk,TH=dark,SDCT=blue)')


customtkinter.set_appearance_mode("dark")  
customtkinter.set_default_color_theme("blue")  

root_tk = customtkinter.CTk() 

root_tk.geometry("1024x1024")

root_tk.title("Minecraft Bedrock Version Manager")

button = customtkinter.CTkButton(master=root_tk, text="Download 1.19.00", command=openweb8)
button.place(relx=0.7, rely=0.1)

button = customtkinter.CTkButton(master=root_tk, text="Download 1.18.31", command=openweb7)
button.place(relx=0.4, rely=0.1)


button = customtkinter.CTkButton(master=root_tk, text="Download 1.18.30", command=openweb)
button.place(relx=0.4, rely=0.2)

button = customtkinter.CTkButton(master=root_tk, text="Download 1.18.12", command=openweb3)
button.place(relx=0.4, rely=0.3)

button = customtkinter.CTkButton(master=root_tk, text="Download 1.18.10", command=openweb2)
button.place(relx=0.4, rely=0.4)

button = customtkinter.CTkButton(master=root_tk, text="Download 1.18.2 ", command=openweb4)
button.place(relx=0.4, rely=0.5)

button = customtkinter.CTkButton(master=root_tk, text="Download 1.18.1 ", command=openweb5)
button.place(relx=0.4, rely=0.6)

button = customtkinter.CTkButton(master=root_tk, text="Download 1.18   ", command=openweb6)
button.place(relx=0.4, rely=0.7)


root_tk.mainloop()

logger.warning('App closed')

text = colored('App Closed!', 'red', attrs=['reverse', 'blink'])
  
print(text)

time.sleep(2)
