# 7.	Create a DataFrame from a dictionary of lists.

import pandas as pd

data = {
    'X': [1, 2, 3, 4],
    'Y': [5, 6, 7, 8]
}
df = pd.DataFrame(data)
print("DataFrame from dictionary:\n", df)
