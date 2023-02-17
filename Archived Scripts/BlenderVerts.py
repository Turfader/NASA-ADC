import bpy
import csv, os, bmesh, math

bpy.ops.object.select_all(action='SELECT')

bpy.ops.object.delete()

misc_data_path = "C:/Users/ashwa/Desktop/ADCLander/ProcessedData/MiscData.csv"

x_and_y_dims = None
dist_btw_pts = None
min_height = None

with open(misc_data_path, mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    full_list = list(csv_reader)
    print(full_list[0])
    x_and_y_dims = int(full_list[0][0])
    dist_btw_pts = float(full_list[1][0])
    min_height = float(full_list[2][0])

# filepaths
filepath = bpy.data.filepath
directory = os.path.dirname(filepath)

verts = []
edges = []
faces = []


def makePolys(input):
    if input + x_and_y_dims + 1 >= len(verts):  # work on changing out the 1277 later
        return
    if (abs(verts[input][0] - verts[(input + x_and_y_dims + 1)][0]) < (dist_btw_pts * 1.25)):
        faces.append([input, (input + x_and_y_dims + 1), input + 1])
        faces.append([input, input + x_and_y_dims, (input + x_and_y_dims + 1)])


csvpoints = "C:/Users/ashwa/Desktop/ADCLander/ProcessedData/ProcessedCoordinateData.csv"  # path name for the csv output by DataProcesser.py
# csvpoints = csvpoints.replace("\\","/")
pointsReader = csv.reader(open(csvpoints, newline=''), delimiter=',')

with open(csvpoints, 'rt', encoding="utf8") as csvfile:
    pointsReader = csv.reader(csvfile, delimiter=',')
    for idx, row in enumerate(pointsReader):
        if (idx > 0):
            vert = (float(row[0]), float(row[1]), float(row[2]) + abs(min_height))
            verts.append(vert)

for i in range(len(verts) - x_and_y_dims):
    makePolys(i)

obj = bpy.context.object
obj.scale[0] = 0.1
obj.scale[1] = 0.1
obj.scale[2] = 0.1

# create mesh and object
mesh = bpy.data.meshes.new("wave")
object = bpy.data.objects.new("wave", mesh)

# create mesh from python data
mesh.from_pydata(verts, [], faces)
mesh.update(calc_edges=True)

# set mesh location
bpy.context.scene.cursor.location = [0, 0, 0]
object.location = bpy.context.scene.cursor.location
bpy.data.collections["Collection"].objects.link(object)

# saves the file as "testBlenderProgram.blend".
# CHANGE THE PATHING TO YOUR OWN COMPUTER!!!
bpy.ops.wm.save_as_mainfile(filepath="C:/Users/ashwa/Desktop/TheMoon.blend")
