from maya import cmds


class MessageCreatorWindow(object):

    def __init__(self, title="Open File Message Creator"):
        self.pop_up_message = "Mensaje de muestra"
        self.pop_up_window_name = "Título de muestra"
        self.window = "open_file_message_creator"
        self.title = title
        self.create_window()

    def create_window(self):
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window)

        self.window = cmds.window(self.window, title=self.title, sizeable=False)

        cmds.columnLayout(adjustableColumn=True, rowSpacing=10)

        cmds.rowLayout(numberOfColumns=2, adjustableColumn=1)

        cmds.columnLayout(adjustableColumn=True, columnAlign="left")

        self.window_title = cmds.textFieldGrp(columnAlign=[(1, "left")], label="Título de la ventana",
                                              adjustableColumn=2, text=self.pop_up_window_name)

        cmds.separator(height=10)

        cmds.columnLayout(adjustableColumn=True, rowSpacing=10)

        cmds.text("Texto del mensaje", align="left", height=14)
        self.message_box = cmds.scrollField(text=self.pop_up_message,  ww=True)

        cmds.setParent("..")

        cmds.setParent("..")

        cmds.columnLayout(adjustableColumn=True, width=100, rowSpacing=10)
        cmds.button(label='CREATE', command=self.create_script_node, height=75, backgroundColor=(0.788, 0.141, 0.392))
        cmds.button(label="Eliminar nodos", command=self.delete_script_nodes)
        cmds.button(label='Cancel', command=('cmds.deleteUI(\"' + self.window + '\", window=True)'))
        cmds.setParent('..')

        cmds.setParent('..')

    def create_script_node(self, *args):
        self.pop_up_message = cmds.scrollField(self.message_box, query=True, text=True)
        self.pop_up_window_name = cmds.textFieldGrp(self.window_title, query=True, text=True)
        win_name = self.pop_up_window_name
        win_message = self.pop_up_message
        pop_up_window = "cmds.confirmDialog(title='{}', message='''{}''')".format(win_name, win_message)

        script_node = cmds.scriptNode(name="fileVer", scriptType=1, beforeScript=pop_up_window, sourceType="python")
        cmds.lockNode(script_node, lock=True)
        print("Node Created")

    @staticmethod
    def delete_script_nodes(*args):
        print("deleting")
        script_nodes = cmds.ls("fileVer*")
        for node in script_nodes:
            cmds.lockNode(node, lock=False)
            cmds.delete(node)


win = MessageCreatorWindow()
cmds.showWindow(win.window)
