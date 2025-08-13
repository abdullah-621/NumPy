import numpy as np
from numpy import random  

# flotting value
x = np.random.random((3,3))
print(x)


# integer value
y = np.random.randint(100) # 1D one value
y = np.random.randint(100, size=5)  # 1D 5 value
y = np.random.randint(50,size = (3,5)) # 3 X 4 matrix
# print(y)


# flotting value
z = np.random.rand(3,3)
print(z)