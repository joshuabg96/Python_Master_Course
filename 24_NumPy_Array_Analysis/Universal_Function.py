import numpy as np

arr_1 = np.arange(1,6)
arr_2 = np.array([-3,7,3,13,0])

# Sum
print(np.add(arr_1,arr_2))

# Substract
print(np.subtract(arr_2,arr_1))

# Sqrt 
print(np.sqrt(arr_1))

#Power
print(np.power(arr_1,2))

#sign= return 1 if the value is positive and 0 if it is negative
print(np.sign(arr_1))

# Trigonometrics
#sin
print(np.sin(arr_1))

#cosin
print(np.cos(arr_1))

#tang
print(np.tan(arr_1))

#Degrees to radian
print(np.deg2rad(arr_1))

#radian to degrees
print(np.rad2deg(arr_1))

# compare
#Max
print(np.maximum(arr_1,arr_2))

#Min
print(np.minimum(arr_1,arr_2))

# Equal
print(np.equal(arr_1,arr_2))

# GReater than
print(np.greater(arr_1,arr_2))

# Float
arr_3 = np.array([3.14,2.57,-6.4,0.47,5.5])

# Abs
print(np.fabs(arr_3))

#Round up
print(np.ceil(arr_3))

#Round down
print(np.floor(arr_3))

# Round
print(np.round(arr_3))