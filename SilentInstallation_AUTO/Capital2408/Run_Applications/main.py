import subprocess
import sys

import psutil
import time
from colored import fg
colorR = fg('red')
colorB = fg('blue')
colorY = fg('yellow')
colorG = fg('green')
colorW = fg('white')


def isApplicationRunning(applicationName):
    for app in psutil.process_iter():
        try:
            if applicationName.lower() == app.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def runApplication(cmd, app):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    time.sleep(40)
    if isApplicationRunning(app):
        print(colorG+app + ' is running')
        print(colorW)
    else:
        print(colorR+app + ' is not running as it could not be licensed')
        print(colorW)
    if app != 'CapitalManager.exe' and app != 'VeSysManager.exe' and app != 'CapitalIntegrationServer.exe':
        process.kill()


file = open(sys.argv[1], "r")
List = file.readlines()
filePath = List[0].strip()
i = 1
while i < len(List):
    appName = List[i].strip()
    i += 1
    path = filePath + appName + " -suppressgui"
    print(colorY+'\nStarting ' + appName)
    print(colorW)
    runApplication(path, appName)
