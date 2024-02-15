#####----Copy houdiniShelf----####
#Author : Akshay Kumar
#Version : 1.1
#Modified Date : 15/02/2024
##################################################################################
import hou
import os
import shutil

userid = hou.userName()

src_path = 'houdini/hip/Scripts/akshay-ku/toolbar/Ak.shelf'
user_path = "/usr/people/%s/houdini18.5/toolbar/Ak.shelf"%(userid)


def Copy_Shelf():
    shutil.copyfile(src_path, user_path)

def Reload_Shelf():
    hou.shelves.loadFile(user_path)


Copy_Shelf()
Reload_Shelf()
hou.ui.displayMessage("Done")

###########----finish----##########
