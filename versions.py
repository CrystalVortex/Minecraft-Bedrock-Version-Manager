from email.utils import localtime

from tkinter import *

import tkinter

from tkinter import ttk

from tkinter.ttk import *

import webbrowser

import datetime

import time

import logging


logger = logging.getLogger('Vlauncher')

handler = logging.FileHandler('VLauncher.log')

logger.addHandler(handler)

print("Starting Application...")

logger.warning('Logging started')

logger.warning('[LOG]:Starting Application...')

time.sleep(1)

print("[LOG]:Application started")

logger.warning('[LOG]:Application started')

logger.warning('[LOG]:Window Name:Minecraft Version Launcher (412x312)')

new = 1
url1 = "https://download2344.mediafire.com/7lo7d4se8m0g/p5yxrsv39uvgdo0/Microsoft.MinecraftUWP_1.18.3004.0_x86__8wekyb3d8bbwe.Appx"

new = 2
url2 = "https://download2265.mediafire.com/13ngbxye53ng/j3gn0szp5zriw6z/Microsoft.MinecraftUWP_1.18.1004.0_x86__8wekyb3d8bbwe.Appx"

new = 3
url3 = "https://download2391.mediafire.com/vembjkpt9kug/zq0pcoqbsfbhvfw/Minecraft-1.18.12.1.Appx"

new = 4 
url4 = "https://download2340.mediafire.com/8vts0fml23gg/5o9wz0ltbb6xv5x/Minecraft-1.18.2.3.Appx"

new = 5
url5 = "https://download2267.mediafire.com/n1susudxioqg/kmelqlxa658388m/Minecraft-1.18.1.2.Appx"

new = 6 
url6 = "https://download2390.mediafire.com/wa607c69vbug/wjekuyje36e51ql/Minecraft-1.18.0.2.Appx"
new = 7 
url7 = "https://download2329.mediafire.com/qxrgkl0b0gkg/tjsgntidc54rru4/Minecraft-1.18.31.4.Appx"


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

print("[LOG]:Versions loaded")
logger.warning('[LOG]:Versions loaded')

root = Tk()

root.title('Minecraft BE Version Launcher')

root.geometry('412x312')

main_frame= Frame(root)
main_frame.pack()

a_canvas = Canvas(main_frame)
a_canvas.pack(side=LEFT, fill=BOTH, expand=1)

b_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=a_canvas.yview)
b_scrollbar.pack(side=RIGHT,fill=Y)

a_canvas.configure(yscrollcommand=b_scrollbar.set)
a_canvas.bind('<Configure>', lambda e: a_canvas.configure(scrollregion= a_canvas.bbox("all")))

second_frame = Frame(a_canvas)

a_canvas.create_window((11,11), window=second_frame, anchor="nw")



Label(second_frame, text = 'Minecraft BE Version Launcher', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)

root.title('Minecraft Version Launcher')

photo = PhotoImage(file = r"d.png")


Label(second_frame, text = '1.18.31', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)

Button(second_frame, text = '1.18.31', command=openweb7, image = photo).pack(side = TOP)

Label(second_frame, text = '1.18.30', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)

Button(second_frame, text = '', command=openweb, image = photo).pack(side = TOP)

Label(second_frame, text = '1.18.12', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)

Button(second_frame, text = '', command=openweb3, image = photo).pack(side = TOP)

Label(second_frame, text = '1.18.10', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)

Button(second_frame, text = '', command=openweb2, image = photo).pack(side = TOP)

Label(second_frame, text = '1.18.2.3', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)

Button(second_frame, text = '', command=openweb4, image = photo).pack(side = TOP)

Label(second_frame, text = '1.18.1.2', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)

Button(second_frame, text = '1.18.1.2', command=openweb5, image = photo).pack(side = TOP)

Label(second_frame, text = '1.18', font =(
  'Verdana', 15)).pack(side = TOP, pady = 10)

Button(second_frame, text = '1.18', command=openweb6, image = photo).pack(side = TOP)

mainloop()



print("[LOG]:Application closed!")

logger.warning('[LOG]:Application closed!')

time.sleep(1)

print("[LOG]:Press enter to continue")

logger.warning('[LOG]:Press enter to continue')

input()

logger.warning('[LOG]:Application closed...')
