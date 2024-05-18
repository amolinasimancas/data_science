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

def find_famous_cats(cats):
    famous = max(sum(item['followers']) for item in cats)
    names = [item['name'] for item in cats if famous == sum(item['followers'])]
    return names

print(find_famous_cats(cats))