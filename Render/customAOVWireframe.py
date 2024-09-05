from maya import cmds, mel
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
    customAOV = "aiAOV_customWireframe"
else:
    customAOV = aovs.AOVInterface().addAOV("customWireframe", aovType="rgba")

mel.eval('createNode aiAOVFilter -n "aiAOVFilter_customWireframe";setAttr ".ai_translator" -type "string" "contour"')

cmds.connectAttr("aiAOVFilter_customWireframe.message", "aiAOV_customWireframe.outputs[0].filter", force=True)

cmds.connectAttr(toonMtl + ".outColor", "aiAOV_customWireframe.defaultValue", force=True)

