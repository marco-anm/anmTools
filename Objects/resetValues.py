from maya import cmds
sel=cmds.ls(sl=True)
for each in sel:
	attr = cmds.listAttr(each, k=True)
	attr.extend(x for x in cmds.listAttr(each, ud=True) if x not in attr) if cmds.listAttr(each, ud=True) else attr
	for eachAttr in attr:
		defVal = cmds.attributeQuery(eachAttr, node=each, listDefault=True)
		try:
			cmds.setAttr(each + "." + eachAttr, defVal[0])
		except:
			pass
