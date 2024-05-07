import pandas as pd
import numpy as np

#Dataframe

s1 = pd.Series([9, 2, 8, 3])
s2 = pd.Series([0, 5, 4, 1])

data = dict(
    first=s1,
    second=s2
)

df = pd.DataFrame(data)
print(df)


#Since random and rand functionas are numpy's inside, we won't import random function.
df = pd.DataFrame(
    data=np.random.rand(3, 5),
    index=['A', 'B', 'C'],
    columns=['Column1', 'Column2', 'Column3', 'Column4', 'Column5']
)
print(df)

#Select data upon DataFrame

#single square brackets give us series type
print(df['Column1'])
print(type(df['Column1']))

# dobule square brackets give us dataframe type
print(df[['Column1']])
print(type(df[['Column1']]))

#loc[] enables us to get row data through index value.

print(df.loc['B'])

# loc['index', 'column_name']
print(df.loc['C', 'Column3'])

