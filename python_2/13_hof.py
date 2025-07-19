# Definición tradicional
def increment(x):
  return x + 1

def high_ord_func(x, func):
  return x + func(x)

result = high_ord_func(2, increment) # 2 + (2 + 1) = 5
print(result)

# Definición con lambdas
increment_v2 = lambda x: x + 1
high_ord_func_v2 = lambda x, func: x + func(x)

result = high_ord_func_v2(2, increment_v2)
print(result)

# Lambda directa
result = high_ord_func_v2(2, lambda x: x + 2)
print(result)

# Cambio dinámico
result = high_ord_func_v2(2, lambda x: x * 5)
print(result)