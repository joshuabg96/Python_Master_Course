import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame(np.random.randn(10, 5), columns=["A", "B", "C", "D", "E"])

#Save Csv
df.to_csv('C:/Users/josue/Documents/GitHub/Mis Repositorios/Python_Master_Course/25_Pandas_Data_Analysis/data.csv', index=False)
del(df)
df = pd.read_csv('C:/Users/josue/Documents/GitHub/Mis Repositorios/Python_Master_Course/25_Pandas_Data_Analysis/data.csv')
print(df,'\n')


#JSON
df.to_json('C:/Users/josue/Documents/GitHub/Mis Repositorios/Python_Master_Course/25_Pandas_Data_Analysis/data.json', index=False)
del(df)
df = pd.read_json('C:/Users/josue/Documents/GitHub/Mis Repositorios/Python_Master_Course/25_Pandas_Data_Analysis/data.json')
print(df,'\n')

#Excel
df.to_excel('C:/Users/josue/Documents/GitHub/Mis Repositorios/Python_Master_Course/25_Pandas_Data_Analysis/data.xlsx', sheet_name='Sheet1', index=False)
del(df)
df = pd.read_excel('C:/Users/josue/Documents/GitHub/Mis Repositorios/Python_Master_Course/25_Pandas_Data_Analysis/data.xlsx', sheet_name='Sheet1')
print(df,'\n')

#HTML
df = pd.read_html('https://web.archive.org/web/20220717170349/https://en.wikipedia.org/wiki/List_of_countries_by_past_fertility_rate')
print(df[2],'\n')

fertility_rate = df[2]
print(fertility_rate.head(),'\n')

# Rename first column to make it easier to manage
fertility_rate.rename(columns = {'Country/dependent territory':'Country'}, inplace=True)

print(fertility_rate,'\n')

print(fertility_rate[["Country", "2010–2015"]],'\n')

fertility_rate = fertility_rate[1:][:].apply(pd.to_numeric, errors='coerce')
print(fertility_rate,'\n')

plt.rcParams["figure.figsize"] = 10,5

fertility_rate.mean()[1:].plot(kind='line', xlabel="Períodos", ylabel="Media de natalidad mundial")




