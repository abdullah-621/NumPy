import numpy as np

arr = np.array([1,2,3,4,5,6,7])

arr_where = np.where(arr > 2)  # store index form arr

print(arr_where)  # index
print(arr[arr_where]) # accutual value


condition_arr = np.where(arr > 3, True, False)
print(arr[condition_arr])