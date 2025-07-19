# Métodos de strings
text = "ATENCIÓN: Para aumentar la vida del refractario es importante antes que nada reducir el tiempo y la temperatura de exposición del mismo al acero, con lo cual es VITAL reducir el tiempo de afino. EL TIEMPO DE AFINO DEBE SER EL MENOR POSIBLE!!!"

# Buscar si hay texto en texto
print("horno" in text) # False
print("refractario" in text) # True

# Tamaño del texto
print(len(text))

# Mayúsculas y minúsculas
print(text.upper())
print(text.lower())

# Contar ocurrencias
print(text.count("a"))
print(text.count("refractario"))

# Otros
print(text.swapcase())
print(text.startswith("Hola"))
print(text.endswith ("chao"))
print(text.replace('refractario','horno'))

# Test de mutabilidad
text2 = text.replace("refractario","horno")
print(text)
print(text2) # No cambia al original pues es inmutable

text3 = "hola mundo!"
print(text3.capitalize()) # Mayúscula en primer caracter
print(text3.title()) # Mayúscula en cada palabra
print(text3.isdigit()) # Chequea si es número