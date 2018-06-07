import requests
import urllib.parse

api="https://maps.googleapis.com/maps/api/geocode/json?"




end="Ativa Restaurante"

url = api+urllib.parse.urlencode({"address":end, "key":"AIzaSyCTtNA0k93PzLx4SKPKIU6tbcyUg3-yTbQ"})

cli = requests.get(url).json()

print(cli["status"])
