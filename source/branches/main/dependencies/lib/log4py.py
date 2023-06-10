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
    print(f"[LOG-MBVL] [INFO] {dt} : {log}")
    if enabled == True:
        file.write(f"[LOG-MBVL] [INFO] {dt} : {log}\n")


def WARNING(log):
    print(colored(f'[LOG-MBVL] [WARNING] {dt}: {log}', 'yellow'))
    if enabled == True:
        file.write(f"[LOG-MBVL] [WARNING] {dt} : {log}\n")

def ERROR(log):
    print(colored(f'[LOG-MBVL] [ERROR] {dt}: {log}', 'red'))
    if enabled == True:
        file.write(f"[LOG-MBVL] [ERROR] {dt} : {log}\n")

def DEBUG(log):
    print(colored(f'[LOG-MBVL] [DEBUG] {dt}: {log}', 'magenta'))
    if enabled == True:
        file.write(f"[LOG-MBVL] [DEBUG] {dt} : {log}\n")

def SUCCESS(log):
    print(colored(f'[LOG-MBVL] [SUCCESS] {dt}: {log}', 'green'))
    if enabled == True:
        file.write(f"[LOG-MBVL] [SUCCESS] {dt} : {log}\n")


