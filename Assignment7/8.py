# 8.	Select the first 3 rows of a DataFrame.
# data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]}

import pandas as pd

data = {'X': [1, 2, 3, 4], 'Y': [5, 6, 7, 8]}
df = pd.DataFrame(data)
first_three_rows = df.head(3)
print("First 3 rows of DataFrame:\n", first_three_rows)
