def calculate_average(numbers):
    if len(numbers) == 0:
        raise ValueError("La lista está vacía")
    try:
       return sum(numbers)/len(numbers)
    except TypeError:
        raise TypeError("La lista contiene elementos no numéricos")

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [10, 20, 30, 40, 50]
lista_3 = []
lista_4 = [1, 2, '3', 4, 5]

print(calculate_average(lista_1))
print(calculate_average(lista_2))
print(calculate_average(lista_3))
print(calculate_average(lista_4))