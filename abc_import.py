##########----abc_improt----###########
#Author : Akshay Kumar
#Version : 1.0
#Modified Date : 23/07/2024
#############################################################

import os
import hou

title = "abc_import"
path = []
abc_dict = {}

start_path = os.listdir(os.getenv("HIP"))
select_msg = "Select path for abc from\n%s"%(os.getenv("HIP"))

def select_abc_path():
    abc_path = hou.ui.selectFromTree(start_path, message=select_msg, title=title)
    path.append(os.getenv("HIP")+"/"+abc_path[0])
    # print(abc_path[0])

def import_abc(path):
    for (root, dir, files) in os.walk(path[0]):
        for file in files:
            if file.endswith(".abc"):
                abc_dict[file.replace(".abc", "")] = (os.sep.join([root, file]))


    for key, value in abc_dict.items():
        obj = hou.node("/obj/")

        #create abc achrive nodes
        abc_achrive_node = obj.createNode("alembicarchive", key)
        abc_achrive_node.parm("buildSingleGeoNode").set(1)
        abc_achrive_node.parm("fileName").set(value)
        abc_achrive_node.parm("buildHierarchy").pressButton()
        # abc_achrive_node.setDisplayFlag(0)
        abc_achrive_node.moveToGoodPosition()
        abc_achrive_node.setCurrent(True)
        
    scene_viewer = hou.ui.paneTabOfType(hou.paneTabType.SceneViewer)
    editor = hou.ui.paneTabOfType(hou.paneTabType.NetworkEditor)
    editor.cd("/obj")
    scene_viewer.cd("/obj")
    editor.homeToSelection()
    scene_viewer.curViewport().frameAll()

    

select_abc_path()
import_abc(path)
