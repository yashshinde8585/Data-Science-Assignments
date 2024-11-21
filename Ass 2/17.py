
#17.	Write a Pandas program to get first 3 records and last 3 records of a DataFrame.

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

# Getting the first 3 and last 3 records
first_three = df.head(3)
last_three = df.tail(3)

print("\nFirst 3 records:")
print(first_three)

print("\nLast 3 records:")
print(last_three)
