'''1.	Write a Python program to draw a line using given axis values taken from a text file, with suitable label in the x axis, y axis and a title.'''

import matplotlib.pyplot as plt

# Reading data from the text file
x_values = [1,2,3]
y_values = [3,4,8]

with open('test.txt', 'r') as file:
    for line in file:
        x, y = map(int, line.split())  # Split the line into two integers
        x_values.append(x)
        y_values.append(y)

# Plotting the graph
plt.plot(x_values, y_values, marker='o')

# Labeling the axes
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Adding a title
plt.title('Line Plot from test.txt')

# Display the graph
plt.show()
