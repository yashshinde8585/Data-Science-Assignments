#18.	Write a Pandas program to remove first 3 rows and last 3 rows of a given DataFrame.

import pandas as pd

# Sample data
data = {
    'col1': [1, 2, 3, 4, 7, 11],
    'col2': [4, 5, 6, 9, 5, 0],
    'col3': [7, 5, 8, 12, 1, 11]
}

# Creating DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Removing the first 3 and last 3 rows
df_removed = df.iloc[3:-3]

print("\nDataFrame after removing first 3 and last 3 rows:")
print(df_removed)
