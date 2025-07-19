# Ejemplo 1
dict = {}
for i in range(1, 5):
  dict[i] = i * 2
print(dict)

dict_v2 = {i: i * 2 for i in range(1, 5)}
print(dict_v2)

# Ejemplo 2
import random
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
  population[country] = random.randint(1, 100)
print(population)

population_v2 = {country: random.randint(1, 100) for country in countries}
print(population_v2)

# Ejemplo 3
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]

# Armado tradicional del diccionario
dict_example = {'nico': 12, 'zule': 56, 'santi': 98}

# Crea lista de tuplas y genera el diccionario
print(list(zip(names, ages)))
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)