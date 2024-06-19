# deseamos usar el diccionario data que esta dentro de main.py
import main

print(main.data)
# Pero vemos que así se ejecuta todo dentro de main.py y no queremos eso, queremos sólo a data...
# Para evitar esto podríamos tener los ejecutables modularizados como funciones, de forma que sólo invocando la función se ejecute lo deseado...
# Vamos a example_2.py para ver como queda