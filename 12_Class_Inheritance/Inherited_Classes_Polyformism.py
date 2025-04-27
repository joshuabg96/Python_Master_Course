#Inherited Classes: In this example we have Product as father class or super class and Ornament, Food and Book is the subclass or son class, so this subclass are inherating all the characteristics of Product super class and we can use it as we are using Product class

#Polyformism: In this case the polyformism is when we use the same method but in a different way, for exampel here we are using __str__ method bu redefined at Food and Book class because we need to show different information even with the same method.
class Product:
    def __init__(self, reference, name, price, description):
        self.reference = reference
        self.name = name
        self.price = price
        self.description = description
    
    def __str__(self):
        return """
        Reference\t{}
        Name\t{}
        PVP\t{}
        Description\t{}""".format(self.reference, self.name, self.price, self.description)

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
    
def Discount(p, discount):
    import copy
    # Return a product with a discount
    P_copy = copy.copy(p)
    P_copy.price = P_copy.price - (P_copy.price/100 * discount)
    return P_copy
    
Orn = Ornament(2034, "Ornamented glass", 15, "Glass")

F = Food(2035, "Olive Oil", 5, "250 ML")
F.manufacturer = "International Oil"
F.distributor = "Oil Distributor"

Bo = Book(2036, "Cooking with granMa", 9,"Recipe book")
Bo.ISBN = "0.1234"
Bo.Author = "Jessica"

Products = [Orn, F]
Products.append(Bo)

#for p in Products:
#    print(p,"\n")

for p in Products:
    if( isinstance(p,Ornament)):
        print(p.reference, p.name)
    elif isinstance(p,Food):
        print(p.reference, p.name, p.manufacturer)
    elif isinstance(p,Book):
        print(p.reference, p.name, p.ISBN)

# BE carefull because the Objects are given as a reference, so if you are modifying one attribute in another function, you would modify it the original object not a copy
# If you want to copy a object you have to use the library copy and the method copy.copy(Object)
Product_discount = Discount(F, 10)
print(Product_discount)             # Copy of F with the discount
print(F)                            # Original F without the discount