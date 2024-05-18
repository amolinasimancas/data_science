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

gatos = []
seguidores = []

for gato in cats:
    gatos.append(gato["name"])
    seguidores.append(sum(gato["followers"]))

# Combinamos las listas en un diccionario
diccionario_gatos = dict(zip(gatos,seguidores))

# Encontramos el máximo número de seguidores
max_seguidores = max(seguidores)

# Creamos una lista con los nombres de los gatos con más seguidores
gatos_mas_populares = [nombre for nombre, seguidores in diccionario_gatos.items() if seguidores == max_seguidores]

print("Los gatos más populares son:", gatos_mas_populares)