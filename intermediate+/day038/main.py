import requests
from info import app_id, api_key
import datetime as dt

APP_ID = app_id
API_KEY = api_key

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise?"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_input = input("What exercises have you done today?: ")
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

sheety_endpoint = "https://api.sheety.co/2896f611e30c5b6f2f226739242e2373/workoutTracking/workouts"
sheet_params = {
    "workout": {
    "Date": date,
    "Time": time,
    "Exercise": exercise,
    "Duration": duration,
    "Calories": calories,
    }
}

print(sheet_params)

response = requests.post(url=sheety_endpoint, json=sheet_params)
print(response.text)