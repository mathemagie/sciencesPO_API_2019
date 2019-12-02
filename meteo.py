import requests
from pprint import pprint


def change_color(color): 
	r = requests.get("https://changecolor-candle.glitch.me/" + color)

r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Paris,fr&appid=96b99a4ac05013d0b00f353b6e48a988&&lang=fr&units=metric")
data=r.json()
#pprint(data)
temp = data['main']['temp']
city  = data['name']


print temp, city

if temp < 5.85:
	change_color('rouge')
else:
	change_color('bleu')

