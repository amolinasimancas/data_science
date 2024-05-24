# Declarar tuplas, verificar tipo y acceder a índices
numeros = (23, 34, 65, 88, 43, 90)
cadenas = ("ricardo", "martina", "ambar", "liliana", "maria")
print(type(numeros))
print(cadenas[2])
print(numeros[3])
# Averiguar índice
print(numeros.index(34))
# Contar ocurrencias
print(cadenas.count("ambar"))
# Tupla a lista
lista = list(numeros)
print(type(lista))
# Lista a tupla
tupla = tuple(lista)
print(type(tupla))