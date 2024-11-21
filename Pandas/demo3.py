import pandas as pd

d = {'one':pd.Series([100.,200.,300.], index = ['apple','ball','anklesh']),
'two': pd.Series([111.,222.,333.,4444.], index ['apple','ball','cat','dan'])}
df = pd.DataFrame(d)
print(df)