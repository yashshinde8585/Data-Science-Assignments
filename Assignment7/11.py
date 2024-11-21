# 11.	Write a Python program to draw a scatter plot using random distributions to generate balls of different sizes.

import numpy as np
import matplotlib.pyplot as plt


x = np.random.rand(50)
y = np.random.rand(50)

sizes = np.random.rand(50) * 100  
plt.figure(figsize=(10, 5))
plt.scatter(x, y, s=sizes, alpha=0.5, c='blue')
plt.title("Scatter Plot of Random Balls")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
