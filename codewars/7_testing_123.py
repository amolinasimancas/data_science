lista_1 = ["a", "b", "c"]
lista_2 = []

def prepended_list(lista):
    resultado = [str(lista.index(elemento) + 1) + ': ' + str(elemento) for elemento in lista]
    return resultado

print(prepended_list(lista_1))
print(prepended_list(lista_2))