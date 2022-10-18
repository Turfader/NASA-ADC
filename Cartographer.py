# This program is used to create the heightmap and slope map from the data

import csv
import os


rect_coord_path = os.getcwd() + "/Raw Data/Rectangular Coordinate Data.csv"
rect_coord_path = rect_coord_path.replace("\\", "/")
with open(rect_coord_path, mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    full_list = list(csv_reader)

# The following function is obsolete, but I am keeping it in for reference
def calculate_color(height):
    color = ((height+2872)*255/4830)
    return int(color), int(color), int(color)
# data is being lost by saving as an int ^^


### Image drawing ###


width, height = (1278, 1278)


def generate_heightmap():
    for i in range(1, len(full_list)):
        x_pos = ((float(full_list[i][0])) + 31062.917916580405)/40  # This section of code still needs a little work. The /40 is used for 
        # compressing it into an image without empty space. IDK how we'll want to port this into blender.
        y_pos = ((float(full_list[i][1])) + 12036.902076767392)/40
        # The following line of code does not work yet. We need to add the minimum height still
        #height = ((float(full_list[i][2])) + ###min height###)
        color = calculate_color(float(full_list[i][2]))  # this line of code is obsolete, but I am keeping it in for reference
        print()
        print(i)
        print(x_pos, x_pos//1)  # the whole number rounding is a product of impercision. This section needs to be looked at again.
        print(y_pos, y_pos//1)
        print(color)

        data[x_pos//1, y_pos//1] = color
