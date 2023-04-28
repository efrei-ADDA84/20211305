import os
import requests
from flask import Flask,request
from dotenv import load_dotenv

#Load data environment
load_dotenv()

#Preparing the app
app = Flask(__name__)

#Homepage
@app.route('/', methods=['GET'])
def get_weather():

    #Request argument for lat and lon    
    LAT = request.args.get('lat')
    LONG = request.args.get('lon')
    if LAT==None and LONG==None : 
        LAT = "0"
        LONG = "0"
        
    #Get api_key from .env    
    API_KEY = os.getenv('API_KEY')
    
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

#Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)