import pandas as pd

s1 = pd.Series([1,2,3,4])
s2 = pd.Series([1,2,3,4], index = ['A','B','C','D'])
print(s1)
print(s2)