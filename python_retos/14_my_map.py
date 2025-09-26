def my_map(lista, funcion):
    return [funcion(item) for item in lista]

print(my_map([1, 2, 3, 4], lambda num: num * 2))

# Expected output: [2, 4, 6, 8]

print(my_map([
{"name": "michi", "age": 2},
{"name": "firulais", "age": 6}],
lambda pet: pet["name"]))

# Expected output: ["michi", "firulais"]