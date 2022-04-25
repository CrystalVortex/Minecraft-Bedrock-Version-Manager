from tkinter import *
from tkinter.ttk import *
import webbrowser

ws = Tk()

ws.title('Minecraft Version Launcher')

ws.geometry('512x512')



new = 1
url1 = "https://download2344.mediafire.com/ec85gea86keg/p5yxrsv39uvgdo0/Microsoft.MinecraftUWP_1.18.3004.0_x86__8wekyb3d8bbwe.Appx"

new = 2
url2 = "https://download2388.mediafire.com/n4u8hpavbxag/j3gn0szp5zriw6z/Microsoft.MinecraftUWP_1.18.1004.0_x86__8wekyb3d8bbwe.Appx"

new = 3
url3 = "https://download2391.mediafire.com/9oijpuvi4xag/zq0pcoqbsfbhvfw/Minecraft-1.18.12.1.Appx"

new = 4 
url4 = "https://download2340.mediafire.com/mgy9tfbk8yvg/5o9wz0ltbb6xv5x/Minecraft-1.18.2.3.Appx"

new = 5
url5 = "https://download2267.mediafire.com/n1susudxioqg/kmelqlxa658388m/Minecraft-1.18.1.2.Appx"

new = 6 
url6 = "https://download2390.mediafire.com/wa607c69vbug/wjekuyje36e51ql/Minecraft-1.18.0.2.Appx"



def openweb():
    webbrowser.open(url1,new=new)

def openweb2():
    webbrowser.open(url2,new=new)

def openweb3():
    webbrowser.open(url3,new=new)

def openweb4():
    webbrowser.open(url4,new=new)

def openweb5():
    webbrowser.open(url5,new=new)

def openweb6():
    webbrowser.open(url6,new=new)



Btn = Button(ws, text = "Download 1.18.30 64 bit",command=openweb)
Btn.pack()

Btn = Button(ws, text = "Download 1.18.12 64 bit",command=openweb3)
Btn.pack()

Btn = Button(ws, text = "Download 1.18.10 64 bit",command=openweb2)
Btn.pack()

Btn = Button(ws,text = "Download 1.18.2.3 64 bit",command=openweb4)
Btn.pack()

Btn = Button(ws,text = "Download 1.18.1 64 bit",command=openweb5)
Btn.pack()

Btn = Button(ws,text= "Download 1.18 64 bit",command=openweb6)
Btn.pack()



ws.mainloop()
