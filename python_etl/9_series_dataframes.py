import pandas as pd

serie = pd.Series([100,200,300])
print(serie)
print(type(serie))

data = {'Product':['A','B'], 'Sales':[100,200]}
df = pd.DataFrame(data)
print(df)

df_from_serie = serie.to_frame(name='new_column')
print(df_from_serie)
print(type(df_from_serie))