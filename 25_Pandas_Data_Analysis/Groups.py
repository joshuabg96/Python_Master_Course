import pandas as pd

sells = {
    'Comercial': ['Juan', 'María', 'Manuel', 'Vanesa', 'Ana', 'Marcos'],
    'Empresa': ['Movistar', 'Jazztel', 'Movistar', 'Jazztel', 'Vodafone', 'Vodafone'],
    'Primas': [300, 220, 140, 70, 400, 175]
} 

df = pd.DataFrame(sells)

print(sells,'\n')

Empresa = df.groupby('Empresa')
print(Empresa,'\n')

