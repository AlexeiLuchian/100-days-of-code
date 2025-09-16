import requests
from info import api_key, lat, lng, twilio_sid, twilio_token, pn, tpn, msid, mtoken, mpn, mtpn
from twilio.rest import Client

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

for item in data["list"]:
    condition_code = item["weather"][0]["id"]
    if condition_code < 700:
        client = Client(twilio_sid, twilio_token)
        client2 = Client(msid, mtoken)

        message = client.messages.create(
            body="It's going to rain💧 Bring an umbrella with you☂️",
            from_=tpn,
            to=pn,
        )

        message2 = client2.messages.create(
            body="Marinocika, O sa ploua💧 Sa iei umbrela cu tine☂️",
            from_=mtpn,
            to=mpn,
        )

        break