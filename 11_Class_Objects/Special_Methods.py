class Movie:
    # __init__ method is called Constructor too
    def __init__(self, title, length, release):
        self.title = title
        self.length = length
        self.release = release
        print("The movie {} has been created".format(self.title))

    # Class destructor
    def __del__(self):
        print("The movie {} has been deleted".format(self.title))

    # Redefinition of str method
    def __str__(self):
        return "{} released in {} and {} minutes length".format(self.title, self.release, self.length)
    
    # Redefinition of len method
    def __len__(self):
        return self.length

GF = Movie("The Goodfather", 175, 1972)
print(str(GF))                  # str method redefined
print(len(GF))                  # len method redefined
del(GF)
