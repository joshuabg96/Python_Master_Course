import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir,"file.txt")

file = open(file_path, 'r')
file.seek(10)
text = file.read()
print(text)

file.seek(0)
text = file.read()
print(text)

file.seek(0)
text = file.read(5)
print(text)

file.close()