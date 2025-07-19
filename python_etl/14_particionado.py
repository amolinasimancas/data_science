import pandas as pd

data = {
    'id_venta': [1, 2, 3, 4, 5, 6],
    'producto': ['Camisa', 'Pantalón', 'Zapatos', 'Camisa', 'Pantalón', 'Zapatos'],
    'cantidad': [2, 3, 1, 2, 0, 5],
    'categoria': ['Ropa', 'Ropa', 'Calzado', 'Ropa', 'Ropa', 'Calzado'],
    'fecha': ['2024-05-01', '2024-05-03', '2024-05-02', '2024-05-01', '2024-05-02', '2024-05-05']
}

df = pd.DataFrame(data)
ropa = df[df['categoria'] == 'Ropa']
calzado = df[df['categoria'] == 'Calzado']

print("Partición Ropa:\n", ropa)
print("Partición Calzado:\n", calzado)

df['mes'] = pd.to_datetime(df['fecha']).dt.month
particiones_por_mes = {mes: datos for mes, datos in df.groupby('mes')}

for mes, datos in particiones_por_mes.items():
    print(f"Mes {mes}:\n{datos}\n")