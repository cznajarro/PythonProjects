import os
import requests
from flask import Flask
from dotenv import load_dotenv
load_dotenv() #loading the .env file to get the API key

app = Flask(__name__)

api_key = os.environ.get("api_key")

user_input = input("Enter city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

weather_statement = "Idk, look outside."

@app.route("/")
def index():
   return weather_statement

if weather_data.json()['cod'] == '404':
    print("Error, try again")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    weather_statement = f"The weather in {user_input} is {weather}. \nThe temperature in {user_input} is {temp} degrees Fahrenheit."

app.run(host="0.0.0.0", port=5001)