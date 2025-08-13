import numpy as np

arr_1D = np.array([1, 2, 3, 4, 5, 6])

newarr1D = np.array_split(arr_1D, 8)

# print(newarr1D)


arr_2D = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9], 
                   [10, 11, 12],
                   [13, 14, 15],
                   [16, 17, 18]])

newarr2D = np.array_split(arr_2D,3,axis=1)

# print(newarr2D)

hsplit_arr = np.hsplit(arr_2D,3)

print(hsplit_arr)


vsplit = np.vsplit(arr_2D,3)
print(vsplit)


dsplit = np.dsplit(arr_2D,3)
print(dsplit)



