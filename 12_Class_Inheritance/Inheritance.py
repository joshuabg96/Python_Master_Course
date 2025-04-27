# The inheritance allows us to create a new class (son) based on another class that  already exist, the son class inherits all the attributes and methods from the father class but son class can add or modify their own methods and attributes.

# Super Class or the Father Class
class Product:
    def __init__(self, reference, type, name, price, description):
        self.reference = reference
        self.type = type
        self.name = name
        self.price = price
        self.description = description
    
    def __str__(self):
        return """
        Reference\t{}
        Name\t{}
        PVP\t{}
        Description\t{}""".format(self.reference, self.name, self.price, self.description)


# SubClass or Son class, we are going to pass Product as father class that will be inheriting all the methods and attributes to Son class
class Ornament(Product):
    pass

class Food(Product):
    manufacturer = ''
    distributor = ''

    def __str__(self):
        return """
        Reference\t{}
        Name\t{}
        PVP\t{}
        Description\t{}
        Manufacturer\t{}
        Distributor\t{}""".format(self.reference, self.name, self.price, self.description, self.manufacturer, self.distributor)

class Book(Product):
    ISBN = ''
    Author = ''
    def __str__(self):
        return """
        Reference\t{}
        Name\t{}
        PVP\t{}
        Description\t{}
        ISBN\t{}
        Author\t{}""".format(self.reference, self.name, self.price, self.description, self.ISBN, self.Author)

Orn = Ornament(2034, "Ornament", "Ornamented glass", 15, "Glass")
print(Orn)

F = Food(2035, "Olive Oil", 5, "250 ML")
F.manufacturer = "International Oil"
F.distributor = "Oil Distributor"
print(F)

Bo = Book(2036, "Cooking with granMa", 9,"Recipe book")
Bo.ISBN = "0.1234"
Bo.Author = "Jessica"      
print(Bo)  