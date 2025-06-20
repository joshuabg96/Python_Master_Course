import numpy as np
import pandas as pd

array = np.random.uniform(-10,10,size=[4,4])
df = pd.DataFrame(array, index=['A','B','C','D'], columns=['W','X','Y','Z'])

print(df)
print(type(df),'\n')

print(df['X'],'\n')
print(df[['Y','Z']],'\n')

# Add a column
df['TOTAL'] = df['W'] + df['X'] + df['Y'] + df['Z']
print(df,'\n')

# Delete a column
df.drop('TOTAL', axis=1, inplace=True)
print(df,'\n')

# Delete a row
df.drop('D', axis=0, inplace=True)
print(df,'\n')

# Select rows
print(df.loc['C'],'\n')
print(df.iloc[2],'\n')

# Select Subset
print(df.loc['C','Z'],'\n')                     # Row C, Column Z
print(df.loc[['A','B'],['W','Y']],'\n')         # Row A,B columns W,Y

# Conditional Select
print(df>0,'\n')                    # REgister greater than 0
print(df[df>0],'\n')                # Value of the register greater than 0

print(df[df['X']>0][['Y','Z']],'\n')            #Value of the registers of the columns Y,Z if X>0

# Logic operators
print(df[(df['X']>0) | (df['Z']<0)],'\n')

# Modify Index
array = np.random.uniform(-10,10, size=[4,4])
df = pd.DataFrame(array, index=['A','B','C','D'], columns=['W','X','Y','Z'])
df['Code'] = ['AA','BB','CC','DD']
print(df,'\n')

# Change Index columns
df.set_index('Code', inplace=True)
print(df,'\n')

print(df.loc['AA'],'\n')

# Reset index 
df.reset_index(drop=True, inplace=True)
print(df)
