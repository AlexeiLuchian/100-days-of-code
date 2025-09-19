import requests
from info import app_id, api_key, USERNAME, auth_token
import datetime as dt

APP_ID = app_id
API_KEY = api_key
AUTH_TOKEN = auth_token

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise?"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_input = input("What exercise have you done today?: ")
params = {
    "query": user_input,
}

response = requests.post(url=nutritionix_endpoint, json=params, headers=headers)
response.raise_for_status()
text_data = response.json()

today = dt.datetime.today()

date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")
exercise = text_data["exercises"][0]["user_input"]
duration = text_data["exercises"][0]["duration_min"]
calories = text_data["exercises"][0]["nf_calories"]

sheety_endpoint = f"https://api.sheety.co/{USERNAME}/workoutTracking/workouts"
sheet_params = {
    "workout": {
    "date": date,
    "time": time,
    "exercise": exercise,
    "duration": duration,
    "calories": calories,
    }
}
sheety_headers = {
    "Authorization": AUTH_TOKEN,
}


response = requests.post(url=sheety_endpoint, json=sheet_params, headers=sheety_headers)
print(response.text)