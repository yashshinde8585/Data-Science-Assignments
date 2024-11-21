#9.	Write a Pandas program to create a dataframe from a dictionary and display it.
'''Sample data: {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
Expected Output:
    X   Y   Z                                                         
0  78  84  86                                                        
1  85  94  97                                                         
2  96  89  96                                                      
3  80  83  72                                                         
4  86  86  83'''

import pandas as pd
data_dict = {'X': [78, 85, 96, 80, 86], 'Y': [84, 94, 89, 83, 86], 'Z': [86, 97, 96, 72, 83]}

df = pd.DataFrame(data_dict)

print(df)