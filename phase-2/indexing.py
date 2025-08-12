import numpy as np

arr = np.array([[1,2,3,4],
                [6,7,8,9]])

print("2D indexing :",arr[1,2])
print("2D row :",arr[1])
print("2D columns :",arr[:,2])

brr = np.array([
  [[1,2,3],
   [4,5,6]],

  [[7,8,9],
   [10,11,12]],

  [[13,14,15],
   [16,17,18]]
  ])

print("3D indexing :",brr[1,1,2])
print("3D row :",brr[1][1])
print("3D columns :",brr[:,:,1])