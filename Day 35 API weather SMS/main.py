import requests
from twilio.rest import Client 
import os

# my location at northridge, ca
# openweather api
LAT = '34.238125'
LONG = '-118.530121'
API_ID = os.environ.get("OWM_API_KEY")

#twilio
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")


# testing
# LAT = '42.359'
# LONG = '-113.950'

# site and params
url = 'https://api.openweathermap.org/data/2.5/onecall'
parameters = {
    'lat': LAT,
    'lon': LONG,
    'exclude': 'current,minutely,daily',
    'appid': API_ID,
}

#grabbing data
response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()

#getting the weather
weather = data["hourly"][0]["weather"][0]['id']

will_rain = False

weather_slice = data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token) 
    
    message = client.messages.create(         
                                body="It's going to rain today. Remember to bring your ☔",
                                from_='+12064861579',
                                to='+15486841584'

                            )
    print(message.status)
