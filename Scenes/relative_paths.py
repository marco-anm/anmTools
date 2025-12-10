from maya import cmds
import os

def __init__(self):
    self.all_files = []
    self.iterable_files = []
    self.file_type = {
        "texture" : "file"
    }

def copy_to_sourceimages():
    files = cmds.filePathEditor(query=True, listFiles="", attributeOnly=True, byType="file")
    sourceimage_files = cmds.filePathEditor(query=True, listFiles="sourceimages", attributeOnly=True)
    proyect_path = cmds.workspace(query=True, rd=True)
    if not sourceimage_files:
        sourceimage_files = [""]

    for i, each_file in enumerate(files):
        if each_file not in sourceimage_files:
            file_full_path = cmds.getAttr(each_file)

            file_path = os.path.split(file_full_path)[0]

            try:
                cmds.filePathEditor(str(each_file), copyAndRepath=(file_path, proyect_path + "sourceimages"),
                                    force=True)
            except:
                print(f"Can't find {each_file} texture")



def set_paths_to_relatives():
    files = cmds.filePathEditor(query=True, listFiles="", attributeOnly=True)
    for each_file in files:
        file_path = cmds.getAttr(each_file)
        if not file_path.startswith(("sourceimages", "/sourceimages")):
            file_name = os.path.split(file_path)[-1]
            new_path = os.path.join("\sourceimages", file_name)
            print(str(each_file) + " new path will be: " + new_path)
            cmds.filePathEditor(each_file, repath="/sourceimages", force=True)
