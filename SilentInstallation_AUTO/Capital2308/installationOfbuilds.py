import os
import subprocess
import PreSetupForSelfInstallation
from colored import fg
colorR = fg('red')
colorB = fg('blue')
colorY = fg('yellow')
colorG = fg('green')
colorW = fg('white')
VariableNeedToPassforLogValidation=PreSetupForSelfInstallation.file # Variable to store the file for log validation
installation='yes'
if installation=='yes': # Check if installation is set to 'yes'
    def replace_line(Exes_filename, binFolderForExes):
        with open(Exes_filename) as file:
            lines = file.readlines() # Read all lines from the file
            line_number=1 # Set the line number to 1
        if (line_number <= len(lines)): # Check if the line number is within the range of lines in the file
            lines[line_number - 1] = binFolderForExes + "\\bin\\"+"\n" # Replace the specified line with the new value
            with open(Exes_filename, "w") as file:
                for line in lines:
                    file.write(line) # Write the modified lines back to the file
        else:
            print("Line", line_number, "not in file.") # Print a message if the specified line is not found
            print("File has", len(lines), "lines.") # Print the total number of lines in the file
    def switch(choice):
        if choice==1: # Check if choice is 1
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
        elif choice==2: # Check if choice is 2
            def listToString(s):
                str1 = " "
                return (str1.join(s))
            rootDir ='C:\\MentorGraphics'
            inputPath=PreSetupForSelfInstallation.path
            path=inputPath.replace('\\','/')
            arr = os.listdir(path)
            filename=arr[0]
            chshome_list=[]
            if '2020' in path:  # Check if '2020' is present in the path
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
            elif '2021' in path: # Check if '2021' is present in the path
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
            elif '2308' in path: # Check if '2308' is present in the path
                # Specify the file to search for in the root directory
                fileToSearch='Capital2308_996-official_Install'
                for relPath,dirs,files in os.walk(rootDir):
                    # Traverse the root directory and its subdirectories
                    l=listToString(files) # Convert the list of files to a single string
                    if(fileToSearch in l): # Check if the file to search for is present in the string
                        fullPath=os.path.join(rootDir,relPath) # Get the full path of the file
                        chshome_list.append(fullPath) # Append the full path to the chshome_list
                        chshome=chshome_list[0] # Get the first chshome path from the list
                chshome=chshome
                binFolderForExes= chshome
                replace_line(Exes_filename,binFolderForExes) # Call the replace_line function
                #print(filename,inputPath,chshome)
                subprocess.call(['SPbuildinstallation.bat',filename,inputPath,chshome]) # Run the ServicePack installation script
    global chshome
    Exes_filename = os.getcwd()+"\Run_Applications\CapitalExecutables.txt"
    # Get the current working directory and append the filename to get the full path
    choice=2 # Set the choice
    switch(choice) # Call the switch function with the specified choice
else:
    print("Skipped Installation....")
