import os
Manager=[]
Symbol=[]
StopService=[]
Essentials=[]
# specify the folder path
folder_path = "C:\\MentorGraphics\\Vesys_Temp"
def ExceptionChecking(Applicationlog):
    pathForApplicationLogs="C:\\MentorGraphics\\Vesys_Temp\\"+Applicationlog
    with open(pathForApplicationLogs, 'r') as file:
        contents = file.read()
        if 'Exception' in contents:
            print('Exceptions are Observed')
        else:
            print('No Exceptions')

# use listdir() method to get all the files in the folder
files = os.listdir(folder_path)

# print the list of files
for file in files:
    if 'CapitalManagerEssentials_itcqa2_' in file:
        Manager.append(file)
    elif 'CapitalSymbolDesignerEssentials_itcqa2_' in file:
        Symbol.append(file)
    elif 'CapitalStopServicesEssentials_itcqa2_' in file:
        StopService.append(file)
    elif 'CapitalEssentials_itcqa2_' in file:
        Essentials.append(file)
        
#ExceptionChecking(Manager[-1])
ExceptionChecking(Symbol[-1])
ExceptionChecking(Essentials[-1])
#ExceptionChecking(StopService[-1])
