import numpy as np

original = np.array([[1,2,3],
                     [4,5,6],
                     [7,8,9]])

deleted_index = np.delete(original,[1,2])

print(deleted_index)

# 0 = row ,1 = col
deleted_row_col = np.delete(original,1,axis=1)

print(deleted_row_col)