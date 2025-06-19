import numpy as np

arr = np.arange(1,7).reshape(2,3)

print(arr)

# Sum
print(arr.sum())

# middle
print(arr.mean())

# Standard deviation
print(arr.std())

# 
print(arr.var())


# Sort Methods
arr = np.random.randint(-10,10,[3,3])

print(arr)

# Sort horizontally
arr.sort()
print(arr)

# Sort vertically
arr.sort(0)
print(arr)