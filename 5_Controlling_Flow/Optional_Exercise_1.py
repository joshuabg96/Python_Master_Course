# Create a program that reads two numbers by keyboard and allow to choose 
# 3 different menu options
# 1) Show the sum between both numbers
# 2) Show the substraction between both numbers
# 3) Show the multiplication between both numbers
# Any different option the program will show that the option is incorrect

n1 = float(input("introduce first number "))
n2 = float(input("introduce second number "))

print("Choose one option of the menu")
print("1) Show the sum between both numbers")
print("2) Show the substraction between both numbers")
print("3) Show the multiplication between both numbers")
option = int(input())

match option:
    case 1:
        print("The operation ", n1, " + ", n2, " = ", n1 + n2)
    case 2:
        print("The operation ", n1, " - ", n2, " = ", n1-n2)
    case 3:
        print("The operation ", n1, " * ", n2, " = ", n1*n2)
    case _:
        print("The option is incorrect")