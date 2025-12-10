from maya import cmds

#all geos
geos = cmds.listRelatives(cmds.ls(cmds.listRelatives(cmds.ls(sl=True), allDescendents=True),
                                  geometry=True), parent=True, path=True)

origGeos = []

#create tmp locator for each geo

for eachGeo in geos:
    if not cmds.listConnections(eachGeo, type="animCurve"):
        pass
    else:
        cmds.spaceLocator(name=eachGeo + "_tmpLoc")
        cmds.parentConstraint(eachGeo, eachGeo + "_tmpLoc", maintainOffset=False)

tmp_locs = cmds.ls("*_tmpLoc")

cmds.select(tmp_locs)

startTime = cmds.playbackOptions(animationStartTime=True, query=True)
endTime = cmds.playbackOptions(animationEndTime=True, query=True)

cmds.bakeResults(sampleBy=1, simulation=False, time=(startTime,endTime), smart=(True,99))

for eachGeo in geos:
    if not cmds.listConnections(eachGeo, type="animCurve"):
        pass
    else:
        cmds.delete(eachGeo, constraints=True)
        cmds.delete(eachGeo, channels=True)
        try:
            cmds.parent(eachGeo, world=True)
        except:
            continue
        cmds.makeIdentity(eachGeo, apply=True, scale=True)


for eachLoc in tmp_locs:
    origGeo = eachLoc.split("_tmpLoc")[0]
    origGeos.append(origGeo)
    cmds.parentConstraint(eachLoc, origGeo)

cmds.select(origGeos, replace=True)
cmds.bakeResults(simulation=False, time=(startTime,endTime), smart=(True,99))

for eachFinal in origGeos:
    cmds.delete(eachFinal, constraints=True)

cmds.delete("*:*_tmpLoc*")
cmds.delete("*_tmpLoc*")