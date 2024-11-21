'''7.	Write a Python programming to display a horizontal bar chart of the popularity of programming Languages.
Sample data:
Programming languages: Java, Python, PHP, JavaScript, C#, C++
Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7 '''

import matplotlib.pyplot as plt

# Sample data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Create a horizontal bar chart
plt.barh(languages, popularity, color=['blue', 'green', 'red', 'purple', 'orange', 'cyan'])

# Add labels and title
plt.xlabel('Popularity (%)')
plt.ylabel('Programming Languages')
plt.title('Popularity of Programming Languages')

# Display the chart
plt.show()
