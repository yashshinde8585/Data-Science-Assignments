import pandas as pd

file_path = 'D:/MCA/SYMCA I/Lab On DATA Science/Pandas/Book1.xlsx'

# Read the CSV file into a DataFrame
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print(df.to_string())