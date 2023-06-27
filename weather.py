# This program uses OpenWeatherMap API to fetch the weather details
import requests

# stores API key
api_key = '10eaecffebbce4860b397b9e6801bba5'
user_input = input("Enter city: ")

# sends HTTP GET request to  OpenWeatherMap API
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

# checks if the response code is 404 in JSON response
if weather_data.json()['cod'] == '404':
    print("No City Found")

# extracts JSON response and stores in variables
else:
    weather = weather_data.json()['weather'][0]['main']
    temp_fahrenheit = round(weather_data.json()['main']['temp'])
    temp_celsius = round((temp_fahrenheit - 32) * 5/9)
    wind = weather_data.json()['wind']['speed']
    humidity = weather_data.json()['main']['humidity']

    print(f"Weather: {weather}")
    print(f"Temperature: {temp_fahrenheit}ºF / {temp_celsius}ºC")
    print(f"Wind: {wind} mph")
    print(f"Humidity: {humidity}%")
    print("Have a nice day!")
