try:
  print(0 / 0)
except ZeroDivisionError as error:
  print(error)

try:
  assert 1 != 1, "Uno no es igual que uno"
except AssertionError as error:
  print(error)

try:
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')
except Exception as error:
  print(error)

print('Hola')

try:
  print(0 / 0)
  assert 1 != 1, "Uno no es igual que uno"
  age = 10
  if age < 18:
    raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
  print(error)
except AssertionError as error:
  print(error)
except Exception as error:
  print(error)

print('Hola 2')