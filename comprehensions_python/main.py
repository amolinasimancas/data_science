# Una carpeta con módulos es un paquete, vamos a importar funciones dentro de módulos de un paquete

# OJO: para versiones de Python anteriores a 3.3 debemos tener un archivo init.py dentro de la carpeta paquete para poder importar sus módulos
'''
from pkg.mod_1 import func_1, func_2
from pkg.mod_2 import func_3, func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())
'''
# Al inicializar un paquete se pasa una sola vez por __init__.py y si hay variables declaradas podemos disponer de ellas
import pkg

print(pkg.URL)

# Supongamos que deseamos importar una función de uno de los módulos...
print(pkg.mod_1.func_1())

# Esto puede causar errores ya que requiere la importación previa de modulos para funcionar (líneas 5 y 6)

# Para no requerir imports explícitos, podemos incluir la importación mediante namespaces en __init__.py
