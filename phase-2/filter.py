import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])


# store bool valu [False  True False  True False  True False  True]
t = arr % 2 == 0  

x = arr[t]

print(t)
print(x)