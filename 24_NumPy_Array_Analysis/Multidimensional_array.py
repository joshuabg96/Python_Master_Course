import numpy as np

arr_2d = np.array(([0,5,10],[15,20,25],[30,35,40]))

print(arr_2d)

# First row
print(arr_2d[0])

# First row and first column
print(arr_2d[0][0])

# Last row and last column
print(arr_2d[-1][-1])


#Slicing 2D
arr_2d_2 = arr_2d[:,:]      # By reference
arr_2d_2[0,0] = 1           ## Modify both arrays

print(arr_2d_2)
print(arr_2d)

arr_2d_2 = arr_2d[:,:].copy()       # Copy the elements
arr_2d_2[0,0] = 2

print(arr_2d_2)
print(arr_2d)

# Fancy index
arr_2d = np.zeros((5,10))           # Array 5 rows 10 columns
print(arr_2d)

# Modify row 1,3 and last with 5
arr_2d[[0,2,-1]] = 5

print(arr_2d)

# Loops
for row in arr_2d:
    print(row)

# Array 3D or more dimentions
# First level 
arr_1d =  np.array([1,2])

# Second level 2 row 2 columns
arr_2d = np.array([[1,2],[3,4]])

# Third level, 2 row, 2 columns, 2 deep
arr_3d = np.array(
    [
        [
            [1,2],
            [3,4]
        ],
        [
            [5,6],
            [7,8]
        ]
    ]
)
print(arr_3d)

# array 3d of zeros 2x2x2
arr_3d = np.zeros([2,2,2])
print(arr_3d)

#array 4d of zeros 2x2x2x2
arr_4d = np.zeros([2,2,2,2])
print(arr_4d)

#reshape of 9 elements to a matrix of 3x3
arr_2d = np.arange(9).reshape(3,3)
print(arr_2d)
