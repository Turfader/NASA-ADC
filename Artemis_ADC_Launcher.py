# This program is the central hub that the other programs are run from

from subprocess import run
import FolderCreator as fc

# runs DataProcessor.py
data_processor_path = fc.path_sub2.replace("\\", "/") + "/DataProcessor.py"
data_processor_program = run(["cmd", "/c", data_processor_path])

# runs Cartographer.py
cartographer_path = fc.path_sub2.replace("\\", "/") + "/Cartographer.py"
cartographer_program = run(["cmd", "/c", cartographer_path])

# runs Display.py
display_path = fc.path_sub2.replace("\\", "/") + "/Display.py"
display_program = run(["cmd", "/c", display_path])