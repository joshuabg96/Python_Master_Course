import numpy as np
import pandas as pd

# RAnge of dates to use as index in a Data Frame
index = pd.date_range("7/15/2022", periods=20)

print(index,'\n')

#Quick request
df =pd.DataFrame(np.random.rand(20,4), index=index, columns=["A","B","C","D"])

print(df,'\n')

# Head
print(df.head(),'\n')

# Head 3 columns
print(df.head(3),'\n')

#Tail
print(df.tail(),'\n')

#Tail 3 columns
print(df.tail(3),'\n')

# Single values
df = pd.DataFrame({
      'enteros': [100, 200, 300, 400],
    'decimales': [3.14, 2.72, 1.618, 3.14],
      'cadenas': ['hola','adiós','hola','adiós']})

# Array of single values of a column
print(df['cadenas'].unique(),'\n')

# Counter of a single values of a column
print(df['cadenas'].nunique(),'\n')

# Data frame with the single values and its counts of a columns
print(df['cadenas'].value_counts(),'\n')

#Functions
print(df['decimales'].sum(),'\n')

print(df['cadenas'].apply(len),'\n')

#apply a defined function
def doblar(n):
    return n*2

print(df['enteros'].apply(doblar),'\n')

#apply an anonimus function
print(df['enteros'].apply(lambda n: n/3),'\n')

# delete a column
del df['decimales']
print(df,'\n')


# Recover index
print(df.columns,'\n')
print(df.index,'\n')

#Apply Sort
print(df.sort_values(by='enteros'),'\n')

print(df.sort_values(by='enteros',ascending=False))