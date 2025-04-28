import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir,"contacts.csv")

contacts = [
    ("Manuel", "Web Developer","manuel@example.com"),
    ("Lorena", "Scrum master", "lorena@example.com"),
    ("Javier", "Data Analyst", "javier@example.com"),
    ("Marta", "Python Expert", "marta@example.com")
]

with open(file_path,"w", newline='\n') as csvfile:
    write = csv.writer(csvfile, delimiter=",")
    for contact in contacts: 
        write.writerow(contacts)

with open(file_path, newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for contact in reader:
        print(contact)