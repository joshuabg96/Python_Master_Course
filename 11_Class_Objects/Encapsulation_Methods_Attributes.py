# Encapsulation = Hide some attributes or methods and you can identify it with "__" at the beginin of the variable name.

class Example:
    __Private_Attribute = "Private Attribute"
    
    def __Private_Method(self):
        print("Private Method")

    def Return_Private_Attribute(self):
        return self.__Private_Attribute
    
    def Return_Private_Method(self):
        self.__Private_Method()

E = Example()
try:
    print(E.__Private_Attribute)
except:
    print("The private Attribute could not be reached due to it is encapsulated")

try:
    E.__Private_Method
except:
    print("The Private method could not be reached becase it is encapsulated")

# With Public Methods we can access private attributes
print(E.Return_Private_Attribute())

# With Public Methods we can access private Methods
E.Return_Private_Method()