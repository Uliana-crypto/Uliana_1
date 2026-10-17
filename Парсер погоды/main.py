import parcer

try:
    city = input("Введите город: ")

    geocoder = parcer.Geocoder()
    coords = geocoder.get_coordinates(city)

    if coords is None:
        print("Город не найден")

    latitude, longitude, name = coords
    print("Найден город:", name)

    client = parcer.WeatherApi()
    data = client.get_current(latitude, longitude)
    weather = parcer.Weather(data)
    weather.show()
except Exception as e:
    print(e)