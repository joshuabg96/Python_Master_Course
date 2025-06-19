import numpy as np

arr = np.arange(0,50,5)     #0 to 50 increasing by 5

print(arr)

print(arr[0])
print(arr[-1])
print(arr[4])

arr[-1] = 99
print(arr)

# Slicing
arr_1 = arr[:]          # Copy by reference

arr_1 = arr[:3]         # Copy of 3 elements

arr_1 = arr[1:-1] = 50  # Changing elements

arr_2 = arr[0:4].copy()       # Copying the elements of the array
arr_2[:] = 5

print(arr_2)
print(arr)