# 2)	Frequency histogram plot of all features, set title for x axis and y axis.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = sns.load_dataset('iris')


sns.set(style='whitegrid')


plt.figure(figsize=(12, 6))


for feature in data.columns[:-1]:  
    plt.hist(data[feature], bins=30, alpha=0.5, label=feature)


plt.title('Frequency Histogram of Iris Features')
plt.xlabel('Value')
plt.ylabel('Frequency')


plt.legend(title='Features')

plt.show()
