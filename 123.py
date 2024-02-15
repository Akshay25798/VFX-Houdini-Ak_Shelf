#####################----setiing up the default template----#####################
#Author : Akshay Kumar
#Version : 1.1
#Modified Date : 15/02/2024
##################################################################################
import hou

class Default_Template():
    def __init__(self) -> None:
        self.obj=hou.node("/obj")
        self.out=hou.node("/out")
        
    def Create_Template(self):
        #color
        self.red = hou.Color((1.0, 0, 0))
        self.green = hou.Color((0.1, 0.8, 0.1))
        self.gray = hou.Color((0.5, 0.5, 0.5))
        self.yellow = hou.Color((1, 0.6, 0))
        self.blue = hou.Color((0, 0.5, 1))

        #size
        self.objSize = hou.Vector2(12,15)
        self.outSize = hou.Vector2(20,12)

        #Position
        self.assetPos = hou.Vector2(0,0)
        self.camPos = hou.Vector2(13,0)
        self.prepPos = hou.Vector2(13*2,0)
        self.simPos = hou.Vector2(13*3,0)
        self.rndrPos = hou.Vector2(13*4,0)

        self.RNDRPos = hou.Vector2(0,0)
        self.SIMPos = hou.Vector2(0,13)

        ###create obj network box in OBJ context

        #asset
        self.asset = self.obj.createNetworkBox()
        self.asset.setColor(self.gray)
        self.asset.setSize(self.objSize)
        self.asset.setPosition(self.assetPos)
        self.asset.setComment("Asset")

        #light and self.camera
        self.cam = self.obj.createNetworkBox()
        self.cam.setColor(self.yellow)
        self.cam.setSize(self.objSize)
        self.cam.setPosition(self.camPos)
        self.cam.setComment("camera and Light")

        #geo self.prep
        self.prep = self.obj.createNetworkBox()
        self.prep.setColor(self.blue)
        self.prep.setSize(self.objSize)
        self.prep.setPosition(self.prepPos)
        self.prep.setComment("Geo prep")

        #self.sim
        self.sim = self.obj.createNetworkBox()
        self.sim.setColor(self.red)
        self.sim.setSize(self.objSize)
        self.sim.setPosition(self.simPos)
        self.sim.setComment("sim")

        #render
        self.rndr = self.obj.createNetworkBox()
        self.rndr.setColor(self.green)
        self.rndr.setSize(self.objSize)
        self.rndr.setPosition(self.rndrPos)
        self.rndr.setComment("Render")


        ###create obj network box in OUT context

        #render
        self.rndr_out = self.out.createNetworkBox()
        self.rndr_out.setColor(self.green)
        self.rndr_out.setSize(self.outSize)
        self.rndr_out.setPosition(self.RNDRPos)
        self.rndr_out.setComment("Renders")

        #self.sim
        self.sim_out = self.out.createNetworkBox()
        self.sim_out.setColor(self.red)
        self.sim_out.setSize(self.outSize)
        self.sim_out.setPosition(self.SIMPos)
        self.sim_out.setComment("caching")

    def Clear_Template(self):
        self.defaults = ["Asset", "camera and Light", "Geo prep", "sim", "Render", "caching", "Renders"]
        self.items = []
        self.obj_items = self.items.extend(hou.Node.allItems(hou.node("/obj")))
        self.out_items = self.items.extend(hou.Node.allItems(hou.node("/out")))

        for self.net_box in self.items:
            if self.net_box.networkItemType().name() == 'NetworkBox':
                if self.net_box.comment() in self.defaults:
                    self.net_box.destroy() 

Tempelate = Default_Template()

try:
    Tempelate.Clear_Template()
except:
    pass
finally:
    Tempelate.Create_Template()

#########>> FINISH << ##############