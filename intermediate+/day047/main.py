import requests
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()
email = os.environ.get("FROM_EMAIL")
password = os.environ.get("PASSWORD")
instant_pot_endpoint = "https://appbrewery.github.io/instant_pot/"
headers = {
    "Content-Type": "text/plain; charset=utf-8",
}

response = requests.get(instant_pot_endpoint)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
price_whole = soup.select_one("span.a-price-whole").getText()
price_fraction = soup.select_one("span.a-price-fraction").getText()
price = float(price_whole + price_fraction)

if price < 100:
    product = " ".join(soup.find(name="span", id="productTitle").getText().split()).encode('utf-8')
    link = soup.find(name="a", id="bylineInfo")['href']
    message = f"{product} is available now for the price of {price}$.\n{link}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr=email,
                            to_addrs=email,
                            msg=f"Subject:DISCOUNT!\n\n{message}")