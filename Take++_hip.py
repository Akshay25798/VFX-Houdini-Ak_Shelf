############----take++ or version up the current hip file----#############
#Author : Akshay Kumar
#Version : 1.1
#Modified Date : 15/02/2024
#############################################################

import hou
isNew = hou.hipFile.isNewFile()
if not isNew==True:
    hou.hipFile.saveAndIncrementFileName()
    #print("Take++ is sucessfull for : "+hou.hipFile.name())
###########----finish----##########