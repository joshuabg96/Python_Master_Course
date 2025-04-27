# Create a class called point with two coordenates x and Y
# Add a constructor Method to create points easilly if a coordenate is not received its value will be 0
# Overwrite string method to print the point at format (X,Y)
# Add a method called quadrant that indicate the quadrant that it belows
# Add a method called vector that takes another point and calculate the resultant vector
# Add a method called distance that takes another point and calculate the distan between points, the formula is the following d=sqrt((x2-x1)^2 + (y2-y1)^2)

import math

class Point():
    def __init__(self, X = 0, Y = 0):
        self.X = X
        self.Y = Y

    def __str__(self):
        return "({},{})".format(self.X, self.Y)
    
    def quadrant(self):
        if self.X >= 0:
            if self.Y >= 0:
                print("The point is at the first quadrant")
            else:
                print("The point is at third quadrant")
        else:
            if self.Y >= 0:
                print("The point is in the second quadrant")
            else:
                print("The point is in the fourth quadrant")
    
    def vector(self, point):
        print("The resultant vector is ({},{})".format(point.X - self.X, point.Y - self.Y))
    
    def distance(self, point):
        print("The distance from points is {}".format(math.sqrt(((point.X - self.X)** 2) +  ((point.Y - self.Y))**2))) 

P1 = Point(2,3)
P2 = Point(5,5)
P3 = Point(2,-1)
P4 = Point(-2,1)
P5 = Point(-1,-1)

print(str(P1))
print(str(P2))

P1.quadrant()
P3.quadrant()
P4.quadrant()
P5.quadrant()

P1.vector(P2)

P1.distance(P2)
