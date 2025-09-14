import requests
import datetime as dt

parameters = {
    "lat": 44.435581,
    "lng": 26.102221,
    "formatted": 0,
    "tzid": "Europe/Bucharest",
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise_time = data["results"]["sunrise"]
sunset_time = data["results"]["sunset"]
now_time = dt.datetime.now()

now_hour = now_time.hour
sunrise_hour = sunrise_time.split("T")[1].split(":")[0]
sunset_hour = sunset_time.split("T")[1].split(":")[0]

if now_hour >= int(sunrise_hour) and now_hour <= int(sunset_hour):
    print("It's day, go touch some grass🎋")
else:
    print("It's still night🌙")