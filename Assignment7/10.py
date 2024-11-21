# 10.	Replace missing values in a DataFrame.
# data = {'X': [1, 2, None, 4], 'Y': [5, None, 7, 8]}

import pandas as pd

data = {'X': [1, 2, None, 4], 'Y': [5, None, 7, 8]}
df = pd.DataFrame(data)
df.fillna(value=0, inplace=True) 
print("DataFrame after replacing missing values:\n", df)
