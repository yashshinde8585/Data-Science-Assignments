# Replace all odd numbers in an array of 1-10 with -1 using NumPy.
import numpy as np


arr2 = np.arange(1, 11)
arr2[arr2 % 2 != 0] = -1
print("Array with odd numbers replaced by -1:", arr2)
