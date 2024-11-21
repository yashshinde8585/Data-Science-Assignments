#15.	Write a Pandas program to replace all the NaN values with Zero's in a column of a dataframe.

import pandas as pd
import numpy as np

# Sample data
data = {
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'name': ['Anastasia', np.nan, 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', np.nan, 'yes', 'no', 'no', 'yes'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19]
}

# Creating DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Replacing NaN values with zeros
df.fillna(0, inplace=True)

print("\nDataFrame after replacing NaN values with zeros:")
print(df)
