import requests
import urllib.parse


api="https://maps.googleapis.com/maps/api/geocode/json?"

end1= input ("Endereço origem?\n\n")
end2= input ("Endereço destino\n\n")

url1 = api+urllib.parse.urlencode({"address":end1, "key":"AIzaSyCTtNA0k93PzLx4SKPKIU6tbcyUg3-yTbQ"})

cli1 = requests.get(url1).json()

obj1 = cli1["results"][0]["geometry"]["location"]

lat1 = (obj1  ["lat"])
lng1 = (obj1  ["lng"])

url2 = api+urllib.parse.urlencode({"address":end2, "key":"AIzaSyCTtNA0k93PzLx4SKPKIU6tbcyUg3-yTbQ"})

cli2 = requests.get(url2).json()

obj2 = cli2["results"][0]["geometry"]["location"]

lat2 = (obj2 ["lat"])
lng2 = (obj2 ["lng"])

api2="https://maps.googleapis.com/maps/api/distancematrix/json?&origins=" +str(lat1) +"," +str(lng1)+"&destinations="+str(lat2)+","+str(lng2) +"&key=AIzaSyCTtNA0k93PzLx4SKPKIU6tbcyUg3-yTbQ"

dist= requests.get(api2).json()

x= dist["rows"][0]["elements"][0]

print(x["distance"]["text"])
print(x["duration"]["text"])
