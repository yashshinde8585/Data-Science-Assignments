# 6.	Write a Pandas program to convert a NumPy array to a Pandas series. Sample Series:  NumPy array: [10 20 30 40 50]?

import pandas as pd
import numpy as np

numpy_array = np.array([10, 20, 30, 40, 50])

series = pd.Series(numpy_array)

print("Original NumPy array:")
print(numpy_array)

print("\nPandas series:")
print(series)

