##########----geo_prep----###########
#Author : Akshay Kumar
#Version : 1.0
#Modified Date : 23/07/2024
#############################################################

import os
import hou

title = "geo_prep"
msg = "Select the node create 'Geo_Prep' node for each selection or merge in one 'Geo_Prep'."

def keep_seperated(selection):
    for sel in selection: #keep seperate
        sel_name = str(sel.name())
        if sel.type().name() == "alembicarchive":
            geo_prep = hou.node("/obj/").createNode("geo",  ("Geo_Prep_"+sel_name) )
            geo_prep.moveToGoodPosition()
            geo_prep.setCurrent(True)

            obj_merge = geo_prep.createNode("object_merge", ("IN_"+sel_name))
            obj_merge.parm("objpath1").set(sel.path()+"/geo")
            obj_merge.parm("createprimstring").set(1)

            scale = geo_prep.createNode("xform", "scale_down")
            scale.parm("scale").set(0.1)
            scale.setDisplayFlag(True)
            scale.setRenderFlag(True)

            convert = geo_prep.createNode("convert")
            delete = geo_prep.createNode("delete")
            delete.parm("negate").set(1)
            delete.parm("entity").set(2)
            delete.parm("geotype").set(9)

            convert.setNextInput(obj_merge)
            delete.setNextInput(convert)
            scale.setNextInput(delete)
            geo_prep.layoutChildren()

    scene_viewer = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)
    editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
    editor.cd("/obj")
    scene_viewer.cd("/obj")
    editor.homeToSelection()
    scene_viewer.curViewport().frameAll()

def merge_in_one(selection):
    sel_name = "Geo_Prep_All"
    geo_prep = hou.node("/obj/").createNode("geo",  (sel_name) )
    geo_prep.moveToGoodPosition()
    geo_prep.setCurrent(True)

    for sel in selection: #keep seperate
        if sel.type().name() == "alembicarchive":
            obj_merge = geo_prep.createNode("object_merge", ("IN_"+sel.name()))
            obj_merge.parm("objpath1").set(sel.path()+"/geo")
            obj_merge.parm("createprimstring").set(1)

            scale = geo_prep.createNode("xform", "scale_down")
            scale.parm("scale").set(0.1)
            scale.setDisplayFlag(True)
            scale.setRenderFlag(True)

            convert = geo_prep.createNode("convert")
            delete = geo_prep.createNode("delete")
            delete.parm("negate").set(1)
            delete.parm("entity").set(2)
            delete.parm("geotype").set(9)

            convert.setNextInput(obj_merge)
            delete.setNextInput(convert)
            scale.setNextInput(delete)
            geo_prep.layoutChildren()

    scene_viewer = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)
    editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
    editor.cd("/obj")
    scene_viewer.cd("/obj")
    editor.homeToSelection()
    scene_viewer.curViewport().frameAll()


def abc_archive_single_geo_prep():
    selection = hou.selectedNodes()
    if selection:
        mode = hou.ui.displayMessage(msg, buttons=("Keep Seperated","Merge in one geo", "Cancle",), close_choice=2, title=title)
        if mode==0:
            keep_seperated(selection)
        if mode==1:
            merge_in_one(selection)

abc_archive_single_geo_prep()