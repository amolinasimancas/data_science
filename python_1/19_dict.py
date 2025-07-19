persona = {
    "nombre": "antonio",
    "apellido": "molina",
    "edad" : 37,
    "nacionalidad": "venezolana"
}
print(type(persona))
print(len(persona))
print(persona["nombre"])
print(persona.get('edad'))
print(persona.get('nacimiento'))
print("nombre" in persona)
print("nacimiento" in persona)