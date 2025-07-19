# importamos modulo integrado para csv de python
import csv

# definimos la función read_csv cuyo argumento recibe el link del archivo csv
def read_csv(path):
  # abrimos la ruta con permisos de lectura y la nombramos "csvfile"
  with open(path, 'r') as csvfile:
    # a la variable reader le asignamos el resultado (iterador) de csv.reader cuyo delimitador es (,)
    reader = csv.reader(csvfile, delimiter=',')
    # los iteradores se corren manualmente, la primera fila corresponde a los encabezados, haciendo una sola iteración obtenemos los encabezados y los asignamos a la variable header
    header = next(reader)
    # se declara el array data
    data = []
    # para cada fila de reader
    for row in reader:
      # armamos tuplas encabezado/fila
      iterable = zip(header, row)
      # armamos el diccionario con la llave:valor que entrega iterable
      country_dict = {key: value for key, value in iterable}
      # se lo anexamos a data
      data.append(country_dict)
    return data  # retornamos data

# lo hacemos ejecutable como script
if __name__ == '__main__':
  # a la variable data se le asigna la invocación de la función read_csv que tiene por argumento la ruta del csv
  data = read_csv('data.csv')
  # imprimimos únicamente la primera posición del array data
  print(data[0])