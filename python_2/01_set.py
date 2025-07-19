# Definición de set, impresión y corroboración de tipo de dato
set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

# Los sets no admiten duplicados, los ignoran
set_countries = {'col', 'mex', 'bol', 'col', 'mex', 'bol'}
print(set_countries)

# Admiten varios tipos de datos
tipos = {"nombre", 457, True}
print(tipos)

# Se pueden armar a partir de strings
set_from_string = set("palabra")
print(set_from_string)

# También a partir de listas o tuplas
numbers = [1,2,3,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers)
set_from_tuple = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuple)