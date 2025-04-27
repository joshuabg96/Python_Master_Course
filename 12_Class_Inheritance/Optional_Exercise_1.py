# Create a superclass called Vehicle that has two subclasses Car and Bicicle
# Car will have two extra attributes Speed and cilinders
# Bicicle will have 1 extra attribute type (urban, sport)
# Car will have a subclass called truck that will have an extra attribute called load
# Bicicle will have a subclass called motorcicle with 2 extra attributes called speed and cilinder.

# Create one object of every subclass and add it to a list called vehicles
# create a function called catalog that recive the list of vehicles and show the name, class and attributes of each vehicle 
# modify the function catalog that receive an extra argument called wheels that only shows the vehicles that meet the number of wheel selected and show "{} Vehicles with {} wheels found" test it with 0,2 and 4 as value

class Vehicle:
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels

    def __str__(self):
        return "color {}, {} wheels".format(self.color, self.wheels)
    
class Car(Vehicle):
    def __init__(self, color, wheels, speed, cilinders):
        # Make it simple, call the constructor of the super class and assign the attributes
        # or we can use Vehicle.__init__(self, color, wheels) 
        super().__init__(color, wheels)                 
        # We only have to add the extra attributes
        self.speed = speed
        self.cilinders = cilinders
    
    def __str__(self):
        return Vehicle.__str__(self) + ", {} km/h, {} cc".format(self.speed, self.cilinders)


class Truck(Car):
    def __init__(self, color, wheels, speed, cilinders, load):
        super().__init__(color, wheels, speed, cilinders)
        self.load = load
    
    def __str__(self):
        return super().__str__() + " {} load".format(self.load)
    
class Bycicle(Vehicle):
    def __init__(self, color, wheels, type):
        super().__init__(color, wheels)
        self.type = type

    def __str__(self):
        return super().__str__() + " {} type".format(self.type)
    
class Motocycle(Bycicle):
    def __init__(self, color, wheels, type, speed, cylinder):
        super().__init__(color, wheels, type)
        self.speed = speed
        self.cylinder = cylinder

    def __str__(self):
        return super().__str__() + " {} km/h, {} cylinder".format(self.speed, self.cylinder)
    
def Catalog(List, wheels = None):
    counter = 0
    for vehicle in List:
        if wheels != None:
            if vehicle.wheels == wheels:
                counter += 1
        else:
            print("{} {}".format(type(vehicle).__name__, vehicle))
    if wheels != None:
        print("{} Vehicles with {} wheels found".format(counter,wheels))

Vehicles = []
    
c = Car("Blue", 4, 150, 4)
t = Truck("Red", 6, 80, 6, 1000)
b = Bycicle("Brown", 2, "Sport")
m = Motocycle("Green", 2, "urban", 100, 1200)

Vehicles.append(c)
Vehicles.append(t)
Vehicles.append(b)
Vehicles.append(m)

Catalog(Vehicles, 0)