import pandas as pd
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# Create a DataFrame using the data and feature names from the iris dataset
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add the target (species) to the DataFrame
iris_df['species'] = iris.target

# Remove duplicate rows from the DataFrame
iris_df_no_duplicates = iris_df.drop_duplicates()

# Display the DataFrame after removing duplicates
print("DataFrame after removing duplicates:")
print(iris_df_no_duplicates)

# Optional: Show the number of rows before and after removing duplicates
print(f"\nNumber of rows before removing duplicates: {iris_df.shape[0]}")
print(f"Number of rows after removing duplicates: {iris_df_no_duplicates.shape[0]}")
