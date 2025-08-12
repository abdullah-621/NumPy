import numpy as np

arr = np.array([1,2,3,4,5])

# Return copy of the original array
x = arr.copy()
x[0] = 9

# Return only reference/view of the original array
y = arr.view()  
y[2] = 0

print("Original :\n",arr)
print("Copy :\n",x)
print("Original :\n",arr)
print("View :\n",y)
print("Original :\n",arr)


"""
The copy returns None.
The view returns the original array.
"""
print(x.base)
print(y.base)