packages = [
  (1, 20, "Mexico"),
  (2, 15.5, "Colombia"),
  (3, 30, "Mexico"),
  (4, 12, "Argentina"),
  (5, 8.2, "Colombia"),
  (6, 25, "Mexico"),
  (7, 18.7, "Argentina"),
  (8, 5, "Colombia"),
  (9, 22.3, "Argentina"),
  (10, 14.8, "Colombia")
]

def get_packages_info(packages):
  total_weight = 0
  countries = []
  destinations = {}
  output = {}
  
  for package in packages:
      total_weight += package[1]
      if package[2] not in countries:
          countries.append(package[2])
  
  counters = []
  for country in countries:
    counter = 0
    for package in packages:
      if country == package[2]:
        counter += 1
    counters.append(counter)
  
  i = 0
  for country in countries:
    destinations[country] = counters[i]
    i += 1
  
  output["total_weight"] = round(total_weight,2)
  output["destinations"] = destinations
  return output

print(get_packages_info(packages))

'''
Output
{
  "total_weight": 171.50,
  "destinations": {
    "Mexico": 3,
    "Colombia": 4,
    "Argentina": 3
  }
}
'''
