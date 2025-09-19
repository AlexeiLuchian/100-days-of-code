import requests
from info import app_id, api_key

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
print(response.text)