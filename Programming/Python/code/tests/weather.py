from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

owm = OWM('2eef922c013bfd291e2dffb083c0774c')
mgr = owm.weather_manager()

weather = input('Город:')

observation = mgr.weather_at_place(weather)
weather = observation.weather

temp = int(weather.temperature('celsius')['temp'])
feels_like = int(weather.temperature('celsius')['feels_like'])
humidity = weather.humidity
speed = weather.wind()['speed']

print("Температура:" + str(temp))
print("Влажность:" + str(humidity) + "%")
print("Скорость ветра:" + str(speed) + "м/с")