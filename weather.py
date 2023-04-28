#Import librairies
import os
import requests

LAT = os.getenv('LAT')
LONG = os.getenv('LONG')
API_KEY = os.getenv('API_KEY')


#Url to weatherAPI
url = f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={API_KEY}&units=metric'
response = requests.get(url)

#If response is 200 so it is working
if response.status_code == 200:
    data = response.json()
    
    #Extract the interested information
    city = data['name']
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    
    #Print the result
    print(f"City : {city} \n Temperature : {temperature}°C \n Weather : {description}")
else:
    print(response)
    print("Problem of response")