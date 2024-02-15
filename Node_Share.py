###########----Node Share,To share node network to anyone on network----##########
#Author : Akshay Kumar
#Version : 1.1
#Modified Date : 15/02/2024
##################################################################################

import hou
import os
title="Node Network Share and Load"
msg = "Developed by Akshay Kumar\n Search select and accept."
user = os.getenv("USERNAME")
userList = r"C:\\Users\\"
nodesBasePath = r"\Documents\\houdini19.5\\ak_node_share"
saveTo = r"C:\\Users\\%s\Documents\\houdini19.5\\ak_node_share"%user
node_name = []

###########----functions----#########

isExist = os.path.exists(saveTo)
if not isExist:
	os.makedirs(saveTo)

def SaveTo():
    name = hou.ui.readInput(message="Provide the setup name", buttons=('OK','Cancle'), severity=hou.severityType.Message, default_choice=0, close_choice=1, title=title)
    node_name.append(name[1].replace(" ","_"))
    #print(name[1])

def ExportHdaSetup(node_name):
    allNodes = hou.selectedNodes()
    if len(allNodes)==0:
        hou.ui.displayMessage("     Please Select any node to Export/Share.          ",title=title, default_choice=0, close_choice=1)
    else:
        print("\n\n\n\n\n***********************************************************************************************\n")
        print("                                ->>Export/Share Fx Setup<<-")
        print("\n***********************************************************************************************\n\n")
        SaveTo()
        node = hou.selectedNodes()[0]
        context = node.type().category().name()
        print(node_name)
        allItems = hou.selectedItems()
        parent = node.parent()
        print(parent)
        saveToFile = saveTo + "\\%s.ak"%(context+"_"+node_name[0])
        parent.saveItemsToFile(allItems,saveToFile)
        print(saveToFile)
        print("\n\n***********************************************************************************************\n")
        print("                           Done!!! Set up saved successfully.")
        print("                               Developed by Akshay Kumar")
        print("\n\n***********************************************************************************************\n")

def LoadSetup():
    choices = []
    users = os.listdir(userList)
    for user in users:
        activeUser = userList+user+nodesBasePath
        if os.path.exists(activeUser):
            nodes = os.listdir(userList+user+nodesBasePath)
            for node in nodes:
                path = "/".join( [user, node])
                choices.append(path)

    OTL_Pick = hou.ui.selectFromTree(choices, picked=(), exclusive=False, message=msg, title=title, clear_on_cancel=True)
    OLT_Name = ""
    if len(OTL_Pick)>0:
        print("\n\n\n\n\n***********************************************************************************************\n")
        print("                                ->>Load Fx Setup<<-")
        print("\n***********************************************************************************************\n\n")
        print(OTL_Pick)
        print(user)
        File = saveTo + "\\%s"%(OTL_Pick[0]) #path for setup
        print(File)
        node = hou.selectedNodes()[0]
        parent = node.parent()
        pos = node.position()
        print(parent)
        hou.clearAllSelected()
        parent.loadItemsFromFile(File) #Load Fx setup
        node = hou.selectedNodes()[0]
        print(node)
        allItems = hou.selectedItems()
        parent = node.parent()
        networkBox = parent.createNetworkBox(name="Ak_Node_Share")
        networkBox.setComment(OTL_Pick[0])
        for i in allItems:
            networkBox.addItem(i) #Create network box
        networkBox.fitAroundContents()
        size = networkBox.size()
        print(size)
        newPos = hou.Vector2(pos[0]-(size[0]/2),pos[1]-size[1]-3)
        print(newPos)
        networkBox.setPosition(newPos) #move nodes under selected node

        print("\n\n***********************************************************************************************\n")
        print("                                   Enjoy!!!")
        print("                           Developed by Akshay Kumar")
        print("\n***********************************************************************************************\n")
        hou.ui.displayMessage("     Done          ",title=title)

def Clean():
    print("\n\n\n\n\n***********************************************************************************************\n")
    print("                                ->>Clean Node Setup<<-")
    print("\n***********************************************************************************************\n\n")
    fileList = hou.ui.selectFromTree(os.listdir(saveTo), picked=(), exclusive=False, message=msg+"\nSelect file to Delete.", title=title, clear_on_cancel=True)
    for f in fileList:
        os.remove(saveTo+"\\"+f)  #clean shared node networks
        print("removed '"+f+"' file form disk.")
    print("\n\n***********************************************************************************************\n")
    print("                                   Enjoy!!!")
    print("                           Developed by Akshay Kumar")
    print("\n***********************************************************************************************\n")

def Close():
    pass

###########----logic----##########

allNodes = hou.selectedNodes()
if len(allNodes)==0:
    hou.ui.displayMessage("     Please Select any node to continue.          ",title=title, default_choice=0, close_choice=0)
else:
    input = hou.ui.readMultiInput(title+"\n"+msg,buttons=("Export Nodes","Load Nodes","CANCEL","Clean"),input_labels="",close_choice=2,title=title)
    if input[0]==0:
        ExportHdaSetup(node_name)
    elif input[0]==1:
        LoadSetup()
    elif input[0]==2:
        Close()
    elif input[0]==3:
        Clean()
    else:
        pass

###########----finish----##########
