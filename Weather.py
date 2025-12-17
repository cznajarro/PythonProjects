import requests

api_key = 'f4162f1bcf5a36a7ab1dd7e225196f88'

user_input = input("Enter city: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("Error, try again")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])

    print(f"The weather in {user_input} is {weather}. \nThe temperature in {user_input} is {temp} degrees Fahrenheit.")