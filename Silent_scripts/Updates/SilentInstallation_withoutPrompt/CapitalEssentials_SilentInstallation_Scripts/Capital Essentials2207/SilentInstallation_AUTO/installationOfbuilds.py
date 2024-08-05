import os
import subprocess
import PreSetupForSelfInstallation
VariableNeedToPassforLogValidation=PreSetupForSelfInstallation.file
installation='yes'
if installation=='yes':
    def replace_line(Exes_filename, binFolderForExes):
        with open(Exes_filename) as file:
            lines = file.readlines()
            line_number=1
        if (line_number <= len(lines)):
            lines[line_number - 1] = binFolderForExes + "\\bin\\"+"\n"
            with open(Exes_filename, "w") as file:
                for line in lines:
                    file.write(line)
        else:
            print("Line", line_number, "not in file.")
            print("File has", len(lines), "lines.")
    def switch(choice):
        if choice==1:
            inputPath=input('enter file path')
            path=inputPath.replace('\\','/')
            foldername_list=[]
            arr = os.listdir(path)
            filename=arr[0]
            for i in path[::-1]:
                if i != '/':
                    foldername_list.append(i)
                else:
                    break
            listToStr = ' '.join([str(elem) for elem in foldername_list])
            rev_foldername=listToStr.replace(" ", "")
            org_foldername=rev_foldername[::-1]
            firstremoval=org_foldername.replace("install_","")
            secondremoval=firstremoval.replace("_win64","")
            chshome="C:\\MentorGraphics\\"+secondremoval
            binFolderForExes= chshome
            replace_line(Exes_filename,binFolderForExes)
            subprocess.call(['basebuildinstallation.bat',filename,inputPath,chshome])
        elif choice==2:
            def listToString(s):
                str1 = " "
                return (str1.join(s))
            rootDir ='C:\\MentorGraphics'
            inputPath=PreSetupForSelfInstallation.path
            path=inputPath.replace('\\','/')
            #print(path)
            arr = os.listdir(path)
            filename=arr[0]
            chshome_list=[]
            if '2020' in path:
                fileToSearch='Capital2020.1.526-official_Install'
                for relPath,dirs,files in os.walk(rootDir):
                    l=listToString(files)
                    if(fileToSearch in l):
                        fullPath=os.path.join(rootDir,relPath)
                        chshome_list.append(fullPath)
                        chshome=chshome_list[0]
                chshome=chshome
                binFolderForExes= chshome
                replace_line(Exes_filename,binFolderForExes)
                #print(filename,inputPath,chshome)
                subprocess.call(['SPbuildinstallation.bat',filename,inputPath,chshome])
            elif '2021' in path:
                fileToSearch='Capital2021.1.722-official_Install'
                for relPath,dirs,files in os.walk(rootDir):
                    l=listToString(files)
                    if(fileToSearch in l):
                        fullPath=os.path.join(rootDir,relPath)
                        chshome_list.append(fullPath)
                        chshome=chshome_list[0]
                chshome=chshome
                binFolderForExes= chshome
                replace_line(Exes_filename,binFolderForExes)
                #print(filename,inputPath,chshome)
                subprocess.call(['SPbuildinstallation.bat',filename,inputPath,chshome])
            elif True:
                fileToSearch='Capital_Essentials2207_586-official_Install'
                for relPath,dirs,files in os.walk(rootDir):
                    l=listToString(files)
                    if(fileToSearch in l):
                        fullPath=os.path.join(rootDir,relPath)
                        chshome_list.append(fullPath)
                        chshome=chshome_list[0]
                chshome=chshome
                binFolderForExes= chshome
                replace_line(Exes_filename,binFolderForExes)
                #print(filename,inputPath,chshome)
                subprocess.call(['SPbuildinstallation.bat',filename,inputPath,chshome])
    global chshome
    Exes_filename = os.getcwd()+"\Run_Applications\VeSysExecutables.txt"
    #print("To install base build enter-->'1'")
    #print("To install ServicePack enter-->'2'")
    choice=2
    switch(choice)
    #print('Zero Warnings - from install log file')
    #print('Run smoke test script')
else:
    print("Skipped Installation....")
