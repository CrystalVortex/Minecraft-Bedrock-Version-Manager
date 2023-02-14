from termcolor import colored

from colorama import init

import datetime

dt = datetime.datetime.now()

init(strip=False)

version = "Log4Py Version 0.1"

def LOG_FILE_ENABLED(mode, log_file_name):
    global enabled
    enabled = False
    if mode == True:
        global file
        enabled = True
        file = open(f"{log_file_name}.log", "a")


def INFO(log):
    print(f"[LOG] [INFO] {dt} : {log}")
    if enabled == True:
        file.write(f"[LOG] [INFO] {dt} : {log}\n")


def WARNING(log):
    print(colored(f'[LOG] [WARNING] {dt}: {log}', 'yellow'))
    if enabled == True:
        file.write(f"[LOG] [WARNING] {dt} : {log}\n")

def ERROR(log):
    print(colored(f'[LOG] [ERROR] {dt}: {log}', 'red'))
    if enabled == True:
        file.write(f"[LOG] [ERROR] {dt} : {log}\n")

def DEBUG(log):
    print(colored(f'[LOG] [DEBUG] {dt}: {log}', 'magenta'))
    if enabled == True:
        file.write(f"[LOG] [DEBUG] {dt} : {log}\n")

def SUCCESS(log):
    print(colored(f'[LOG] [SUCCESS] {dt}: {log}', 'green'))
    if enabled == True:
        file.write(f"[LOG] [SUCCESS] {dt} : {log}\n")


