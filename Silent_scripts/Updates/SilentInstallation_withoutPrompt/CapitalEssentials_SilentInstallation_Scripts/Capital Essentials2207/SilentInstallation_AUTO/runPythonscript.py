import os
import subprocess
root_dir = os.getcwd()
path1=root_dir+"\Run_Applications"
EAD_AUTO_folder=path1.replace("\\","/")
exeTxtpath=EAD_AUTO_folder+"/VeSysExecutables.txt"
subprocess.call(['running_python_script.bat',EAD_AUTO_folder,exeTxtpath], shell=True)
