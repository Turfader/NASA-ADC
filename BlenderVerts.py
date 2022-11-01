import bpy
import csv, os, bmesh, math

#filepaths
filepath = bpy.data.filepath
directory = os.path.dirname(filepath)

verts = []
edges = []
faces = []

csvpoints= "C:\\test.csv"     #path name for the csv output by DataProcesser.py 
pointsReader = csv.reader(open(csvpoints, newline=''), delimiter=',')   

with open(csvpoints, 'rt', encoding="utf8") as csvfile:
    pointsReader = csv.reader(csvfile, delimiter=',')
    for idx, row in enumerate(pointsReader):
        if (idx > 0):
            vert = (float(row[0]), float(row[1]), float(row[2])) 
            verts.append(vert)

obj = bpy.context.object

#create mesh and object
mesh = bpy.data.meshes.new("wave")
object = bpy.data.objects.new("wave",mesh)

#create mesh from python data
mesh.from_pydata(verts,[],[])
mesh.update(calc_edges=True)

#set mesh location
bpy.context.scene.cursor.location = [0,0,0]
object.location = bpy.context.scene.cursor.location
bpy.data.collections["Collection"].objects.link(object)
