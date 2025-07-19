import json
import pandas as pd
import requests

# Lectura de datos desde un JSON

with open('1_ETL_ingesta_datos/example.json', mode='r') as file:
    data = json.load(file)

temperature = data['main']['temp']
print(f"Temperatura actual: {temperature}")

# Armado de un dataframe a partir de una lista de diccionarios

paises = [
    {"pais": "Alemania", "moneda": "Euro"},
    {"pais": "Estados Unidos", "moneda": "Dólar estadounidense"},
    {"pais": "Canada", "moneda": "Dólar canadiense"},
    {"pais": "Mexico", "moneda": "Peso mexicano"},
    {"pais": "Argentina", "moneda": "Peso argentino"}
]

df = pd.DataFrame(paises)
print(df.head())

# Uso de requests para consultar APIs

# Realizar una solicitud GET
response = requests.get('http://dataservice.accuweather.com/forecasts/v1/daily/1day/11222?apikey=gSFnXqJghMNKcPGp6TTsBllFQ0VIxKcP')
data = response.json()

print(data)

# Otro ejemplo
response = requests.get('https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY')
data = response.json()
print(data)