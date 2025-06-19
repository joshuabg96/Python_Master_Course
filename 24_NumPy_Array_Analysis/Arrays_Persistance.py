import numpy as np

arr_1 = np.random.randint(0,4,[3,3])

print(arr_1)

# Binary save
np.save('arr_1.npy', arr_1)

del(arr_1)

# Load file
arr_1 = np.load('arr_1.npy')

print(arr_1)


arr_2 = np.random.randint(-4,0,[3,3])

print(arr_2)

# Save compressed
np.savez('arrays.npz', arr_1=arr_1, arr_2=arr_2)

del(arr_1)
del(arr_2)

# Load
arrays = np.load('arrays.npz')

print(arrays['arr_1'])
print(arrays['arr_2'])



arr_3 = np.random.randint(-10,10,[3,3])

print(arr_3)

# text file
np.savetxt('arr_3.txt', arr_3)
np.savetxt('arr_3.txt', arr_3, delimiter=',')   # Save with ','

del(arr_3)

arr_3 = np.loadtxt('arr_3.txt', delimiter=',')
print(arr_3)
