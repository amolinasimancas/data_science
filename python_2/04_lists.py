# List Comprehension: [element for element in iterable]

# Forma larga
numbers = []
for element in range(1, 11):
  numbers.append(element)
print(numbers)
# List comprehension
numbers_v2 = [element for element in range(1, 11)]
print(numbers_v2)

# Forma larga
numbers = []
for element in range(1, 11):
  numbers.append(element * 2)
print(numbers)
# List comprehension
numbers_v2 = [element * 2 for element in range(1, 11)]
print(numbers_v2)

# List Comprehension Condicional: [element for element in iterable if condition]
# p.ejm: variable = [i*2 for i in range (1, 101) if i % 2 == 0]

# Forma larga
numbers = []
for i in range(1, 11):
  if i % 2 == 0:
    numbers.append(i * 2)
print(numbers)

# List comprehension
numbers_v2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print(numbers_v2)