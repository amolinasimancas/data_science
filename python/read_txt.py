# Leer un archivo li­nea por li­nea
'''
with open('little_red_riding_hood.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())
'''

# Leer todas las li­neas en una lista
with open('little_red_riding_hood.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    print(len(lines))

# Añadir texto
'''
with open('little_red_riding_hood.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")
'''

# Sobreescribir el texto
'''
with open('little_red_riding_hood.txt', 'w') as file:
    file.write("\n\nBy:ChatGPT")
'''