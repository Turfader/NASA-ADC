# This program takes the files from the csv and repackages them as an array of objects

import csv
import math
import FolderCreator as fc

DISTANCE_BETWEEN_POINTS = 40

with open(fc.testerpathfile_path, 'r') as f:
    paths = f.readlines()
    f.close()

latitude_path = paths[0].replace("\\", "/").rstrip("\n")
longitude_path = paths[1].replace("\\", "/").rstrip("\n")
height_path = paths[2].replace("\\", "/").rstrip("\n")
slope_path = paths[3].replace("\\", "/").rstrip("\n")

# Creates Lists of each Data Type from the Paths Given.
with open(latitude_path) as csv_file:
    latitude_list = list(csv.reader(csv_file, delimiter=','))
    csv_file.close()
with open(longitude_path) as csv_file:
    longitude_list = list(csv.reader(csv_file, delimiter=','))
    csv_file.close()
with open(height_path) as csv_file:
    height_list = list(csv.reader(csv_file, delimiter=','))
    csv_file.close()
with open(slope_path) as csv_file:
    slope_list = list(csv.reader(csv_file, delimiter=','))
    csv_file.close()

dataArray = []


# Call from each file instead of class specific calls.
def generate_data_array():
    if not len(longitude_list) == len(latitude_list) == len(height_list) == len(slope_list):
        print("Number of rows are inconsistent")
        return

    if not len(longitude_list[0]) == len(latitude_list[0]) == len(height_list[0]) == len(slope_list[0]):
        print("Number of columns are inconsistent")
        return

    rows = len(longitude_list)
    cols = len(longitude_list[0])
    xy_dim = len(longitude_list)

    for row in range(rows):
        for data_pt in range(cols):
            # dataArray[k][0] = Lat, dA[k][1] = long, dA[k][2] = ht, dA[k][3] = slope
            dataArray.append(
                # TODO: Double Check the Correctness of this Statement.
                [latitude_list[row][data_pt], longitude_list[row][data_pt], height_list[row][data_pt],
                 slope_list[row][data_pt]]
            )

    return xy_dim


# Helper Functions for Math
def convert_degrees_to_meters(deg):  # takes in degrees latitude
    return (30366 + 1 / 9) * (90 + float(deg))
def x_cord_from_polar(r, theta):
    return r * math.cos(float(theta) * math.pi / 180)
def y_cord_from_polar(r, theta):
    return r * math.sin(float(theta) * math.pi / 180)


def write_rect_file(data_arr):
    rect_coord_path = fc.path_sub1.replace("\\", "/") + "/ProcessedCoordinateData.csv"  # Processed Data Folder given from FolderCreator.py
    # min_x = 0
    # min_y = 0
    with open(rect_coord_path, mode="w", newline="") as datafile:
        csv_writer = csv.writer(datafile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['x cord (in meters)', 'y cord (in meters)', 'height (in meters)', 'slope (in degrees)'])
        for i in range(len(data_arr)):
            r_meters = convert_degrees_to_meters(data_arr[i][0])  # 0 is Latitude
            x = x_cord_from_polar(r_meters, data_arr[i][1])  # 1 is Longitude
            y = y_cord_from_polar(r_meters, data_arr[i][1])
            csv_writer.writerow([x, y, data_arr[i][2],  # 2 is Height
                                 data_arr[i][3]])  # 3 is Slope
        datafile.close()

    return rect_coord_path
            # if x < min_x:
            #    min_x = x
            # if y < min_y:
            #    min_y = y
    # print("min x: ", min_x)
    # print("min y: ", min_y)

def write_misc_file(min_height):
    misc_path = fc.path_sub1.replace("\\", "/") + "/MiscData.csv"

    with open(misc_path, mode="w", newline="") as f:
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([x_and_y_dim]) # Line 1
        csv_writer.writerow([DISTANCE_BETWEEN_POINTS]) # Line 2
        csv_writer.writerow([min_height]) # Line 3

    f.close()
    return misc_path

# Helper Methods for Finding Maximums and Minimums of Each Attribute of <DataArray>
def find_max_value(data_arr, attr):
    tmp = float(data_arr[0][attr])
    for i in range(len(data_arr)):
        if float(data_arr[i][attr]) > tmp:
            tmp = float(data_arr[i][attr])
    return tmp

def find_min_value(data_arr, attr):
    tmp = float(data_arr[0][attr])
    for i in range(len(data_arr)):
        if float(data_arr[i][attr]) < tmp:
            tmp = float(data_arr[i][attr])
    return tmp


# Latitude is DataArr[0], Longitude is DataArr[1], Height is DataArr[2], Slope is DataArr[3]
def find_min_height(data_arr):
    return find_min_value(data_arr, 2)
def find_max_height(data_arr):
    return find_max_value(data_arr, 2)
def find_max_lon(data_arr):
    return find_max_value(data_arr, 1)
def find_min_lon(data_arr):
    return find_min_value(data_arr, 1)
def find_max_lat(data_arr):
    return find_max_value(data_arr, 0)
def find_min_lat(data_arr):
    return find_min_value(data_arr, 0)


x_and_y_dim = generate_data_array()

absolute_min_height = find_min_height(dataArray)
absolute_max_height = find_max_height(dataArray)
abs_zero_height_scale = (abs(absolute_max_height) + abs(absolute_min_height))

rect_file_path = write_rect_file(dataArray)
misc_path = write_misc_file(absolute_min_height)
print("Data Processing Success")


# TODO: Find a plausible landing zone, and find a way for the algorithm to get between it / i.e. we nee a startpoint and an endpoint for djikstra
