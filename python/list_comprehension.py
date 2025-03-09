# Doble de los números
numeros = [1,2,3,4,5]
dobles = [numero * 2 for numero in numeros]
print(dobles)

# Filtrar y transformar en un solo paso
palabras = ['sol','mar','montaña','rio','estrella']
filtradas = [palabra.upper() for palabra in palabras if len(palabra) > 3]
print(filtradas)

# Crear un diccionario con list comprehension
claves = ['nombre','edad','ocupacion']
valores = ['Juan',30,'Ingeniero']
diccionario = {clave:valor for clave,valor in zip(claves,valores)}
print(diccionario)
diccionario_alt = {claves[i]:valores[i] for i in range(len(claves))}
print(diccionario_alt)

# Anidación de list comprehensions
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpuesta = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print(transpuesta)

# Extraer información de una lista de diccionarios
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]
filtrado = [persona['nombre'] for persona in personas if persona["ciudad"] == "Madrid" and persona['edad'] > 30]
print(filtrado)

# List comprehensions con un else
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
transformada = [elemento * 2 if elemento % 2 == 0 else elemento for elemento in numeros]
print(transformada)