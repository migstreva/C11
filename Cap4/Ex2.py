import numpy as np

arr1 = np.arange(0, 51, 2)
arr2 = np.arange(100, 50, -2)
concatenated = np.concatenate((arr1, arr2))
result = np.sort(concatenated)
print(result)
