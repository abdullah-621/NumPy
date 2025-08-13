import numpy as np

resturant = np.array(['biriyari','chaken','mango','goyava'])

vectorized_operation = np.vectorize(str.upper)

print("Vectorized operation : ",vectorized_operation(resturant))