# note that this file primarily tests locations for files and creates new file locations.

import os # mkdir and Pathing
import shutil as sh # Shell Utility for File Copy from Project

# Names
main_folder_name = "ADCLander"
sub_folder_1_name = "ProcessedData"
sub_folder_2_name = "FilesMisc"
sub_folder_3_name = "RawData"
path_main = None

# Ask for Path
parent_dir = input("Enter a installation path: ")

# Terminates all operations if the files exist.
try:
    # Create the Main Folder
    try:
        path_main = os.path.join(parent_dir, main_folder_name)
        os.mkdir(path_main)
    except FileNotFoundError:
        print("Invalid Path")

    # Add the Subfolder Paths and Directories
    path_sub1, path_sub2, path_sub3 = os.path.join(path_main, sub_folder_1_name), os.path.join(path_main, sub_folder_2_name), os.path.join(path_main, sub_folder_3_name)
    os.mkdir(path_sub1)
    os.mkdir(path_sub2)
    os.mkdir(path_sub3)

    # Add the Raw Data Path
    raw_path_sub1 = os.path.join(path_sub3, "RegionalData")
    os.mkdir(raw_path_sub1)

    # THIS SECTION WILL NOT BE IN THE FINAL PRODUCT --------------------------
    datanames = ['RegHeight.csv', 'RegLat.csv', 'RegLong.csv', 'RegSlope.csv']
    for file in datanames:
        sh.copy(file, raw_path_sub1)
    # ------------------------------------------------------------------------

    # Add the Data File
    textfile_path = os.path.join(path_sub2, "RunnerData")
    with open(textfile_path, 'w') as f:
        f.write(
            f"Folder Created.\n{path_main}\n{path_sub1}\n{path_sub2}\n{path_sub3}\n{raw_path_sub1}/".replace("\\", "/"))
        f.close()

except FileExistsError: # Termination Alert.
    print("Folder Exists")


