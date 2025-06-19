import numpy as np      # Import the library numpy
import pandas as pd     # Import the lbirary pandas
import matplotlib.pyplot as plt    ## import matplotlib.plypot

# Create an array 
array = np.array([1,2,3,4,5])

print(array)
print(type(array))
print(array.ndim)       # Show the dimention of the array (1)
print(array.shape)      # Show the dimention of the sections (5,)

array = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(array)
print(type(array))
print(array.ndim)       # Show the dimention of the array (2)
print(array.shape)      # Show the dimention of the sections (2,5)
print(array.dtype)      # Type of the array int64


array = np.array([1,2,3,4,5,6.1234])

print(array)
print(array.dtype)      # Type of the array float64


array = np.array(["Hi", "how", "are", "you"])

print(array)
print(array.dtype)      # Type of the array <U3 = Unicode 3 Bytes

array = np.array(["Hi", "how", "are", "you", 1])

print(array)
print(array.dtype)      # Type of the array <U21 = Unicode 21 Bytes


table = pd.DataFrame(
    np.random.randint(0,100, size=(4,3)),
    columns=['Pepe','María','Juan']
)

print(table)
table.plot()
plt.show()