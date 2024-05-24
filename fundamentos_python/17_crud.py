numeros = [0,1,2,3,4,5,6,7,8,0]
print(numeros)
# Cambiar por índice
numeros[-1] = 9
print(numeros)
# Agregar elemento
numeros.append(11)
print(numeros)
numeros.insert(10,10) # Inserta antes del indice (indice, elemento)
print(numeros)
# Concatenar listas
numeros2 = [12,13,99,15]
numeros = numeros + numeros2
print(numeros)
# Averiguar índice y cambiar elemento por indice
indice = numeros.index(99)
numeros[indice] = 14
print(numeros)
# Remover elemento específico
numeros.append(16)
print(numeros)
numeros.remove(16)
print(numeros)
# Remover último elemento
numeros.pop()
print(numeros)
# Remover elemento por índice
numeros.pop(0)
print(numeros)
# Invertir lista
numeros.reverse()
print(numeros)
# Ordenar números
lista = [34, 56, 12, 43, 2, 134]
lista.sort()
print(lista)
# Ordenar strings
nombres = ["ricardo", "maria", "liliana", "ambar", "tanger"]
nombres.sort()
print(nombres)