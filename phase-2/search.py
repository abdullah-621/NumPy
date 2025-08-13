import numpy as np

arr = np.array([1, 2, 3, 4,4, 5, 7, 8])

x = np.where(arr % 2 == 1) # return index

print(x)


y = np.searchsorted(arr, 4)
z = np.searchsorted(arr, 4,side='right')
x = np.searchsorted(arr,[6,12,0])
print(y)
print(z)
print(x)