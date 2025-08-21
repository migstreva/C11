import numpy as np

i, j = np.random.randint(0, 10, 2)
mtx = np.zeros([i, j])
rows, cols = mtx.shape

if (rows * cols) % 2 == 0:
    print("Can be reshaped into a vector with even number of elements")
else:
    print("Can be reshaped into a vector with odd number of elements")