# Locate the error in the following code and create an exception to avoid the program crash
# Explain with a message the root and the solution of the error

try:
    #Original Code
    colors = {'rojo':'red', 'verde':'green','negro':'black'}
    colors['blanco']
except KeyError:
    print("Error: the element that you are trying to access do not exist")