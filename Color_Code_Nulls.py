##################################################################################
#Author : Akshay Kumar
#Version : 1.1
#Modified Date : 15/02/2024
##################################################################################
import hou

#get assess to the nodes
root = hou.node("/obj/")
child = root.allSubChildren()

#set color
black = hou.Color((0,0,0))
red = hou.Color((1,0.2,0.1))

#logic
for node in child:
    nodeName = node.name().upper()
    nodeType = str(node.type().name())

    if nodeName.startswith("OUT") and nodeType == "null":
        colorNode = node.setColor(black)

    if nodeName.endswith("_OUT") and nodeType == "null":
        colorNode = node.setColor(black)

    if nodeName.startswith("IN") and nodeType == "null":
        colorNode = node.setColor(red)

    if nodeName.endswith("_IN") and nodeType == "null":
        colorNode = node.setColor(red)

    if nodeName.startswith("IN") and nodeType == "object_merge":
        colorNode = node.setColor(red)

    if nodeName.endswith("_IN") and nodeType == "object_merge":
        colorNode = node.setColor(red)
        
#########>> FINISH << ##############