# Create a script called counter.py that do some task in a file called counter.txt that store a visitor counter
# Check if the file does not exist or is empty in that case we are going toi create it with 0, otherwise we are going to read the value
# with a given argument you are going to do different task
# - inc = increase the counter +1 and show by screen 
# - dec = decrease the counter -1 and show by screen
# - none or different to inc or dec = show the value by screen

import os
from io import open
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir,"Counter.txt")

file = open(file_path, "a+")
file.seek(0)
data = file.readline()

if len(data) == 0:
    data = "0"
    file.write(data)

file.close()

try:
    counter = int(data)
    if (len(sys.argv) == 2):
        if sys.argv[1] == "inc":
            counter += 1
        elif sys.argv[1] == "dec":
            counter -= 1

    print(counter)
    file = open(file_path, "w")
    file.write(str(counter))
    file.close()
except:
    print("Error: File is corrupted")

