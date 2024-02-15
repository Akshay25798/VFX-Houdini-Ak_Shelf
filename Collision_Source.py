###########----Create collision Sourece in one click----##########
#Author : Akshay Kumar
#Version : 1.1
#Modified Date : 15/02/2024
##################################################################################
import hou

title = "FX_Coll._Src."
check=[]
for node in hou.selectedNodes():
    check = node.name()

def Collisions():
    for node in hou.selectedNodes():
        selected = node.path()
        parent = node.parent()
        name = node.name()
        path = selected.replace(name,"")
        #print(name)
        if(selected != None):
            #create nodes
            coll = parent.createNode("collisionsource::2.0")
            null_geo = parent.createNode("null", "OUT_Coll_Geo")
            null_vdb = parent.createNode("null", "OUT_Coll_VDB")
            #set parameters
            coll.parm("voxelsize").set(0.05)
            #set connection
            coll.setNextInput(node)
            null_geo.setNextInput(coll)
            null_vdb.setNextInput(coll,1)
            #set render flag
            null_geo.setDisplayFlag(True)
            null_geo.setRenderFlag(True)
            #move to goodposition
            coll.moveToGoodPosition()
            null_geo.moveToGoodPosition()
            null_vdb.moveToGoodPosition()

##########################################

if(len(check)>0):
    Collisions()
else:
    hou.ui.diaplayMessage("Please select node to create collision source.",title=title)

#########>> FINISH << ##############
