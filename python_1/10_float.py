# Comparación de flotantes (problema no menor!)
x = 3.3
y = 1.1 + 2.2
print(x == y) # Dará False

# Comparación vía strings
y_str = format(y,".2g") # Format convierte al float en string y deja 1 decimal
print(type(y_str))
print(y_str)
x_str = str(x)
print(x_str == y_str) # Ahora sí dará True

# Comparación por tolerancia
print(x, y)
tolerance = 0.00001
print(abs(x - y))
print(abs(x - y) < tolerance) # Dará True
