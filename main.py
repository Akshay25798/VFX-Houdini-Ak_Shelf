import os
import shutil
import platform

title="Ak Shelf - Copying scripts to user's houdini folder."
msg = "Developed by Akshay Kumar"
donotCopy = [".git", "Win_exe.bat", "pythonExec.py", "Linux_exe.sh", "Ak.shelf", "README.md"]
donotCopy123 = [".git", "Win_exe.bat", "pythonExec.py", "Linux_exe.sh", "Ak.shelf", "README.md", "123.py"]
osName = platform.system()
if osName=="Linux":
    slash = r"/"
    user = os.getenv("USERNAME")
    baseFolder = "~/" #user houdini folder
else:
    slash = r"\\"
    user = os.getenv("USERNAME")
    baseFolder = r"C:\Users\%s\Documents"%user #user houdini folder


allFolders = os.listdir(baseFolder)

houdiniVer = []
for folder in allFolders:
    if folder.startswith("houdini"):
        houdiniVer.append(folder)

for houdini in houdiniVer:
    scriptsFolder = slash.join([baseFolder, houdini, "scripts"])
    toolbarFolder = slash.join([baseFolder, houdini, "toolbar"])
    if not os.path.exists(scriptsFolder):
        os.makedirs(scriptsFolder)

currentFolder = os.path.dirname(os.path.realpath(__file__))
scripts = os.listdir(currentFolder)
print("-------------------------------"+title+"------------------------------\n")
print("All scripts : " + str(scripts) + "\n\n\n")
print("There is 123.py script also if you are allready using 123.py please select 'NO'.")
userInput = input("Want to copy 123.py also [Yes/No] : ").upper()
while userInput not in ["YES", "NO"]:
    userInput = input("Want to copy 123.py also [Yes/No] : ").upper()

for script in scripts:
    if userInput=="YES":
        if script not in donotCopy:
            scriptPath = slash.join([currentFolder, script])
            shutil.copy(scriptPath, scriptsFolder) #copy python scripts to user houdini foler
            print(scriptPath + "    ----> Copying ---->    " + scriptsFolder+slash + script)
    if userInput=="NO":
        if script not in donotCopy123:
            scriptPath = slash.join([currentFolder, script])
            shutil.copy(scriptPath, scriptsFolder) #copy python scripts to user houdini foler
            print(scriptPath + "    ----> Copying ---->    " + scriptsFolder+slash + script)

    if script == "Ak.shelf":
        toolbarPath = slash.join([currentFolder, script])
        shutil.copy(toolbarPath, toolbarFolder) #copy Ak.shelf file to user houdini folder
        print("\n"+toolbarPath + "    ----> Copying ---->    " + toolbarFolder+slash + script)
        
print("\nDone you are all set, Enjoy...\n"+msg)

input()
