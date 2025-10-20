import requests
from bs4 import BeautifulSoup

instant_pot_endpoint = "https://appbrewery.github.io/instant_pot/"

response = requests.get(instant_pot_endpoint)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
price_whole = soup.select_one("span.a-price-whole").getText()
price_fraction = soup.select_one("span.a-price-fraction").getText()
price = float(price_whole + price_fraction)

print(price)