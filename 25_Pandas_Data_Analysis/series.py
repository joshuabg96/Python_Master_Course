import numpy as np
import pandas as pd

tickets = ['A','B','C','D']

L = [25,50,75,100]

# Basic series
print(pd.Series(data=L),'\n')

# Ticket series
print(pd.Series(data=L, index=tickets),'\n')

# Array Series
array = np.random.randint(50, size=4)
print(pd.Series(data=array),'\n')


# Dictionary series
dicc = {'A':25,'B':75,'D':100}
print(pd.Series(dicc),'\n')

# index
Income = pd.Series([100,300,200], index=["January", "February", "March"])
print(Income,'\n')
print(Income["January"],'\n')

# Methods
S = pd.Series([100,150,250], index=["January", "February", "March"])
print(S,'\n')
print(Income.subtract(S),'\n')

print(type(Income))