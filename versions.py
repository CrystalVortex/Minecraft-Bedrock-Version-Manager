from tkinter import *
from tkinter.ttk import *
import webbrowser

root = Tk()

root.geometry('1024x1024')  


new = 1
url1 = "https://download2344.mediafire.com/ec85gea86keg/p5yxrsv39uvgdo0/Microsoft.MinecraftUWP_1.18.3004.0_x86__8wekyb3d8bbwe.Appx"

new = 2
url2 = "https://download2388.mediafire.com/n4u8hpavbxag/j3gn0szp5zriw6z/Microsoft.MinecraftUWP_1.18.1004.0_x86__8wekyb3d8bbwe.Appx"

new = 3
url3 = "https://download2391.mediafire.com/9oijpuvi4xag/zq0pcoqbsfbhvfw/Minecraft-1.18.12.1.Appx"

def openweb():
    webbrowser.open(url1,new=new)

def openweb2():
    webbrowser.open(url2,new=new)

def openweb3():
    webbrowser.open(url3,new=new)

Btn = Button(root, text = "Download 1.18.30 64 bit",command=openweb)
Btn.pack()

Btn = Button(root, text = "Download 1.18.12 64 bit",command=openweb3)
Btn.pack()

Btn = Button(root, text = "Download 1.18.10 64 bit",command=openweb2)
Btn.pack()

root.mainloop()
