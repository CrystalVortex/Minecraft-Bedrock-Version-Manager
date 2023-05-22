import customtkinter #makes tkinter's ui look 100x better

from lib.downloader.bedrock.versions import Versions # for getting links to download an appx

import tkinter # gui window thing

from lib import log4py # a custom made logging module, find it in lib/log4py.py

import wget # Used to download file

import threading # create a thread to make sure it wget.download() (for downloading a file) does not freeze the gui/window

from tkinter import messagebox # To tell you some info

import webbrowser # Used for going to the github page to check for updates




# enable a log file for log4py
log4py.LOG_FILE_ENABLED(False,"bedrocklauncherlog") 

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue")  

app = customtkinter.CTk() 
app.geometry("700x340")

app.title("MCBE Version Launcher 7.2") 



def download_zero_five():
    def r(): 
        log4py.INFO("Downloading 1.19.0.5...")

        version = Versions.get_by_version("1.19.0.5")
        log4py.SUCCESS(version.uri)
        wget.download(version.uri)
        log4py.INFO("\n")
        log4py.SUCCESS("Download complete")
    thread = threading.Thread(target=r)
    thread.start()
    messagebox.showinfo("See download progress","Check the console aka terminal to see download progress!")

def download_fifone_one():
    def r(): 
        log4py.INFO("Downloading 1.19.51.1...")

        version = Versions.get_by_version("1.19.51.1")
        log4py.SUCCESS(version.uri)
        wget.download(version.uri)
        log4py.INFO("\n")
        log4py.SUCCESS("Download complete")
    thread = threading.Thread(target=r)
    thread.start()
    messagebox.showinfo("See download progress","Check the console aka terminal to see download progress!")

def download_ten():
    def r(): 
        log4py.INFO("Downloading 1.19.10...")

        version = Versions.get_by_version("1.19.10.3")
        log4py.SUCCESS(version.uri)
        wget.download(version.uri)
        log4py.INFO("\n")
        log4py.SUCCESS("Download complete")
    thread = threading.Thread(target=r)
    thread.start()
    messagebox.showinfo("See download progress","Check the console aka terminal to see download progress!")


def eighty_ot():
    def r():
        log4py.INFO("Downloading 1.19.80.2...")
        version = Versions.get_by_version("1.19.80.2")
        log4py.SUCCESS(version.uri)
        wget.download(version.uri)
        log4py.INFO("\n")
        log4py.SUCCESS("Download complete")
    thread = threading.Thread(target=r)
    thread.start()



def github():
    webbrowser.open_new_tab("https://github.com/CrystalVortex/Minecraft-Bedrock-Version-Manager")


button = customtkinter.CTkButton(master=app, text="Download 1.19.0.5", command=download_zero_five)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Download 1.19.51.1", command=download_fifone_one)
button.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Download 1.19.10", command=download_ten)
button.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

button = customtkinter.CTkButton(master=app, text="Download 1.19.80.02", command=eighty_ot)
button.place(relx=0.10, rely=0.2, anchor=tkinter.CENTER)


button = customtkinter.CTkButton(master=app, text="Check for updates", command=github)
button.place(relx=0.10, rely=0.5, anchor=tkinter.CENTER)


app.mainloop()
