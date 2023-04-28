import os
import requests
from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def home():
    return "Homepage"

@app.route('/weather', methods=['GET'])
def get_weather():
    LAT = request.args.get('LAT')
    LONG = request.args.get('LONG')
    API_KEY = request.args.get('API_KEY')
    
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LONG}&appid={API_KEY}&units=metric'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        city = data['name']
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        return f"City : {city} \n Temperature : {temperature}°C \n Weather : {description}"
    else:
        return "Problem of response"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)