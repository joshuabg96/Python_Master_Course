import numpy as np

# number between 0,1
print(np.random.rand())

# Array 1D between 0,1, four values
print(np.random.rand(4))

# Array 2D between 0,1, four values, 2 dimensions
print(np.random.rand(4,2))

# Array 3D between 0 and N Ex: 0-10
print(np.random.uniform(10, size=[2,2,2]))

# Array 4D between -N and N Ex: 0-10
print(np.random.uniform(-10,10, size=[2,2,2,2]))

# Integer number between 0 and N
print(np.random.randint(10))

# Array of integers between 0 and N
print(np.random.randint(10, size=[3,2]))

# Array of integers between -N and N
print(np.random.randint(-10, 10, size=[3,2]))


# Permutation
arr = np.arange(10)

print(arr)

# Unsorted array
np.random.shuffle(arr)
print(arr)

# Generate secuence permuted based on a number
print(np.random.permutation(15))
