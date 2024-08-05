This script is used to run Capital and VeSys executables automatically for EAD testing. This way, we don't need to check manually if an executable having an expired license runs or not.

Python version used- 3.9
To run this script, following installations are needed-
1. Download Python from https://www.python.org/downloads/
2. Go to https://visualstudio.microsoft.com/visual-cpp-build-tools/ and download build tools. During installation, select C++ build tools under Workloads tab.
3. Install psutil library by executing the following command from Python/Scripts- pip install psutil
Note- psutil cannot be installed without visual c++ build tools so the above installations must be done in the given order

CapitalExecutables.txt- The first line is the folder location where all the Capital executables are present. Make sure the path specified ends with '/'. Subsequent lines should contain the name of the executables to be tested. Each line must contain only one executable name. Also, there must not be any blank lines.

VeSysExecutables.txt- The first line is the folder location where all the VeSys executables are present. Make sure the path specified ends with '/'. Subsequent lines should contain the name of the executables to be tested. Each line must contain only one executable name. Also, there must not be any blank lines.

main.py- This script will read the path and executables from the above txt files and run each executable in the same order as specified in the file.

To run this script-
1. The license server should be up and running before executing this script
2. Open cmd from where main.py is stored
3. Execute the command- python -u main.py C:/Users/itcqa2/Desktop/EAD/CapitalExecutables.txt
   (Note- The path specified here should either contain ‘/’ or ‘\\’. Using ‘\’ will throw an error)
4. Similarly, specify the VeSysExecutables.txt file path to test VeSys executables
5. Once the task is completed, close CapitalManager or VeSysManager from Task Manager