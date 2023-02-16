"""
FolderCreator.py makes folders and directories for all files for the FPA Team NASA
App Development Challenge Application.
"""
import os
import csv

import tkinter as tk
from tkinter import messagebox


# Names
main_folder_name = "ADCLander"
sub_folder_1_name = "ProcessedData"
sub_folder_2_name = "AppFiles"
sub_folder_3_name = "RawData"
path_main = None

def show_error(err_type):
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror('ADC Lander Installation Error', err_type)

def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

# Defaults to User's Desktop as the Installation Location
parent_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

# Terminates all operations if the files exist.
try:

    path_main = os.path.join(parent_path, main_folder_name)
    os.mkdir(path_main)

    # Add the Subfolder Paths and Directories
    path_sub1, path_sub2, path_sub3 = os.path.join(path_main, sub_folder_1_name), os.path.join(path_main, sub_folder_2_name), os.path.join(path_main, sub_folder_3_name)
    os.mkdir(path_sub1)
    os.mkdir(path_sub2)
    os.mkdir(path_sub3)

    # THIS SECTION WILL NOT BE IN THE FINAL PRODUCT --------------------------
    # datanames = ['RegHeight.csv', 'RegLat.csv', 'RegLong.csv', 'RegSlope.csv']
    # for file in datanames:
    #    sh.copy(file, raw_path_sub1)
    # ------------------------------------------------------------------------

    # Add the Data File
    textfile_path = os.path.join(path_sub2, "RunnerData")
    with open(textfile_path, 'w') as f:
        f.write(
            f"Folder Created.\n{path_main}\n{path_sub1}\n{path_sub2}\n{path_sub3}\n".replace("\\", "/"))
        f.close()


    # THESE LINES IMITATE THE FUNCTIONS OF PathFinder.cp, AND SHOULD BE REMOVED IN THE FINAL PRODUCT ----
    pathfile_path = os.path.join(path_sub3, "Paths to Data.txt")
    with open(pathfile_path, 'w') as f:
        path_data_path = find_file(name='PathData.csv', path=os.getcwd())
        with open(path_data_path) as csv_file:
            paths = list(csv.reader(csv_file, delimiter=','))
            csv_file.close()
            # Lat, Long, Height, Slope [In Order]
            slash = "\\"
            f.write(f'{str(paths[1])[2:-2].replace(slash, "/")}\n')
            f.write(f'{str(paths[0])[2:-2].replace(slash, "/")}\n')
            f.write(f'{str(paths[2])[2:-2].replace(slash, "/")}\n')
            f.write(f'{str(paths[3])[2:-2].replace(slash, "/")}\n')
            f.write(f'{int(str(paths[4])[2:-2])}\n')


        f.close()
    # ---------------------------------------------------------------------------------------------------

except FileExistsError: # Termination Alert.
    show_error("Folder Already Exists on " + parent_path)
    quit()

print("Installation Success")


