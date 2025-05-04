import pandas as pd
 
# Crear el DataFrame de ejemplo
data = {
	'producto': ['Camisa', 'Pantalón', 'Zapatos', 'Sudadera', 'Sombrero'],
	'precio': [20.0, 40.0, 50.0, 60.0, 15.0],
    'cantidad': [2, 3, 1, 2, 5]
}
 
df = pd.DataFrame(data)
print(df)

def total_ventas(cantidad, precio):
	return cantidad * precio

def clasificador(precio):
	if precio < 20:
		return 'Barato'
	elif precio < 50:
		return 'Medio'
	else:
		return 'Caro'

df['clasificación'] = df['precio'].apply(clasificador)

df['total_ventas'] = total_ventas(df['cantidad'], df['precio'])

print(df)