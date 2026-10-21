import parcer

try:
    city = input("Введите город: ")

    geocoder = parcer.Geocoder()
    coord = geocoder.get_coordinates(city)

    api = parcer.WeatherAPI()
    w = api.weather(lat=coord.lat, lon=coord.lon)

    print(f"\nПогода в городе {city}:")
    print(f"  Температура:    {w.main.temp} C")
    print(f"  Ощущается как:  {w.main.feels_like} C")
    print(f"  Мин/макс:       {w.main.temp_min} / {w.main.temp_max} C")
    print(f"  Давление:       {w.main.pressure} ")
    print(f"  Влажность:      {w.main.humidity} %")

except Exception as e:
    print(e)

