###########----Node Share,To share node network to anyone on network----##########
#Author : Akshay Kumar
#Version : 1.1
#Modified Date : 15/02/2024
##################################################################################

import hou
import os
import platform

title="Node Network Share and Load"
msg = "Developed by Akshay Kumar\n Search select and accept."
osName = platform.system()
if osName=="Linux":
    slash = r"/"
    user = os.getenv("USER")
    userList = "/usr/people" #users dir
    nodesBasePath = "/node_network_snippets" #folder for node network to save
    saveTo = "/usr/people/%s/houdini19.5/node_network_snippets"%user #user houdini folder
else:
    slash = r"\\"
    user = os.getenv("USERNAME")
    userList = r"C:\Users" #users dir
    nodesBasePath = r"\Documents\houdini19.5\node_network_snippets" #folder for node network to save
    saveTo = r"C:\Users\%s\Documents\houdini19.5\node_network_snippets"%user #user houdini folder

###########----functions----#########

isExist = os.path.exists(saveTo)
if not isExist:
	os.makedirs(saveTo)

def ExportHdaSetup():
    name = hou.ui.readInput(message="Provide the setup name", buttons=('OK','Cancle'), severity=hou.severityType.Message, default_choice=0, close_choice=1, title=title)
    node_name = name[1].replace(" ","_")
    if name[0]==0:
        print("\n\n\n\n\n***********************************************************************************************\n")
        print("                                ->>%s<<-"%(title))
        print("\n***********************************************************************************************\n\n")
        print(node_name)
        node = hou.selectedNodes()[0]
        context = node.type().category().name()
        allItems = hou.selectedItems()
        parent = node.parent()
        saveToFile = saveTo + slash +"%s.ak"%(context+"_"+node_name)
        parent.saveItemsToFile(allItems,saveToFile)
        print("Node network name : " + node_name)
        print("Node network context : " + context)
        print("Network file path : " + saveToFile)
        print("\n\n***********************************************************************************************\n")
        print("                           Done!!! Set up saved successfully.")
        print("                               Developed by Akshay Kumar")
        print("\n\n***********************************************************************************************\n")

def LoadSetup():
    choices = []
    users = os.listdir(userList)
    for activeUser in users: #fetching the active user list with there shared node network setups
        activeUserPath = saveTo[:-(len(nodesBasePath)+len(user))] + activeUser + nodesBasePath
        #print(activeUserPath)
        if os.path.exists(activeUserPath):
            nodes = os.listdir(activeUserPath)
            for node in nodes:
                path = "/".join( [activeUser, node])
                choices.append(path)
    #print(choices)
    #print(path)
    OTL_Pick = hou.ui.selectFromTree(choices, picked=(), exclusive=False, message=msg, title=title, clear_on_cancel=True)
    if len(OTL_Pick)>0: #pick needed node network
        print("\n\n\n\n\n***********************************************************************************************\n")
        print("                                ->>%s<<-"%(title))
        print("\n***********************************************************************************************\n\n")
        if osName=="Linux":
            OTL_Pick = OTL_Pick[0].split(os.sep)
        else:
            OTL_Pick = OTL_Pick[0].replace("/","\\")
            OTL_Pick = OTL_Pick.split(os.sep)
        print("Loading from : " + OTL_Pick[0])
        print("Node network name : " + OTL_Pick[1])
        File = slash.join([ saveTo[:-(len(nodesBasePath)+len(user))] , OTL_Pick[0] , nodesBasePath , OTL_Pick[1] ])
        print("Network file path : " + File)
        node = hou.selectedNodes()[0]
        parent = node.parent()
        pos = node.position()
        hou.clearAllSelected()
        parent.loadItemsFromFile(File) #Load Fx setup
        node = hou.selectedNodes()[0]
        allItems = hou.selectedItems()
        parent = node.parent()
        networkBox = parent.createNetworkBox(name="Ak_Node_Share")
        networkBox.setComment(OTL_Pick[1])
        for i in allItems:
            networkBox.addItem(i) #Create network box
        networkBox.fitAroundContents()
        size = networkBox.size()
        newPos = hou.Vector2(pos[0]-(size[0]/2),pos[1]-size[1]-3)
        networkBox.setPosition(newPos) #move nodes under selected node

        print("\n\n***********************************************************************************************\n")
        print("                                   Enjoy!!!")
        print("                           Developed by Akshay Kumar")
        print("\n***********************************************************************************************\n")
        hou.ui.displayMessage("     Done          ",title=title)

def Clean():
    fileList = hou.ui.selectFromTree(os.listdir(saveTo), picked=(), exclusive=False, message=msg+"\nSelect file to Delete.", title=title, clear_on_cancel=True)
    if len(fileList)!=0:
        print("\n\n\n\n\n***********************************************************************************************\n")
        print("                                ->>Clean Node Setup<<-")
        print("\n***********************************************************************************************\n\n")
        for f in fileList:
            path = saveTo + slash + f
            os.remove(path)  #clean shared node networks
            print("Removed node network '"+f+"' file form disk.")
            print("Removed file path : " + path)
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
    input = hou.ui.readMultiInput(title+"\n"+msg,buttons=("Export Nodes","Load Nodes","Cancle","CLEAN"),input_labels="",close_choice=2,title=title)
    if input[0]==0:
        ExportHdaSetup()
    elif input[0]==1:
        LoadSetup()
    elif input[0]==2:
        Close()
    elif input[0]==3:
        Clean()
    else:
        pass

###########----finish----##########
