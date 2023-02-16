# This program is the central hub that the other programs are run from

from subprocess import run
import os


# runs DataProcessor.py
data_processor_path = fc.path_sub2.replace("\\", "/") + "/DataProcessor.py"
data_processor_program = run(["cmd", "/c", data_processor_path])

# runs Cartographer.py
cartographer_path = fc.path_sub2.replace("\\", "/") + "/Cartographer.py"
cartographer_program = run(["cmd", "/c", cartographer_path])
