# Create a program that sum all the even interger number from 0 to 100
suma = 0
for i in range(2, 101, 2):
    suma += i

#Second way
suma = sum(range(0,101, 2))
print("The sum is ", suma)