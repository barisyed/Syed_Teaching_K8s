import os
import glob
from pathlib import Path
import shutil
from colored import fg
colorR = fg('red')
colorB = fg('blue')
colorY = fg('yellow')
colorG = fg('green')
colorW = fg('white')

for root, dirs, files in os.walk(Path.home() / "Downloads\Latest_Builds\\"):
    for f in files:
        os.unlink(os.path.join(root, f))
    for d in dirs:
        shutil.rmtree(os.path.join(root, d))
print(colorG+"Folder Cleaned Successfully!")
print(colorW)
