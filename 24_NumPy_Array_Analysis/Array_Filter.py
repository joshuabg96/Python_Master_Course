import numpy as np

# 40 numbers from 0 to 10
arr = np.random.randint(0,10,40)

#Apply filter unique
print(np.unique(arr))

# Filter 1D
print(np.in1d([-1,4,8,12], arr))

# Where
#Generate an array with random numbers
arr_1 = np.random.uniform(-5, 5, size=[3,2])
print(arr_1)

# Create a filter that says that all the negatives are 0
arr_2 = np.where(arr_1<0, 0, arr_1)
print(arr_2)

# Create a filter that says that all positives are 1
arr_2 = np.where(arr_2>0, True, arr_2)
print(arr_2)

# Bool filters
# Define bool filter
arr_bool = np.array([True,True,True,False])

# Check if all the elements are true
print(arr_bool.all())

# Check if any element is true
print(arr_bool.any())

# Define 2d bool array
arr_bool_2d = np.array(
    [
        [False, True],
        [False, True],
        [False, True]
    ]
)

# All true
print(arr_bool_2d.all(0))

#Any row with a value tryue
print(arr_bool_2d.any(1))


 