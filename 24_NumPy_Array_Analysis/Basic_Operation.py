import numpy as np

# Two array
arr_1 = np.array([1,2,3,4])
arr_2 = np.array([5,6,7,8])

#sum
print(arr_1 + arr_2)

# If the arrays do not have the same size we can not sum it
arr_3 = np.array([1,2])

#print(arr_1 + arr_3)

#Rest
print(arr_2-arr_1)

# Multiply 
print(arr_1*arr_2)

# Multiply by a number
print(arr_1*10)

#Divide
print(arr_1/arr_2)

#Divide by a number
print(arr_1/2)

# Inverse of the array
print(1 / arr_1)

# Power inverse
print(arr_1 ** -1.)

# power of two arrays
print(arr_1 ** arr_2)

# 2D array operations
arr_4 = np.array([[1,2],[3,4]])
arr_5 = np.array([[5,6],[7,8]])

print(arr_4 + arr_5)

print(arr_5 * 3)