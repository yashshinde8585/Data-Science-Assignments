import pandas as pd
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# Create a DataFrame using the data and feature names from the iris dataset
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add the target (species) to the DataFrame
iris_df['species'] = iris.target

# Display detailed information about the DataFrame
print("Detailed information about the DataFrame:")
iris_df.info()
