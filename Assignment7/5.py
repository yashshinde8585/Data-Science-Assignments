# 13.	Write a Python program to draw a scatter plot to find sea level rise in past 100 years.
 
import numpy as np
import matplotlib.pyplot as plt

years = np.arange(1920, 2021)

sea_level = np.random.normal(0, 0.5, len(years)).cumsum() + np.linspace(0, 20, len(years))

plt.figure(figsize=(10, 5))
plt.scatter(years, sea_level, color='blue', alpha=0.6)
plt.title("Sea Level Rise Over 100 Years")
plt.xlabel("Year")
plt.ylabel("Sea Level Rise (mm)")
plt.grid(True)
plt.show()
 
 
