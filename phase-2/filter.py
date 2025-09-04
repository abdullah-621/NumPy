import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])


l = []

for i in arr:
  if i > 3:
    l.append(True)
  else:
    l.append(False)

new_arr = arr[l]
print(l)
print(new_arr)