#save file the in correct folder

import hou

def SAVE_HIP():

    msg="Give the naming to the .hip file."

    #check if the file is new
    isNew = hou.hipFile.isNewFile()
    #print("Is this a new file : "+str(isNew))

    if isNew==True:
        fileName = hou.ui.readInput(message=msg,buttons=("Ok","Cancel"),close_choice=1)
        #print("Name given to .hip file is : "+fileName[1])

        #give the naming to the file
        hou.hipFile.setName(hou.expandString('$HIP')+"/hip/"+fileName[1]+"_v000.hip")

    #saving the file
    hou.hipFile.save()


SAVE_HIP()
#print("HIP file is saved sucessfully as : " + hou.hipFile.name())