#setiing up the empty houdini file
import hou

def MPC_TEMPLATE():
    obj=hou.node("/obj")
    out=hou.node("/out")

    #color
    red = hou.Color((1.0, 0, 0))
    green = hou.Color((0.1, 0.8, 0.1))
    gray = hou.Color((0.5, 0.5, 0.5))
    yellow = hou.Color((1, 0.6, 0))
    blue = hou.Color((0, 0.5, 1))

    #size
    objSize = hou.Vector2(12,15)
    outSize = hou.Vector2(20,12)

    #Position
    assetPos = hou.Vector2(0,0)
    camPos = hou.Vector2(13,0)
    prepPos = hou.Vector2(13*2,0)
    simPos = hou.Vector2(13*3,0)
    rndrPos = hou.Vector2(13*4,0)

    RNDRPos = hou.Vector2(0,0)
    SIMPos = hou.Vector2(0,13)

    ###create obj network box in OBJ context

    #asset
    asset = obj.createNetworkBox()
    asset.setColor(gray)
    asset.setSize(objSize)
    asset.setPosition(assetPos)
    asset.setComment("Asset")

    #light and camera
    cam = obj.createNetworkBox()
    cam.setColor(yellow)
    cam.setSize(objSize)
    cam.setPosition(camPos)
    cam.setComment("Camera and Light")

    #geo prep
    prep = obj.createNetworkBox()
    prep.setColor(blue)
    prep.setSize(objSize)
    prep.setPosition(prepPos)
    prep.setComment("Geo prep")

    #sim
    sim = obj.createNetworkBox()
    sim.setColor(red)
    sim.setSize(objSize)
    sim.setPosition(simPos)
    sim.setComment("SIM")

    #render
    rndr = obj.createNetworkBox()
    rndr.setColor(green)
    rndr.setSize(objSize)
    rndr.setPosition(rndrPos)
    rndr.setComment("Render")


    ###create obj network box in OUT context

    #render
    rndr = out.createNetworkBox()
    rndr.setColor(green)
    rndr.setSize(outSize)
    rndr.setPosition(RNDRPos)
    rndr.setComment("Render")

    #sim
    sim = out.createNetworkBox()
    sim.setColor(red)
    sim.setSize(outSize)
    sim.setPosition(SIMPos)
    sim.setComment("SIM")


#print("Loading MPC Tempelate...")

MPC_TEMPLATE()

#########>> FINISH << ##############