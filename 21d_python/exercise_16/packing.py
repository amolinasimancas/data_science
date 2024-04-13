def get_packages_info(packages):
    weights = []
    countries = []
    answer = {
        "total_weight": 0,
        "destinations": {}
    }
    for package in packages:
        weights.append(package[1])
        countries.append(package[2])
    
    distinct_countries = list(set(countries))
    total_weight = round(sum(weights),2)

    i = 0
    countries_count = []
    while i < len(distinct_countries):
        for package in packages:
            if distinct_countries[i] == package[2]:
                countries_count[i] += 1
        i += 1
    
    answer["total_weight"] = total_weight
        
    return answer

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

"""
{
  "total_weight": 171.50,
  "destinations": {
    "Mexico": 3,
    "Colombia": 4,
    "Argentina": 3
  }
}
"""
print(get_packages_info(packages))