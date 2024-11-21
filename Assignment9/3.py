# 3)	Draw histogram plot for showing (distribution of data for various columns) highest frequency for all features sepal length, sepal width, petal length, petal width.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = sns.load_dataset('iris')


features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']


num_features = len(features)
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))


for i, feature in enumerate(features):
    ax = axes[i // 2, i % 2]  
    sns.histplot(data[feature], bins=30, kde=False, ax=ax) 
    ax.set_title(f'Histogram of {feature}')
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')


plt.tight_layout()
plt.show()
