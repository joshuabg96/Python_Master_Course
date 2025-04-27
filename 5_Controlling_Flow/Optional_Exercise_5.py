# We have a list of numbers, ask the user a number between 0 and 9 and 
# if the number is not in the list repit the process

numbers = [1, 3, 6, 9]
number = -1
while number not in numbers:
    number = int(input("Give me a number "))
