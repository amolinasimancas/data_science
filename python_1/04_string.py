# Concatenación
name = input("Introduce your name: ")
last_name = input("Introduce your last name: ")
Full_name = name + " " + last_name
print (Full_name)

# Template Literals
template1 = f"Hola, mi nombre es {name} y mi apellido {last_name}"
template2 = "Hello, my name is {} and my last name is {}".format(name, last_name)
print(template1)
print(template2)