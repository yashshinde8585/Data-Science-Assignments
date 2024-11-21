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

# Map species values (0, 1, 2) to actual species names
species_mapping = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
iris_df['species_name'] = iris_df['species'].map(species_mapping)

# Create a scatter plot for sepal length vs sepal width, colored by species
plt.figure(figsize=(8, 6))
scatter = sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', 
                          hue='species_name', data=iris_df, palette='Set1')

# Move the legend outside the plot
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', title='Species')

# Set plot labels and title
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Sepal Length vs Sepal Width')

# Display the plot
plt.tight_layout()  # Adjusts plot to ensure everything fits
plt.show()
