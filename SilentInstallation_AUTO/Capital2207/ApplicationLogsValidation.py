import os
from colored import fg
colorR = fg('red')
colorB = fg('blue')
colorY = fg('yellow')
colorG = fg('green')
colorW = fg('white')
LogicDesigner=[]
Manager=[]
HarnessDesigner=[]
CIS=[]
Integrator=[]
# specify the folder path
folder_path = "C:\\MentorGraphics\\CapitalTemp"
def ExceptionChecking(Applicationlog):
    pathForApplicationLogs="C:\\MentorGraphics\\CapitalTemp\\"+Applicationlog
    with open(pathForApplicationLogs, 'r', encoding='latin-1') as file:
        contents = file.read()
        if 'Exception' in contents:
            print(colorR+'Exceptions are Observed in '+Applicationlog)
            print(colorW)
        else:
            print(colorG+'No Exceptions')
            print(colorW)

# use listdir() method to get all the files in the folder
files = os.listdir(folder_path)

# print the list of files
for file in files:
    if 'CapitalLogicDesigner_itcqa2_' in file:
        LogicDesigner.append(file)
    elif 'CapitalManager_itcqa2_' in file:
        Manager.append(file)
    elif 'CapitalHarnessDesigner_itcqa2_' in file:
        HarnessDesigner.append(file)
    elif 'CapitalIntegrationServer_itcqa2_' in file:
        CIS.append(file)
    elif 'CapitalSystemsIntegrator_itcqa2_' in file:
        Integrator.append(file)


ExceptionChecking(CIS[-1])
ExceptionChecking(LogicDesigner[-1])
ExceptionChecking(Manager[-1])
ExceptionChecking(HarnessDesigner[-1])
ExceptionChecking(Integrator[-1])
