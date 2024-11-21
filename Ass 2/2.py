#Write a Pandas program to convert a Panda module Series to Python list and it's type.
import pandas as pd
# Creating a Pandas Series
data = pd.Series([10, 20, 30, 40, 50])
# Converting Series to Python list
data_list = data.tolist()
# Display the list and its type
print("Converted List:", data_list)
print("Type of the List:", type(data_list))
