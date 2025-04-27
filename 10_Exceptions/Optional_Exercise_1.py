# Locate the error in the following code and create an exception to avoid the program crash
# Explain with a message the root and the solution of the error

try:
    result = 10/0 #Original Code
except ZeroDivisionError:
    print("Error: It is not possible to divide by 0")

