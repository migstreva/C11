import numpy as np

arr_of_ones = np.ones(8)
arr_of_randoms = np.random.randint(0, 10, 8)
result_arr = arr_of_ones + arr_of_randoms
sum_of_elements = result_arr.sum()

if sum_of_elements >= 40:
    result_arr = result_arr.reshape(4, 2)
else:
    result_arr = result_arr.reshape(2, 4)

print(result_arr)

