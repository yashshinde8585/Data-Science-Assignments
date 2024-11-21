#17.	Write a Pandas program to get first 3 records and last 3 records of a DataFrame.

import pandas as pd
import numpy as np
data = {
    'col1': [1, 2, 3, 4, 7, 11],
    'col2': [4, 5, 6, 9, 5, 0],
    'col3': [7, 5, 8, 12, 1, 11]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Get the first 3 records
first_three = df.head(3)

# Get the last 3 records
last_three = df.tail(3)

# Display the first 3 records
print("First 3 records of the DataFrame:")
print(first_three)

# Display the last 3 records
print("\nLast 3 records of the DataFrame:")
print(last_three)
