# 5. Reshape a 1D array to a 2D array with 5 rows and 2 columns.

import numpy as np

arr = np.arange(1, 11)
reshaped_arr = arr.reshape(5, 2)
print("Reshaped array (5 rows, 2 columns):\n", reshaped_arr)
