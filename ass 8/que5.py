import pandas as pd
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# Create a DataFrame using the data and feature names from the iris dataset
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add the target (species) to the DataFrame
iris_df['species'] = iris.target

# Display the count of missing values in each column
missing_values_count = iris_df.isnull().sum()
print("Count of missing values in each column:")
print(missing_values_count)
