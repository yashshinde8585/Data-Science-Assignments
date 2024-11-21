# 7.	Write a Pandas program to convert Series of lists to one Series.Sample Output: 
# Original Series of list
# 0    [Red, Green, White]
# 1           [Red, Black]
# 2               [Yellow]
# dtype: object
# One Series
# 0       Red
# 1     Green
# 2     White
# 3       Red
# 4     Black
# 5    Yellow

import pandas as pd
series_of_lists = pd.Series([['Red', 'Green', 'White'], ['Red', 'Black'], ['Yellow']])

print("Original Series of list:")
print(series_of_lists)

one_series = series_of_lists.explode()

print("\nOne Series:")
print(one_series.reset_index(drop=True))
