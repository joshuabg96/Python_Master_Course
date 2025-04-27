# Create a module called operations it will include sum, substraction, product and division
# The functions of the module shall be error management including
#   TypeError
#   ZeroDivisionError
# Ones the module has been created, execute the following opeartions.

from Operations import * 

a,b,c,d = (10,5,0,"Hola")
print("{} + {} = {}".format(a,b,M_Sum(a,b)))
print("{} - {} = {}".format(b,d,M_Sub(b,d)))
print("{} * {} = {}".format(b,b,M_Pro(b,b)))
print("{} / {} = {}".format(a,c,M_Div(a,c)))