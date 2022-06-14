import sys


from PyQt5.QtWidgets import *


from PyQt5.QtWebEngineWidgets import *

from PyQt5.QtCore import *

import time

import os

import subprocess

subprocess.call('start WS.exe', shell=True)

time.sleep(2)


class Window(QMainWindow):

    
    def __init__(self):
        
        super(Window,self).__init__()

        
        self.browser = QWebEngineView()

        
        self.browser.setUrl(QUrl('http://localhost:4748'))

        
        self.setCentralWidget(self.browser)

        
        
        self.showMaximized()


MyApp = QApplication(sys.argv)


QApplication.setApplicationName('Minecraft Bedrock Version Launcher')


window = Window()


MyApp.exec_()


