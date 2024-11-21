#16.Write a Pandas program to drop a list of rows from a specified DataFrame.

import pandas as pd
import numpy as np
data = {
    'col1': [1, 4, 3, 4, 5],
    'col2': [4, 5, 6, 7, 8],
    'col3': [7, 8, 9, 0, 1]
}

# Create a DataFrame
df = pd.DataFrame(data)

# List of row indices to drop
rows_to_drop = [1, 3]

# Drop the specified rows
df_dropped = df.drop(rows_to_drop)

# Display the DataFrame after dropping the rows
print("DataFrame after dropping specified rows:")
print(df_dropped)

