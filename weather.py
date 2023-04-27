import os
import requests

LAT = os.getenv('LAT')
LONG = os.getenv('LONG')
API_KEY = os.getenv('API_KEY')



url = f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={API_KEY}&units=metric'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    city = data['name']
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    print(f"City : {city} \n Temperature : {temperature}°C \n Weather : {description}")
else:
    print(response)
    print("Problem of response")