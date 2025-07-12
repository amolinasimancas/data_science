list1 = [1, 2, 3, 4, 5]
list2 = [1, -2, 3, -4, 5]
list3 = []

def invert(lst):
    inverted_list = [element * -1 for element in lst]
    return inverted_list

print(invert(list1))
print(invert(list2))
print(invert(list3))