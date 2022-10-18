# This program takes the files from the csv and repackages them as an array of objects

import csv
import math
import os


latitude_path = os.getcwd() + "/Raw Data/fy20-adc-regional-data-file-latitude/" \
                              "FY20 ADC Regional Data File LATITUDE.csv"
latitude_path = latitude_path.replace("\\", "/")
with open(latitude_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    latitude_list = list(csv_reader)


longitude_path = os.getcwd() + "/Raw Data/fy20-adc-regional-data-file-longitude/" \
                               "FY20 ADC Regional Data File LONGITUDE.csv"
longitude_path = longitude_path.replace("\\", "/")
with open(longitude_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    longitude_list = list(csv_reader)


height_path = os.getcwd() + "/Raw Data/fy20-adc-regional-data-file-height/" \
                               "FY20 ADC Regional Data File HEIGHT.csv"
height_path = height_path.replace("\\", "/")
with open(height_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    height_list = list(csv_reader)


slope_path = os.getcwd() + "/Raw Data/fy20-adc-regional-data-file-slope/" \
                           "FY20 ADC Regional Data File SLOPE.csv"
slope_path = slope_path.replace("\\", "/")
with open(slope_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    slope_list = list(csv_reader)


dataArray = []


class DataPoint:

    def __init__(self, lat, lon, hei, slo):
        self.latitude = float(lat)
        self.longitude = float(lon)
        self.height = float(hei)
        self.slope = float(slo)

    def get_lat(self):
        return self.latitude

    def get_lon(self):
        return self.longitude

    def get_height(self):
        return self.height

    def get_slope(self):
        return self.slope

    def print_data(self):
        print(f"Latitude: {self.latitude}")
        print(f"Longitude: {self.longitude}")
        print(f"Height: {self.height}")
        print(f"Slope: {self.slope}")


def generate_data_array():
    if not len(longitude_list) == len(latitude_list) == len(height_list) == len(slope_list):
        print("Number of rows are inconsistent")
        return

    if not len(longitude_list[0]) == len(latitude_list[0]) == len(height_list[0]) == len(slope_list[0]):
        print("Number of columns are inconsistent")
        return

    number_of_rows = len(longitude_list)
    number_of_col = len(longitude_list[0])

    for row in range(number_of_rows):  # Replace 1 with number_of_rows
        for data_pt in range(number_of_col):
            dataArray.append(DataPoint(latitude_list[row][data_pt], longitude_list[row][data_pt],
                                       height_list[row][data_pt], slope_list[row][data_pt]))


def convert_degrees_to_meters(deg):  # takes in degrees latitude
    return (30366+1/9) * (90 + deg)


def x_cord_from_polar(r, theta):
    return r * math.cos(theta * math.pi / 180)


def y_cord_from_polar(r, theta):
    return r*math.sin(theta*math.pi/180)


def write_rect_file(dataArr):
    rect_coord_path = os.getcwd() + "/Raw Data/Rectangular Coordinate Data.csv"
    rect_coord_path = rect_coord_path.replace("\\", "/")
    min_x =0
    min_y = 0
    with open(rect_coord_path, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(['x cord (in meters)', 'y cord (in meters)', 'height (in meters)', 'slope (in degrees)'])
        for i in range(len(dataArr)):
            r_meters = convert_degrees_to_meters(dataArr[i].latitude)
            x = x_cord_from_polar(r_meters, dataArr[i].longitude)
            y = y_cord_from_polar(r_meters, dataArr[i].longitude)
            csv_writer.writerow([x, y, dataArr[i].height,
                                 dataArr[i].slope])
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y
    print("min x: ", min_x)
    print("min y: ", min_y)


def find_min_height(dataArr):
    temp_min_height = float(dataArr[0].height)
    for i in range(len(dataArr)):
        if float(dataArr[i].height) < temp_min_height:
            temp_min_height = float(dataArr[i].height)
    return temp_min_height


def find_max_height(dataArr):
    temp_max_height = float(dataArr[0].height)
    for i in range(len(dataArr)):
        if float(dataArr[i].height) > temp_max_height:
            temp_max_height = float(dataArr[i].height)
    return temp_max_height


def find_max_lon(dataArr):
    temp_max_lon = float(dataArr[0].longitude)
    for i in range(len(dataArr)):
        if float(dataArr[i].longitude) > temp_max_lon:
            temp_max_lon = float(dataArr[i].longitude)
    return temp_max_lon


def find_min_lon(dataArr):
    temp_min_lon = float(dataArr[0].longitude)
    for i in range(len(dataArr)):
        if float(dataArr[i].longitude) < temp_min_lon:
            temp_min_lon = float(dataArr[i].longitude)
    return temp_min_lon


def find_max_lat(dataArr):
    temp_max_lat = float(dataArr[0].latitude)
    for i in range(len(dataArr)):
        if float(dataArr[i].latitude) > temp_max_lat:
            temp_max_lat = float(dataArr[i].latitude)
    return temp_max_lat


def find_min_lat(dataArr):
    temp_min_lat = float(dataArr[0].latitude)
    for i in range(len(dataArr)):
        if float(dataArr[i].latitude) < temp_min_lat:
            temp_min_lat = float(dataArr[i].latitude)
    return temp_min_lat


generate_data_array()


absolute_min_height = find_min_height(dataArray)
absolute_max_height = find_max_height(dataArray)
abs_zero_height_scale = (abs(absolute_max_height)+abs(absolute_min_height))

write_rect_file(dataArray)
