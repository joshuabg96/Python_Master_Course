# Write a program that meet the following points
# Create the variable "magic_number" with the following number 12345679
# Read a variable "user_number" between 1 - 9
# Multiply user_number by 9
# Multiply magic_number by user_number
# show the magic_number

magic_number = 12345679
user_number = int(input("Write a number between 1 and 9 "))
user_number *= 9
magic_number *= user_number
print("Magic Number", magic_number)