import requests
import time
from bs4 import BeautifulSoup


def time_is_valid(user_input):
    try:
        time.strptime(user_time, '%Y-%m-%d')
        return True
    except:
        return False
    
valid = False

while not valid:
    user_time = input("Which year do you want to travel to?\nType the date in this format YYYY-MM-DD: ")
    valid = time_is_valid(user_time)

billboard_endpoint = f"https://www.billboard.com/charts/hot-100/{user_time}/"
headers = {
    "User-Agent" :
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
}

response = requests.get(url=billboard_endpoint, headers=headers)
response.raise_for_status()

billboard_soup = BeautifulSoup(response.text, 'html.parser')
title_headers = billboard_soup.select('li > h3.c-title')
titles = [title.getText().strip() for title in title_headers]
print(titles)