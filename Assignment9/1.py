# 1)	Draw multiple scatter plots and histograms of sepal length, sepal width, petal length and petal width features in one graph. Use subplot function to show multiple plots.

from sklearn import datasets
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


iris = datasets.load_iris()


iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

fig, axs = plt.subplots(2, 3, figsize=(18, 10))


sns.scatterplot(ax=axs[0, 0], x='sepal length (cm)', y='sepal width (cm)', data=iris_df, hue=iris.target, palette='viridis')
axs[0, 0].set_title('Sepal Length vs Sepal Width')

sns.scatterplot(ax=axs[0, 1], x='sepal length (cm)', y='petal length (cm)', data=iris_df, hue=iris.target, palette='viridis')
axs[0, 1].set_title('Sepal Length vs Petal Length')

sns.scatterplot(ax=axs[0, 2], x='sepal length (cm)', y='petal width (cm)', data=iris_df, hue=iris.target, palette='viridis')
axs[0, 2].set_title('Sepal Length vs Petal Width')

sns.histplot(iris_df['sepal length (cm)'], ax=axs[1, 0], bins=15, kde=True)
axs[1, 0].set_title('Histogram of Sepal Length')

sns.histplot(iris_df['sepal width (cm)'], ax=axs[1, 1], bins=15, kde=True)
axs[1, 1].set_title('Histogram of Sepal Width')

sns.histplot(iris_df['petal length (cm)'], ax=axs[1, 2], bins=15, kde=True)
axs[1, 2].set_title('Histogram of Petal Length')


plt.tight_layout()
plt.show()
