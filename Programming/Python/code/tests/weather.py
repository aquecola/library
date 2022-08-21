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

print("Температура:" + str(temp))

if feels_like > 25:
    print('Пиздец как жарко')

if feels_like < 5:
    print('Пиздец как холодно')