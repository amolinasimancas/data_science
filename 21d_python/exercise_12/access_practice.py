cats =[
  {
    "name": "Mimi",
    "followers": [320, 120, 70]
  },
  {
    "name": "Milo",
    "followers": [400, 300, 100, 200]
  },
  {
    "name": "Gizmo",
    "followers": [250, 750]
  }
]

# Acceso a un diccionario de la lista
print(cats[0])

# Acceso a valores de claves específicas de un diccionario de la lista
print(cats[0]["name"])
print(cats[0]["followers"])

# Acceso a valores de sub-listas
print(cats[0]["followers"][0])

# Operaciones sobre sublistas
mimi_followers = sum(cats[0]["followers"])
print(mimi_followers)
print(type(mimi_followers))

# Imprimir nombres de cada diccionario recorriendo la lista
for i in cats:
    print(i["name"])

# Armar una lista con esos nombres
names_list = []

for i in cats:
    names_list.append(i["name"])

print(names_list)
print(type(names_list))

# Armar una lista con la suma de seguidores
score_list = []

for i in cats:
    score_list.append(sum(i["followers"]))

print(score_list)
print(type(score_list))

# Determinar el mayor valor de la lista
max_value = max(score_list)
print(max_value)
print(type(max_value))

# Imprimir lista de tuplas (nombre, seguidores)
print(list(zip(names_list,score_list)))

# Armar diccionario con listas
dict = {i:j for (i, j) in zip(names_list,score_list)}
print(dict)
print(type(dict))