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

# Debemos cambiar la referencia en memoria
def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * .19
    return new_item

new_items = list(map(add_taxes, items))
print(new_items)
print(items)