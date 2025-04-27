# Locate the error in the following code and create an exception to avoid the program crash
# Explain with a message the root and the solution of the error

try:
    #Original Code
    L = [1,2,3,4,5]
    L[10]
except IndexError:
    print("Error: The index that you are trying to access do not exist")
