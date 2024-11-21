'''14.	Write a Pandas program to count the NaN values in one or more columns in DataFrame.
Sample data:
Original DataFrame
   attempts       name qualify  score
0         1  Anastasia     yes   12.5
1         3       Dima      no    9.0
2         2  Katherine     yes   16.5
3         3      James      no    NaN
4         2      Emily      no    9.0
5         3    Michael     yes   20.0
6         1    Matthew     yes   14.5
7         1      Laura      no    NaN
8         2      Kevin      no    8.0
9         1      Jonas     yes   19.0'''

import pandas as pd
import numpy as np

data = {
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes'],
    'score': [12.5, 9.0, 16.5, np.nan, 9.0, 20.0, 14.5, np.nan, 8.0, 19.0]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Count the NaN values in each column
nan_count = df.isna().sum()

# Display the count of NaN values
print("NaN values in each column:")
print(nan_count)