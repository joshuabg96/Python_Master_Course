# Attributes: All the variables that has an object
# Methods: All the function that has an object

class Cookie:
    chocolate = False       # This is an attribute

    # As soon as a new object of this class has been created the __init__ Method is executed
    def __init__(self, flavor = None, color = None):  # We can pass some attributes that can be necessary when we make a new class instance, but if we initiallize this attributes we can use it without the need of give this attributes
        self.flavor = flavor        # We need self. to reference to class attributes
        self.color = color          # We need self. to reference to class attributes
        if self.flavor != None and self.color != None:
            print("Cookie has been created {} and {}".format(flavor, color))

    def Put_Chocolate(self):
        self.chocolate = True   # self. has to be used to reference to all the attributes of the class

    def Check_Chocolate(self):
        if self.chocolate:
            print("The Cookie has chocolate")
        else:
            print("The Cookie doesn't have chocolate")
        

C_1 = Cookie("Salty", "Brown")

print(C_1.chocolate)        # False
C_1.chocolate = True        # Modify attribute chocolate
print(C_1.chocolate)        # True
print("\n")

C_1.chocolate = False       # Modify attribute chocolate
print(C_1.chocolate)        # False
C_1.Put_Chocolate()         # Call the Method Put_Chocolate()
print(C_1.chocolate)        # True
print("\n")


C_1.chocolate = False       # Modify attribute chocolate
print(C_1.chocolate)        # False
C_1.Put_Chocolate()         # Call the Method Put_Chocolate()
C_1.Check_Chocolate()
print("\n")

