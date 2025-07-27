import json

# Lectura del archivo
with open('products.json', mode='r') as file:
    products = json.load(file)

# Mostrar el contenido
for product in products:
    print(product) # Imprimir como lista de diccionarios

for product in products:
    print(f"Product: {product['name']}, Price: {product['price']}") # Imprimir como columnas