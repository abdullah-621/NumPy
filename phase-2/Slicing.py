import numpy as np

arr = np.array([[1,2,3,4],
                [6,7,8,9],
                [8,9,10,11]])

print("2D Slicing :\n",arr[1:,1:])

brr = np.array([
  [[1,2,3],[4,5,6]],
  [[7,8,9],[10,11,12]]
  ])

print("3D Slicing :",brr[1,1,:-0])