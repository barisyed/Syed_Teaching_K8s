import os
Publisher=[]
Symbol=[]
Project=[]
# specify the folder path
folder_path = "C:\\MentorGraphics\\CapitalTemp"
def ExceptionChecking(Applicationlog):
    pathForApplicationLogs="C:\\MentorGraphics\\CapitalTemp\\"+Applicationlog
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
    if 'CapitalSymbol_itcqa2_' in file:
        Symbol.append(file)
    elif 'CapitalPublisher_itcqa2_' in file:
        Publisher.append(file)
    elif 'CapitalProject_itcqa2_' in file:
        Project.append(file)

ExceptionChecking(Symbol[-1])
ExceptionChecking(Publisher[-1])
ExceptionChecking(Project[-1])
