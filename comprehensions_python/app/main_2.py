# Crear mis propios módulos (cualquier archivo .py)
# Crear carpeta app
# python app/main.py (para correr desde una carpeta en Replit)

import utils

data = [{
  'Country': 'Colombia',
  'Population': 500
}, {
  'Country': 'Bolivia',
  'Population': 300
}]

# metemos todo el código acá excepto data


def run():
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)
  print(result)