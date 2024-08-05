import subprocess
import sys

import psutil
import time


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
    time.sleep(30)
    if isApplicationRunning(app):
        print(app + ' is running')
    else:
        print(app + ' is not running as it could not be licensed')
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
    print('\nStarting ' + appName)
    runApplication(path, appName)
