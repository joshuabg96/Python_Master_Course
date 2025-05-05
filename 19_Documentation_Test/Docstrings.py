def Hi(arg):
    """This is the docstring of the function"""
    print("Hi", arg, "!")

Hi("Josué")

help(Hi)

class Clase:
    """This is the docstring of the class"""
    def __init__(self):
        """This is the docstring of the init of the class"""
        pass

    def method(self):
        """This is the docstring of the class method"""
        pass

o = Clase()
help(o)