# Locate the error in the following code and create an exception to avoid the program crash
# Explain with a message the root and the solution of the error

try:
    #original Code
    result = "20" + 15
except TypeError:
    print("Error: You can not concatenate string and int")