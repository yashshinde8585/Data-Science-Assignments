
#15.Write a Pandas program to replace all the NaN values with Zero's in a column of a dataframe.


import pandas as pd
import numpy as np
data = {
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2],
    'name': ['Anastasia', np.nan, 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin'],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', np.nan, 'yes', 'no', 'no'],
    'score': [12.5, 9.0, 16.5, np.nan, 9.0, 20.0, 14.5, np.nan, 8.0]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Replace all NaN values with 0
df.fillna(0, inplace=True)

# Display the DataFrame after replacing NaN values
print("DataFrame after replacing NaN values with zeros:")
print(df)
