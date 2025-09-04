import numpy as np

a = np.array([[1,2,3,4,5],[3,4,5,6,7]])
b = np.array([[1,2,3,4,5],[4,5,6,7,8]])

c = np.concatenate((a,b),axis=1)
print(a.shape)
print(b.shape)
print(c.shape)
print(c)
print()

d = np.stack((a,b),axis=1)
print(a.shape)
print(b.shape)
print(d.shape)
print(d)