'''8.	Write a Python programming to display a bar chart of the popularity of programming Languages. Use different color for each bar.
Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7 '''

import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Define different colors for each bar
colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan']

# Create a bar chart with different colors for each bar
plt.bar(languages, popularity, color=colors)

# Add labels and title
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages')

# Display the chart
plt.show()
