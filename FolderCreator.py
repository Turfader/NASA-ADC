"""
FolderCreator.py makes folders and directories for all files for the FPA Team NASA
App Development Challenge Application.
"""
import os
import csv
from winreg import * # for downloads folder access

# Names
main_folder_name = "ADCLander"
sub_folder_1_name = "ProcessedData"
sub_folder_2_name = "AppFiles"
sub_folder_3_name = "RawData"
path_main = None


def find_file(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

# Ask for Path
# If Path is Invalid, Try Again until Valid Path is Entered.
while True:
    parent_path = input("Enter a installation path: ")

    if not os.path.exists(parent_path):
        print("Invalid Install Path")
        continue
    else:
        break

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
        # Lat, Long, Height, Slope [In Order]
        with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
            Downloads_Path = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]

        path_data_path = find_file(name='PathData.csv', path=Downloads_Path)
        with open(path_data_path) as csv_file:
            paths = list(csv.reader(csv_file, delimiter=','))
            csv_file.close()

            slash = "\\"
            f.write(f'{str(paths[1])[2:-2].replace(slash, "/")}\n')
            f.write(f'{str(paths[0])[2:-2].replace(slash, "/")}\n')
            f.write(f'{str(paths[2])[2:-2].replace(slash, "/")}\n')
            f.write(f'{str(paths[3])[2:-2].replace(slash, "/")}\n')
            f.write(f'{int(str(paths[4])[2:-2])}\n')


        f.close()
    # ---------------------------------------------------------------------------------------------------

except FileExistsError: # Termination Alert.
    print("Folder Exists")
    quit()


print("Installation Success")


