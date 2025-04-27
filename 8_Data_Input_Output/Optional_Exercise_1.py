# Apply a format to the following values to show the result
# - "Hola Mundo" Right in 20 characters
# - "Hola Mundo" Truncation of the fourth character
# - "Hola Mundo" Center in 20 character and truncation in second character
# - 150 Format 5 integer numbers filled with 0's
# - 7887 Format 7 interger number filled with spaces
# - 20.02 Format 3 integers and 3 decimal

print("{:>20}".format("Hola Mundo"))
print("{:.3}".format("Hola Mundo"))
print("{:^20.1}".format("Hola Mundo"))
print("{:05d}".format(150))
print("{:7d}".format(7887))
print("{:07.3f}".format(20.02))