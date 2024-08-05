import os
import shutil
import zipfile
import datetime
from pathlib import Path
import time

Builds=[]
global downloads_path
downloads_path = str(Path.home() / "Downloads\Latest_Builds\\")
def latestEXEfetch():
    folder_path = downloads_path
    files = os.listdir(folder_path)

    latest_file = ""
    latest_time = datetime.datetime.fromtimestamp(0)

    # Loop through the list of files and check each file's creation time
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        file_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        
        if file_time > latest_time:
            latest_file = file_name
            latest_time = file_time


    return latest_file

def BuildZipName():
    entries = os.listdir(Builds[-1]+'\Win64\\')
    return entries[0]
def stringBeforeOfficial(d):
    my_string = d
    my_substring = "-beta"
    substring_position = my_string.find(my_substring)
    if substring_position != -1 and substring_position != 0:
        char_before_substring = my_string[substring_position-1]
        if char_before_substring.isdigit():
            return char_before_substring
        
def listdirs(rootdir):
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        k=stringBeforeOfficial(d)
        if type(k) is type(None):
            continue
        else:
            k=int(k)
        if os.path.isdir(d) and k:
            if '2207' in d:
                Builds.append(d)
                #listdirs(d)
    global BuildZipPath
    BuildZipPath=Builds[-1]+'\Win64\\'+BuildZipName()
    src_path = BuildZipPath
    dst_path = downloads_path
    shutil.copy(src_path, dst_path)
    print('Files Copied Successfully!')

print("Fetching Build.........")    
rootdir = r'\\inh.india.mentorg.com\dfs\nobackup\iesd_release\UNReleased\iterationReleases\CHS_Iteration_rel\CapitalEssentials'
listdirs(rootdir)
#print(BuildZipPath)
#CreateFolderForBuildExtraction()
#BuildZipExtraction()
#RemoveCopiedBuildZip()
print("Installing.........")
path=(downloads_path)
file=(latestEXEfetch())
#print(path)





	

