#Activa el modo de visualización xRay en cada objeto seleccionado. Pulsando Control desactiva este modo)

import maya.cmds as cmds

sel=cmds.ls(sl=True)

mods=cmds.getModifiers() #Obtiene los modificadores al pulsar teclas como control, shift, etc.

if (mods & 4) > 0:
    cmds.displaySurface(sel, xRay=False)
else:
    for each in sel:
        if cmds.displaySurface(each, q=True, xRay=False):
            cmds.displaySurface(each, xRay=True)
        elif cmds.displaySurface(each, q=True, xRay=True):
            cmds.displaySurface(each, xRay=False)