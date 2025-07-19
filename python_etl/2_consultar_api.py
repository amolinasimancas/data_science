import pandas as pd
import requests

url = 'http://dataservice.accuweather.com/forecasts/v1/daily/1day/11222?apikey=gSFnXqJghMNKcPGp6TTsBllFQ0VIxKcP'
response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    df = pd.json_normalize(weather_data)
    print(df.head())
else:
    print(f"Error en la solicitud: {response.status_code}")