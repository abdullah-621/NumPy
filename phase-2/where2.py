import numpy as np

arr = np.array([30,15,20,10])

# new_arr = np.where(arr % 2 == 0)

# print(new_arr)

x = np.searchsorted(arr,11)
print(x)