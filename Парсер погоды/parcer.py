import requests
from typing import Literal
from pydantic import BaseModel

KEY = '40d01881f2f7c2b42757e586f744db54'
URL = 'https://api.openweathermap.org/data/2.5/weather'
GEO_URL = 'http://api.openweathermap.org/geo/1.0/direct'

class Coord(BaseModel):
    lon: float
    lat: float

class WeatherInfo(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int

class Weather(BaseModel):
    coord: Coord
    main: WeatherInfo

class WeatherAPI:
    def __init__(self, url: str = URL, key: str = KEY):
        self.url = url
        self.key = key

    def weather(self, 
            lat: float,
            lon: float,
            mode: Literal['json'] = 'json',
            units: Literal['standard', 'metric', 'imperial'] = 'metric',
            lang: str = "ru") -> Weather:
        
        params={
            "lat": lat,
            "lon": lon,
            "appid": self.key,
            "mode": mode,
            "units": units,
            "lang": lang
        }

        response = requests.get(self.url, params=params)
        response.raise_for_status()
        data = response.json()

        return Weather.model_validate(data)

class Geocoder:
    def __init__(self, url: str = GEO_URL, key: str = KEY):
        self.url = url
        self.key = key

    def get_coordinates(self, city: str) -> Coord:
        params = {
            "q": city, 
            "limit": 1,
            "appid": self.key}
        response = requests.get(self.url, params=params)
        response.raise_for_status()
        data = response.json()

        if not data:
            raise ValueError(f"Город не найден: {city}")

        return Coord(lon=data[0]["lon"], lat=data[0]["lat"])