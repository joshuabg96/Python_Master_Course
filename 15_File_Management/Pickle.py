import pickle
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir,"file.pckl")
file_path_2 = os.path.join(script_dir,"People.pckl")

L_1 = [1,2,3,4,5]
file = open(file_path, 'wb')

pickle.dump(L_1, file)

file = open(file_path, 'rb')
L2 = pickle.load(file)

print(L2)
file.close()

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
    
names = ["Hector", "Mario", "Marta"]
people = []
for n in names:
    p = Person(n)
    people.append(p)

file = open(file_path_2, 'wb')
pickle.dump(people, file)

file.close()

file = open(file_path_2, 'rb')
L2 = pickle.load(file)
file.close()
for p in L2:
    print(p)