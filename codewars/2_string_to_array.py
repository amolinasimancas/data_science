texto_1 = "Robin Singh"
texto_2 = "I love arrays they are my favorite"
texto_3 = ""

def string_to_array(texto):
    palabras = texto.split(' ')
    return(palabras)

print(string_to_array(texto_1))
print(string_to_array(texto_2))
print(string_to_array(texto_3))