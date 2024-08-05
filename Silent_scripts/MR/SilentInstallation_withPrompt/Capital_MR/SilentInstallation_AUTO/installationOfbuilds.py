import os
import subprocess
import PreSetupForSelfInstallation
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
    def BaseBuildInstallation():
        inputPath=PreSetupForSelfInstallation.path
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
        #replace_line(Exes_filename,binFolderForExes)
        subprocess.call(['basebuildinstallation.bat',filename,inputPath,chshome])
        print(filename,inputPath,chshome)
        print("Installing.........")
    global chshome
    BaseBuildInstallation() 
else:
    print("Skipped Installation....")
