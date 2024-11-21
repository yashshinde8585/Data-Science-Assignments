import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()

# Create a DataFrame using the data and feature names from the iris dataset
iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Set up the matplotlib figure
plt.figure(figsize=(12, 10))

# Create a histogram for each feature in separate subplots
plt.subplot(2, 2, 1)  # 2 rows, 2 columns, 1st subplot
plt.hist(iris_df['sepal length (cm)'], bins=10, color='skyblue', edgecolor='black')
plt.title('Histogram of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')

plt.subplot(2, 2, 2)  # 2nd subplot
plt.hist(iris_df['sepal width (cm)'], bins=10, color='salmon', edgecolor='black')
plt.title('Histogram of Sepal Width')
plt.xlabel('Sepal Width (cm)')
plt.ylabel('Frequency')

plt.subplot(2, 2, 3)  # 3rd subplot
plt.hist(iris_df['petal length (cm)'], bins=10, color='lightgreen', edgecolor='black')
plt.title('Histogram of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')

plt.subplot(2, 2, 4)  # 4th subplot
plt.hist(iris_df['petal width (cm)'], bins=10, color='gold', edgecolor='black')
plt.title('Histogram of Petal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Frequency')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the histograms
plt.show()
