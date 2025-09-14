import requests
import datetime as dt
import smtplib
from info import from_email, password
import time

MY_LAT = 44.435581
MY_LNG = 26.102221

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
    "tzid": "Europe/Bucharest",
}
while True:
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
        print("It's day outside, you won't see the ISS")
    else:
        iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
        iss_response.raise_for_status()

        iss_data = iss_response.json()
        iss_lat = float(iss_data["iss_position"]["latitude"])
        iss_lng = float(iss_data["iss_position"]["longitude"])

        if iss_lat - 5 <= MY_LAT <= iss_lat + 5 and iss_lng - 5 <= MY_LNG <= iss_lng + 5:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=from_email, password=password)
                connection.sendmail(from_addr=from_email,
                                    to_addrs=from_email,
                                    msg="Subject: Look Up!\n\nYou'll be able to spot the ISS very soon.")
        else:
            print("The ISS won't be over you soon")
    time.sleep(60)