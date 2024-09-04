"""

SELECCIONAR TODOS LOS OBJETOS DE LA ESCENA, USAR SCRIPT

Solo funciona con materiales aiStandard. Conecta mapas de textura en baseColor, si no encuentra,
busca en sss, si no lo hubiese, copia el color y la transparencia del objeto

"""

import maya.cmds as cmds

sel = cmds.ls(sl=True)
sg = cmds.listConnections(cmds.listRelatives(sel, s=True), type='shadingEngine')

for eachSg in sg:
    material = cmds.ls(cmds.listConnections(eachSg), materials = True)
    materialType = cmds.nodeType(material)
  
    if cmds.nodeType(material)== "aiStandardSurface":
        for eachMat in material:
             
            if cmds.listConnections(eachMat+".baseColor"):
                difMap = cmds.listConnections(eachMat+".baseColor") 
                newLamb=cmds.shadingNode("lambert", asShader=True, n="lambert_"+eachMat)
                cmds.connectAttr(difMap[0]+".outColor", newLamb+".color")
                cmds.connectAttr(newLamb+".outColor", eachSg+".surfaceShader", force=True)
                cmds.connectAttr(eachMat+".outColor", eachSg+".aiSurfaceShader", force=True)
                
                print (newLamb + " created")  
                
            elif cmds.listConnections(eachMat+".subsurfaceColor"):
                difMap = cmds.listConnections(eachMat+".subsurfaceColor")
                newLamb=cmds.shadingNode("lambert", asShader=True, n="lambert_"+eachMat)
                cmds.connectAttr(difMap[0]+".outColor", newLamb+".color")
                cmds.connectAttr(newLamb+".outColor", eachSg+".surfaceShader", force=True)
                cmds.connectAttr(eachMat+".outColor", eachSg+".aiSurfaceShader", force=True)
                
                print (newLamb + " created") 
            
            else:
                difColor = cmds.getAttr(eachMat+".baseColor")[0]
                difTrans = cmds.getAttr(eachMat+".transmission")
                
                newLamb=cmds.shadingNode("lambert", asShader=True, n="lambert_"+eachMat)
                cmds.setAttr(newLamb+".color", difColor[0], difColor[1], difColor[2], type="double3")
                cmds.setAttr(newLamb+".transparency", difTrans, difTrans, difTrans, type="double3")
                cmds.connectAttr(newLamb+".outColor", eachSg+".surfaceShader", force=True)
                cmds.connectAttr(eachMat+".outColor", eachSg+".aiSurfaceShader", force=True)
                
    else:
        print ("Can't create Lambert for " + eachSg + " material")