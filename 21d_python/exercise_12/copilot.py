cats = [
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
    },
    {
        "name": "Pepe",
        "followers": [500, 500]
    }
]

# Calculamos la suma de seguidores para cada gato
sumas_seguidores = {}
for cat in cats:
    sumas_seguidores[cat["name"]] = sum(cat["followers"])

# Encontramos la mayor suma de seguidores
mayor_suma_seguidores = max(sumas_seguidores.values())

# Filtramos los gatos con la mayor suma de seguidores
gatos_ganadores = [cat["name"] for cat in cats if sumas_seguidores[cat["name"]] == mayor_suma_seguidores]

print(f"Los gatos con la mayor suma de seguidores son: {', '.join(gatos_ganadores)}")

print(sumas_seguidores)
