# Do a program that reads 2 numbers by keyboard and determine the following:
# If both numbers are equal
# if both numbers are different
# if the first is greater than second
# if the second is greater or equal than first

N_1 = float(input("Introduce first number "))
N_2 = float(input("introduce second number "))

print("Are both numbers equal?", N_1 == N_2)
print("Are both numbers different?", N_1 != N_2)
print("Is first number greater than second?", N_1 > N_2)
print("Is second number greater than or equal to fisrt", N_2 >= N_1)