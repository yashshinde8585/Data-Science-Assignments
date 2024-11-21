import matplotlib.pyplot as plt

# Data for plotting
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [25, 16, 9, 4, 1]
y3 = [10, 20, 30, 40, 50]

# Plotting the lines with different styles
plt.plot(x, y1, label='Line 1 - Solid', color='r', linestyle='-', marker='o')  # Solid line with circles
plt.plot(x, y2, label='Line 2 - Dashed', color='g', linestyle='--', marker='x')  # Dashed line with x markers
plt.plot(x, y3, label='Line 3 - Dotted', color='b', linestyle=':', marker='s')  # Dotted line with square markers

# Adding labels and title
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Multiple Lines with Different Styles')

# Adding a legend
plt.legend()

# Show grid
plt.grid(True)

# Display the plot
plt.show()
