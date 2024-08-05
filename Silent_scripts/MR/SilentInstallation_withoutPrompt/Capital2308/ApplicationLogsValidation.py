import os
#these lists are to store the log files according to respective application  
CIS=[]
Manager=[]
LogicDesigner=[]
ProjectManager=[]
StopService=[]
# specify the folder path
folder_path = "C:\\MentorGraphics\\CapitalTemp"  #this filepath helps in getting the application logs in Temp location...
def ExceptionChecking(Applicationlog):
    pathForApplicationLogs="C:\\MentorGraphics\\CapitalTemp\\"+Applicationlog
    with open(pathForApplicationLogs, 'r') as file:
        contents = file.read()
        if 'Exception' in contents:
            print('Exceptions are observed')
        else:
            print('No exceptions')

# use listdir() method to get all the files in the folder
files = os.listdir(folder_path)

#segregates the logs...
for file in files:
    if 'CapitalIntegrationServer_itcqa2_' in file:
        CIS.append(file)
    elif 'CapitalLogicDesigner_itcqa2_' in file:
        LogicDesigner.append(file)
    elif 'CapitalManager_itcqa2_' in file:
        Manager.append(file)
    elif 'CapitalProjectManager_itcqa2_' in file:
        ProjectManager.append(file)
    elif 'CapitalStopServices_itcqa2_' in file:
        StopService.append(file)
#filters the latest logs
ExceptionChecking(CIS[-1])
ExceptionChecking(Manager[-1])
ExceptionChecking(LogicDesigner[-1])
ExceptionChecking(ProjectManager[-1])
ExceptionChecking(StopService[-1])
