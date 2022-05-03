
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import*
import sys
from email.utils import localtime
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize  
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


print("[LOG]:Application started")

logger.warning('[LOG]:Application started')

logger.warning('[LOG]:Window Name:Minecraft Version Launcher (512x512)')

print("[LOG]:Warning, you are using the testing version (mostly broken or incomplete)")





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


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        # set the title of main window
        self.setWindowTitle('Minecraft BE Version Manager')
        # set the size of window
        self.Width = 800
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)

        self.setStyleSheet("background-color: #1e1e1e")
        pybutton = QPushButton('Download 1.18.31(Latest)', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(200,100)
        pybutton.move(0, 0)
        pybutton.setStyleSheet("border-radius: 8px")
    def clickMethod(self):
        webbrowser.open(url7,new=new)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())
