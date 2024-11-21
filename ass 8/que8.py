import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# Create a DataFrame using the data and feature names from the iris dataset
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add the target (species) to the DataFrame
iris_df['species'] = iris.target

# Create a bar plot for the count of each species
sns.countplot(x='species', data=iris_df)

# Set plot labels and title
plt.xlabel('Species')
plt.ylabel('Count of Observations')
plt.title('Count of Observations for Each Species')

# Display the plot
plt.show()
