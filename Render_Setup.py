###########----Create render geo for fx elements Mantra setup in OUT----##########
#Author : Akshay Kumar
#Version : 1.1
#Modified Date : 25/02/2024
##################################################################################
import hou

root = hou.node("/obj/")
root_out = hou.node("/out/")
force_name = ""
check=[]
is_SOP=[]
title="Setup_Render_Geo"

#set color
Green = hou.Color((0,0.5,0))
Black = hou.Color((0,0,0))

for node in hou.selectedNodes():
    check = node.name()
    node_type = str(node.type())
    is_SOP = node_type.find("SopNode")

def RenderGeo():
    for node in hou.selectedNodes():
        selected = node.path()
        selected_name = node.name()
        new_name = selected_name.replace("OUT_","")
        new_name = selected_name.replace("RENDER_","")

        if(selected != None):
            #create nodes
            render_geo = root.createNode("geo", "RENDER_" + new_name)

            force_name = render_geo.name()

            obj_merge = render_geo.createNode("object_merge")
            #set parameters
            import_ = obj_merge.parm("objpath1").set(selected)
            trans = obj_merge.parm("xformtype").set(1)
            velocity_blur = render_geo.parm("geo_velocityblur").set(1)

            null = render_geo.createNode("null", "OUT")

            null.setNextInput(obj_merge)

            render_geo.moveToGoodPosition()
            obj_merge.moveToGoodPosition()
            null.moveToGoodPosition()

            null.setDisplayFlag(True)
            null.setRenderFlag(True)
            #print(force_name)



def Mantra():
    for node in hou.selectedNodes():
        selected = node.path()
        parent = node.parent()
        name = node.name()
        new_name = name.replace("OUT_","")
        new_name = name.replace("RENDER_","")
        path = selected.replace(name,"")
        render_node = ("/obj/"+(name)+"/render/OUT")

        if(selected != None):
            #create nodes
            mantra = root_out.createNode("ifd", "RENDER_" + new_name)
            #set parameters
            force_obj = mantra.parm("forceobject").set("RENDER_" + new_name)
            candidate_obj = mantra.parm("vobject").set("")
            motion_blur = mantra.parm("allowmotionblur").set(1)
            mantra.setColor(Green)
            #set position
            mantra.moveToGoodPosition()

##############----Logic----########################

if(len(check)>0):
    if is_SOP>0:
        RenderGeo()
        Mantra()
        hou.ui.displayMessage("     Done          ",title=title)
    else:
        hou.ui.displayMessage("You have selected OBJ level node please select SOP level node.",title=title)
else:
    hou.ui.displayMessage("Please select node to create render geometry and mantra node.",title=title)
###########----finish----##########
