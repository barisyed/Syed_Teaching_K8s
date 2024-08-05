import os
import glob
import installationOfbuilds

SP_Iteration=installationOfbuilds.VariableNeedToPassforLogValidation
#print(SP_Iteration)


string_original=SP_Iteration
string1='install_capitalessentials_'
string2='_win64.exe'
r1=string_original.replace(string1,'')
r2=r1.replace(string2,'')
#print(r2)




path=r"C:\\MentorGraphics"
l=[]
l=os.listdir(path)
for root, dirs, files in os.walk(path):
    for f in files:
        l.append(os.path.join(root,f))
le=len(l)
for i in range(le):
    if r2 in l[i]:
        requiredLogFilepath=l[i]

print("Log File Available at:", requiredLogFilepath)
        


# Open the file in read-only mode
def CheckingWarningsFatalerrorsNonFatalerrors(line_number):
    with open(requiredLogFilepath, 'r') as file:
        # Read all the lines in the file into a list
        lines = file.readlines()
        
        # Get the specific line you want and store it in a new list
        # change this to the line number you want
        specific_line = [lines[line_number - 1]]
        
        # Print the specific line
        return specific_line

warnings=CheckingWarningsFatalerrorsNonFatalerrors(85)
NonFatalErrors=CheckingWarningsFatalerrorsNonFatalerrors(86)
FatalErrors=CheckingWarningsFatalerrorsNonFatalerrors(87)
if '0 Warnings\n' in warnings and '0 NonFatalErrors\n' in NonFatalErrors and '0 FatalErrors\n' in FatalErrors:
    print('No Warnings, No NonFatalErrors, No Fatal Errors')
InstalledVersion=''.join(CheckingWarningsFatalerrorsNonFatalerrors(63))
GettingInstalledVersion=InstalledVersion.split()
print(GettingInstalledVersion[-1], "- Installed Successfully!")
print(" ")
print("Validating the Applications.........")
