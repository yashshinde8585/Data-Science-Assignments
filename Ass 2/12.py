#12.	Write a Pandas program to calculate the sum of the examination attempts by the students and mean of all students' scores.

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

# Calculating the sum of examination attempts
total_attempts = df['attempts'].sum()
print("Sum of examination attempts:", total_attempts)

# Calculating the mean of all students' scores (ignoring NaN values)
mean_score = df['score'].mean()
print("Mean of all students' scores:", mean_score)
