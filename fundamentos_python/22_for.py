# Ciclo for: emplea cualquier iterable
for element in range(10, 21):
    print(element)

tupla = ("antonio", "liliana", "maria", "ricardo", "tanger", "martina")

for element in tupla:
    print(element)

product = {
'name': 'Camisa',
'price': 100,
'stock': 89
}

for element in product:
	print(element)

for element in product:
	print(product[element])
      
for key in product:
	print(key, '=>', product[key])

for key, value in product.items():
	print(key, '=>', value)

people = [
	{
		'name': 'nico',
		'age': 34
	},
	{
		'name': 'zule',
		'age': 45
	},
	{
		'name': 'santi',
		'age': 4
	}
]

for person in people:
	print(person)

for person in people:
	print('name =>', person['name'])