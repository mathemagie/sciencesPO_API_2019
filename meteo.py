import requests
from pprint import pprint

def change_color(color): 
	r = requests.get("https://changecolor-candle.glitch.me/" + color)

r = requests.get("http://api.openweathermap.org/data/2.5/weather?q=Marseille,fr&appid=96b99a4ac05013d0b00f353b6e48a988&")
data=r.json()
pprint(data)