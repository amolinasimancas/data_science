import pandas as pd

# Leer el archivo CSV en un DataFrame
df = pd.read_csv('_data/vgsales.csv')

'''
pd.head()
pd.shape()
pd.describe()
'''

print(df.head())
print(df.info())
print(df.describe())

'''
Leer CSV con delimitador ";" y comillas simples
df = pd.read_csv('dataset.csv', sep=';', quotechar="'")
'''