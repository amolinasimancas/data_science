# Permisos de lectura y escritura con r+
with open('./text.txt', 'w+') as file:
  for line in file:
    print(line)
  file.write('nuevas cosas en este archivo\n')
  file.write('otra linea\n')

# w+ para sobreescribir (OJO)