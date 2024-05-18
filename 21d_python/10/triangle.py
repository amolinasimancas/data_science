def print_triangle(size,character):
    triangle = ''
    for i in range(size):
        triangle += ' ' * (size-i-1)
        triangle += character * (1+2*i)
        if i < size:
            triangle += '\n'
    return triangle

print(print_triangle(6,'*'))