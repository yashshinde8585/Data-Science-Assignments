# 5.	Write a Python program to plot two or more lines with different styles.

import matplotlib.pyplot as plt

# Data for the lines
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]  # Quadratic
y2 = [1, 8, 27, 64, 125]  # Cubic

# Plotting the first line (Quadratic) with style
plt.plot(x, y1, label='Quadratic', color='blue', linestyle='-', marker='o')

# Plotting the second line (Cubic) with style
plt.plot(x, y2, label='Cubic', color='red', linestyle='--', marker='s')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Two Lines with Different Styles')

# Adding a legend
plt.legend()

# Displaying the plot
plt.show()
