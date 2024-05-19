age = 37
# print("My age is: " + age) dará error por ser diferentes tipos de dato
print("My age is: " + str(age))
print(f"Mi edad es: {age}")

edad = input("Introduce tu edad: ")
print(type(edad))
edad = int(edad)
edad +=10
print(type(edad))
print(f"Tu edad en 10 años será de: {edad}")