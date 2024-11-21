#16.	Write a Pandas program to drop a list of rows from a specified DataFrame.

import pandas as pd

# Sample data
data = {
    'col1': [1, 4, 3, 4, 5],
    'col2': [4, 5, 6, 7, 8],
    'col3': [7, 8, 9, 0, 1]
}

# Creating DataFrame
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Dropping specified rows (for example, rows with index 1 and 3)
df_dropped = df.drop([1, 3])

print("\nDataFrame after dropping rows with index 1 and 3:")
print(df_dropped)
