import requests
from decouple import config

LAT = config('LAT')
LONG = config('LONG')
API_KEY = config('API_KEY')

if not LAT or not LONG or not API_KEY:
    raise ValueError("Environment variables LAT, LONG, and API_KEY must be set")

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