# 6.	Count the number of occurrences of a specific value in an array.

import numpy as np

arr = np.array([1, 2, 3, 1, 2, 1])
value_to_count = 1
value_count = np.count_nonzero(arr == value_to_count)
print(f"Count of occurrences of {value_to_count}: {value_count}")
