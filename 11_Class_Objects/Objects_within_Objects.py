class Movie:
    # Class constructor
    def __init__(self, title, lenght, release):
        self.title = title
        self.lenght = lenght
        self.release = release
        print("The movie {} has been created".format(self.title))

    def __str__(self):
        return '{} ({})'.format(self.title, self.release)

class Catalog:
    Movies = []
    def __init__(self, movies = []):
        self.Movies = movies
    
    def Add_Movie(self, Movie):
        self.Movies.append(Movie)

    def show_Movies(self):
        for Movie in self.Movies:
            print(Movie)
        

GF = Movie("The Goodfather", 175, 1972)
C = Catalog([GF])
C.Add_Movie(Movie("The Goodfather 2", 202, 1974))

C.show_Movies()