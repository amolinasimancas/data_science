# Listas
numeros = [0,1,2,3,4,5,6,7,8,9]
consolas = ["switch", "playstation 5", "xbox series x", "xbox series s"]
varios = ["Antonio", 37, True]
# Ver tipo de variable "list"
print(type(numeros), type(consolas), type(varios))
print(numeros, consolas, varios)
# Acceder a elemento de lista
print(numeros[0], consolas[0], varios[0])
print(numeros[1], consolas[1], varios[1])
print(numeros[2], consolas[2], varios[2])
# Cambiar elemento de lista
consolas[0] = "gamecube"
print(consolas)
# Slicing
print(numeros[3:])
print(numeros[:3])
# Verificar si hay elemento
print("Ramon" in varios)
print("switch" in consolas)