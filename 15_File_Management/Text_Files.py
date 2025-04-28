import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir,"file.txt")

text = "Line with text\nAnother line with text"
file = open(file_path,"w")
file.write(text)
file.close()

file = open(file_path,"r")
text2 = file.read()
file.close()
print(text2)

text = text + "\nMore Lines"
file = open(file_path,"w")
file.write(text)
file.close()

file = open(file_path,"r")
text2 = file.readlines()
file.close()
print(text2)

file = open(file_path,"a")
file.write("\nAppend line")
file.close()

with open(file_path,'r') as file:
    for line in file:
        print(line)
