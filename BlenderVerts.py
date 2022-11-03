import bpy
import csv, os, bmesh, math

#filepaths
filepath = bpy.data.filepath
directory = os.path.dirname(filepath)

verts = []
edges = []
faces = []


def makePolys(input):

    if input + 1277 + 1 >= len(verts): # work on changing out the 1277 later
        return
    if (abs(verts[input][0] - verts[(input+1277+1)][0]) < 45):
        faces.append([ input, (input+1277+1), input+1 ])
        faces.append([ input, input+1277, (input+1277+1) ])

csvpoints= "C:/Users/Owner/PycharmProjects/NASA_Artemis_ADC/Artemis_ADC/Raw Data/Rectangular Coordinate Data.csv"     #path name for the csv output by DataProcesser.py 
pointsReader = csv.reader(open(csvpoints, newline=''), delimiter=',')   

with open(csvpoints, 'rt', encoding="utf8") as csvfile:
    pointsReader = csv.reader(csvfile, delimiter=',')
    for idx, row in enumerate(pointsReader):
        if (idx > 0):
            vert = (float(row[0]), float(row[1]), float(row[2])+3000) 
            verts.append(vert)
            

for i in range(len(verts)-1277):
    makePolys(i)


obj = bpy.context.object

#create mesh and object
mesh = bpy.data.meshes.new("wave")
object = bpy.data.objects.new("wave",mesh)

#create mesh from python data
mesh.from_pydata(verts,[],faces)
mesh.update(calc_edges=True)

#set mesh location
bpy.context.scene.cursor.location = [0,0,0]
object.location = bpy.context.scene.cursor.location
bpy.data.collections["Collection"].objects.link(object)
