#18.	Write a Pandas program to remove first 3 rows and last 3 rows of a given DataFrame.

import pandas as pd
import numpy as np
data = {
    'col1': [1, 2, 3, 4, 7, 11],
    'col2': [4, 5, 6, 9, 5, 0],
    'col3': [7, 5, 8, 12, 1, 11]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Remove the first 3 rows and last 3 rows
df_removed = df.iloc[3:-3]

# Display the DataFrame after removing the first and last 3 rows
print("DataFrame after removing the first 3 and last 3 rows:")
print(df_removed)