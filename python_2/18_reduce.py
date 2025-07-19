import functools
numbers = [1,2,3,4]

def accum(counter, item):
    print('counter => ', counter)
    print('item => ', item)
    return counter + item

result = functools.reduce(accum, numbers)
result = functools.reduce(lambda counter, item: counter + item, numbers)
print(result)

# Reduce nos sirve cuando deseamos scar un único resultado a partir de una lista, por ejemplo la suma, mayor valor, menor valor, pronmedio, etc...