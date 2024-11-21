# 5.	Write a Pandas program to convert a dictionary to a Pandas series.?

import pandas as pd

my_dict = {'A': 10, 'B': 20, 'C': 30, 'D': 40, 'E': 50}

my_series = pd.Series(my_dict)

print(my_series)