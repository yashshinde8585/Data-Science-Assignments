# 4)	Draw boxplots to show the distribution of categorical value with other numerical values. Use subplot function to show multiple plots. For x axis consider all species and for y consider sepal length, sepal width, petal length, petal width features.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


iris = sns.load_dataset('iris')


fig, axs = plt.subplots(2, 2, figsize=(12, 10))


palette = sns.color_palette("Set2")


sns.boxplot(x='species', y='sepal_length', data=iris, ax=axs[0, 0], palette=palette)
axs[0, 0].set_title('Sepal Length by Species')

sns.boxplot(x='species', y='sepal_width', data=iris, ax=axs[0, 1], palette=palette)
axs[0, 1].set_title('Sepal Width by Species')

sns.boxplot(x='species', y='petal_length', data=iris, ax=axs[1, 0], palette=palette)
axs[1, 0].set_title('Petal Length by Species')

sns.boxplot(x='species', y='petal_width', data=iris, ax=axs[1, 1], palette=palette)
axs[1, 1].set_title('Petal Width by Species')


plt.tight_layout()
plt.show()
