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

def simplifySTL(ms, newFaceCount=1000):
	ms.apply_filter('simplification_quadric_edge_collapse_decimation', targetfacenum=newFaceCount, preservenormal=True)

def convertSTLtoDAE(file):
    ms = pymeshlab.MeshSet()
    ms.load_new_mesh(file)
    newfile = file.replace('.stl','') + '.dae'
    m = ms.current_mesh()
    bounding = m.bounding_box()
    x = bounding.dim_x()
    y = bounding.dim_y()
    z = bounding.dim_z()
    face = m.face_number()
    vertex = m.vertex_number()
    msg = f"Dimensions of 3D model:\n\nX: {x} Y: {y} Z: {z}\n\nComplexity of model:\n\nFace Count: {face}\nVertex Count: {vertex}\n\nDo you want to simplify model? Recommended to simplify when face count is greater than 40000."
    shouldSimplify = easygui.ynbox(msg, 'Create Collada DAE for Sketchup')
    if shouldSimplify:
    	faceCount = easygui.integerbox(msg='Enter new face count', title='Create Collada DAE for Sketchup', default=face, upperbound=1000000000)
    	simplifySTL(ms, faceCount)
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
