import os
import shutil
import zipfile
from pathlib import Path
import datetime
from colored import fg
colorR = fg('red')
colorB = fg('blue')
colorY = fg('yellow')
colorG = fg('green')
colorW = fg('white')

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
    my_substring_beta = "-beta"
    my_substring_official = "-official"

    beta_substring_position = my_string.find(my_substring_beta)
    official_substring_position = my_string.find(my_substring_official)

    if beta_substring_position != -1 and beta_substring_position != 0:
        char_before_beta_substring = my_string[beta_substring_position - 1]
        if char_before_beta_substring.isdigit():  # Check if it's a digit
            return char_before_beta_substring  # Return the character before "-beta"

    if official_substring_position != -1 and official_substring_position != 0:
        char_before_official_substring = my_string[official_substring_position - 1]
        if char_before_official_substring.isdigit():  # Check if it's a digit
            return char_before_official_substring  # Return the character before "-official"

    # If neither "-beta" nor "-official" is found, return None
    return None
def refinedDirectory(file):
    string = file
    substring_beta = "-beta"
    substring_official = "-official"
    substring_capital = "Capital"
    
    checknumeric_beta = []
    checknumeric_official = []
    checkempty_beta = []
    checkempty_official = []
    
    try:
        position_beta = string.index(substring_beta)  # Find the position of substring "-beta" in the string
    except ValueError:
        position_beta = -1  # Substring "-beta" not found
    
    try:
        position_official = string.index(substring_official)  # Find the position of substring "-official" in the string
    except ValueError:
        position_official = -1  # Substring "-official" not found
    
    for i in range(len(substring_capital), position_beta if position_beta != -1 else len(string)):
        checknumeric_beta.append(string[i])  # Add characters between "Capital" and "-beta"
    
    # Check for non-digit and non-special characters for "-beta"
    for i in range(len(checknumeric_beta)):
        if checknumeric_beta[i].isdigit():
            continue
        elif '.' in checknumeric_beta[i] or '_' in checknumeric_beta[i] or 'P' in checknumeric_beta[i] or 'S' in checknumeric_beta[i]:
            continue
        else:
            checkempty_beta.append(checknumeric_beta[i])
    
    for i in range(len(substring_capital), position_official if position_official != -1 else len(string)):
        checknumeric_official.append(string[i])  # Add characters between "Capital" and "-official"
    
    # Check for non-digit and non-special characters for "-official"
    for i in range(len(checknumeric_official)):
        if checknumeric_official[i].isdigit():
            continue
        elif '.' in checknumeric_official[i] or '_' in checknumeric_official[i] or 'P' in checknumeric_official[i] or 'S' in checknumeric_official[i]:
            continue
        else:
            checkempty_official.append(checknumeric_official[i])
    
    if (len(checkempty_beta) == 0 or position_beta == -1) and (len(checkempty_official) == 0 or position_official == -1):
        return string  # If no special characters found for both "-beta" and "-official", return the original string
    
    return None  # If special characters found for either "-beta" or "-official", return None

def listdirs(rootdir):
    global Builds

    recent_folder = None
    recent_datetime = None

    for file1 in os.listdir(rootdir):
        file = refinedDirectory(file1)  # Get the refined directory name
        if type(file) == str:
            d = os.path.join(rootdir, file)
            k = stringBeforeOfficial(d)  # Get the numeric character before "-official"
            if type(k) is type(None):
                continue
            else:
                k = int(k)
            if os.path.isdir(d) and k:  # Check if it's a directory and k is not None
                if '2408' in d:      #TO BE CHANGED FOR UPGRATING TO NEXT VERSION
                    current_datetime = datetime.datetime.fromtimestamp(os.path.getctime(d))
                    if recent_datetime is None or current_datetime > recent_datetime:
                        recent_datetime = current_datetime
                        recent_folder = d

    if recent_folder:
        if Builds:
            Builds[-1] = recent_folder  # Update the recently created folder at the -1 index of the list
        else:
            Builds.append(recent_folder)  # If Builds is empty, add the recent folder to the list
        # print(f"Recently created folder: {recent_folder}")
    else:
        print(colorR+"No valid build found.")
        print(colorW)



    global BuildZipPath
    BuildZipPath=Builds[-1]+'\Win64\\'+BuildZipName() # Get the path of the build zip file
    src_path = BuildZipPath
    dst_path = downloads_path
    shutil.copy(src_path, dst_path) # Copy the build zip file to the downloads path
    print(colorG+'Files Copied Successfully!')
    print(colorW)

print(colorR+"!!!ENSURE THAT THE DATABASE IS RUNNING, IF NOT RUNNING PLEASE START BEFORE INSTALLATION!!!")
print()
print(colorW)
print(colorY+"Fetching Build.........")
print(colorW)
rootdir = r'\\inh.india.mentorg.com\dfs\nobackup\iesd_release\UNReleased\iterationReleases\CHS_Iteration_rel\Capital'
listdirs(rootdir) # Call the function to list directories
#print(BuildZipPath)
CreateFolderForBuildExtraction() # Create a folder for extracting the build contents
BuildZipExtraction() # Extract the build zip file
RemoveCopiedBuildZip()# Remove the copied build zip file
print(colorY+"Installing.........")
print(colorW)







	

