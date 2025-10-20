import requests
import smtplib
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()
email = os.environ.get("FROM_EMAIL")
password = os.environ.get("PASSWORD")
endpoint = "https://www.amazon.com/Keurig-K-Elite-Temperature-Capability-Programmable/dp/B078NN17K3?ref=dlx_deals_dg_dcl_B078NN17K3_dt_sl14_69_pi&pf_rd_r=44FPNSYZ5THHRAK7G6D4&pf_rd_p=bce1014c-f639-474b-b8f1-f2e8a12b2f69&th=1"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", 
    "Accept-Encoding": "gzip, deflate, br, zstd", 
    "Accept-Language": "ro-RO,ro;q=0.9,en-US;q=0.8,en;q=0.7",  
    "Priority": "u=0, i", 
    "Sec-Ch-Ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"", 
    "Sec-Ch-Ua-Mobile": "?0", 
    "Sec-Ch-Ua-Platform": "\"Windows\"", 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "cross-site", 
    "Sec-Fetch-User": "?1", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
  }

response = requests.get(endpoint, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
price_whole = soup.find(name="span", class_="a-price-whole")
price_fraction = soup.find(name="span", class_="a-price-fraction")
price = float(price_whole + price_fraction)
print(price)

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