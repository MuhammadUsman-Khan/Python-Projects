import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == 200:
        main = data["main"]
        wind = data["wind"]
        weather = data["weather"][0]
        
        temperature = main["temp"]
        humidity = main["humidity"]
        pressure = main["pressure"]
        wind_speed = wind["speed"]
        description = weather["description"]
        
        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Pressure: {pressure} hPa")
        print(f"Wind Speed: {wind_speed} m/s")
        print(f"Description: {description}")
    else:
        print("City not found!")

api_key = "28936c444318f6cdc4cb87138d1dc586"
city = input("Enter city name: ")
get_weather(city, api_key)
