import json
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir,"contacts.json")

contacts = [
    ("Manuel", "Web Developer","manuel@example.com"),
    ("Lorena", "Scrum master", "lorena@example.com"),
    ("Javier", "Data Analyst", "javier@example.com"),
    ("Marta", "Python Expert", "marta@example.com")
]

data = []

for name, role, email in contacts:
    data.append({"name":name, "role":role, "email":email})

with open(file_path, "w") as jsonfile:
    json.dump(data, jsonfile)

data = []
with open(file_path) as jsonfile:
    data = json.load(jsonfile)
    for contact in data:
        print(contact["name"], contact["role"], contact["email"])