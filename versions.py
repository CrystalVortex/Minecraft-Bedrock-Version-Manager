from tkinter import *
from tkinter.ttk import *
import webbrowser

root = Tk()

root.geometry('1024x1024')  


new = 1
url1 = "https://download2344.mediafire.com/ec85gea86keg/p5yxrsv39uvgdo0/Microsoft.MinecraftUWP_1.18.3004.0_x86__8wekyb3d8bbwe.Appx"

new = 2
url2 = "https://download2388.mediafire.com/n4u8hpavbxag/j3gn0szp5zriw6z/Microsoft.MinecraftUWP_1.18.1004.0_x86__8wekyb3d8bbwe.Appx"



def openweb():
    webbrowser.open(url1,new=new)

def openweb2():
    webbrowser.open(url2,new=new)

Btn = Button(root, text = "Download 1.18.30 (x86)",command=openweb)
Btn.pack()

Btn = Button(root, text = "Download 1.18.10 (x86)",command=openweb2)
Btn.pack()

root.mainloop()
