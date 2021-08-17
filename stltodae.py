# python -m pip install easygui 
# python -m pip install PyMeshLab

# TODO: simplification_quadric_edge_collapse_decimation
#       in pymeshlab.print_filter_list()
#       https://pymeshlab.readthedocs.io/en/latest/intro.html

# py->exe using nuitka
# https://github.com/Nuitka/NUITKA-Utilities/pull/63/files
# using hint compilation

#numpy problem
#https://github.com/Nuitka/Nuitka/issues/736

# EDIT: cx_freeze works!

import easygui
import xml.etree.ElementTree as ET
import sys
import numpy
import pymeshlab

def convertSTLtoDAE(file):
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(file)
    newfile = file.replace('.stl','') + '.dae'
    ms.save_current_mesh(newfile)
    return newfile

easygui.msgbox('Welcome. Click OK to select a STL file to convert to DAE(Collada)', 'Create Collada DAE for Sketchup')
inputfile = easygui.fileopenbox(default="*.stl", filetypes=["*.dae", "*.stl"])
if inputfile is None:
    sys.exit(0)
isSTL = False
if inputfile.endswith('dae'):
    pass
elif inputfile.endswith('stl'):
    inputfile = convertSTLtoDAE(inputfile)
    isSTL = True
else:
    pass
ET.register_namespace('', "http://www.collada.org/2005/11/COLLADASchema")
tree = ET.parse(inputfile)
root = tree.getroot()
assetTag = root[0]
#print(assetTag)

'''
Want to append this to the asset tag as child element

<unit name="millimeters" meter="0.001"/>

'''

unitTag = ET.Element('unit')
unitTag.set('name', 'millimeters')
unitTag.set('meter', '0.001')

assetTag.append(unitTag)
if isSTL:
    newfile = inputfile
else:
    newfile = inputfile.replace('.dae', '') + '-converted.dae'
tree.write(newfile)

easygui.msgbox("Fix successful. New file created: " + newfile)
