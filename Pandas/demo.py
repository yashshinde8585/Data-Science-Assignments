import pandas as pd
s1=pd.Series([1,2,3,4])
print(s1)
s2=pd.Series([1,2,3,4], index=['A','B','C','D'])
print(s2)


df = pd.DataFrame({'foo': ['x','Y','Z'],
                   'bar':[6,10, None],
                   'baz':[True,True,False]})
print(df)


data = {
"calories": [420, 380, 390],
"duration": [50, 40, 45]
}
df= pd.DataFrame(data, index=["day1", "day2", "day3"])
print(df)