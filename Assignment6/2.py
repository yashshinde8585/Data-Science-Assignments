# # 2. Write a Python programming to create a pie chart with a title of the 
# popularity of programming Languages.
# Sample data:
# Programming languages: Java, Python, PHP, JavaScript, C#, C++
# Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

import matplotlib.pyplot as plt
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
plt.figure(figsize=(10, 6)) 
plt.pie(popularity, labels=languages, autopct='%1.1f%%', 
startangle=140)
plt.title('Popularity of Programming Languages')
plt.axis('equal') 
plt.show()