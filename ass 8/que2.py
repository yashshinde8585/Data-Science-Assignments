import pandas as pd
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# Create a DataFrame using the data and feature names from the iris dataset
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add the target (species) to the DataFrame
iris_df['species'] = iris.target

# Display the number of rows and columns
print(f"Number of rows: {iris_df.shape[0]}")
print(f"Number of columns: {iris_df.shape[1]}")

# Display general information about the DataFrame
print("\nDataset information:")
print(iris_df.info())
