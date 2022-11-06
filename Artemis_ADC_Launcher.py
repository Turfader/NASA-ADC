# This program is the central hub that the other programs are run from

import subprocess
import FolderCreator as fc

# runs DataProcessor.py
data_processor_path = fc.path_sub2.replace("\\", "/") + "/DataProcessor.py"
data_processor_program = subprocess.run(["cmd", "/c", data_processor_path])

# runs Cartographer.py
cartographer_path = fc.path_sub2.replace("\\", "/") + "/Cartographer.py"
cartographer_program = subprocess.run(["cmd", "/c", cartographer_path])
