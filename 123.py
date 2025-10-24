#####################----setiing up the default template----#####################
#Author : Akshay Kumar
#Version : 1.2
#Modified Date : 24/10/2025
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
        #self.assetPos = hou.Vector2(0,0)
        #self.camPos = hou.Vector2(13,0)
        self.camPos = hou.Vector2(13*2,0)
        self.simPos = hou.Vector2(13*3,0)
        self.rndrPos = hou.Vector2(13*4,0)

        self.RNDRPos = hou.Vector2(0,0)
        self.SIMPos = hou.Vector2(0,13)

        ###create obj network box in OBJ context


        #light and self.camera
        self.cam = self.obj.createNetworkBox()
        self.cam.setColor(self.yellow)
        self.cam.setSize(self.objSize)
        self.cam.setPosition(self.camPos)
        self.cam.setComment("camera and Light")

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


    def Clear_Template(self):
        self.defaults = ["Asset", "camera and Light", "Geo prep", "sim", "Render", "caching", "Renders"]
        self.items = []
        self.obj_items = self.items.extend(hou.Node.allItems(hou.node("/obj")))
        self.out_items = self.items.extend(hou.Node.allItems(hou.node("/out")))

        for self.net_box in self.items:
            if self.net_box.networkItemType().name() == 'NetworkBox':
                if self.net_box.comment() in self.defaults:
                    self.net_box.destroy() 
                    
    def Set_Inital_Framerange(self):
        hou.playbar.setFrameRange(1001, 1100)
        hou.setFrame(1001)

Tempelate = Default_Template()

try:
    Tempelate.Clear_Template()
except:
    pass
finally:
    Tempelate.Create_Template()
    Tempelate.Set_Inital_Framerange()

#########>> FINISH << ##############
