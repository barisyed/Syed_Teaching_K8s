import os
from pathlib import Path

def create_folder(downloads_path):
    # Check if the folder already exists
    if not os.path.exists(downloads_path):
        # If the folder does not exist, create it
        os.makedirs(downloads_path)
        #print("Folder created successfully!")
    else:
        pass
        #print("Folder already exists.")

# Specify the path where you want to create the folder
downloads_path = str(Path.home() / "Downloads\Latest_Builds\\")

# Call the function to create the folder
create_folder(downloads_path)
