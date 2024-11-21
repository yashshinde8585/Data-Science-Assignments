'''9.	Write a Python programming to display a bar chart of the popularity of programming Languages. Select the width of each bar and their positions.
Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7 '''

import matplotlib.pyplot as plt
import numpy as np

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Define bar width
bar_width = 0.5

# Set positions for each bar on the x-axis
positions = np.arange(len(languages))

# Create the bar chart with specified width and positions
plt.bar(positions, popularity, color='blue', width=bar_width)

# Add labels and title
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages')

# Adjust the x-axis ticks to show the names of the languages at the correct positions
plt.xticks(positions, languages)

# Display the chart
plt.show()
