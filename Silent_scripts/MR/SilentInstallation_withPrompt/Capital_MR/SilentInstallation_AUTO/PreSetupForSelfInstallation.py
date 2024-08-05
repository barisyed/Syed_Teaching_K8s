import os
import shutil
import zipfile
from pathlib import Path
import sys
import time

Builds=[] # List to store build paths

# Set the downloads path to the user's home directory followed by "Downloads\Latest_Builds\"
global downloads_path
downloads_path = str(Path.home() / "Downloads\Latest_Builds\\")
def BuildZipExtraction():
    # Extract the contents of the build zip file
    with zipfile.ZipFile(downloads_path +'\\'+ BuildZipName() ) as zip_ref:
        zip_ref.extractall(downloads_path +'\\'+ BuildZipName().replace('.zip',''))
def CreateFolderForBuildExtraction():
    global path
    # Create a folder for extracting the build contents
    path = downloads_path+'\\' + BuildZipName().replace('.zip','')
    try:
    	os.mkdir(path) # Create the folder
    except OSError as error:
    	print(error)
def RemoveCopiedBuildZip():
    global file
    file = BuildZipName()
    location=downloads_path
    path = os.path.join(location, file)
    os.remove(path) # Remove the copied build zip file
def BuildZipName():
    entries = os.listdir(Builds[-1]+'\Win64\\')
    for i in range(len(entries)):
        if '.zip' in entries[i]:
            return entries[i] # Return the name of the first entry in the "Win64" subdirectory
        else:
            continue
def stringBeforeOfficial(d):
    my_string = d
    my_substring = "-beta"
    substring_position = my_string.find(my_substring)
    if substring_position != -1 and substring_position != 0:
        char_before_substring = my_string[substring_position-1]
        if char_before_substring.isdigit(): # Check if it's a digit
            return char_before_substring # Return the character before "-official"
def refinedDirectory(file):
    string = file
    substring0 = "-beta"
    substring1 = len("Capital")
    checknumeric = []
    checkempty = []
    try:
        position0 = string.index(substring0) # Find the position of substring0 ("-official") in the string
    except ValueError:
        return None  # Substring not found, return None
    for i in range(substring1, position0):
        checknumeric.append(string[i]) # Add characters between substring1 ("Capital") and position0 ("-official")
    for i in range(len(checknumeric)):
        if checknumeric[i].isdigit(): # Check if it's a digit
            continue
        elif '.' in checknumeric[i] or '_' in checknumeric[i] or 'P' in checknumeric[i] or 'S' in checknumeric[i]:
            continue  # Skip if it contains special characters
        else:
            checkempty.append(checknumeric[i]) # Add non-digit and non-special characters
    if len(checkempty) == 0:
        return string   # If no special characters found, return the original string

def listdirs(rootdir):
    for file1 in os.listdir(rootdir):
        file=refinedDirectory(file1) # Get the refined directory name
        if type(file) == str:
            d = os.path.join(rootdir, file)
            k=stringBeforeOfficial(d) # Get the numeric character before "-official"
            if type(k) is type(None):
                continue
            else:
                k=int(k)
            if os.path.isdir(d) and k: # Check if it's a directory and k is not None
                if RequiredBuildNumber in d:
                    Builds.append(d) # Add the build path to the list
                    #print(d)
                
            if RequiredBuildNumber not in d:
                pass
                    
        elif type(file) is type(None):
            continue
                #listdirs(d)
        
    if not Builds:
        print("Build Not Found!")
        sys.exit()
    global BuildZipPath
    BuildZipPath=Builds[-1]+'\Win64\\'+BuildZipName() # Get the path of the build zip file
    src_path = BuildZipPath
    dst_path = downloads_path
    shutil.copy(src_path, dst_path) # Copy the build zip file to the downloads path
    print('File Copied Successfully!')
    time.sleep(5)
    print("Preparing For Installation.........")




RequiredBuildNumber=input("Enter the Required Main Release Build Number: ")
time.sleep(3)
print("Fetching Build.........")
rootdir = r'\\inh.india.mentorg.com\dfs\nobackup\iesd_release\UNReleased\iterationReleases\CHS_Iteration_rel\Capital'
listdirs(rootdir) # Call the function to list directories
#print(BuildZipPath)
CreateFolderForBuildExtraction() # Create a folder for extracting the build contents
BuildZipExtraction() # Extract the build zip file
RemoveCopiedBuildZip() # Remove the copied build zip file






	

