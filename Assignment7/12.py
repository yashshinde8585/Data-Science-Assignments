# 12.	Write a Python program to draw a scatter plot for three different groups comparing weights and heights.
 

import numpy as np
import matplotlib.pyplot as plt

group1 = {'weights': np.random.normal(60, 5, 50), 'heights': np.random.normal(170, 5, 50)}
group2 = {'weights': np.random.normal(70, 5, 50), 'heights': np.random.normal(175, 5, 50)}
group3 = {'weights': np.random.normal(80, 5, 50), 'heights': np.random.normal(180, 5, 50)}

plt.figure(figsize=(10, 5))
plt.scatter(group1['weights'], group1['heights'], label='Group 1', alpha=0.5, color='red')
plt.scatter(group2['weights'], group2['heights'], label='Group 2', alpha=0.5, color='green')
plt.scatter(group3['weights'], group3['heights'], label='Group 3', alpha=0.5, color='blue')

plt.title("Scatter Plot Comparing Weights and Heights")
plt.xlabel("Weight (kg)")
plt.ylabel("Height (cm)")
plt.legend()
plt.grid(True)
plt.show()

