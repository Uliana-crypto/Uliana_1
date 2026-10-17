import requests

class Geocoder:
    def __init__(self):
        self.url = "https://geocoding-api.open-meteo.com/v1/search"

    def get_coordinates(self, city : str):
        params = {
            "name": city,
            "count": 1,
            "language": "ru",
            "format": "json"
        }

        response = requests.get(self.url, params=params)
        data = response.json()
        print(data, end='\n')

        if "results" not in data:
            raise Exception(f"Город '{city}' не найден")

        result = data["results"][0]
        return result["latitude"], result["longitude"], result["name"]

class WeatherApi:
    def __init__(self):
        self.url = "https://api.open-meteo.com/v1/forecast"

    def get_current(self, latitude, longitude):
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current_weather": True,
            "timezone": "auto"
        }
        response = requests.get(self.url, params=params)
        data = response.json()
        print(data, end='\n') 
        return data
    
class Weather:
    def __init__(self, data: dict):
        cw = data["current_weather"]
        self.temperature = cw["temperature"]
        self.windspeed = cw["windspeed"]
        self.winddirection = cw["winddirection"]
        self.time = cw["time"]

    def show(self):
        print("Температура:", self.temperature)
        print("Ветер:", self.windspeed)
        print("Направление ветра:", self.winddirection)
        print("Время:", self.time)