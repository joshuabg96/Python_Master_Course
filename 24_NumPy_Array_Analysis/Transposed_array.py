import numpy as np

arr = np.array([[1,2,3],[4,5,6]])

print(arr, '\n')
print(arr.T, '\n')

# swapaxes, chage the rows with the columns

print(arr.swapaxes(1,0))