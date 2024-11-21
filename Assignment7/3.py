# Replace all even numbers in a 1D array with their negative

import numpy as np

arr = np.arange(1, 11)
arr[arr % 2 == 0] = -arr[arr % 2 == 0]
print("Array with even numbers replaced by their negatives:", arr)
