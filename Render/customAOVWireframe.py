from maya import cmds
from mtoa import aovs


if cmds.objExists("customAOV_wireframe_mtl"):
    toonMtl = "customAOV_wireframe_mtl"
else:
    toonMtl = cmds.shadingNode("aiToon", asShader=True, n="customAOV_wireframe_mtl")

if cmds.objExists("customAOV_wireframe_mask"):
    utilityNode = "customAOV_wireframe_mask"
else:
    utilityNode = cmds.shadingNode("aiUtility", asShader=True, n="customAOV_wireframe_mask")
    
cmds.connectAttr(utilityNode + ".outColor", toonMtl + ".maskColor", force=True)

cmds.setAttr(utilityNode + ".shadeMode", 2)
cmds.setAttr(utilityNode + ".colorMode", 12)
cmds.setAttr("customAOV_wireframe_mtl.edgeColor", 1, 1, 1)
cmds.setAttr("customAOV_wireframe_mtl.baseColor", 0, 0, 0)

if cmds.objExists("aiAOV_customWireframe"):
    customFilter = "aiAOV_customWireframe"
else:
    aovs.AOVInterface().addAOV("customWireframe", aovType="rgba")

cmds.connectAttr(toonMtl + ".outColor", customFilter+".defaultValue", force=True)

cmds.confirmDialog(m="Go to AOVs settings and change customWireframe's filter to contour", b=["Ok"])
