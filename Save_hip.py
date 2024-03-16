##########----save file the in correct folder----###########
#Author : Akshay Kumar
#Version : 1.1
#Modified Date : 15/02/2024
#############################################################

import hou

def SAVE_HIP():
    msg="Give the naming to the .hip file."
    #check if the file is new
    isNew = hou.hipFile.isNewFile()
    if isNew==True:
        saveFilePath = hou.expandString('$JOB')
        space = "                                                                     \n\n"
        fileName = hou.ui.readInput(message=space+msg+"\nSave Path : "+saveFilePath+space,buttons=("Ok","Cancel"),close_choice=1)
        if fileName[0]==0:
            hou.hipFile.setName(saveFilePath+"/"+fileName[1]+"_v000.hip")
            #saving the file
            hou.hipFile.save()
            print("HIP file is saved sucessfully as : " + hou.hipFile.name())


SAVE_HIP()


###########----finish----##########