import requests
from datetime import datetime

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

# print(longitude, latitude)

parameters = {
    "lng": longitude,
    "lat": latitude,
    "formatted": 0
}

reponse = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
reponse.raise_for_status()

rise = reponse.json()
sunrise = int(rise["results"]['sunrise'].split("T")[1].split(":")[0])
sunset = int(rise["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)