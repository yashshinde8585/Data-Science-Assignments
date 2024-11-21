# 8.	Write a Pandas program to add some data to an existing Series.
# Sample Output: 
# Original Data Series:
# 0       100
# 1       200
# 2    python
# 3    300.12
# 4       400


# Data Series after adding some data:
# 0       100
# 1       200
# 2    python
# 3    300.12
# 4       400
# 5       500
# 6       php

import pandas as pd

original_series = pd.Series([100, 200, 'python', 300.12, 400])

print("Original Data Series:")
print(original_series)

new_data = pd.Series([500, 'php'])
updated_series = original_series._append(new_data, ignore_index=True)

print("\nData Series after adding some data:")
print(updated_series)
