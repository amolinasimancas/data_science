# Abrir archivo
file = open('./text.txt')
# Leer todo
print(file.read())
# Leer lineas en manual
print(file.readline())
print(file.readline())
print(file.readline())

# Leer linea a linea hasta el final
for line in file:
  print(line)

# Liberar memoria cerrando al culminar la lectura
file.close()

# Cerrar automáticamente
with open('./text.txt') as file:
  for line in file:
    print(line)