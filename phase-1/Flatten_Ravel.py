import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])

# Return copy of the original array
flatten = arr.flatten() 
flatten[2] = 30

print("Flatten array :\n",flatten)
print("Original array :\n",arr)

print("\n")
# Return only reference/view of the original array
raveled = arr.ravel()
raveled[2] = 500
print("Ravel array :\n",raveled)
print("Original array :\n",arr)
