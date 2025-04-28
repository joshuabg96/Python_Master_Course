# Create an script called people.py that reads the data of a txt file that convert every file in a dicctionary y add it to a list called people, after that print the list in a nice way
# people.txt will have the following text
# 1;Carlos;Pérez;05/01/1989
# 2;Manuel;Heredia;26/12/1973
# 3;Rosa;Campos;12/06/1961
# 4;David;García;25/07/2006
#
# The dicctionary will have the following data id, name, last name, born date

import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir,"People.txt")

contacts = []

with open(file_path,'r', encoding='utf8') as file:
    for line in file:
        data = line.split(";")
        person = {"id":data[0], "name":data[1], "Last Name":data[2], "Born date":data[3]}
        contacts.append(person)

for person in contacts:
    print("id: {}) {} {} -> {}".format(person["id"], person["name"],person["Last Name"],person["Born date"]))


