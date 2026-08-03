import requests

city = input("enter city name : ")

url = f"https://wttr.in/{city}?format=Tempurature: %t\nWeather: %C\nWind: %w\nHumidity: %h"
response = requests.get(url)

if response.status_code == 200 :
    print(response.text)

else :
    print ("could not fetch weather data.")