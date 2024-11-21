# 9.	Sort a DataFrame by a column.
# data = {'X': [4, 3, 2, 1], 'Y': [8, 7, 6, 5]}

import pandas as pd

data = {'X': [4, 3, 2, 1], 'Y': [8, 7, 6, 5]}
df = pd.DataFrame(data)
sorted_df = df.sort_values(by='X')
print("Sorted DataFrame by column 'X':\n", sorted_df)
