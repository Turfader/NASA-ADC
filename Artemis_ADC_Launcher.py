# This program is the central hub that the other programs are run from

import os
import subprocess


# runs DataProcessor.py

data_processor_path = os.getcwd() + "/Artemis_ADC/DataProcessor.py"
data_processor_path = data_processor_path.replace("\\", "/")
data_processor_program = subprocess.run(["cmd", "/c", data_processor_path])

# runs Cartographer.py

cartographer_path = os.getcwd() + "/Artemis_ADC/Cartographer.py"
cartographer_path = cartographer_path.replace("\\", "/")
cartographer_program = subprocess.run(["cmd", "/c", cartographer_path])
