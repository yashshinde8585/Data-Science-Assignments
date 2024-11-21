import pandas as pd
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# Create a DataFrame using the data and feature names from the iris dataset
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add the target (species) to the DataFrame
iris_df['species'] = iris.target

# Display the unique count of values for the species column
species_counts = iris_df['species'].value_counts()
print("Unique count of values for the species column:")
print(species_counts)
