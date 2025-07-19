persona = {
    "nombre": "antonio",
    "apellido": "molina",
    "edad" : 37,
    "nacionalidad": "venezolana",
    "idiomas": ['ingles', 'español', 'portugués']
}

persona["apellido"] = "simancas"
persona["edad"] += 10
persona["idiomas"].append("aleman")

print(persona)

print(persona.values())
print(persona.keys())
print(persona.items())

del persona['edad']
persona.pop("nombre")

print(persona)