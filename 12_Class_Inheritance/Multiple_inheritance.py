# Multiple Inheritance: It is the possibility to inheritate from two or more super classes, however, we have the problem if we have the same methods in two or more super classes that we are inheritating, but python solve this situation giving priority to the first superclass that is at left 

class A:
    def __init__(self):
        print("Class A")
    def a(self):
        print("A")

class B:
    def __init__(self):
        print("Class B")
    def b(self):
        print("B")

class C(A,B):
    def c(self):
        print("C")

class D(B,A):
    pass

c = C()         # Here the __init__ priority is the A becase it is first at the inheritate
d = D()         # Here the __init__ priority is the B becase it is first at the inheritate

c.a()           # inherated from A
c.b()           # Inherated from B
c.c()           # own method


