'''
Input:

sets = [
  {1, 2, 3, 4},
  {2, 3, 4, 5},
  {3, 4, 5, 6}
]

find_set_intersection(sets)

Output: {3, 4}

Input:

sets = [
  {1, 2, 3, 4},
  {2, 4, 6, 8},
  {3, 6, 9, 12}
]

find_set_intersection(sets)

Output: set()
'''
sets_a = [
  {1, 2, 3, 4},
  {2, 3, 4, 5},
  {3, 4, 5, 6}
]
sets_b = [
  {1, 2, 3, 4},
  {2, 4, 6, 8},
  {3, 6, 9, 12}
]

def find_set_intersection(sets):
  intersection = sets[0]
  for element in sets[1:]:
    intersection = intersection & element
  return intersection

print(find_set_intersection(sets_a))
print(find_set_intersection(sets_b))
