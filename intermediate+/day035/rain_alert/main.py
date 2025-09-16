import requests
from info import api_key, lat, lng

owm_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
params = {
    "lat": lat,
    "lon": lng,
    "appid": api_key,
    "units": "metric",
    "cnt": 4,
}

response = requests.get(url=owm_endpoint, params=params)
response.raise_for_status()

data = response.json()

print(data["cod"])
for item in data["list"]:
    if item["weather"][0]["id"] < 700:
        print("Bring an umbrella!")
        break