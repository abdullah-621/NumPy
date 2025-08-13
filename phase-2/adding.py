import numpy as np

original = np.array([[1,2,3],[4,5,6]])
new_row = np.array([7,8,9])

# add row wise
with_new_row = np.vstack((original,new_row))  
print("With new Row :\n",with_new_row)



new_col = np.array([[10],[11]])

#add col wise
with_new_col = np.hstack((original,new_col))
print("With new col :\n",with_new_col);