import os
import shutil
import platform

title="Copy scripts to user houdini folder."
msg = "Developed by Akshay Kumar"
donotCopy = ["Win_exe.bat", "pythonExec.py", "Linux_exe.sh", "Ak.shelf", "README.md"]
osName = platform.system()
if osName=="Linux":
    slash = r"/"
    user = os.getenv("USER")
    baseFolder = "/usr/people/%s"%user #user houdini folder
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
print("All scripts : " + str(scripts) + "\n")
for script in scripts:
    if script not in donotCopy:
        scriptPath = slash.join([currentFolder, script])
        shutil.copy(scriptPath, scriptsFolder) #copy python scripts to user houdini foler
        print(scriptPath + "    ----> Copying ---->    " + scriptsFolder+slash + script)
    if script == "Ak.shelf":
        toolbarPath = slash.join([currentFolder, script])
        shutil.copy(toolbarPath, toolbarFolder) #copy Ak.shelf file to user houdini folder
        print("\n"+toolbarPath + "    ----> Copying ---->    " + toolbarFolder+slash + script)
        
print("\n-------------------------------Done,"+msg+"------------------------------\n")

input()