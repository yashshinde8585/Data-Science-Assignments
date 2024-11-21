# 4.Write a Python program to draw a scatter plot with empty circles 
# taking a random distribution in X and Y and plotted against each 
# other.

import matplotlib.pyplot as plt
import numpy as np
np.random.seed(42)
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y, facecolors='none', edgecolors='k')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot with Empty Circles')
plt.show()
