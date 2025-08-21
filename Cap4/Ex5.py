import numpy as np

np.random.seed(10)
mtx = np.random.randint(1, 50, (4, 4))
row1_mean = np.mean(mtx, 1)[0]
row2_mean = np.mean(mtx, 1)[1]
row3_mean = np.mean(mtx, 1)[2]
row4_mean = np.mean(mtx, 1)[3]

col1_mean = np.mean(mtx, 0)[0]
col2_mean = np.mean(mtx, 0)[1]
col3_mean = np.mean(mtx, 0)[2]
col4_mean = np.mean(mtx, 0)[3]

avg_of_rows = np.array([row1_mean, row2_mean, row3_mean, row4_mean])
avg_of_cols = np.array([col1_mean, col2_mean, col3_mean, col4_mean])

print("Rows means:", avg_of_rows)
print("Columns means:", avg_of_cols)

print("Highest rows mean: ", avg_of_rows.max())
print("Highest columns mean: ", avg_of_cols.max())

values, counts = np.unique(mtx, True)
print(values, counts)

doubled_numbers = values[counts == 2]
print("\nNumbers doubled:", doubled_numbers)

