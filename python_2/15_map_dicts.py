items = [
    {
    'product': 'camisa',
    'price': 100
    }, 
    {
    'product': 'pantalon',
    'price': 300
    }, 
    {
    'product': 'sueter',
    'price': 200
    }
]

# Vamos a obtener una lista: prices = [100, 300, 200]
prices = list(map(lambda item: item['price'], items))
print(prices)

def add_taxes(item):
    item['taxes'] = item['price'] * .19
    return item

new_items = list(map(add_taxes, items))
print(new_items)
print(items)

'''
OJO: esto modificará el estado original del diccionario y puede generar errores!
Si se desea conservar el diccionario original y generar otro nuevo modificado ver siguiente ejercicio...
'''