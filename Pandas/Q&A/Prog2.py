import pandas as pd

data = [10, 20, 30, 40, 50]
series = pd.Series(data)

python_list = series.tolist()

print("Python list:", python_list)

print("Type of the Python list:", type(python_list))
