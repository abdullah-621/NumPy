import numpy as np

arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

# arr3 = np.concatenate((arr1, arr2),axis=1)

# arr4 = arr3.flatten()

# print(arr3)



arr = np.stack((arr1, arr2), axis=0)
print(arr)

print()

x = np.hstack((arr1,arr2))
print(x)

print()

y = np.vstack((arr1,arr2))
print(y)

z = np.dstack((arr1,arr2))
print(z)