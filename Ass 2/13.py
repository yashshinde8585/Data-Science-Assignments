#13.	Write a Pandas program to append a new row 'k' to data frame with given values for each column. Now delete the new row and return the original DataFrame.

import pandas as pd
import numpy as np

# Specified dictionary data
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}

# Specified list of labels
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Creating a DataFrame from the dictionary with index labels
df = pd.DataFrame(exam_data, index=labels)

# Appending a new row 'k' to the DataFrame
df.loc['k'] = ['Suresh', 15.5, 1, 'yes']

print("DataFrame after appending new row 'k':")
print(df)

# Deleting the new row 'k' to return to the original DataFrame
df = df.drop('k')

print("\nOriginal DataFrame after deleting the new row:")
print(df)
