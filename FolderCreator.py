"""
FolderCreator.py makes folders and directories for all files for the FPA Team NASA
App Development Challenge Application.
"""
import os

# Names
main_folder_name = "ADCLander"
sub_folder_1_name = "ProcessedData"
sub_folder_2_name = "AppFiles"
sub_folder_3_name = "RawData"
path_main = None


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
    testerpathfile_path = os.path.join(path_sub3, "TestPaths")
    with open(testerpathfile_path, 'w') as f:
        # Long, Lat, Height, Slope [In Order]
        f.write("C:/Users/ashwa/Downloads/RegLong.csv\n")
        f.write("C:/Users/ashwa/Downloads/RegLat.csv\n")
        f.write("C:/Users/ashwa/Downloads/RegHeight.csv\n")
        f.write("C:/Users/ashwa/Downloads/RegSlope.csv\n")
        f.close()
    # ---------------------------------------------------------------------------------------------------

except FileExistsError: # Termination Alert.
    print("Folder Exists")
    quit()


print("Installation Success")


