#14.	Write a Pandas program to count the NaN values in one or more columns in DataFrame.

import pandas as pd
import numpy as np

# Sample data
data = {
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Counting NaN values in each column
nan_counts = df.isna().sum()

print("Count of NaN values in each column:")
print(nan_counts)
