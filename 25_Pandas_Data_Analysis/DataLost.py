import numpy as np
import pandas as pd

df = pd.DataFrame({
    'A':[7,8,-6,8],
    'B':[12,np.nan,1,np.nan],
    'C':[4,np.nan,np.nan,np.nan],
    'D':[4,np.nan,-2,-10]
})
print(df,'\n')

# Comprobe null registers
print(df.isnull(),'\n')

# Discart rows with null registers
print(df.dropna(),'\n')

# Discard rows with null registers
print(df.dropna(axis=1),'\n')

# Show rows with at least two no null registers
print(df.dropna(thresh=2),'\n')

# Fill null register with a value
print(df.fillna(value=0),'\n')

# Fill a null register with a function
print(df['B'].fillna(value=df['B'].min()))