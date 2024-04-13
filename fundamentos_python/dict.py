numbers = [1,2,3,4,5,6,7,8,9,10]
print(len(numbers))

yo = {
    'nombre': 'Antonio',
    'apellido': 'Molina',
    'edad': 36,
    'peso': 82,
    'estatura': 1.75,
    'lenguajes': ['ingles','español','portugues','aleman']
}
print(len(yo))
print(yo['nombre']) # Da error si no encuentra la clave!
print(yo.get('ciudad')) # No da error! Da None
print('avion' in yo)

print(yo)
yo['nombre'] = 'Ramon'
yo['edad'] += 4
yo['lenguajes'].append('italiano')
print(yo)

del yo['apellido']
yo.pop('edad')
print(yo)

print(yo.items())
print(yo.keys())
print(yo.values())