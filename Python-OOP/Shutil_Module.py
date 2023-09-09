import shutil
import os
# Copy only files
shutil.copy("shutil_Module.py", "shutil_Modul2.py")

# Copy Complete Directory
shutil.copytree("New_Folder","New_Folder2")


# Move file from one to another place
shutil.move("Access Modifiers.py","NewFolder/Access Modifiers.py")

# Help in delte directory
shutil.rmtree("NewFolder/Access Modifiers.py")

# Help in delte File
os.remove("shutil_Modul2")