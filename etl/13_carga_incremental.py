import pandas as pd

# Actualizando con nuevos productos (sin duplicados)

# Dataset inicial
data_base = {
	'id': [1,2,3],
	'producto': ['Camisa', 'Pantalón', 'Zapatos'],
	'cantidad': [10, 5, 8]
}
df_base = pd.DataFrame(data_base)

# Nuevos datos incrementales
data_incremental = {
	'id': [4,5],
	'producto': ['Sombrero', 'Bufanda'],
	'cantidad': [3, 2]
}
df_incremental = pd.DataFrame(data_incremental)

df_actualizada = pd.concat([df_base, df_incremental], ignore_index=True)
print('\nCarga incremental (base actualizada):')
print(df_actualizada)

# Actualizando con nuevos productos y stock de existentes (gestionando duplicados)

# Datos incrementales con duplicados
data_incremental = {
    'id': [3, 4],
    'producto': ['Zapatos', 'Sombrero'],
    'cantidad': [12, 3]
}
df_incremental = pd.DataFrame(data_incremental)

# Concatenar y eliminar duplicados
df_actualizada = pd.concat([df_base, df_incremental], ignore_index=True).drop_duplicates(subset=['id'], keep='last')
print("\nBase actualizada sin duplicados:")
print(df_actualizada)