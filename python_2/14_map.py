# La función map hace transformaciones sobre una lista de elementos
# Se maneja el mismo número de elementos antes y después de la transformación
# map recibe una función y un iterable donde aplicarla

# Definición tradicional
numbers = [1, 2, 3, 4, 5]
numbers_v2 = []
for i in numbers:
    numbers_v2.append(i*2)
print(numbers)
print(numbers_v2)

# Definición con map y lambdas en una sola línea
numbers_v3 = list(map(lambda i:i*2, numbers))
print(numbers_v3)

# Suma valores de dos listas hasta el último elemento de la lista más corta
numbers_1 = [1, 2, 3, 4]
numbers_2 = [5, 6, 7]
result = list(map(lambda x, y : x + y, numbers_1, numbers_2))
print(result)

# Ver salida de map (por eso debemos llevarlo a lista)
revision = map(lambda i: i*2, numbers)
print(revision)