# Write a program that asks the user how many numbers wants to enter and returns the average
n = int(input("How many number do you want to introduce? "))
sum_n = 0
for a in range(n):
    sum_n += float(input("Write a number "))
print("The average is ", sum_n / n)