import os
import requests

LAT = "31.2504"
LONG = "-99.2506"
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
    

import os
import requests
from flask import Flask,request
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_weather():
    LAT = request.args.get('lat')
    LONG = request.args.get('lon')
    if LAT==None and LONG==None : 
        LAT = "31.2504"
        LONG = "-99.2506"
    API_KEY = os.getenv('API_KEY')
    
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={API_KEY}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        city = data['name']
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return f"City : {city} \n Temperature : {temperature}°C \n Weather : {description}"
    else:
        return ("Problem of response", "response" ,response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)